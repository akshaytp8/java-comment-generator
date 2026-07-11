```java
import java.util.Scanner;

/**
 * This class checks whether a given integer is a palindrome or not.
 */
public class PalindromeCheck {
   /**
    * Main method to execute the palindrome check.
    * @param args command line arguments (not used in this program)
    */
   public static void main(String[] args) {
       // Create a Scanner object to read user input
       Scanner scanner = new Scanner(System.in);
       System.out.print("Enter a number: ");
       // Store the user input in the 'number' variable
       int number = scanner.nextInt();
       // Store the original number for later comparison
       int originalNumber = number;
       // Initialize a variable to store the reversed number
       int reversedNumber = 0;
       // Loop until all digits of the number have been processed
       while (number > 0) {
           // Calculate the remainder of the number when divided by 10 (i.e., the last digit)
           int remainder = number % 10;
           // Append the remainder to the reversed number
           reversedNumber = (reversedNumber * 10) + remainder;
           // Remove the last digit from the number
           number /= 10;
       }
       // Check if the original number is equal to the reversed number
       if (originalNumber == reversedNumber) {
           // Print a message indicating that the number is a palindrome
           System.out.println(originalNumber + " is a Palindrome.");
       } else {
           // Print a message indicating that the number is not a palindrome
           System.out.println(originalNumber + " is not a Palindrome.");
       }
       // Close the Scanner object to prevent resource leaks
       scanner.close();
   }
}
```