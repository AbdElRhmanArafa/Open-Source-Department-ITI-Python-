"""
Ask the user for his name then confirm that he has entered his name
(not an empty string/integers). then proceed to ask him for his email and
print all this data 
"""
import sys
def validEmail(email):
    """
    #! The only acceptable domain is @gmail.com
    """
    atSchool =email.index('@')
    for i in range(atSchool):
        if not(email[i].isalnum()) and not(email[i]=="_"):
            return False
    str=email[atSchool:]
    if(str!="@gmail.com"):
        return False 
    return True  

def validUserName(Name):    
    if(Name == ""):
        return False
    for i in Name:
        if (i.isdigit()):
            return False
    return True 

userName=input("Please enter your User Name : ")
if not(validUserName(userName)):
    sys.exit("Please enter your Right User Name , program will terminate")

email=input("Please enter your email address : ")
if not(validEmail(email)):
    sys.exit("Please enter your Right email address , program will terminate")

print ("🎊🎉🎊conguration if you reached to her so is ever thing is good ")




