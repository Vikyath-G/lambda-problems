#Problem 5: List Transformation
#Given a list of strings, use a lambda function with the map function to create a new list that contains the length of each string from the original list.


length=lambda x:[x,len(x)]

names=['Ravi',"Rohan","Harry","Emma","Robin"]

string_length=list(map(length,names))
print(string_length)