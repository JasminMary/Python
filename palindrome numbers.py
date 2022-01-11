palindrome = False
number = input("Enter any number: ")
count = 0
while(palindrome == False):
    if(str(number) == str(number)[::-1]):
        print("Took " + str(count) + " iterations to find palindrome")
        palindrome = True
    else:
        number = int(number) + int(str(number)[::-1])
    count = count + 1
