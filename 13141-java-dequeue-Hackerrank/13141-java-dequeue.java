}
                
                // 3. Slide the window: remove the oldest element from 
                the front
                int first = deque.removeFirst();
                int currentCount = frequencyMap.get(first);
                
                if (currentCount == 1) {
                    frequencyMap.remove(first);
                } else {
                    frequencyMap.put(first, currentCount - 1);
                }
            }
        }
        
        System.out.println(maxUnique);
        in.close();
    }
}

// Synced seamlessly with LeetHub Pro
// Pro features: https://bit.ly/leethubpro | Free version: https://bit.ly/leethubv4
// Get it here: https://chromewebstore.google.com/detail/bcilpkkbokcopmabingnndookdogmbna