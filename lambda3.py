#Problem 3: Filtering Even and Odd Numbers
#Given a list of integers, use a lambda function with the filter function to separate even and odd numbers into two separate lists.

even=lambda x:x%2==0
odd=lambda x:x%2!=0

numbers=[2,5,34,13,11,12,7,8]

even_numbers=list(filter(even,numbers))
odd_numbers=list(filter(odd,numbers))

print(even_numbers)
print(odd_numbers)