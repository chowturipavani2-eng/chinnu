def simon_says(list1, list2):

   return list1[:-1] == list2[1:]

print(simon_says([1, 2], [5, 1]))

print(simon_says([1, 2], [5, 5]))

print(simon_says([1, 2, 3, 4, 5], [0, 1, 2, 3, 4]))

print(simon_says([1, 2, 3, 4, 5], [5, 5, 1, 2, 3]))
