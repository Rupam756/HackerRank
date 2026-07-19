public class Solution {

    public static void main(String[] args) {
        /* Enter your code here. Read input from STDIN. Print 
        output to STDOUT. Your class should be named Solution. 
        */
        Scanner scan = new Scanner(System.in);
        
        int lineCount = 1;
        
        while (scan.hasNext()){
            String line = scan.nextLine();
            
            System.out.println(lineCount + " "+line);
            
            lineCount++;
        }
import java.text.*;
import java.math.*;
import java.util.regex.*;
import java.io.*;
import java.util.*;

// Synced seamlessly with LeetHub Pro
// Pro features: https://bit.ly/leethubpro | Free version: https://bit.ly/leethubv4
// Get it here: https://chromewebstore.google.com/detail/bcilpkkbokcopmabingnndookdogmbna