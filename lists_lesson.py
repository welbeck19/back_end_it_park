#Task_1
list = ['olma', 'banan', 'gilos', 'xurmo', 'anjir']
print(list[2], list[4])

#Task_2
def create_list_replace(n):
    list = []
    for i in range(0, n, 1):
        list.append(i)
    list[3] = 10
    return list
print(create_list_replace(5))

#Task_3
list = ['dog', 'cat', 'chicken']
del list[1]
print(list)

#Task_4
list = ['red', 'green', 'blue', 'yellow', 'purple']
print(len(list))

#Task_5
list1 = ['a', 'b', 'c']
list2 = ['d', 'e', 'f']
list_extended = list1 + list2
print(list_extended)

#Task_6
list = ['mashina', 'avtobus', 'velosiped', 'poyezd']
print('avtobus' in list)

#Task_7
list = [3, 1, 4, 2, 5]
list.sort()
print(list)

#Task_8
list = [10, 20, 30, 40, 50]
list.reverse()
print(list)

#Task_9
list = ['kitob', 'qalam', 'daftar', 'sumka']
list.clear()
print(list)

#Task_10
list = [1, 2, 3]
list1 = list * 4
print(list1)

#Task_11
list = [25, 17, 9, 50, 33]
min = min(list)
max = max(list)
print("Minimum element:", min)
print("Maximum element:", max)

#Task_12
list = [100, 200, 300, 400, 500]
new_list = list.copy()
print(new_list)

#Task_13
list = [2, 4, 6, 8, 10]
sum = sum(list)
print("Sum of elements:", sum)

#Task_14
list = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
new_list = list[1::2]
print(new_list)

#Task_15
list = [[1, 2], [3, 4], [5, 6]]
print(list[1][1])