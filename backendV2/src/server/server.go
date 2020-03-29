package main

import (
	"log"
	"firebase.google.com/go"
	"firebase.google.com/go/auth"
	"net/http" 
	"golang.org/x/net/context"
	"google.golang.org/api/option"
	"fmt"
	"encoding/json"
	"github.com/elgs/gostrgen"
)

var app *firebase.App

//specify user interface
type User struct {
    rank     int 	`json:"rank"`
    username string `json:"username"`
    score float64 	`json:"score"`
}

type LeaderboardResponse struct {
	users []User 	`json:users`
}

type startConversationRequest struct {
	auth string 	"json: auth"
}

type conversationID struct {
	cid string 		"json: cid"
}

type endConversationRequest struct{
	auth string  	"json: auth"
	guess int   	"json: guess"
}

type newUser struct {
    username string "json:  username"
    score float64 	"json: score"
}

type sendMessage struct {
  auth  string 		"json:auth"
  text  string 		"json:text"
}

type message struct {
	message		string `json:"message"`
	timestamp	string `json:"timestamp"`
}

func main() {
	app = authenticateServer()

	// database client
	dbClient, err := app.Database(context.Background())
	if err != nil {
        log.Fatalln("Error initializing database client:", err)
	}

	//TODO just test dataset output, remove later
	// context.Background just creates empty context that we can pass if we dont need this tool
	ref := dbClient.NewRef("")
	var data map[string]interface{}
	if err := ref.Get(context.Background(), &data); err != nil {
        log.Fatalln("Error reading from database:", err)
	}
	fmt.Println(data)

	//go func() {
		log.Fatal(http.ListenAndServe("localhost:422/api/conversation/send/:cid", http.HandlerFunc(sendMessageHandler)))
		//listener
		log.Fatal(http.ListenAndServe("/api/leaderboards", http.HandlerFunc(leaderboardHandler)))
		log.Fatal(http.ListenAndServe("/api/conversation/start", http.HandlerFunc(startConversationHandler)))
		log.Fatal(http.ListenAndServe("/api/conversation/start", http.HandlerFunc(endConversationHandler)))
		log.Fatal(http.ListenAndServe("/api/conversation/start", http.HandlerFunc(flagConversationHandler)))
		
	//}

}

// This method should be called on initialization
// It connects our server as an admin and returns the app instance
func authenticateServer() *firebase.App {
	ctx := context.Background()
	conf := &firebase.Config{
        DatabaseURL: "https://turing-game-e5059.firebaseio.com",
	}
	// Fetch the service account key JSON file contents
	opt := option.WithCredentialsFile("src/server/serverKeys.json")

	// Initialize the app with a service account, granting admin privileges
	app, err := firebase.NewApp(ctx, conf, opt)
	if err != nil {
        log.Fatalln("Error initializing app:", err)
	}
	return app
}

// Method verifies if incoming token is a valid and logged-in users token
func checkUserAuthentication(idToken string) (*auth.Token, error) {
	ctx := context.Background()
	client, err := app.Auth(ctx)
	if err != nil {
        log.Fatalf("error getting Auth client: %v\n", err)
	}

	token, err := client.VerifyIDToken(ctx, idToken)
	if err != nil {
        log.Printf("Error verifying ID token: %v\n", err)
        return nil, err
	}

	log.Printf("Verified ID token: %v\n", token)
	return token, nil
}

// Method returns the current leaderboard to request issuer
func leaderboardHandler(w http.ResponseWriter, req *http.Request) {
  ctx := context.Background()	
  // Create a database client from App.
  client, err := app.Database(ctx)
  if err != nil {
          log.Printf("Error initializing database client: %v", err)
  }

  // Get a database reference to posts
  ref := client.NewRef("Leaderboards")

  var lboard LeaderboardResponse
  if err := ref.Get(ctx, &lboard); err != nil {
          log.Printf("Error reading value: %v", err)
  }
  jsonLb, err := json.Marshal(lboard)
  if err != nil {
  	log.Printf("Error Marshalling leaderbaords json: %v", err)
  }
  w.Write(jsonLb)
}

//Method returns newly generated cid to request origin
func startConversationHandler(w http.ResponseWriter, r *http.Request) {
	//decode JSON and authenticate user
	var startReq startConversationRequest
	err := json.NewDecoder(r.Body).Decode(&startReq)
	auth := startReq.auth
	_, err = checkUserAuthentication(auth) // dont need the token here
	if err != nil {
		log.Fatalf("error verifying ID token: %v\n", err)
	}

	var newConvID conversationID
	newConvID.cid = getNewConversationID()
	id, err := json.Marshal(newConvID)
	if err != nil {
		log.Fatalf("error converting to json: %v\n", err)
	}
	w.Write(id)

}

func getNewConversationID() string {
	//generates a random string that could contain any lowercase and uppercase letters and digits 0 to 9

	charsToGenerate := 10 //Length of the conversatoinID string
	charSet := gostrgen.Lower | gostrgen.Digit
	includes := "" // optionally include some additional letters
	excludes := "" //exclude big 'O' and small 'l' to avoid confusion with zero and one.

	str, err := gostrgen.RandGen(charsToGenerate, charSet, includes, excludes)
	if err != nil {
		log.Println(err)
	}
	return str
	//log.Println(str) // zxh9pvoxbaup32b7s0d
}

// Method end the conversaion with a given CID and updates apropriate fields in the database
func endConversationHandler(w http.ResponseWriter, r *http.Request){

	ctx := context.Background()
	//Authenticate User
	var endReq endConversationRequest
	err := json.NewDecoder(r.Body).Decode(&endReq)
	auth:=endReq.auth
	userToken, err := checkUserAuthentication(auth)
	if err!=nil {
		log.Fatalf("error verifying ID token: %v\n", err)
	}


	//get a reference to the chat rooms section of the database
	//cid:= r.URL.Path[1:]
	cid:= r.URL.Path[len("/api/conversation/end/"):]
	client, err := app.Database(ctx)

//	ref := client.NewRef("availableGames/chatRoomId")
//	//results,err := ref.OrderByKey().EqualTo(cid).GetOrdered(ctx)
	if err != nil{
		log.Fatalln("Error querying database:", err)
	}
//
//	//make this chatroom complete
//	//roomStatus := results.Get()
	address := "availableGames/" + cid
	ref := client.NewRef(address)
	err = ref.Set(ctx,"complete")
	if err != nil{
		log.Fatalln("Error setting value as complete:", err)
	}

	// Submit guess
	userRef := client.NewRef("leaderboards/user")
	_,err = userRef.OrderByKey().EqualTo(userToken.UID).GetOrdered(ctx)
	if err!= nil{
		if _, err := userRef.Push(ctx, &newUser{
			username: userToken.UID,
			score: 1,
		});
		err != nil {
			log.Printf("Error pushing child node: %v", err)
		}
		return
	}
	//Getting the score of the user
	var nUser newUser
	userAdd := "leaderboards/" + userToken.UID
	userRef = client.NewRef(userAdd)
	if err = userRef.Get(ctx,&nUser); err!= nil{
		log.Fatalln("Error getting value:", err)}

	//Setting the score of the user
	userAdd = "leaderboards/" + userToken.UID + "/score"
	ref = client.NewRef(userAdd)
	userScore := nUser.score + 1;
	err = ref.Set(ctx,userScore)
	if err != nil{
		log.Fatalln("Error setting value", err)
	}
	w.WriteHeader(http.StatusOK)
}

//Handler which decodes json objects and then sends message 'text' from 'auth'
//to conversation 'convid'
func sendMessageHandler(w http.ResponseWriter, r *http.Request) {
	ctx := context.Background()

	//get conversation id
	cid := r.URL.Path[len("api/conversation/send/"):]
	var msg sendMessage

	//decode json
	decoder := json.NewDecoder(r.Body)
	err := decoder.Decode(&msg)
	if err != nil {
	    log.Printf("Decode failure! %v", err)
	}

	//get and verify userid
	userToken, err := checkUserAuthentication(msg.auth)
	if err != nil {
	    log.Printf("Authentication failure!", err)
    }

    //initializing database
    client, err := app.Database(ctx)
	if err != nil{
		log.Fatalln("Initialization Error!")
	}

	address := "chatRooms/"+cid
    //sending message to database
    chatRef := client.NewRef(address)

   err = chatRef.Set(ctx, map[string]*message{
	   userToken.UID : &message{  
           message : msg.text,
           timestamp: "2069-04-20  09:11:01",
	   },
   })
   if err != nil {
     log.Fatalln("Error setting value")
   }
   w.WriteHeader(http.StatusOK)
}

func flagConversationHandler(w http.ResponseWriter, r *http.Request) {
	//Creating database client from app
	ctx := context.Background()
	client, err := app.Database(ctx)
	if err != nil {
		log.Fatalf("error getting Auth client: %v\n", err)
	}

	//Getting the conversation id from the URL
	cid := r.URL.Path[len("/api/conversation/flag/"):]

	//Creating a reference to flaggedConversations in database
	path := "flaggedConversations" + cid
	ref := client.NewRef(path)


	//Set /flaggedConversations/:cid in DB to "flagged"
	err = ref.Set(ctx,"flagged")
	if err != nil {
		log.Fatalln("Error setting flagged:", err)
	}
	w.WriteHeader(http.StatusOK)
}

