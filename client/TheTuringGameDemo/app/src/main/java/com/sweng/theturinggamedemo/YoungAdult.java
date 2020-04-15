// Class worked on by the AI Group: Claire McNamara

package com.sweng.theturinggamedemo;

import java.util.HashMap;
import java.util.Iterator;
import java.util.Map;
import java.util.Random;
import java.util.regex.Pattern;

public class YoungAdult extends BotPersonality {

    public int age, probSpellingMistake;
    private HashMap<String, char[]> emojis = new HashMap<>();

    public YoungAdult(String name) {
        super(name);
        Random rand = new Random();
        this.age = rand.nextInt((21 - 13) + 1) + 13;
        this.probSpellingMistake = rand.nextInt((5 - 1) + 1) + 5;
        createEmojiHashMap();
    }

    @Override
    public String addPersonality(String input){
        input = shortenWords(input);
        input = addEmpojis(input);
        return input;
    }

    public void createEmojiHashMap(){
        emojis.put("sad", ":(".toCharArray());
        emojis.put("happy", ":)".toCharArray());
        emojis.put("funny", ":')".toCharArray());
        emojis.put("love", "<3".toCharArray());
    }

    // Adds in slang into the AI's message.
    private String shortenWords(String input){
        HashMap<String, String>  shortenedWords = new HashMap<>();
        shortenedWords.put("for your information", "fyi");
        shortenedWords.put("okay", "kk");
        shortenedWords.put("ok", "kk");
        shortenedWords.put("easy", "ez");
        shortenedWords.put("see you", "cya");
        shortenedWords.put("very", "v");
        shortenedWords.put("because", "cuz");
        shortenedWords.put("to be honest", "tbh");
        shortenedWords.put("oh my god", "OMG");
        shortenedWords.put("boyfriend", "bf");
        shortenedWords.put("girlfriend", "gf");
        shortenedWords.put("awesome", "cool");
        shortenedWords.put("in trouble", "screwed");

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

    // Adds emojis where appropriate in a sentence i.e. after the first punctuation character, or at
    // the end of a sentence.
    public String addEmpojis(String input){
        Iterator iter = emojis.entrySet().iterator();
        boolean found = false;
        while (iter.hasNext() && !found){
            Map.Entry elem = (Map.Entry)iter.next();
            String word = (String)elem.getKey();
            if (input.indexOf(word) != -1){
                int index = input.indexOf(word) + word.length();
                input = findPunctuation(input, (char[])elem.getValue(), index);
                found = true;
            }
        }
        return input;
    }

    public String findPunctuation(String input, char[] emoji, int index){
        StringBuilder tmpInput = new StringBuilder(input);
        boolean found = false;
        for (int i = index; i < input.length() && !found; i++){
            if (checkPunctuation(Character.toString(input.charAt(i)))){
                tmpInput.insert(i+1, emoji, 0, 2);
                found = true;
            }
        }
        if (!found) tmpInput.append(emoji);
        input = tmpInput.toString();
        return input;
    }

    public Boolean checkPunctuation(String input){
        return Pattern.matches("[!.,]", input);
    }
}