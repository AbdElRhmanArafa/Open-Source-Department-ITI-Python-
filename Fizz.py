"""
write a function that takes a number as an argument and if the number
divisible by 3 return "Fizz" and if it is divisible by 5 return "buzz" and if is is
divisible by both return "FizzBuzz" 
"""
def FizzBuzz(number):
    """
    @param number : check if number is divisible by 3 or 5 or both 
    return "FizzBuzz" if both return "Fizz" if 3 
    """
    returnAnswer=""
    if number % 3==0:
        returnAnswer+="Fizz"
    if number % 5==0:
        if returnAnswer=="": 
            returnAnswer+="buzz"
        else :
            returnAnswer+="Buzz"
    return returnAnswer

while True:
    Test=input("Enter a number : ")    
    result=FizzBuzz(int(Test))
    print(result+"\n"+"*"*20)

