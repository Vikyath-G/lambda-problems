#Problem 2: Square and Cube
#Create two lambda functions, one that computes the square of a number and another that computes the cube of a number. Use these functions to calculate the square and cube of a list of numbers.

square=lambda x:x*x
cube=lambda x:x*x*x

numbers=[2,4,3,7,5,9,11]

print(list(map(square,numbers)))
print(list(map(cube,numbers)))