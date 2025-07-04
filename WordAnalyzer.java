import java.io.BufferedReader;
import java.io.FileReader;
import java.util.*;

public class WordAnalyzer {
    static final String ALPHABET = "abcdefghijklmnopqrstuvwxyząčęėįšųūž";
    
    public static void main(String[] args) {
        String fileName = "C:\\Users\\zabit\\Documents\\GitHub\\Lithuanian-Word-Square\\11_length_words.txt";
        int n = 11;
        
        Set<String> allWords = new HashSet<>();
        Set<String> validWords = new HashSet<>();
        Set<String> invalidWords = new HashSet<>();
        Set<String> upperCaseWords = new HashSet<>();
        Set<String> digitWords = new HashSet<>();
        Set<String> wrongLengthWords = new HashSet<>();
        Set<Character> uniqueChars = new HashSet<>();
        
        try (BufferedReader br = new BufferedReader(new FileReader(fileName))) {
            String word;
            while ((word = br.readLine()) != null) {
                allWords.add(word);
                
                // Collect all unique characters
                for (char c : word.toCharArray()) {
                    uniqueChars.add(c);
                }
                
                // Check filters
                if (word.length() != n) {
                    wrongLengthWords.add(word);
                    continue;
                }
                
                if (Character.isDigit(word.charAt(0))) {
                    digitWords.add(word);
                    continue;
                }
                
                if (Character.isUpperCase(word.charAt(0))) {
                    upperCaseWords.add(word);
                    continue;
                }
                
                if (!isValidWord(word)) {
                    invalidWords.add(word);
                    continue;
                }
                
                validWords.add(word);
            }
        } catch (Exception e) {
            e.printStackTrace();
        }
        
        System.out.println("Total words read: " + allWords.size());
        System.out.println("Valid words: " + validWords.size());
        System.out.println("Invalid words (bad chars): " + invalidWords.size());
        System.out.println("Uppercase words: " + upperCaseWords.size());
        System.out.println("Digit words: " + digitWords.size());
        System.out.println("Wrong length words: " + wrongLengthWords.size());
        
        System.out.println("\nUnique characters found:");
        List<Character> sortedChars = new ArrayList<>(uniqueChars);
        Collections.sort(sortedChars);
        for (char c : sortedChars) {
            System.out.print("'" + c + "' ");
        }
        System.out.println();
        
        System.out.println("\nCharacters NOT in alphabet:");
        for (char c : sortedChars) {
            if (ALPHABET.indexOf(c) == -1) {
                System.out.print("'" + c + "' ");
            }
        }
        System.out.println();
        
        if (invalidWords.size() > 0) {
            System.out.println("\nFirst 10 invalid words:");
            invalidWords.stream().limit(10).forEach(System.out::println);
        }
    }
    
    static boolean isValidWord(final String word) {
        for (final char c : word.toCharArray()) {
            if (ALPHABET.indexOf(c) == -1)
                return false;
        }
        return true;
    }
}
