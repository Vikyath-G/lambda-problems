#Problem 6: Maximum and Minimum in a List
#Write a lambda function that takes a list of numbers as input and returns both the maximum and minimum numbers. Use the built-in functions max() and min() in your lambda function.


lam=lambda x:[max(x),min(x)]

numbers=[2,34,1,64,45,23,56]

max_min=lam(numbers)

print(f"Maximum={max_min[0]}  minimum={max_min[1]}")