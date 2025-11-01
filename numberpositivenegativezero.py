#if-elif-else statement to deteremine the sign of the number

def check_sign(num):
    if num > 0:
        return "Positive"
    elif num < 0:
        return "Negative"
    else:
        return "Zero"
number =int(input("Enter a number: "))
print(check_sign(number))