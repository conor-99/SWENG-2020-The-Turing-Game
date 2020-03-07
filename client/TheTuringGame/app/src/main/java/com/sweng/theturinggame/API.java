package com.sweng.theturinggame;

import org.json.JSONObject;
import java.util.Date;

public class API {

    public static int startConversation() {
        return 123;
    }

    public static void endConversation(int conversationId, int guess) {

    }

    public static void flagConversation(int conversationId) {

    }

    public static void sendMessage(int conversationId, String text) {

    }

    public static Message receiveMessage(int conversationId) {

        JSONObject response = RequestHandler.httpGet("leaderboards");

        return new Message(0, "", new Date());

    }

    public static UserRanking[] getLeaderboards() {
        return new UserRanking[] { new UserRanking(0, "user1", 0.95) };
    }

}
