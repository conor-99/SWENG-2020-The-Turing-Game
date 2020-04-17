package com.sweng.theturinggamedemo;

import androidx.annotation.NonNull;
import androidx.annotation.Nullable;
import androidx.appcompat.app.AppCompatActivity;

import android.content.Intent;
import android.os.Bundle;
import android.view.View;
import android.widget.Toast;

import com.google.android.gms.auth.api.signin.*;
import com.google.android.gms.common.SignInButton;
import com.google.android.gms.common.api.Api;
import com.google.android.gms.common.api.ApiException;
import com.google.android.gms.tasks.OnCompleteListener;
import com.google.android.gms.tasks.Task;
import com.google.firebase.auth.AuthCredential;
import com.google.firebase.auth.AuthResult;
import com.google.firebase.auth.FirebaseAuth;
import com.google.firebase.auth.FirebaseUser;
import com.google.firebase.auth.GoogleAuthProvider;

import java.util.Objects;

public class Authentication extends AppCompatActivity {

    private SignInButton signInButton;
    private GoogleSignInClient mGoogleSignInClient;
    private FirebaseAuth mAuth;
    private int RC_SIGN_IN = 1;

    @Override
    protected void onCreate(Bundle savedInstanceState) {

        super.onCreate(savedInstanceState);
        setContentView(R.layout.activity_authentication);
        Objects.requireNonNull(getSupportActionBar()).hide();

        signInButton = findViewById(R.id.auth_button_sign_in);

        // Initialise authentication
        mAuth = FirebaseAuth.getInstance();
        GoogleSignInOptions gso = new GoogleSignInOptions.Builder(GoogleSignInOptions.DEFAULT_SIGN_IN)
                .requestIdToken(getString(R.string.default_web_client_id))
                .requestEmail()
                .build();
        mGoogleSignInClient = GoogleSignIn.getClient(this, gso);

        signInButton.setOnClickListener(new View.OnClickListener() {
            @Override
            public void onClick(View view) {
                startActivityForResult(mGoogleSignInClient.getSignInIntent(), RC_SIGN_IN);
            }
        });

    }

    @Override
    protected void onStart() {

        super.onStart();
        FirebaseUser currentUser = mAuth.getCurrentUser();

        // Check if a user is signed in
        if (currentUser != null)
            updateUI(currentUser);

    }

    @Override
    protected void onActivityResult(int requestCode, int resultCode, @Nullable Intent data) {

        super.onActivityResult(requestCode, resultCode, data);

        // Handle result of sign-in activity
        if (requestCode == RC_SIGN_IN) {

            Task<GoogleSignInAccount> task = GoogleSignIn.getSignedInAccountFromIntent(data);

            try {
                GoogleSignInAccount account = task.getResult(ApiException.class);
                firebaseAuth(account);
            } catch (ApiException e) {
                firebaseAuth(null);
            }

        }

    }

    private void firebaseAuth(GoogleSignInAccount account) {

        AuthCredential credential = GoogleAuthProvider.getCredential(account.getIdToken(), null);

        // Use the sign-in account to get a Firebase user
        mAuth.signInWithCredential(credential).addOnCompleteListener(this, new OnCompleteListener<AuthResult>() {
            @Override
            public void onComplete(@NonNull Task<AuthResult> task) {
                if (task.isSuccessful()) {
                    FirebaseUser user = mAuth.getCurrentUser();
                    updateUI(user);
                } else {
                    updateUI(null);
                }
            }
        });

    }

    private void updateUI(FirebaseUser user) {

        GoogleSignInAccount account = GoogleSignIn.getLastSignedInAccount(getApplicationContext());

        // If the user is signed in go to the main activity
        if (account != null) {
            Contact.email = account.getEmail();
            startActivity(new Intent(Authentication.this, MainActivity.class));
        }
        else {
            Toast.makeText(Authentication.this, "Could not sign in", Toast.LENGTH_SHORT).show();
        }

    }

}
