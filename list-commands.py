if __name__ == '__main__':
    n = int(input())  # Read number of commands
    lst = []  # Initialize an empty list
    
    for _ in range(n):
        command = input().split()  # Read command and split into parts
        action = command[0]
        
        if action == "insert":
            lst.insert(int(command[1]), int(command[2]))
        elif action == "print":
            print(lst)
        elif action == "remove":
            lst.remove(int(command[1]))
        elif action == "append":
            lst.append(int(command[1]))
        elif action == "sort":
            lst.sort()
        elif action == "pop":
            lst.pop()
        elif action == "reverse":
            lst.reverse()


