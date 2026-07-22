break;
                case "XOR":
                    bitsets[arg1].xor(bitsets[arg2]);
                    break;
                case "FLIP":
                    bitsets[arg1].flip(arg2);
                    break;
                case "SET":
                    bitsets[arg1].set(arg2);
                    break;
            }

            // Print set bits count using cardinality()
            System.out.println(b1.cardinality() + " " + b2.cardinality
            ());
        }

        scanner.close();
    }
}

// Synced seamlessly with LeetHub Pro
// Pro features: https://bit.ly/leethubpro | Free version: https://bit.ly/leethubv4
// Get it here: https://chromewebstore.google.com/detail/bcilpkkbokcopmabingnndookdogmbna