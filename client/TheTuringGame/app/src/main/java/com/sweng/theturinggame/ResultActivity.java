package com.sweng.theturinggame;

import androidx.appcompat.app.AppCompatActivity;

import android.content.Intent;
import android.os.Bundle;
import android.view.View;

public class ResultActivity extends AppCompatActivity {

        private int user_choice;
        private int correct_choice; //fetch correct answer from server

        @Override
        protected void onCreate(Bundle savedInstanceState) {
            super.onCreate(savedInstanceState);
            setContentView(R.layout.activity_result);

            Bundle c = getIntent().getExtras();
            user_choice = c.getInt("choice");

            if(user_choice == correct_choice){
                findViewById(R.id.correct_title).setVisibility(View.VISIBLE);
                //also update score;
            }

            else{
                findViewById(R.id.incorrect_title).setVisibility(View.VISIBLE);
            }

            //when 'Complete Our Survey' button clicked...
            findViewById(R.id.survey_button).setOnClickListener(new View.OnClickListener(){
                @Override
                public void onClick(View v){
                    startActivity(new Intent(ResultActivity.this, MainActivity.class)); //replace with survey activity
                }
            });

            //when 'Main Menu' button clicked...
            findViewById(R.id.home_button).setOnClickListener(new View.OnClickListener(){
                @Override
                public void onClick(View v){
                    startActivity(new Intent(ResultActivity.this, MainActivity.class));
                }
            });

        }
}
