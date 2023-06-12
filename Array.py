#Write a Python program 
#to find the second largest element in an array of integers.
numbers = [12,43,22,56,11,9,78]
numbers.sort()
print(numbers);
y =(numbers[-2])
print(y)

#Write a Python program to reverse 
# an array of integers
number = [12,43,22,56,11,9,78]
number.reverse()
print(number)

#Write a Python program to 
# remove duplicates from an array.
num = [12,43,22,12,43,11,13,12,56,11,9,78]
new =[]
[new.append (a) for a in num if a not in new ]
print(new)


