my_list = [1, 2, 3, 4, 5]

for element in my_list:
    print(element)
    if element == 3:
        print("in break")
        break  # break the loop instantly

for element in my_list:
    if element == 4:
        continue # continue to the next iteration directly
     
    print(element)

