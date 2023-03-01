"""
Write a program that counts up the number of vowels [a, e, i, o, u] contained in the string
#! this function not handles uppercase characters :(
"""
#* O(n^2) 
vowelsLetters = ['a', 'e', 'i', 'o','u']
str=input("Enter the word : ")
countNumberOfVowels =0;
for i in str:
    for j in vowelsLetters:
        if(i==j):
            countNumberOfVowels += 1
print (f"Number of vowels in word is {countNumberOfVowels}\n")
print("="*20+" method two "+"="*20 )
#* O(n)
str2=input("Enter the word : ")
countNumberOfVowels2=0
for i in str2:
    if i=='a' or i=='e' or i=='i' or i=='o'or i=='u':
        countNumberOfVowels2+=1
print (f"Number of vowels in word is {countNumberOfVowels2}\n")


