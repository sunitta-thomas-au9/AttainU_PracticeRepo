if __name__ == '__main__':
    n = int(input())
    if (1 <= n <= 20):
        index = 0    
        while (index < n):
            print(index * index)
            index += 1
    else:
        print("Please enter a valid number between 1 -20")