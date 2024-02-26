#Problem 9: Calculate the Total of a List
#Given a list of dictionaries where each dictionary represents an item with keys name and price, use a lambda function to calculate the total price of all items in the list.


palindrome=lambda x: x == x[::-1]

strings=["rohan","hari","madam","radar"]

palindrome_strings=list(filter(palindrome,strings))
print(palindrome_strings)