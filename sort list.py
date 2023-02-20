# Take input of integers list
lst = list(map(int, input("Enter a list of integers: ").split()))
# Sort the list
sorted_lst = sorted(lst)

# Print the sorted list
print("Sorted list:", sorted_lst)

new_num = int(input("Enter a number to add to the list: "))

# Find the position to insert the new number in the sorted list
for i in range(len(sorted_lst)):
    if new_num <= sorted_lst[i]:
        sorted_lst.insert(i, new_num)
        break
else:
    sorted_lst.append(new_num)

# Print the updated sorted list with the new number added
print("Sorted list with new number added:", sorted_lst)