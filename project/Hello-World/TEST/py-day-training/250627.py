#Kaggle_learn_Intro to Lists

flowers_list = ["pink primrose", "hard-leaved pocket orchid", "canterbury bells", "sweet pea", "english marigold", "tiger lily", "moon orchid", "bird of paradise", "monkshood", "globe thistle"]
print(flowers_list)
print(type(flowers_list)
      )
print(len(flowers_list))  # Length of the list
print(flowers_list[0])  # First element of the list
print(flowers_list[1])  # Second element of the list
print("Last_entry:", flowers_list[9])
print(flowers_list[-3])  # Last element of the list
# Last element of the list

hardcover_sales = [139, 128, 172, 139, 191, 168, 170]
print(hardcover_sales)
print(type(hardcover_sales))
print("Entry at index 0:", hardcover_sales[0])  
print("Entry at index 2:", hardcover_sales[2])  
print("Minimum:",min(hardcover_sales))# Minimum value in the list
print("Maximum:",max(hardcover_sales))# Maximum value in the list
print("Sum:",sum(hardcover_sales))# Sum of all values in the list
print("Average:", sum(hardcover_sales) / len(hardcover_sales))  # Average of the list