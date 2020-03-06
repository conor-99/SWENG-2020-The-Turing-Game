package com.sweng.theturinggame;

import java.util.Date;

public class API {

    public static int StartConversation() {
        return 123;
    }

    public static void EndConversation(int conversationId, int guess) {

    }

    public static void FlagConversation(int conversationId) {

    }

    public static void SendMessage(int conversationId, String text) {

    }

    public static Message ReceiveMessage(int conversationId) {
        return new Message(0, "", new Date());
    }

    public static UserRanking[] GetLeaderboards() {
        return new UserRanking[] { new UserRanking(0, "user1", 0.95) };
    }

}
