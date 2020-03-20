package com.sweng.theturinggame;

import android.os.AsyncTask;
import android.util.Log;

import org.json.JSONObject;

import java.io.BufferedReader;
import java.io.InputStreamReader;
import java.net.HttpURLConnection;
import java.net.URL;
import java.util.Date;
import java.util.Dictionary;

public class API {

    public static int startConversation() {

        String route = "conversation_start.json"; // for testing
        //String route = "conversation/start";

        RequestParameters params = new RequestParameters(route);
        new Request().execute(params);

        return 123;

    }

    public static void endConversation(int conversationId, int guess) {

        String route = String.format("conversation/end/%d", conversationId);

    }

    public static void flagConversation(int conversationId) {

        String route = String.format("conversation/flag/%d", conversationId);

    }

    public static void sendMessage(int conversationId, String text) {

        String route = String.format("conversation/send/%d", conversationId);

    }

    private static Message receiveMessageRaw(int conversationId) {

        String route = "conversation_receive.json"; // for testing
        //String route = String.format("conversation/receive/%d", conversationId);

        RequestParameters params = new RequestParameters(route);
        new Request().execute(params);

        return new Message(0, "", new Date());

    }

    public static Message receiveMessage(int conversationId) {

        Message message = receiveMessageRaw(conversationId);
        message.text = Personality.apply(conversationId, message.text);
        return message;

    }

    public static void guessConversantType(int conversationId, ConversantType type) {

    }

    public static ConversantType getConversantType(int conversationId) {
        return ConversantType.Bot;
    }

    public static void submitSurveyResults(int rating, String feedback) {

    }

    public static UserRanking[] getLeaderboards() {

        String route = "leaderboards.json"; // for testing
        //String route = "leaderboards";

        RequestParameters params = new RequestParameters(route);
        new Request().execute(params);

        return new UserRanking[] { new UserRanking(0, "user1", 0.95) };

    }

    static class Request extends AsyncTask<RequestParameters, Void, JSONObject> {

        private String baseUrl = "http://macamhlaoibh.com/api/";

        @Override
        protected JSONObject doInBackground(RequestParameters... paramsArray) {

            RequestParameters params = paramsArray[0];

            if (params.type == RequestType.GET)
                return httpGet(params.route);
            else
                return httpPost(params.route, params.postParams);

        }

        @Override
        protected void onPostExecute(JSONObject response) {

        }

        private JSONObject httpGet(String route) {

            JSONObject response = null;

            try {

                URL url = new URL(baseUrl + route);
                HttpURLConnection conn = (HttpURLConnection) url.openConnection();
                conn.setRequestMethod("GET");

                StringBuilder content = new StringBuilder();

                String line;
                BufferedReader in = new BufferedReader(new InputStreamReader(conn.getInputStream()));
                while ((line = in.readLine()) != null)
                    content.append(line);
                in.close();

                conn.disconnect();

                Log.d("DEBUG", content.toString());

                response = new JSONObject(content.toString());

            } catch (Exception e) {
                Log.d("DEBUG", e.toString());
            }

            return response;

        }

        private JSONObject httpPost(String route, Dictionary<String, Object> params) {
            return null;
        }

    }

    static class RequestParameters {

        RequestType type;
        String route;
        Dictionary<String, Object> postParams;

        RequestParameters(String route, Dictionary<String, Object> postParams) {
            this.type = RequestType.POST;
            this.route = route;
            this.postParams = postParams;
        }

        RequestParameters(String route) {
            this.type = RequestType.GET;
            this.route = route;
            this.postParams = null;
        }

    }

    enum RequestType {
        GET,
        POST
    }

}
