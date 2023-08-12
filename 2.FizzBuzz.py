# Write a program that prints the numbers from 1 to 100. But for
# multiples of three, print "Fizz" instead of the number, and for
# the multiples of five, print "Buzz". For numbers which are
# multiples of both three and five, print "FizzBuzz".

def fizz_buzz(number):
    if number % 3 == 0 and number % 5 == 0:
        print("FizzBuzz")
    elif number % 3 == 0:
        print("Fizz")
    elif number % 5 == 0:
        print("Buzz")
    else:
        print("Nothing")
# fizz_buzz(12)


numbers = int(input("Enter Your Value:"))

fizz_buzz(numbers)
