import os

current_dir = os.getcwd()
print("Items in current directory:")
for item in os.listdir(current_dir):
    print(item)
