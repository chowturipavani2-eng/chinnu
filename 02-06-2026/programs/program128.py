def is_symmetrical(num):

  num_str = str(num)

  return num_str == num_str[::-1]

print(is_symmetrical(7227))

print(is_symmetrical(12567)) 

print(is_symmetrical(44444444))

print(is_symmetrical(44444444)) 

print(is_symmetrical(1112111))
