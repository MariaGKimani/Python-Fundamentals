# Write a Python program to count the number of items 
#in a dictionary that have a value greater than a certain number.


# a = list(age.values())
# b = list(age.keys())
# print(b[a.index(max(a))])
age ={"Maria": 22,"Irene": 24,"Eleanor": 32,"Terry": 26,"Steve": 34}
count = 20
counts =0
for key,value in age.items():
    if value > count:
        counts +=1
print(counts)

