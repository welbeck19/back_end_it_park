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