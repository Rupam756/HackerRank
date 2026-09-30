if __name__ == '__main__':
    N = int(input())
    
    my_list =[]
    
    for i in range(N):
        
        parts = input().split()
        cmd = parts[0]
        args = parts[1:]
        
        if cmd == "insert":
            my_list.insert(int(args[0]),int(args[1]))
        elif cmd == "print":
            print(my_list)
        elif cmd == "remove":
            my_list.remove(int(args[0]))
        elif cmd == "append":
            my_list.append(int(args[0]))
        elif cmd == "sort":
            my_list.sort()
        elif cmd == "pop":
            my_list.pop()
        elif cmd == "reverse":
            my_list.reverse()


# Synced seamlessly with LeetHub Pro
# Pro features: https://bit.ly/leethubpro | Free version: https://bit.ly/leethubv4
# Get it here: https://chromewebstore.google.com/detail/bcilpkkbokcopmabingnndookdogmbna