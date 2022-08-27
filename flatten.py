l1 = [[1,[2,4],3], "a", [5, 6]]

l_flattened = []
def flatten(n):
    for i in n:
        if isinstance(i, list):
            flatten(i)
        else:
            l_flattened.append(i)
    
    return l_flattened


print(flatten(l1))







