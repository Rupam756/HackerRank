Scanner in = new Scanner(System.in);
        int t=in.nextInt();
        for(int i=0;i<t;i++){
            int a = in.nextInt();
            int b = in.nextInt();
            int n = in.nextInt();int currentTerm = a;
            
            // Generate the n terms of the series
            for (int j = 0; j < n; j++) {
                // Math.pow(2, j) gives 2^j. 
                // We cast to (int) because Math.pow returns a double.
                currentTerm += (int) Math.pow(2, j) * b;
                
                // Print the term followed by a space
                System.out.print(currentTerm + " ");
            }
        }
        in.close();
    }
            System.out.println();
}

// Synced seamlessly with LeetHub Pro
// Pro features: https://bit.ly/leethubpro | Free version: https://bit.ly/leethubv4
// Get it here: https://chromewebstore.google.com/detail/bcilpkkbokcopmabingnndookdogmbna