/* Reference: https://github.com/ScaleDrone/android-chat-tutorial */

package com.sweng.theturinggamedemo;

import androidx.appcompat.app.AppCompatActivity;
import android.content.Intent;
import android.os.Bundle;
import android.util.Log;
import android.view.View;
import android.widget.EditText;
import android.widget.ImageButton;
import android.widget.ListView;
import android.widget.TextView;
import android.widget.Toast;

import org.json.JSONArray;
import org.json.JSONObject;
import java.io.IOException;
import java.util.Objects;
import java.util.Timer;
import java.util.TimerTask;
import okhttp3.Call;
import okhttp3.Callback;
import okhttp3.OkHttpClient;
import okhttp3.Request;
import okhttp3.RequestBody;
import okhttp3.Response;

public class PlayActivity extends AppCompatActivity {

    private MessageAdapter messageAdapter;
    private ListView messageView;
    private EditText textInput;
    private TextView textTyping;
    private int messageNum = 1;
    private int countdown = 30;
    private String oldText = "";

    @Override
    protected void onCreate(Bundle savedInstanceState) {

        super.onCreate(savedInstanceState);
        setContentView(R.layout.activity_play);
        Objects.requireNonNull(getSupportActionBar()).hide();

        messageAdapter = new MessageAdapter(this);
        messageView = findViewById(R.id.play_list_messages);
        messageView.setAdapter(messageAdapter);

        ImageButton sendButton = findViewById(R.id.play_input_send);
        textInput = findViewById(R.id.play_input_text);
        textTyping = findViewById(R.id.play_text_typing);

        sendButton.setOnClickListener(new View.OnClickListener() {
            @Override
            public void onClick(View v) {

                String messageText = textInput.getText().toString().trim();

                if (messageText.length() != 0) {
                    addMessage(true, messageText);
                    textInput.getText().clear();
                    sendMessage(messageText);
                    messageNum++;
                }

            }
        });

        TextView timerText = findViewById(R.id.play_text_timer);
        Timer timer = new Timer();
        timer.scheduleAtFixedRate(new TimerTask() {
            @Override
            public void run() {

                if (countdown < 0) {

                    timer.cancel();
                    try {
                        Thread.sleep(1000);
                    } catch (Exception ignored) { }

                    endConversation();

                } else {

                    String padding = (countdown < 10) ? "0" : "";
                    timerText.setText(String.format("00:%s%d", padding, countdown));
                    countdown--;

                    if (textInput.getText().toString().trim() != oldText)
                        setTyping();

                    getTyping();
                    getMessages();

                }

            }
        }, 1000, 1000);

    }

    private void addMessage(boolean ourMessage, String text) {

        Message message = new Message(ourMessage, text);

        runOnUiThread(() -> {
            messageAdapter.add(message);
            messageView.setSelection(messageView.getCount() - 1);
        });

    }

    private void sendMessage(String messageText) {

        String route = Globals.API.BASE_URL + String.format(Globals.API.CONVERSATION_SEND, Globals.conversationId);
        String json = String.format("{'text': %s}", messageText);

        RequestBody body = RequestBody.create(json, Globals.JSON);
        OkHttpClient client = new OkHttpClient();
        Request request = new Request.Builder().url(route).post(body).build();

        client.newCall(request).enqueue(new Callback() {

            @Override
            public void onFailure(Call call, IOException e) {

                PlayActivity.this.runOnUiThread(new Runnable() {
                    public void run() {
                        Toast.makeText(PlayActivity.this, "Sorry, there was an error sending your message", Toast.LENGTH_SHORT).show();
                    }
                });

                call.cancel();

            }

            @Override
            public void onResponse(Call call, Response response) throws IOException {

                try {
                    // do nothing
                } catch (Exception e) {
                    finish();
                }

            }

        });

    }

    private void getMessages() {

        String route = Globals.API.BASE_URL + String.format(Globals.API.CONVERSATION_RECEIVE, Globals.conversationId);

        OkHttpClient client = new OkHttpClient();
        Request request = new Request.Builder().url(route).build();

        client.newCall(request).enqueue(new Callback() {

            @Override
            public void onFailure(Call call, IOException e) {
                call.cancel();
            }

            @Override
            public void onResponse(Call call, Response response) throws IOException {

                try {

                    JSONObject json = new JSONObject(response.body().string());
                    JSONArray messages = json.getJSONArray("messages");

                    for (int i = 0; i < messages.length(); i++) {
                        String messageText = messages.getJSONObject(i).getString("text");
                        messageText = Personality.apply(Globals.conversationId, messageText);
                        addMessage(false, messageText);
                    }

                } catch (Exception e) {
                    finish();
                }

            }

        });

    }

    private void getTyping() {

        String route = Globals.API.BASE_URL + String.format(Globals.API.CONVERSATION_TYPING_GET, Globals.conversationId);

        OkHttpClient client = new OkHttpClient();
        Request request = new Request.Builder().url(route).build();

        client.newCall(request).enqueue(new Callback() {

            @Override
            public void onFailure(Call call, IOException e) {
                call.cancel();
            }

            @Override
            public void onResponse(Call call, Response response) throws IOException {

                try {

                    JSONObject json = new JSONObject(response.body().string());
                    int result = json.getInt("typing");

                    runOnUiThread(new Runnable() {
                        @Override
                        public void run() {
                            if (result == 1) textTyping.setVisibility(View.VISIBLE);
                            else textTyping.setVisibility(View.GONE);
                        }
                    });

                } catch (Exception e) {
                    finish();
                }

            }

        });

    }

    private void setTyping() {

        String route = Globals.API.BASE_URL + String.format(Globals.API.CONVERSATION_TYPING_SET, Globals.conversationId);

        OkHttpClient client = new OkHttpClient();
        Request request = new Request.Builder().url(route).build();

        client.newCall(request).enqueue(new Callback() {

            @Override
            public void onFailure(Call call, IOException e) {
                call.cancel();
            }

            @Override
            public void onResponse(Call call, Response response) throws IOException {
                try {
                    // do nothing
                } catch (Exception e) {
                    finish();
                }
            }

        });

    }

    private void endConversation() {

        String route = Globals.API.BASE_URL + String.format(Globals.API.CONVERSATION_FLAG, Globals.conversationId);

        OkHttpClient client = new OkHttpClient();
        Request request = new Request.Builder().url(route).build();

        client.newCall(request).enqueue(new Callback() {

            @Override
            public void onFailure(Call call, IOException e) {

                PlayActivity.this.runOnUiThread(new Runnable() {
                    public void run() {
                        Toast.makeText(PlayActivity.this, "Sorry, something went wrong while trying to end the conversation", Toast.LENGTH_SHORT).show();
                    }
                });

                call.cancel();

            }

            @Override
            public void onResponse(Call call, Response response) throws IOException {

                try {
                    startActivity(new Intent(PlayActivity.this, GuessActivity.class));
                } catch (Exception e) {
                    finish();
                }

            }

        });

    }

}
