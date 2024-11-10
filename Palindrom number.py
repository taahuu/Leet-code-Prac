def plaindrom(number):
    if number<0:
        return False
    numbers=[int(digit) for digit in str(number)]  # Split and store in a list
    # print(numbers)
    a= numbers
    b= numbers[::-1]
    print(a)
    print(b)
    if a==b:
        # print("Palindrom")
        return "Palindrom"
    else:
        # print("no")
        return "No"



number=int(input("Enter The Number: "))
a=plaindrom(number)
print(a)
