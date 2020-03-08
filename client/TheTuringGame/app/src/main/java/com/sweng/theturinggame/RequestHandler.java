package com.sweng.theturinggame;

import android.util.Log;

import org.json.JSONObject;

import java.io.BufferedReader;
import java.io.InputStreamReader;
import java.net.HttpURLConnection;
import java.net.URL;
import java.util.Dictionary;

public class RequestHandler {

    private static String baseUrl = "http://127.0.0.1:1234/api/";

    public static JSONObject httpGet(String route) {

        JSONObject response = null;

        try {

            URL url = new URL(baseUrl + route);
            HttpURLConnection conn = (HttpURLConnection) url.openConnection();
            conn.setRequestMethod("GET");

            StringBuffer content = new StringBuffer();

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

    public static JSONObject httpPost(String route, Dictionary<String, Object> params) {
        return null;
    }

}
