list1 = [8, 6, 7, 4, 5]
list2 = [5, 4, 3, 2, 1]
common_values = set(list1) & set(list2)
if common_values:
 print(f"c. Common values in both lists: {common_values}")
else:
 print("c. There are no common values in both lists.")
