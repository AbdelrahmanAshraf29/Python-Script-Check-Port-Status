import abdelrahman_fileoperation_day3


contents = abdelrahman_fileoperation_day3.read("file.txt", "all")
print("Content of the file:")
print(contents)


result = abdelrahman_fileoperation_day3.write("file.txt", "Hello, World!\n", "write")
print("Write operation result:", result)

result = abdelrahman_fileoperation_day3.append("file.txt", ["Line 2\n", "Line 3\n"], "lines")
print("Append operation result:", result)