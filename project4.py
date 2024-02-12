import math
while True:
    print("=======================================================")
    print("---------------------CALCULATOR------------------------")
    print("=======================================================")
    print("1. For Two digit Calculation")
    print("2. log calculation")
    print("3. Trignometric Functions")
    print("5. Exit")
    q = int(input("Enter Choice  :   "))
    if q==1:
        n1 = int(input("Enter First Number :   "))
        n2 = int(input("Enter Second Nuber :   "))
        print("Select Operation")
        print("1. Addition")
        print("2. Subtraction")
        print("3.Multiplication")
        print("4. Division")
        print("0. To go back")
        n = int(input("input operation:  "))
        if n==1:
            a=n1+n2
            print("The result is :  ",a)
            input("press enter")
        if n==2:
            a=n1-n2
            print("The result is :  ",a)
            input("press enter")
        if n==3:
            a=n1*n2
            print("The result is :  ",a)
            input("press enter")
        if n==4:
            a=n1/n2
            print("The result is :  ",a)
            input("press enter")
        if n==0:
            print("Exiting....1")
    if q==2:
        b=int(input("Enter The Number log has to be Calculated  :  "))
        b1 = math.log(b,10)
        print("The log of ",b," is ",b1)
        input("press enter")
    if q==3:
        print("1. sin(x)")
        print("2. cos(x)")
        print("3. tan(x)")
        c = int(input("Enter the Value of x :  "))
        c1 = c*math.pi/180
        f = int(input("Select Function :  "))
        if f==1:
            w = math.sin(c1)
            print(w)
        if f==2:
            w= math.cos(c1)
            print(w)
        if f==3:
            w = math.tan(c1)
            print(w)
        input("press enter")
    if q==5:
            print("=============EXITING PROCESS=============≠≠")
