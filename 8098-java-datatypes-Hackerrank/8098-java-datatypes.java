System.out.println("* int");
                }
                // Check Long limits: -2^63 to 2^63-1
                if (x >= Long.MIN_VALUE && x <= Long.MAX_VALUE) {
                    System.out.println("* long");
                }
                
            } catch (Exception e) {
                // This executes if the input overflows a 64-bit 'long'
                // Read the oversized value as a String to print the 
                error message
                String oversizedInput = sc.next();
                System.out.println(oversizedInput + " can't be fitted 
                anywhere.");
            }
        }
        
        sc.close();
    }
}

// Synced seamlessly with LeetHub Pro
// Pro features: https://bit.ly/leethubpro | Free version: https://bit.ly/leethubv4
// Get it here: https://chromewebstore.google.com/detail/bcilpkkbokcopmabingnndookdogmbna