import java.util.Scanner;
import java.util.regex.Matcher;
import java.util.regex.Pattern;

/**
 * CodeDefense
 * @author Caleb Krauter, Nathan Hinthorne, Trae Claar
 */
public class CodeDefense {
    
    public static void main(String[] args) {
        final String firstName = firstName();

    }

    // PROMPT FOR FIRST NAME
    // Between 1 and 50 characters
    // Decide legitimate characters (likely use regex)
    // [a-zA-Z0-9]
    //https://regexr.com/7t0oj -> Regex(^([a-zA-Z0-9]{1,50}){1}$)
    static private String firstName () {
        System.out.println("Please provide your first name.");
        System.out.println("Must be between 1-50 characters and contain only letters and numbers.");
        // String regexPattern = "^(?![9]|[6]{3}|[0]{3})\\d{3}[ -]?(?![0]{2})\\d{2}[ -]?(?![0]{4})\\d{4}$";
        // Pattern pattern = Pattern.compile(regexPattern);
        // Matcher match = pattern.matcher(testInput);
        // String resultMatched = "";
        // // Check for a match.
        
        
        Scanner input = new Scanner(System.in);
        String firstName = input.next();
        
        String regex = "^([a-zA-Z0-9]{1,50}){1}$";
        Pattern pattern = Pattern.compile(regex);
        // pattern.match.group();
        Matcher matcher = pattern.matcher(firstName);

        if (!matcher.find()) {
            System.out.println(matcher.group() + " is not a valid first name. Please try again.");
            firstName();
        }
    
        // while (matcher.find()) {
        //     String resultMatched = matcher.group();
        //     System.out.print("Matched: " + resultMatched);
        // }
        // No match found so output an empty Stirng.
        return "";
        
        

        //return firstName;
    
    }



}