package com.sweng.theturinggame;

import androidx.appcompat.app.AppCompatActivity;

import android.content.Intent;

import android.os.Bundle;
import android.view.View;

import javax.xml.transform.Result;

public class DecisionActivity extends AppCompatActivity {

    @Override
    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        setContentView(R.layout.activity_decision);

        //if "Human Player' button clicked...
        findViewById(R.id.hp_button).setOnClickListener(new View.OnClickListener(){
            @Override
            public void onClick(View v){
                openResult("Human");
            }
        });

        //if 'AI Player' button clicked...
        findViewById(R.id.ai_button).setOnClickListener(new View.OnClickListener(){
            @Override
            public void onClick(View v){
                openResult("Bot");
            }
        });
    }

    public void openResult(String choice){
        Intent intent = new Intent(this, Result.class);
        Bundle c = new Bundle();
        c.putString("choice", choice);
        intent.putExtras(c);
        startActivity(intent);
        finish();
    }
}
