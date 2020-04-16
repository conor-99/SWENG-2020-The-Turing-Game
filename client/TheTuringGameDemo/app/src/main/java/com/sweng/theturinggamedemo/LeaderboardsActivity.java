package com.sweng.theturinggamedemo;

import androidx.appcompat.app.AppCompatActivity;
import android.os.Bundle;
import android.widget.TextView;
import org.json.JSONArray;
import org.json.JSONObject;
import java.io.IOException;
import java.util.Objects;
import okhttp3.Call;
import okhttp3.Callback;
import okhttp3.OkHttpClient;
import okhttp3.Request;
import okhttp3.Response;

public class LeaderboardsActivity extends AppCompatActivity {

    private TextView textView;

    @Override
    protected void onCreate(Bundle savedInstanceState) {

        super.onCreate(savedInstanceState);
        setContentView(R.layout.activity_leaderboards);
        Objects.requireNonNull(getSupportActionBar()).hide();

        textView = (TextView) findViewById(R.id.textView3);
        getLeaderboards();

    }

    private void getLeaderboards() {

        String route = Globals.API.BASE_URL + Globals.API.LEADERBOARDS;

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

                    StringBuilder resultString = new StringBuilder();
                    JSONObject json = new JSONObject(response.body().string());
                    JSONArray rankings = json.getJSONArray("users");

                    for (int i = 0; i < rankings.length() && i < 20; i++) {
                        JSONObject ranking = (JSONObject) rankings.get(i);

                        int rankingRank = ranking.getInt("rank");
                        String rankingPad = (rankingRank < 10) ? "0" : "";
                        String rankingName = ranking.getString("username");
                        double rankingScore = ranking.getDouble("score");

                        String rankingString = String.format("%s%d.     %s     (%.2f)\n", rankingPad, rankingRank, rankingName, rankingScore);
                        resultString.append(rankingString);

                    }

                    textView.setText(resultString.toString());

                } catch (Exception e) {
                    finish();
                }

            }

        });

    }

}
