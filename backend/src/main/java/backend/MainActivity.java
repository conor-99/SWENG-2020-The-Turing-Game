package backend;

import java.io.FileInputStream;
import java.io.IOException;
import java.util.concurrent.ExecutionException;

import com.google.auth.oauth2.GoogleCredentials;
import com.google.firebase.FirebaseApp;
import com.google.firebase.FirebaseOptions;
import com.google.firebase.auth.FirebaseAuth;
import com.google.firebase.auth.FirebaseAuthException;
import com.google.firebase.auth.FirebaseToken;
import com.google.firebase.auth.UserRecord;
import com.google.firebase.database.DataSnapshot;
import com.google.firebase.database.DatabaseError;
import com.google.firebase.database.DatabaseReference;
import com.google.firebase.database.FirebaseDatabase;
import com.google.firebase.database.ValueEventListener;

public class MainActivity {

	public static void main(String[] args) {
		try {
			authenticateServer();
			System.out.println("Admin server authenticated!");
		} catch(Exception e) {
			System.out.println("Failed authenticating the server");
			e.printStackTrace();
		}	
	}
	
	private static void authenticateServer() throws IOException {
		// Fetch the service account key JSON file contents
		FileInputStream serviceAccount = new FileInputStream("serverKeys.json");

		// Initialize the app with a service account, granting admin privileges
		FirebaseOptions options = new FirebaseOptions.Builder()
		    .setCredentials(GoogleCredentials.fromStream(serviceAccount))
		    .setDatabaseUrl("https://turing-game-e5059.firebaseio.com")
		    .build();
		FirebaseApp.initializeApp(options);

		// As an admin, the app has access to read and write all data, regardless of Security Rules
		DatabaseReference ref = FirebaseDatabase.getInstance()
		    .getReference("restricted_access/secret_document");
		ref.addListenerForSingleValueEvent(new ValueEventListener() {
		  @Override
		  public void onDataChange(DataSnapshot dataSnapshot) {
		    Object document = dataSnapshot.getValue();
		    System.out.println(document);
		  }

		  @Override
		  public void onCancelled(DatabaseError error) {
		  }
		});
	}
	
	/**
	 * Method for verifying if incoming token is a logged in user.
	 * If yes, it returns the userID of that user
	 * NOTE: idToken != userID
	 * @param idToken
	 * @return userID
	 * @throws FirebaseAuthException 
	 */
	static String checkUserAuthentication(String idToken) throws FirebaseAuthException {
		FirebaseToken decodedToken = FirebaseAuth.getInstance().verifyIdToken(idToken);
		System.out.println("Successfully verified the user with toke: "+idToken);
		String userID = decodedToken.getUid();
		return userID;
	}
}

//FEEDBACK UPLOAD PART

//private EditText mContactEmail;
//private EditText mMessage;
//
//mContactEmail = findViewById(R.id.contactEmail);
//mMessage = findViewById(R.id.contactMessage);
//private void uploadContactMessage(){
//    String message = mMessage.getText().toString().trim();
//    String email = mContactEmail.getText().toString().trim();
//
//    FirebaseAuth Auth = FirebaseAuth.getInstance();
//    FirebaseDatabase Database = FirebaseDatabase.getInstance();
//    DatabaseReference DatabaseRefFeedback = Database.getReference("feedback");
//    DatabaseReference newFeedback = DatabaseRefFeedback.push();
//    newFeedback.child("message").setValue(message);
//    newFeedback.child("reply-email").setValue(email);
//
//
//}

// ACTUAL DATA UPLOAD PART
////Firebase atributes
//private FirebaseAuth mAuth;
//private FirebaseUser mCurrentUser;
//private FirebaseAuth.AuthStateListener mAuthListener;
//
////Firebase listeners
//ValueEventListener mCurrentGameStatusListener;
//ValueEventListener mAvailableGameListener;
//ChildEventListener mChatRoomMessageListener;
//
////firebase realtime database
//private FirebaseDatabase mDatabase;
//private DatabaseReference mDatabaseRef;
//
//
////reference to a game obect
////private TuringGame currentGame;
//private boolean isHumanGame;
//private boolean gameJoined;
//private String gameState;
//private int messageNum;
//private String myId;
//private String chatRoomId;
//private int mGameStatus;
//private int mPrevGameStatus;
//private static final int GAME_NOT_ACTIVE = 1;
//private static final int GAME_ACTIVE = 5;
//private static final int GAME_STOPPED = 15;
//private static final int GAME_STARTING = 25;
//private static final int GAME_PAUSED = 35;
//private static final int GAME_NULL = 0;
//
//// MATCHMAKING
//new Thread(new Runnable() {
//    @Override
//    public void run() {
//        matchmaking();  //find an opponent
//        initialRequest = true;
//        createWatsonServices(); //create text-to-speech and voice-to-text services
//        if (isHumanGame) {
//            createFirebaseServices();
//        } else {
//            initialRequest = false; // set it randomly, it determines who starts the conversation
//            createWatsonAssistant();
//        }
//        runOnUiThread(new Runnable() {
//            @Override
//            public void run() {
//                if(MainActivity.this == null)
//                    return;
//                mProgressBar.setVisibility(View.GONE);
//                recyclerView.setVisibility(View.VISIBLE);
//                mAdapter = new ChatAdapter(messageArrayList, myId);
//                recyclerView.setAdapter(mAdapter);
//                mAdapter.notifyDataSetChanged();
//                //TODO: see this
//                //mGameStatus = GAME_ACTIVE;
//
//
//
//            }
//        });
//        //start the timer
//        //TODO: synchronise time
//        //startTimer();
//    }
//}).start();
//
///**
// * Method to be called when activity is started
// * created: 15:00 22/03/2019 by J.Cistiakovas
// * last modified: -
// */
//@Override
//public void onStart() {
//    super.onStart();
//    //initiate sign in check
//    //mAuthListener.onAuthStateChanged(mAuth);
//}
//
//@Override
//public void onPause() {
//    super.onPause();
//    detachListeners();
////    mPrevGameStatus = mGameStatus;
////    mGameStatus = GAME_PAUSED;
//}
//
//@Override
//public void onResume() {
//    super.onResume();
//    attachListeners();
////    if(mPrevGameStatus != GAME_NULL) {
////        mGameStatus = mPrevGameStatus;
////    }
//}
//
//@Override
//public void onDestroy() {
//    super.onDestroy();
//    if(mCountDownTimer != null) {
//        mCountDownTimer.cancel();
//    }
//}
//
///**
// * Method that sends a message to a human play via Firebase realtime databse
// * created: 22:00 23/03/2019 by J.Cistiakovas
// * last modified: 19:00 24/03/2019 by C.Coady - updated messages to include new type
// * attribute. This denotes if the message was sent by a human or a bot.
// */
//private void sendMessageHuman() {
//    //create a new TuringMessage object using values from the editText box
//    String id = mAuth.getUid() + (new Integer(messageNum++).toString());
//    Message message = new Message();
//    message.setMessage(this.inputMessage.getText().toString().trim());
//    message.setId(id);
//    message.setSender(myId);
//    message.setType("human");
//
//    //return if message is empty
//    if (message.getMessage().equals("")) {
//        return;
//    }
//    //publish the message in an chatRooms
//    mDatabaseRef.child("chatRooms").child(chatRoomId).child(message.getId()).setValue(message);
//    // add a message object to the list
//    messageArrayList.add(message);
//    this.inputMessage.setText("");
//    // make adapter to update its view and add a new message to the screen
//    //mAdapter.notifyDataSetChanged();
//    new SayTask().execute(message.getMessage());
//    scrollToMostRecentMessage();
//}
//
//// Sending a message to Watson Assistant Service
//private void sendMessageBot() {
//    final String inputmessage = this.inputMessage.getText().toString().trim();
//    if (!this.initialRequest) {
//        Message inputMessage = new Message();
//        inputMessage.setMessage(inputmessage);
//        inputMessage.setId("1");
//        inputMessage.setSender(myId);
//        inputMessage.setType("human");
//        messageArrayList.add(inputMessage);
//    } else {
//        Message inputMessage = new Message();
//        inputMessage.setMessage(inputmessage);
//        inputMessage.setId("100");
//        inputMessage.setSender(myId);
//        inputMessage.setType("human");
//        this.initialRequest = false;
//        showToast("Tap on the message for Voice", Toast.LENGTH_LONG);
//
//    }
//
//    this.inputMessage.setText("");
//    mAdapter.notifyDataSetChanged();
//    scrollToMostRecentMessage();
//    Thread thread = new Thread(new Runnable() {
//        public void run() {
//            try {
//                if (watsonAssistantSession == null) {
//                    ServiceCall<SessionResponse> call = watsonAssistant.createSession(
//                            new CreateSessionOptions.Builder().assistantId(mContext.getString(R.string.assistant_id)).build());
//                    watsonAssistantSession = call.execute();
//                }
//
//                MessageInput input = new MessageInput.Builder()
//                        .text(inputmessage)
//                        .build();
//                MessageOptions options = new MessageOptions.Builder()
//                        .assistantId(mContext.getString(R.string.assistant_id))
//                        .input(input)
//                        .sessionId(watsonAssistantSession.getSessionId())
//                        .build();
//
//                //blocking statement
//                MessageResponse response = watsonAssistant.message(options).execute();
//                Log.i(TAG, "run: " + response);
//                final Message outMessage = new Message();
//                if (response != null &&
//                        response.getOutput() != null &&
//                        !response.getOutput().getGeneric().isEmpty() &&
//                        "text".equals(response.getOutput().getGeneric().get(0).getResponseType())) {
//                    outMessage.setMessage(response.getOutput().getGeneric().get(0).getText());
//                    outMessage.setId("2");
//                    outMessage.setType("bot");
//                    //add random delay to make it seem more like a human responding
//                    double delay = Math.random() * (1000000000 * outMessage.getMessage().length()) + 1000000000;
//                    for(int i = 0; i < delay; i++){}
//                    messageArrayList.add(outMessage);
//
//                    // speak the message
//                    new SayTask().execute(outMessage.getMessage());
//                    scrollToMostRecentMessage();
//                }
//            } catch (Exception e) {
//                e.printStackTrace();
//            }
//        }
//    });
//
//    thread.start();
//
//}
//
///**
// * Check Internet Connection
// *
// * @return
// */
//private boolean checkInternetConnection() {
//    // get Connectivity Manager object to check connection
//    ConnectivityManager cm =
//            (ConnectivityManager) getSystemService(Context.CONNECTIVITY_SERVICE);
//
//    NetworkInfo activeNetwork = cm.getActiveNetworkInfo();
//    boolean isConnected = activeNetwork != null &&
//            activeNetwork.isConnectedOrConnecting();
//
//    // Check for network connections
//    if (isConnected) {
//        return true;
//    } else {
//        showToast(" No Internet Connection available ", Toast.LENGTH_LONG);
//        return false;
//    }
//
//}
//
///**
// * Method to initialise Firebase services, such as Auth and Realtime Database
// * created: 04/03/2019 by J.Cistiakovas
// * last modified: 24/03/2019 by C.Coady - removed message listener as this is handled in the
// * loadMessages method
// */
//private void createFirebaseServices() {
//    //Firebase anonymous Auth
//    FirebaseApp.initializeApp(this);
//    mAuth = FirebaseAuth.getInstance();
//    mCurrentUser = mAuth.getCurrentUser();
//    //listener that listens for change in the Auth state
//    mAuthListener = new FirebaseAuth.AuthStateListener() {
//        @Override
//        public void onAuthStateChanged(@NonNull final FirebaseAuth firebaseAuth) {
//            FirebaseUser currentUser = firebaseAuth.getCurrentUser();
//            //check if user is already signed in
//            //TODO: retrieve/reset local information from the memory, e.g. score
//            if (currentUser == null) {
//                mAuth.signInAnonymously().addOnCompleteListener(MainActivity.this, new OnCompleteListener<AuthResult>() {
//                    @Override
//                    public void onComplete(@NonNull Task<AuthResult> task) {
//                        if (task.isSuccessful()) {
//                            mCurrentUser = firebaseAuth.getCurrentUser();
//                            showToast("Hello, " + mCurrentUser.getUid(), Toast.LENGTH_LONG);
//                        } else {
//                            showToast("Authentication failed!", Toast.LENGTH_LONG);
//                            //TODO: fail the program or do something here
//                        }
//                    }
//                });
//            } else {
//                //user is signed in - happy days
//                mCurrentUser = currentUser;
//                showToast("Hello, " + currentUser.getUid(), Toast.LENGTH_LONG);
//                Log.d(TAG, "User already signed in. User id : " + mCurrentUser.getUid());
//
//            }
//        }
//    };
//    mAuth.addAuthStateListener(mAuthListener);
//    myId = mAuth.getUid();
//
//    //Firebase realtime database initialisation
//    mDatabase = FirebaseDatabase.getInstance();
//    mDatabaseRef = mDatabase.getReference();
//}
//
///**
// * This method starts a listener on the chatRoom in the database.
// * When ever a message is added to the chatRoom the listener will
// * add the new message to the arrayList of messages so it can be
// * displayed on screen
// * created: 11/03/2019 by C.Coady
// * last modified: 23/03/2019 by C.Coady
// */
//private void loadMessages(){
//    if(isHumanGame){
//        DatabaseReference messageRef = mDatabaseRef.child("chatRooms");
//        mChatRoomMessageListener = new ChildEventListener() {
//            // TODO: not load previous conversation, possibly use timestamps
//            @Override
//            public void onChildAdded(@NonNull DataSnapshot dataSnapshot, @Nullable String s) {
//                //retrieve the message from the datasnapshot
//                Message newMessage = dataSnapshot.getValue(Message.class);
//                //TODO: deal with double messages, sould not be much of  a problem if we start a new chat each time
//                if (TextUtils.equals(newMessage.getSender(), mAuth.getUid())) {
//                    //don't add own message
//                    return;
//                }
//                messageArrayList.add(newMessage);
//                //mAdapter.notifyDataSetChanged();
//                scrollToMostRecentMessage();
//            }
//            @Override
//            public void onChildChanged(@NonNull DataSnapshot dataSnapshot, @Nullable String s) { }
//            @Override
//            public void onChildRemoved(@NonNull DataSnapshot dataSnapshot) { }
//            @Override
//            public void onChildMoved(@NonNull DataSnapshot dataSnapshot, @Nullable String s) { }
//            @Override
//            public void onCancelled(@NonNull DatabaseError databaseError) { }
//        };
//        messageRef.child(chatRoomId).addChildEventListener(mChatRoomMessageListener);
//    }
//}
//
///**
// * This method loops through the arrayList of messages and uploads each one
// * to the chat room corresponding to 'chatRoomId' on the database.
// * created: 23/03/2019 by C.Coady
// * last modified: 24/03/2019 by C.Coady
// */
//private void uploadMessages(){
//    //get a reference to the chat rooms section of the database
//    DatabaseReference chatRef = mDatabaseRef.child("chatRooms").child(chatRoomId);
//
//    //loop through messages and upload them to the chat
//    for(int i = 0; i < messageArrayList.size(); i++){
//        chatRef = chatRef.push();
//        Message message = (Message) messageArrayList.get(i);
//        message.setId(chatRef.getKey());
//        //publish the message in an chatRooms
//        chatRef.setValue(message);
//        chatRef = mDatabaseRef.child("chatRooms").child(chatRoomId);
//    }
//}
//
///**
// * This method loops through the completeGames arrayList and deletes
// * the chat room id corresponding to the deleted game from the
// * database. This will prevent the list of elements in available games
// * from getting too big. May have potential problems if a game has just
// * ended and new player searching for a game deletes the chatroom before
// * both players of that game have guessed. A possible solution would be
// * to introduce timestamps to each chatroom, then if the chatroom is more
// * than a certain age, it can be assumed that the game is over and then
// * deleted.
// * created: 01/04/2019 by C.Coady
// * last modified: 01/04/2019 by C.Coady
// */
//private void deleteFinishedGames(){
//    if(completeGames != null) {
//        //get a reference to the chat rooms section of the database
//        DatabaseReference chatRef = mDatabaseRef.child("availableGames");
//        for(int i = 0; i < completeGames.size(); i++){
//            //remove the chatroom from availableGames
//            chatRef.child((String)completeGames.get(i)).removeValue();
//        }
//    }
//}
//
///**
// * This method takes creates an availableGame which players can join.
// * A random game key is generated by firebase which is used to identify
// * the game 'chatRoomId'.
// * The status of the new chatroom is set to empty while we wait for
// * other players to join the game.
// * created: 21/03/2019 by C.Coady
// * last modified: 24/03/2019 by C.Coady
// */
//private boolean createGame(){
//    //get a reference to the chat rooms section of the database
//    DatabaseReference chatRef = mDatabaseRef.child("availableGames");
//    //create a new chatroom with a unique reference
//    chatRef = chatRef.push();
//    //update the chatroom id to the newly generated one
//    chatRoomId = chatRef.getKey();
//    //make this chatroom empty
//    chatRef.setValue("empty");
//    //TODO add some error checking if we fail to connect to the database
//    return true;
//}
//
///**
// * This method sets the gameState to 'complete' on the availableGames section
// * of the database and then uploads the messages to the database if the game
// * was against a bot those messages are only stored locally.
// * created: 21/03/2019 by C.Coady
// * last modified: 24/03/2019 by C.Coady
// */
//private boolean endGame(){
//    //get a reference to the chat rooms section of the database
//    DatabaseReference chatRef = mDatabaseRef.child("availableGames");
//    //make this chatroom complete
//    chatRef.child(chatRoomId).setValue("complete");
//    //if the game is against a bot, push messages to the database
//    if(!isHumanGame){
//        uploadMessages();
//    }
//    //TODO add some error checking if we fail to connect to the database
//    return true;
//}
//
//private void detachListeners(){
//
//    if(mCurrentGameStatusListener != null) {
//        mDatabaseRef.child("availableGames").removeEventListener(mCurrentGameStatusListener);
//    }
//    if(mAvailableGameListener != null) {
//        mDatabaseRef.child("availableGames").removeEventListener(mAvailableGameListener);
//    }
//    if(mChatRoomMessageListener != null) {
//        mDatabaseRef.child("chatRooms").removeEventListener(mChatRoomMessageListener);
//    }
//}
//
//private void attachListeners(){
//    if(mCurrentGameStatusListener != null) {
//        mDatabaseRef.child("availableGames").addValueEventListener(mCurrentGameStatusListener);
//    }
//    if(mAvailableGameListener != null) {
//        mDatabaseRef.child("availableGames").addListenerForSingleValueEvent(mAvailableGameListener);
//    }
//    if(mChatRoomMessageListener != null) {
//        mDatabaseRef.child("chatRooms").addChildEventListener(mChatRoomMessageListener);
//    }
//}