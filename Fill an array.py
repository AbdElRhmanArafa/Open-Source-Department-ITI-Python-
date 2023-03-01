"""
Fill an array of 5 elements from the user, Sort it in descending and
ascending orders then display the output
"""
def SwapNum(a, b):
    temp = a
    a = b
    b = temp

sortedArray = []
element="element"
for i in range(5):
    if i!=0:
        element="Next element"
    if i==4:
        element="Last element"
    userInput = input(f"Please enter your {element} : ")
    sortedArray.append(int(userInput))
#! sort the array by insertion sort 
for i in range(4): #! 1 5 3 6 7 
    key=i+1 #* 3
    j=i #* 5  
    while j>=0 and sortedArray[key]<sortedArray[j]: #*  3< 5
          temp = sortedArray[j]
          sortedArray[j]=sortedArray[key] 
          sortedArray[key]=temp
print(sortedArray)

print("in ascending order is : " + str(sortedArray[::-1]))





