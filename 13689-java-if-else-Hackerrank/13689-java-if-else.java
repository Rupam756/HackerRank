int N = scanner.nextInt();
        scanner.skip("(\r\n|[\n\r\u2028\u2029\u0085])?");
        
        if (N % 2 != 0) {
    System.out.println("Weird");
} 
    System.out.println("Not Weird");
} 
else if (N % 2 == 0 && N >= 2 && N <= 5) {
else if (N % 2 == 0 && N >= 6 && N <= 20) {
    System.out.println("Weird");
} 
else if (N % 2 == 0 && N > 20) {
    System.out.println("Not Weird");
}


        scanner.close();
    }
}

// Synced seamlessly with LeetHub Pro
// Pro features: https://bit.ly/leethubpro | Free version: https://bit.ly/leethubv4
// Get it here: https://chromewebstore.google.com/detail/bcilpkkbokcopmabingnndookdogmbna