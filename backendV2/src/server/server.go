package main

import (
	"log"
	"firebase.google.com/go"
	"firebase.google.com/go/auth"
	"net/http" 
	"golang.org/x/net/context"
	"google.golang.org/api/option"
	"encoding/json"
	"github.com/elgs/gostrgen"
)

var app *firebase.App

//specify user interface
type User struct {
    Rank     int 	`json:"rank"`
    Username string `json:"username"`
    Score float64 	`json:"score"`
}

type LeaderboardResponse struct {
	Users []User 	`json:users`
}

type StartConversationRequest struct {
	Auth string 	"json: auth"
}

type ConversationID struct {
	CID string 		"json: cid"
}

type EndConversationRequest struct{
	Auth string  	"json: auth"
	Guess int   	"json: guess"
}

type NewUser struct {
    Username string "json:  username"
    Score float64 	"json: score"
}

type SendMessage struct {
  Auth  string 		"json:auth"
  Text  string 		"json:text"
}

type Message struct {
	Message		string `json:"message"`
	Timestamp	string `json:"timestamp"`
}

func main() {
	app = authenticateServer()

	http.Handle("/api/conversation/send", http.HandlerFunc(sendMessageHandler))
	http.Handle("/api/leaderboards", http.HandlerFunc(leaderboardHandler))
	http.Handle("/api/conversation/start", http.HandlerFunc(startConversationHandler)) // checked
	http.Handle("/api/conversation/end/", http.HandlerFunc(endConversationHandler))
	http.Handle("/api/conversation/flag/", http.HandlerFunc(flagConversationHandler)) // checked
	log.Fatal(http.ListenAndServe("localhost:420", nil))
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
        log.Printf("error getting Auth client: %v\n", err)
        return nil, err
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
	  return
  }
  jsonLb, err := json.Marshal(lboard)
  if err != nil {
  	log.Printf("Error Marshalling leaderbaords json: %v", err)
  	return
  }
  w.Write(jsonLb)
}

//Method returns newly generated cid to request origin
func startConversationHandler(w http.ResponseWriter, r *http.Request) {
	
	//decode JSON and authenticate user
	var startReq StartConversationRequest
	err := json.NewDecoder(r.Body).Decode(&startReq)
	if err != nil {
		log.Printf("Error decoding json: %v\n", err)
		http.Error(w, err.Error(), http.StatusInternalServerError)
		return
	}
	auth := startReq.Auth
	_, err = checkUserAuthentication(auth) // dont need the token here
	if err != nil {
		log.Printf("error verifying ID token: %v\n", err)
		http.Error(w, err.Error(), http.StatusUnauthorized)
		return
	}

	var newConvID ConversationID
	newConvID.CID = getNewConversationID()
	id, err := json.Marshal(newConvID)
	if err != nil {
		log.Printf("error converting to json: %v\n", err)
		http.Error(w, err.Error(), http.StatusInternalServerError)
		return
	}
	w.Write(id)

}

//generates a random string that could contain any lowercase and uppercase letters and digits 0 to 9
func getNewConversationID() string {
	charsToGenerate := 10 //Length of the conversatoinID string
	charSet := gostrgen.Lower | gostrgen.Digit
	includes := "" // optionally include some additional letters
	excludes := "" //exclude big 'O' and small 'l' to avoid confusion with zero and one.

	str, err := gostrgen.RandGen(charsToGenerate, charSet, includes, excludes)
	if err != nil {
		log.Println(err)
		return ""
	}
	return str
}

// Method end the conversaion with a given CID and updates apropriate fields in the database
func endConversationHandler(w http.ResponseWriter, r *http.Request){

	ctx := context.Background()
	//Authenticate User
	var endReq EndConversationRequest
	err := json.NewDecoder(r.Body).Decode(&endReq)
	auth:=endReq.Auth
	userToken, err := checkUserAuthentication(auth)
	if err!=nil {
		log.Printf("error verifying ID token: %v\n", err)
		return
	}


	//get a reference to the chat rooms section of the database
	cid:= r.URL.Path[len("/api/conversation/end/"):]
	client, err := app.Database(ctx)
	if err != nil{
		log.Printf("Error querying database:", err)
		return	
	}
//
//	//make this chatroom complete
	address := "availableGames/" + cid
	ref := client.NewRef(address)
	err = ref.Set(ctx,"complete")
	if err != nil{
		log.Printf("Error setting value as complete:", err)
		return
	}

	// Submit guess
	userRef := client.NewRef("Leaderboards/user")
	_,err = userRef.OrderByKey().EqualTo(userToken.UID).GetOrdered(ctx)
	if err!= nil{
		if _, err := userRef.Push(ctx, &NewUser{
			Username: userToken.UID,
			Score: 1,
		});
		err != nil {
			log.Printf("Error pushing child node: %v", err)
			return
		}
		return
	}
	//Getting the score of the user
	var nUser NewUser
	userAdd := "Leaderboards/" + userToken.UID
	userRef = client.NewRef(userAdd)
	if err = userRef.Get(ctx,&nUser); err!= nil{
		log.Fatalln("Error getting value:", err)}

	//Setting the score of the user
	userAdd = "Leaderboards/" + userToken.UID + "/score"
	ref = client.NewRef(userAdd)
	userScore := nUser.Score + 1;
	err = ref.Set(ctx,userScore)
	if err != nil{
		log.Printf("Error setting value", err)
		return
	}
	w.WriteHeader(http.StatusOK)
}

//Handler which decodes json objects and then sends message 'text' from 'auth'
//to conversation 'convid'
func sendMessageHandler(w http.ResponseWriter, r *http.Request) {
	ctx := context.Background()

	//get conversation id
	cid := r.URL.Path[len("api/conversation/send/"):]
	var msg SendMessage

	//decode json
	decoder := json.NewDecoder(r.Body)
	err := decoder.Decode(&msg)
	if err != nil {
	    log.Printf("Decode failure! %v", err)
	    return
	}

	//get and verify userid
	userToken, err := checkUserAuthentication(msg.Auth)
	if err != nil {
	    log.Printf("Authentication failure!", err)
	    return
    }

    //initializing database
    client, err := app.Database(ctx)
	if err != nil{
		log.Printf("Initialization Error!")
		return
	}

	address := "chatRooms/"+cid
    //sending message to database
    chatRef := client.NewRef(address)

   err = chatRef.Set(ctx, map[string]*Message{
	   userToken.UID : &Message{  
           Message : msg.Text,
           Timestamp: "2069-04-20  09:11:01",
	   },
   })
   if err != nil {
     log.Printf("Error setting value")
     return
   }
   w.WriteHeader(http.StatusOK)
}

func flagConversationHandler(w http.ResponseWriter, r *http.Request) {
	//Creating database client from app
	ctx := context.Background()
	client, err := app.Database(ctx)
	if err != nil {
		log.Printf("error getting database client: %v\n", err)
		return
	}

	//Getting the conversation id from the URL
	cid := r.URL.Path[len("/api/conversation/flag/"):]

	ref := client.NewRef("flaggedConversations")


	//Set /flaggedConversations/:cid in DB to "flagged"
	err = ref.Set(ctx, map[string]string {
	   cid : "flagged",
   })
	if err != nil {
		log.Printf("Error setting flagged: %v", err)
		return
	}
	w.WriteHeader(http.StatusOK)
}

