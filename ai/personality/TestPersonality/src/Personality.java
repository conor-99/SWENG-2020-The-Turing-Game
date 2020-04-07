import java.util.HashMap;
import java.util.Random;

public class Personality {

    private static HashMap<Integer, BotPersonality> botPersonalities = new HashMap<>();

    public static String apply(int conversationId, String message) {
        BotPersonality personality;
        if (!botPersonalities.containsKey(conversationId)){
            Random rand = new Random();
            int personalityNum = rand.nextInt((3 - 1) + 1) + 1;
            String name = getName();
            switch (personalityNum) {
                case 1:
                    personality = new Adult(name);
                    break;
                case 2:
                    personality = new Teenager(name);
                    break;
                default:
                    personality = new YoungAdult(name);
            }
            botPersonalities.put(conversationId, personality);
        } else{
            personality = botPersonalities.get(conversationId);
        }
        message = personality.addPersonality(message);
        message = addSpellingMistake(message);	
        return message;
    }
    
    // Add in the spelling mistakes - Luiz Fellipe
    public static String addSpellingMistake(String input) {
    	return input;
    }
    
    
    // Get a random name - Kishore
    public static String getName() {
    	String name = "";
    	return name;
    }

}
