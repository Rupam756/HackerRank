case "OR":
                    if (arg1 == 1) b1.or(b2);
                    else b2.or(b1);
                    break;
                    
                case "XOR":
                    if (arg1 == 1) b1.xor(b2);
                    else b2.xor(b1);
                    break;
                    
                case "FLIP":
                    if (arg1 == 1) b1.flip(arg2);
                    else b2.flip(arg2);
                    break;
                    
                case "SET":
                    if (arg1 == 1) b1.set(arg2);
                    else b2.set(arg2);
                    break;
            }
            
            // Print the count of set bits (cardinality) after each operation
            System.out.println(b1.cardinality() + " " + b2.cardinality());
        }
        
        sc.close();
    }
}

// Synced seamlessly with LeetHub Pro
// Pro features: https://bit.ly/leethubpro | Free version: https://bit.ly/leethubv4
// Get it here: https://chromewebstore.google.com/detail/bcilpkkbokcopmabingnndookdogmbna