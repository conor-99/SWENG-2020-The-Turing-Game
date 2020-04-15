// Class worked on by the AI Group: Claire McNamara

package com.sweng.theturinggamedemo;

import java.util.HashMap;
import java.util.Random;

public class Personality {

    // HashMap to store which user is contacting which bot personality for continuity.
    private static HashMap<Integer, BotPersonality> botPersonalities = new HashMap<>();

    // Applies the post processing changes to the AI generated response.
    public static String apply(int conversationId, String message) {
        BotPersonality personality;

        // If the conversation is a new one and the ID has not already been stored - create a new
        // personality with a new random name and add the conversation ID and personality to the
        // HashMap.
        if (!botPersonalities.containsKey(conversationId)){
            Random rand = new Random();
            int personalityNum = rand.nextInt((3 - 1) + 1) + 1;
            switch (personalityNum) {
                case 1:
                    personality = new Adult("tmp");
                    break;
                case 2:
                    personality = new Teenager("tmp");
                    break;
                default:
                    personality = new YoungAdult("tmp");
            }
            botPersonalities.put(conversationId, personality);
        } else{
            personality = botPersonalities.get(conversationId);
        }

        // Returns the message with the relevant changes made to it.
        return personality.addPersonality(message);
    }

}