import java.util.Random;

public class Adult extends BotPersonality {

    public int age, probSpellingMistake;

    public Adult(String name){
        super(name);
        Random rand = new Random();
        this.age = rand.nextInt((40 - 29) + 1) + 29;
        this.probSpellingMistake = rand.nextInt((7 - 5) + 1) + 5;
    }

    @Override
    public String addPersonality(String input){
    	input = addPuctuation(input);
        return input;
    }
    
    // Add punctuation to the string - Diego
    public static String addPuctuation(String input) {
        // Sentence Openers 
        input = input.replace("hello", "hello,");
        input = input.replace("hi", "hi!");
        input = input.replace("heya", "heya!");
        input = input.replace("hey", "hey,");
        input = input.replace("greetings", "greetings,");
        input = input.replace("good morning", "good morning,");
        input = input.replace("good evening", "good evening,");
        input = input.replace("good afternoon", "good afternoon!");
    

        // Words ending in nt 
        input = input.replace("isnt", "isn't");
        input = input.replace("cant", "can't");
        input = input.replace("wont" , "won't");
        input = input.replace("dont" , "don't");
        input = input.replace("would", "wouldn't");
        input = input.replace("hadnt", "hadn't");
        input = input.replace("aint", "ain't");
        input = input.replace("arent", "aren't");
        input = input.replace("didnt", "didn't");
        input = input.replace("doesnt" , "doesn't");
        input = input.replace("dont" , "don't");
        input = input.replace("dont", "don't");
        input = input.replace("hasnt", "hasn't");
        input = input.replace("shoudlnt", "shouldn't");
        input = input.replace("couldnt", "couldn't");
        input = input.replace("wasnt", "wasn't");
        input = input.replace("werent" , "were't");
        input = input.replace("wouldnt" , "wouldn't");

        //Questions
        String q1 = "what";
        String q2 = "when";
        String q3 = "where";
        String q4 = "which";
        String q5 = "who";
        String q6 = "whom";
        String q7 = "whose";
        String q8 = "why";
        String q9 = "how";

        if (input.contains(q1) || input.contains(q2) || input.contains(q3) 
            || input.contains(q4) || input.contains(q5) || input.contains(q6) 
            || input.contains(q7) || input.contains(q8)  || input.contains(q9)) 
            {
                input = input + "?";
            }

        else
        {
            input = input + ".";
        }


        //Other
        input = input.replace("however", "however,");
        input = input.replace("ill" , "i'll");
        input = input.replace("im", "i'm");
        return input;
    }
}