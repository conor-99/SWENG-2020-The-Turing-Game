public class Main {

    public static void main(String args[]){
        String result = Personality.apply(123, "Hello, you are sad. I am happy");
        System.out.println(result);
        result = Personality.apply(123, "hows your life going? I am happy");
        System.out.println(result);
    }
}