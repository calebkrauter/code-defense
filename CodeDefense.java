import java.io.PrintWriter;
import java.io.File;
import java.io.FileNotFoundException;
import java.io.FileWriter;
import java.io.IOException;
import java.math.BigInteger;
import java.security.NoSuchAlgorithmException;
import java.security.SecureRandom;
import java.security.spec.InvalidKeySpecException;
import java.security.spec.KeySpec;
import java.util.Arrays;
import java.util.Base64;
import java.util.Scanner;
import java.util.regex.Matcher;
import java.util.regex.Pattern;

import javax.crypto.SecretKeyFactory;
import javax.crypto.spec.PBEKeySpec;
import java.util.Base64;

/**
 * CodeDefense propmts the user for various forms of input with security
 * in mind to ensure no malicous input could break the system.
 * 
 * @author Caleb Krauter, Nathan Hinthorne, Trae Claar
 */
public class CodeDefense {

    /**
     * Driver code.
     * 
     * @throws NoSuchAlgorithmException
     * @throws InvalidKeySpecException
     */
    public static void main(final String[] args) throws InvalidKeySpecException, NoSuchAlgorithmException {
        Scanner input = new Scanner(System.in);
        // final String firstName = promptForName("first", input);
        // System.out.println("First Name: " + firstName);

        // final String lastName = promptForName("last", input);
        // System.out.println("Last Name: " + lastName);

        // final BigInteger value1 = promptForInt(input);
        // System.out.println("Value 1: " + value1);

        // final BigInteger value2 = promptForInt(input);
        // System.out.println("Value 2: " + value2);

        // final String inputFile = promptForInputFileName(input);
        // System.out.println("Input File Name: " + inputFile);

        // final String outputFile = promptForOutputFileName(input, inputFile);
        // System.out.println("Output File Name: " + outputFile);

        getPasswords(input);

    }

    /**
     * Helper method to match input to our pattern
     * 
     * @param input
     * @param regex a pattern
     */
    static private boolean mismatchedInput(final String input, final String regex) {
        Pattern pattern = Pattern.compile(regex);
        Matcher matcher = pattern.matcher(input);

        return !matcher.matches();
    }

    // PROMPT FOR FIRST NAME
    // Between 1 and 50 characters

    /**
     * Prompts user for a name first or last.
     * 
     * @param firstOrLast name
     * @param input
     */
    static private String promptForName(final String firstOrLast, final Scanner input) {
        System.out.println("Please provide your " + firstOrLast + " name.");
        System.out.println("Must be between 1-50 characters and contain only letters and numbers.");

        String name = input.nextLine();

        if (mismatchedInput(name, "^[a-zA-Z0-9]{1,50}$")) {
            System.out.println("Not a valid first name. Please try again.");
            return promptForName(firstOrLast, input);
        }

        return name;
    }

    /**
     * Prompts the user for a <=4byte integer value that is converted
     * to BigInt for security.
     * 
     * @param input
     */
    static private BigInteger promptForInt(final Scanner input) {
        BigInteger min = BigInteger.valueOf(2).pow(31).negate();
        BigInteger max = BigInteger.valueOf(2).pow(31).subtract(BigInteger.ONE);

        BigInteger n;
        do {
            System.out.println("Please provide a 4 byte integer.");
            n = new BigInteger(input.next());
        } while (min.compareTo(n) > 0 || max.compareTo(n) < 0);

        return n;
    }

    static private String promptForInputFileName(final Scanner input) {
        System.out.println("Please provide the input file name.");
        System.out.println("Must be a .txt file in the current directory. The file name must"
                + " be between 1 and 50 characters");

        String name = input.next();

        if (mismatchedInput(name, "^[a-zA-Z0-9]{1,50}.txt$")) {
            System.out.println("Not a valid file name. Please try again.");
            return promptForInputFileName(input);
        }

        return name;
    }

    static private String promptForOutputFileName(final Scanner input, final String inputFileName) {
        System.out.println("Please provide the output file name.");
        System.out.println("Must be a .txt file in the current directory. The file name must"
                + " be between 1 and 50 characters and must not match the input file name.");

        String name = input.next();

        if (mismatchedInput(name, "^[a-zA-Z0-9]{1,50}.txt$") || name.equals(inputFileName)) {
            System.out.println("Not a valid file name. Please try again.");
            return promptForOutputFileName(input, inputFileName);
        }

        return name;
    }

    /**
     * Validate a String as a password that contains at least 10 characters and
     * includes at
     * least one upper case character, one lower case character, one digit, one
     * punctuation
     * mark, and does not have more than 3 consecutive lower case characters.
     * Special characters
     * other than punctuation are not allowed.
     *
     * @param input scanner.
     * @return the validated password or a reprompt.
     * @throws NoSuchAlgorithmException
     * @throws InvalidKeySpecException
     */
    static private String promptForPassword(final Scanner input, final String message)
            throws InvalidKeySpecException, NoSuchAlgorithmException {
        System.out.println(message);
        System.out.println("");

        String password = input.next();

        if (mismatchedInput(password, "^(?=.*[A-Z])(?=.*[a-z])(?=.*\\d)(?=.*[\\.,!\\?'\";:-])"
                + "(?!.*[a-z]{4,}).{10,}$")) {

            System.out.println("Not a valid password. Please try again.");
            password = promptForPassword(input, message);
        }
        return password;
    }

    /**
     * Generate a random salt for hashing.
     * 
     * @return a random salt.
     */
    static private byte[] generateSalt() {
        SecureRandom secureRandom = new SecureRandom();
        byte[] salt = new byte[16];
        secureRandom.nextBytes(salt);
        return salt;
    }

    // Secure Hash code originally from:
    // https://stackoverflow.com/questions/2860943/how-can-i-hash-a-password-in-java
    static private byte[] hashPassword(final String password, final byte[] salt)
            throws InvalidKeySpecException, NoSuchAlgorithmException {
        KeySpec spec = new PBEKeySpec(password.toCharArray(), salt, 65536, 128);
        SecretKeyFactory key = SecretKeyFactory.getInstance("PBKDF2WithHmacSHA1");
        byte[] hash = key.generateSecret(spec).getEncoded();

        return hash;
    }

    /**
     * Store the password in a file.
     * 
     * @param input scanner.
     * @throws InvalidKeySpecException
     * @throws NoSuchAlgorithmException
     * @throws IOException
     */
    static private void storePassword(final Scanner input) throws InvalidKeySpecException, NoSuchAlgorithmException {
        final String password = promptForPassword(input, "Please provide a password.");
        System.out.println("Password: " + password);

        byte[] salt = generateSalt();
        byte[] hash = hashPassword(password, salt);
        try {
            Base64.Encoder encoder = Base64.getEncoder();
            PrintWriter printWriter = new PrintWriter(new FileWriter("./resources/password.txt"));
            printWriter.println(encoder.encodeToString(salt));
            printWriter.print(encoder.encodeToString(hash));
            printWriter.close();
        } catch (IOException e) {
            System.out.println(e);
        }
    }

    static private void getPasswords(final Scanner input) throws InvalidKeySpecException, NoSuchAlgorithmException {
        storePassword(input);
        comparePassword(input);
    }

    /**
     * Compare a new password to the stored password.
     * 
     * @param input scanner.
     * @throws InvalidKeySpecException
     * @throws NoSuchAlgorithmException
     * @throws FileNotFoundException
     */
    static private void comparePassword(final Scanner input) throws InvalidKeySpecException, NoSuchAlgorithmException {
        final String password2 = promptForPassword(input, "Please re-enter your password.");
        System.out.println("Password: " + password2);
        File passwordFile = new File("./resources/password.txt");

        byte[] salt;
        byte[] hash;
        try (Scanner file = new Scanner(passwordFile)) {
            salt = Base64.getDecoder().decode(file.nextLine());
            hash = Base64.getDecoder().decode(file.nextLine());
        } catch (FileNotFoundException e) {
            // e.printStackTrace();
            getPasswords(input);
            return;
        }

        byte[] hash2 = hashPassword(password2, salt);

        if (!Arrays.equals(hash, hash2)) {
            System.out.println("Passwords do not match.");
            comparePassword(input);
        } else {
            System.out.println("Passwords match.");
        }
    }
}