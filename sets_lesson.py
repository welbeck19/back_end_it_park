#Task 1
my_set = set()
my_set.add(10)
my_set.add(20)
my_set.add(30)
print(my_set)

#Task 2
my_set = {1, 2, 2, 3, 3, 3, 4}
uniques = set(my_set)
print(uniques)

#Task 3
my_set = {5, 10, 15, 20}
my_set.remove(15)
print(my_set)

#Task 4
my_set = {100, 200, 300}
my_set.discard(400)
print(my_set)

#Task 5
a = {1, 2, 3, 4}
b = {3, 4, 5, 6}
intersection_result = a & b
print(intersection_result)

#Task 6
a = {1, 2, 3, 4}
b = {3, 4, 5, 6}
intersection_result = a.intersection(b)
print(intersection_result)

#Task 7
x = {10, 20, 30}
y = {30, 40, 50}
result = x.difference(y)
print(result)

#Task 8
x = {10, 20, 30}
y = {30, 40, 50}
result = x - y
print(result)

#Task 9
a = {"python", "java"}
b = {"c++", "java", "go"}

unique_set = a | b
print(unique_set)

