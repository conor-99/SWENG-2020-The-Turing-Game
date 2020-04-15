package com.sweng.theturinggamedemo;

import androidx.appcompat.app.AppCompatActivity;

import android.content.Intent;
import android.os.Bundle;
import android.view.View;

import java.util.Objects;

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
                // make API request
            }
        });

    }

    private void submitGuess(int guess) {

        // make API request to submit guess and set result to response

        int result = 0;

        Intent intent = new Intent(GuessActivity.this, ResultActivity.class);
        Bundle b = new Bundle();
        b.putInt("result", result);
        intent.putExtras(b);
        startActivity(intent);

    }

}
