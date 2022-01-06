def fibonacciSequence(number):
    n1 = 1
    n2 = 1
    for i in range(1, number+1):

        print()
        if i == 1:
            print(str(n1) + " , ")
            continue
        if i == 2:
            print(str(n2) + " , ")
            continue

        next = n1+n2
        n1 = n2
        n2 = next
        print(str(next) + " , ")
        


number = int(input("Hey ! How many Fibonacci do you want to see ? "))
fibonacciSequence(number)