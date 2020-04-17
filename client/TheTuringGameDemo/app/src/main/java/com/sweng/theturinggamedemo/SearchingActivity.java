package com.sweng.theturinggamedemo;

import androidx.appcompat.app.AppCompatActivity;
import android.content.Intent;
import android.os.Bundle;
import org.json.JSONObject;
import java.io.IOException;
import java.util.Objects;
import okhttp3.Call;
import okhttp3.Callback;
import okhttp3.OkHttpClient;
import okhttp3.Request;
import okhttp3.Response;

public class SearchingActivity extends AppCompatActivity {

    @Override
    protected void onCreate(Bundle savedInstanceState) {

        super.onCreate(savedInstanceState);
        setContentView(R.layout.activity_searching);
        Objects.requireNonNull(getSupportActionBar()).hide();

        startConversation();

    }

    private void startConversation() {

        String route = Globals.API.BASE_URL + Globals.API.CONVERSATION_START;

        OkHttpClient client = new OkHttpClient();
        Request request = new Request.Builder().url(route).build();

        // Make the API start conversation request
        client.newCall(request).enqueue(new Callback() {

            @Override
            public void onFailure(Call call, IOException e) {
                call.cancel();
            }

            @Override
            public void onResponse(Call call, Response response) throws IOException {

                try {
                    JSONObject json = new JSONObject(response.body().string());
                    Globals.conversationId = json.getInt("cid"); // set the conversation ID of this conversation
                    startActivity(new Intent(SearchingActivity.this, PlayActivity.class));
                } catch (Exception e) {
                    finish();
                }

            }

        });

    }

}
