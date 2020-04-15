/* Reference: https://github.com/ScaleDrone/android-chat-tutorial */

package com.sweng.theturinggamedemo;

import androidx.appcompat.app.AppCompatActivity;
import android.content.Intent;
import android.os.Bundle;
import android.view.View;
import android.widget.EditText;
import android.widget.ImageButton;
import android.widget.ListView;
import android.widget.TextView;
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
import okhttp3.Response;

public class PlayActivity extends AppCompatActivity {

    private MessageAdapter messageAdapter;
    private ListView messageView;
    private int messageNum = 1;
    private int countdown = 30;

    @Override
    protected void onCreate(Bundle savedInstanceState) {

        super.onCreate(savedInstanceState);
        setContentView(R.layout.activity_play);
        Objects.requireNonNull(getSupportActionBar()).hide();

        messageAdapter = new MessageAdapter(this);
        messageView = findViewById(R.id.play_list_messages);
        messageView.setAdapter(messageAdapter);

        EditText textInput = findViewById(R.id.play_input_text);
        ImageButton sendButton = findViewById(R.id.play_input_send);

        sendButton.setOnClickListener(new View.OnClickListener() {
            @Override
            public void onClick(View v) {

                String messageText = textInput.getText().toString().trim();

                if (messageText.length() != 0) {

                    addMessage(true, messageText);
                    textInput.getText().clear();
                    getMessages(messageNum);

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
                    startActivity(new Intent(PlayActivity.this, GuessActivity.class));
                } else {
                    String padding = (countdown < 10) ? "0" : "";
                    timerText.setText(String.format("00:%s%d", padding, countdown));
                    countdown--;
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

    private void getMessages(int messageNum) {

        String route = Globals.BASE_URL + String.format("message%d.json", messageNum);

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
                        Thread.sleep(1000);
                        String messageText = messages.getJSONObject(i).getString("text");
                        addMessage(false, messageText);
                    }

                } catch (Exception e) {
                    finish();
                }

            }

        });

    }

}

