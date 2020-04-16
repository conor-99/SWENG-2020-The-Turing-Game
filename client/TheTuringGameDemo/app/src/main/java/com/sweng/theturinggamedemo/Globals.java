package com.sweng.theturinggamedemo;

import okhttp3.MediaType;

class Globals {

    static final String TAG = "DEMO_DEBUG";
    static final MediaType JSON = MediaType.parse("application/json; charset=utf-8");

    static int conversationId = Integer.MAX_VALUE;
    static boolean guessResult = false;

    class API {

        static final String BASE_URL = "https://mccaulco.pythonanywhere.com/api";

        static final String CONVERSATION_START = "/conversation/start";
        static final String CONVERSATION_END = "/conversation/end/%d";
        static final String CONVERSATION_FLAG = "/conversation/flag/%d";
        static final String CONVERSATION_GUESS = "/conversation/guess/%d";
        static final String CONVERSATION_SEND = "/conversation/send/%d";
        static final String CONVERSATION_RECEIVE = "/conversation/receive/%d";
        static final String CONVERSATION_TYPING_SET = "/conversation/typing/set/%d";
        static final String CONVERSATION_TYPING_GET = "/conversation/typing/get/%d";
        static final String LEADERBOARDS = "/leaderboards";

    }

}
