import java.util.HashMap;
import java.io.BufferedReader;
import java.io.FileReader;
import java.io.IOException;
import java.util.ArrayList;
import java.util.List;
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
    	double prob=0.1;
        Hashtable<Character, String> keyApprox = new Hashtable<Character, String>();

        keyApprox.put('q', "qwasedzx");
        keyApprox.put('w', "wqesadrfcx");
        keyApprox.put('e', "ewrsfdqazxcvgt");
        keyApprox.put('r', "retdgfwsxcvgt");
        keyApprox.put('t', "tryfhgedcvbnju");
        keyApprox.put('y', "ytugjhrfvbnji");
        keyApprox.put('u', "uyihkjtgbnmlo");
        keyApprox.put('i', "iuojlkyhnmlp");
        keyApprox.put('o', "oipklujm");
        keyApprox.put('p', "plo['ik");
        keyApprox.put('a', "aqszwxwdce");
        keyApprox.put('s', "swxadrfv");
        keyApprox.put('d', "decsfaqgbv");
        keyApprox.put('f', "fdgrvwsxyhn");
        keyApprox.put('g', "gtbfhedcyjn");
        keyApprox.put('h', "hyngjfrvkim");
        keyApprox.put('j', "jhknugtblom");
        keyApprox.put('k', "kjlinyhn");
        keyApprox.put('l', "lokmpujn");
        keyApprox.put('z', "zaxsvde");
        keyApprox.put('x', "xzcsdbvfrewq");
        keyApprox.put('c', "cxvdfzswergb");
        keyApprox.put('v', "vcfbgxdertyn");
        keyApprox.put('b', "bvnghcftyun");
        keyApprox.put('n', "nbmhjvgtuik");
        keyApprox.put('m', "mnkjloik");
        keyApprox.put(' ', " ");

        int probOfTypo = (int)(prob * 100);
        String returnText = input;
        while(input.equals(returnText)){
            char newletter;
            returnText = "";
            for(int letter = 0; letter<input.length(); letter++){
                char lcletter = input.charAt(letter);
                lcletter = Character.toLowerCase(lcletter);
                if(!keyApprox.containsKey(lcletter)){
                    newletter = lcletter;
                }
                else{
                    int x = (int)(Math.random()*((1000-0)+1))+0;
                    if(x<=probOfTypo){
                        String alternatives = keyApprox.get(lcletter);
                        Random rand = new Random(); 
                        int index = rand.nextInt(alternatives.length());
                        newletter = alternatives.charAt(index);
                    }
                    else{
                        newletter=lcletter;
                    }
                }
                //back to original case
                if(lcletter!=input.charAt(letter)){
                    newletter = Character.toUpperCase(newletter);
                }
                returnText+=newletter;    
            }
        }
        return returnText;
    }
    
    
    // Get a random name - Kishore
    public static String getName() {
    	String name = "";
    	String filePath = "data/names.txt";  	
	    String[] words = null;
		
	    try {
			words = readLines(filePath);
		} catch (IOException e) {
			// TODO Auto-generated catch block
			e.printStackTrace();
		}
	     
		Random r = new Random();
		int low = 0;
		int high = 4944;
		int result = r.nextInt(high-low) + low;

		name = words[result];
    	    
		return name;
   }

    public static String[] readLines(String filename) throws IOException {
        FileReader fileReader = new FileReader(filename);
        BufferedReader bufferedReader = new BufferedReader(fileReader);
        List<String> lines = new ArrayList<String>();
        String line = null;
        while ((line = bufferedReader.readLine()) != null) {
            lines.add(line);
        }
        bufferedReader.close();
        return lines.toArray(new String[lines.size()]);
    }
    


}
