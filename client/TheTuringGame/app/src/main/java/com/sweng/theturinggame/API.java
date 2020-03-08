package com.sweng.theturinggame;

import org.json.JSONObject;
import java.util.Date;

public class API {

    public static int startConversation() {

        JSONObject response = RequestHandler.httpGet("conversation/start");
        return 123;

    }

    public static void endConversation(int conversationId, int guess) {

        String route = String.format("conversation/end/%d", conversationId);
        //RequestHandler.httpPost(route, params);

    }

    public static void flagConversation(int conversationId) {

        String route = String.format("conversation/flag/%d", conversationId);
        RequestHandler.httpGet(route);

    }

    public static void sendMessage(int conversationId, String text) {

        String route = String.format("conversation/send/%d", conversationId);
        //RequestHandler.httpPost(route, params);

    }

    public static Message receiveMessage(int conversationId) {

        String route = String.format("conversation/receive/%d", conversationId);
        JSONObject response = RequestHandler.httpGet(route);

        return new Message(0, "", new Date());

    }

    public static UserRanking[] getLeaderboards() {

        JSONObject response = RequestHandler.httpGet("leaderboards");
        return new UserRanking[] { new UserRanking(0, "user1", 0.95) };

    }

}
