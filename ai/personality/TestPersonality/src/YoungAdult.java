// Class worked on by: Claire

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

    public String shortenWords(String input){
        return input;
    }

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
