# Get user weights in float form
user_weight_1 = float(input("Enter weight 1:\n"))
user_weight_2 = float(input("Enter weight 2:\n"))
user_weight_3 = float(input("Enter weight 3:\n"))
user_weight_4 = float(input("Enter weight 4:\n"))
# Store weights in a list
weight_list = [user_weight_1, user_weight_2, user_weight_3, user_weight_4]
print("Weights:", weight_list)
print()
# Calculate average and max weights
average_weight = sum(weight_list) / len(weight_list)
max_weight = max(weight_list)
print("Average weight:", average_weight)
print(f"Max weight: {max_weight:.2f}\n")
# Get user input to find the index, must be an integer
user_location = int(input("Enter a list location (1 - 4):\n"))
weight_location = weight_list[user_location - 1]
print(f"Weight in pounds: {weight_location:.2f}")
weight_in_kilograms = weight_list[user_location - 1] / 2.2
print(f"Weight in kilograms: {weight_in_kilograms:.2f}\n")
# Sort the list
sorted_list = sorted(weight_list)
print(f"Sorted list: {sorted_list}")
