package com.sweng.theturinggamedemo;

import androidx.appcompat.app.AppCompatActivity;

import android.os.Bundle;
import android.widget.TextView;

import java.util.Objects;

public class LeaderboardsActivity extends AppCompatActivity {

    @Override
    protected void onCreate(Bundle savedInstanceState) {

        super.onCreate(savedInstanceState);
        setContentView(R.layout.activity_leaderboards);
        Objects.requireNonNull(getSupportActionBar()).hide();

        TextView textView = (TextView) findViewById(R.id.textView3);

        // make API request and update textView

    }

}
