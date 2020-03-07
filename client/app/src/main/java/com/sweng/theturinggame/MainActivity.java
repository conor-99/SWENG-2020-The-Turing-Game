package com.sweng.theturinggame;

import androidx.appcompat.app.AppCompatActivity;

import android.content.Intent;
import android.os.Bundle;
import android.view.View;

public class MainActivity extends AppCompatActivity {

    @Override
    protected void onCreate(Bundle savedInstanceState) {

        super.onCreate(savedInstanceState);
        setContentView(R.layout.activity_main);

        // when the 'Play' button is clicked go to 'TestActivity'
        findViewById(R.id.buttonPlay).setOnClickListener(new View.OnClickListener() {
            public void onClick(View v) {
                //startActivity(new Intent(MainActivity.this, TestActivity.class));
            }
        });

        // when the 'Leaderboards' button is clicked ...
        findViewById(R.id.buttonLeaderboards).setOnClickListener(new View.OnClickListener() {
            public void onClick(View v) {
                // to-do
            }
        });

        // when the 'Settings' button is clicked ...
        findViewById(R.id.buttonSettings).setOnClickListener(new View.OnClickListener() {
            public void onClick(View v) {
                // to-do
            }
        });

    }

}
