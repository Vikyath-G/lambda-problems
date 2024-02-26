#Problem 9: Calculate the Total of a List
#Given a list of dictionaries where each dictionary represents an item with keys name and price, use a lambda function to calculate the total price of all items in the list.

items=[{"name":"Bread","Price":30},{"name":"Milk","Price":27},{"name":"Buscuits","Price":55},{"name":"Noodles","Price":35}]

add=lambda x:x['Price']

total=sum(map(add,items))
print(total)
