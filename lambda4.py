#Problem 4: Sorting a List of Tuples
#Consider a list of tuples where each tuple contains a name and age pair. Use a lambda function with the sorted function to sort the list by age.

data=[("John",25),("Rohan",19),("Emma",20),("Ravi",29)]

sorted_data=sorted(data,key=lambda people:people[1])
print(sorted_data)