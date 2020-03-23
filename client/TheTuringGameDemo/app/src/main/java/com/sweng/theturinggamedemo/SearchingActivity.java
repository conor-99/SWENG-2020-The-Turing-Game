package com.sweng.theturinggamedemo;

import androidx.appcompat.app.AppCompatActivity;

import android.content.Intent;
import android.os.AsyncTask;
import android.os.Bundle;
import android.util.Log;

import org.jetbrains.annotations.NotNull;
import org.json.JSONObject;

import java.io.IOException;
import java.util.Objects;
import java.util.concurrent.ExecutionException;

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

        String route = Constants.BASE_URL + "start.json";

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
                    int conversationId = json.getInt("cid");
                    startActivity(new Intent(SearchingActivity.this, PlayActivity.class));
                } catch (Exception e) {
                    finish();
                }

            }

        });

    }

}
