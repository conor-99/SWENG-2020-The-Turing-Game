package com.sweng.theturinggame;

import androidx.appcompat.app.AppCompatActivity;

import android.content.Intent;
import android.os.Bundle;
import android.view.View;

public class ResultActivity extends AppCompatActivity {

        private String user_choice;
        private String correct_choice;

        @Override
        protected void onCreate(Bundle savedInstanceState) {
            super.onCreate(savedInstanceState);
            setContentView(R.layout.activity_result);

            Bundle c = getIntent().getExtras();
            user_choice = c.getString("choice");
            correct_choice = API.getConversantType().toString();

            //if correct decision made...
            if(user_choice.equals(correct_choice)){
                findViewById(R.id.incorrect_title).setVisibility(View.INVISIBLE);
                findViewById(R.id.correct_title).setVisibility(View.VISIBLE);
                //also update score;
            }

            //if incorrect decision made...
            else{
                findViewById(R.id.correct_title).setVisibility(View.INVISIBLE);
                findViewById(R.id.incorrect_title).setVisibility(View.VISIBLE);
            }

            //when 'Complete Our Survey' button clicked...
            findViewById(R.id.survey_button).setOnClickListener(new View.OnClickListener(){
                @Override
                public void onClick(View v){
                    startActivity(new Intent(ResultActivity.this, SurveyActivity.class));
                    finish();
                }
            });

            //when 'Main Menu' button clicked...
            findViewById(R.id.home_button).setOnClickListener(new View.OnClickListener(){
                @Override
                public void onClick(View v){
                    startActivity(new Intent(ResultActivity.this, MainActivity.class));
                    finish();
                }
            });

        }
}
