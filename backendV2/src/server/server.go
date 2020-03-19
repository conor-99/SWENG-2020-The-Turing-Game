package main

import (
	"log"
	"firebase.google.com/go"
	"firebase.google.com/go/auth"
	//"net/http" // UNCOMMENT this when using http package
	"golang.org/x/net/context"
	"google.golang.org/api/option"
	"fmt"
)

func main() {
	app := authenticateServer()
		
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
func checkUserAuthentication(app *firebase.App, idToken string) *auth.Token {
	ctx := context.Background()
	client, err := app.Auth(ctx)
	if err != nil {
        log.Fatalf("error getting Auth client: %v\n", err)
	}

	token, err := client.VerifyIDToken(ctx, idToken)
	if err != nil {
        log.Fatalf("error verifying ID token: %v\n", err)
	}
	
	log.Printf("Verified ID token: %v\n", token)
	return token
}
