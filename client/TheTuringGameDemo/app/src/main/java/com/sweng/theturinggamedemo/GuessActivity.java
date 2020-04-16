package com.sweng.theturinggamedemo;

import androidx.appcompat.app.AppCompatActivity;
import android.content.Intent;
import android.os.Bundle;
import android.util.Log;
import android.view.View;
import android.widget.Toast;
import org.json.JSONObject;
import java.io.IOException;
import java.util.Objects;
import okhttp3.Call;
import okhttp3.Callback;
import okhttp3.OkHttpClient;
import okhttp3.Request;
import okhttp3.RequestBody;
import okhttp3.Response;

public class GuessActivity extends AppCompatActivity {

    @Override
    protected void onCreate(Bundle savedInstanceState) {

        super.onCreate(savedInstanceState);
        setContentView(R.layout.activity_guess);
        Objects.requireNonNull(getSupportActionBar()).hide();

        findViewById(R.id.guess_button_ai).setOnClickListener(new View.OnClickListener() {
            @Override
            public void onClick(View v) {
                submitGuess(0);
            }
        });

        findViewById(R.id.guess_button_human).setOnClickListener(new View.OnClickListener() {
            @Override
            public void onClick(View v) {
                submitGuess(1);
            }
        });

        findViewById(R.id.guess_button_flag).setOnClickListener(new View.OnClickListener() {
            @Override
            public void onClick(View v) {
                flagConversation();
            }
        });

    }

    private void submitGuess(int guess) {

        String route = Globals.API.BASE_URL + String.format(Globals.API.CONVERSATION_GUESS, Globals.conversationId);
        String json = String.format("{'guess': %d}", guess);

        RequestBody body = RequestBody.create(json, Globals.JSON);
        OkHttpClient client = new OkHttpClient();
        Request request = new Request.Builder().url(route).post(body).build();

        client.newCall(request).enqueue(new Callback() {

            @Override
            public void onFailure(Call call, IOException e) {
                startActivity(new Intent(GuessActivity.this, ResultActivity.class));
                call.cancel();
            }

            @Override
            public void onResponse(Call call, Response response) throws IOException {

                try {

                    JSONObject json = new JSONObject(response.body().string());
                    int result = json.getInt("result");
                    Globals.guessResult = (result == 1);

                    startActivity(new Intent(GuessActivity.this, ResultActivity.class));

                } catch (Exception e) {
                    finish();
                }

            }

        });

    }

    void flagConversation() {

        String route = Globals.API.BASE_URL + String.format(Globals.API.CONVERSATION_FLAG, Globals.conversationId);

        OkHttpClient client = new OkHttpClient();
        Request request = new Request.Builder().url(route).build();

        client.newCall(request).enqueue(new Callback() {

            @Override
            public void onFailure(Call call, IOException e) {

                GuessActivity.this.runOnUiThread(new Runnable() {
                    public void run() {
                        Toast.makeText(GuessActivity.this, "Sorry, we could not flag this conversation", Toast.LENGTH_SHORT).show();
                    }
                });

                call.cancel();
            }

            @Override
            public void onResponse(Call call, Response response) throws IOException {

                try {
                    GuessActivity.this.runOnUiThread(new Runnable() {
                        public void run() {
                            Toast.makeText(GuessActivity.this, "Conversation has been flagged", Toast.LENGTH_SHORT).show();
                        }
                    });
                } catch (Exception e) {
                    finish();
                }

            }

        });

    }

}
