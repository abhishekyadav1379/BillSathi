import os

def get_folder_size(folder_path):
    total_size = 0

    for dirpath, dirnames, filenames in os.walk(folder_path):
        for filename in filenames:
            file_path = os.path.join(dirpath, filename)
            total_size += os.path.getsize(file_path)

    return total_size


# Example usage
file_path = "./Main_Software"
size = get_folder_size(file_path)
if size is not None:
    print(f"File size: {size} bytes")
else:
    print("File not found or error occurred.")
