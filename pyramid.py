def pyramid(number):
    a = 2 * number-2
    for i in range(0,number):
        for j in range(0, a):
            print(end=" ")
        a = a-1
        for j in range(0, i+1):
            print("*", end=" ")
        print("\r")

pyramid(int(input("Please enter a number: ")))