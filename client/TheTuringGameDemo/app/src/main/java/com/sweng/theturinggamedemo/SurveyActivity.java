package com.sweng.theturinggamedemo;

import androidx.appcompat.app.AppCompatActivity;

import android.content.Intent;
import android.os.Bundle;
import android.view.View;
import android.widget.AutoCompleteTextView;
import android.widget.Button;
import android.widget.RatingBar;

import java.util.Objects;

public class SurveyActivity extends AppCompatActivity {

    @Override
    protected void onCreate(Bundle savedInstanceState) {

        super.onCreate(savedInstanceState);
        setContentView(R.layout.activity_survey);
        Objects.requireNonNull(getSupportActionBar()).hide();

        // initiate rating bar and a button
        final RatingBar simpleRatingBar = (RatingBar) findViewById(R.id.ratingBar);
        final AutoCompleteTextView textView = (AutoCompleteTextView) findViewById(R.id.autoCompleteTextView2);
        Button submitButton = (Button) findViewById(R.id.button);

        // perform click event on button
        submitButton.setOnClickListener(new View.OnClickListener() {
            @Override
            public void onClick(View v) {
                Contact.submitSurveyResults(simpleRatingBar.getNumStars(), textView.getText().toString());
                startActivity(new Intent(SurveyActivity.this, MainActivity.class));
            }
        });

    }

}
