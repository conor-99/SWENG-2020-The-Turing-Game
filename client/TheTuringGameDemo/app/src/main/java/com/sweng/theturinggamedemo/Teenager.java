// Class worked on by the AI Group: Claire McNamara

package com.sweng.theturinggamedemo;

import java.util.HashMap;
import java.util.Random;

public class Teenager extends BotPersonality {

    public int age, probSpellingMistake;

    public Teenager(String name){
        super(name);
        Random rand = new Random();
        this.age = rand.nextInt((21 - 13) + 1) + 13;
        this.probSpellingMistake = rand.nextInt((5 - 1) + 1) + 5;
    }

    @Override
    public String addPersonality(String input){
        input = shortenWords(input);
        return input;
    }

    // Adds in slang into the AI's message.
    private String shortenWords(String input){
        HashMap<String, String>  shortenedWords = new HashMap<>();
        shortenedWords.put("your", "ur");
        shortenedWords.put("tonight", "2nite");
        shortenedWords.put("for your information", "fyi");
        shortenedWords.put("okay", "k");
        shortenedWords.put("ok", "k");
        shortenedWords.put("to", "2");
        shortenedWords.put("tomorrow", "2moro");
        shortenedWords.put("easy", "ez");
        shortenedWords.put("because", "cuz");
        shortenedWords.put("you", "u");

        String[] inputAr = input.split(" ");
        int wordIndex = 0;
        for (String word:inputAr) {
            if (shortenedWords.containsKey(word)){
                inputAr[wordIndex] = shortenedWords.get(word);
            }
            wordIndex++;
        }
        input = String.join(" ", inputAr);
        return input;
    }
}