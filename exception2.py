try:
    num1 = int(input("Enter First Number: "))
    num2 = int(input("Enter Second Number: "))

    result = num1 / num2

    print("division=",result)
except Exception as e: 
        print("The error is: ",e)
finally:
        print ("OVER AND OUT")
