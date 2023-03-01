""" 
Write a function that accepts two arguments (length, start) to generate
an array of a specific length filled with integer numbers increased by one from start
"""

def generateArrayOfLength(length, start):
    """
    @param length: the length of the array
    @param start: number to increment 
    return list of integers [start=> start+length] increases by one 
    """
    list = []
    for i in range(length):
        list.append(start)
        start += 1
    return list
#* main 
#! never forget input return a string variable so you should always make casting  !#
length = input("Length of the array : ")
start = input("Start of the array : ") 
list =generateArrayOfLength(int(length), int(start))
print (f"The list of integers : {list}")

