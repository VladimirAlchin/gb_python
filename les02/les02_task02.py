my_list = [0, 1, 2, 3, 4, 5, 6, 7, 8]
if len(my_list) % 2 > 0:
    max_iter = (len(my_list) - 1)
else:
    max_iter = len(my_list)
i = 0
while i < max_iter:
    new_el = my_list[i]
    my_list[i] = my_list[i + 1]
    my_list[i + 1] = new_el
    i += 2
print(my_list)
