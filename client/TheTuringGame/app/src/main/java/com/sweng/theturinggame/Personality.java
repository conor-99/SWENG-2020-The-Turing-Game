// Class worked on by the AI Group: Claire McNamara

package com.sweng.theturinggame;

import java.util.HashMap;
import java.util.Random;

public class Personality {

    private static HashMap<Integer, BotPersonality> botPersonalities = new HashMap<>();

    public static String apply(int conversationId, String message) {
        BotPersonality personality;
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
        return personality.addPersonality(message);
    }

}