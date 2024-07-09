# Problem 1
s = 'fullstackslp'

# Print 'f'
print(s[0])

# Print 'p'
print(s[-1])

# Print 'stack'
print(s[4:9])

# Print 'slp'
print(s[-3:])

# Print 'cks'
print(s[7:10])

# Bonus: Reverse the string
print(s[::-1])

# Problem 2
d1 = {'simple_key': 'hello'}
print(d1['simple_key'])

d2 = {'k1': {'k2': 'hello'}}
print(d2['k1']['k2'])

d3 = {'k1': [{'nest_key': ['this is deep', ['hello']]}]}
print(d3['k1'][0]['nest_key'][1][0])

# Problem 4
mylist = [1, 1, 1, 1, 1, 2, 2, 2, 2, 3, 3, 3, 3]
unique_values = set(mylist)
print(unique_values)

# Problem 5
age = 45
name = "Kyle"
print(f"Hello my dog's name is {name} and he looks {age} years old")
