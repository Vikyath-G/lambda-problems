#Problem 8: Sorting a List of Dictionaries
#Consider a list of dictionaries where each dictionary contains the keys name and score. Use a lambda function with the sorted function to sort the list by score in descending order.


score_board=[{"name":"Rohan","score":39},{"name":"Harry","score":43},{"name":"Robert","score":34},{"name":"Vikrant","score":54},{"name":"Roshan","score":45}]

sort=sorted(score_board,key=lambda x:x['score'],reverse=True)

print(sort)