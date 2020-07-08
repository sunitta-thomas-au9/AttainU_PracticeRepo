from __future__ import print_function

if __name__ == '__main__':
    n = int(input())
    if (1 <= n <= 150 ):
        index = 1    
        while (index <= n):
            print (index, end = '')
            index += 1
    else:
        print ("please enter in range between 1 and 150")


