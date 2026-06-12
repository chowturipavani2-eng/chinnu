def filter_list(list):
    result = []

    for element in list:
        if type(element) == int:
            result.append(element)
    return result
print(filter_list([1,2,"a","b"]))

print(filter_list([1,"a","b",0,15]))

print(filter_list([1,2,"aasf","1","123",123]))
