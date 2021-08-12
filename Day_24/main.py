# To open a file
file = open("my_file.txt")

# To Read a file
contents = file.read()

# To print the contents of a file
print(contents)

# To close the opened a file
file.close()

# Alternate method to open and close a file
# this method closes the file on its own
# Both the methods have the same output
with open("my_file.txt") as file2:
    contents_file2 = file2.read()
    print(contents_file2)

# To write to a file open the file in a specific mode
# w  - write
# r+ - opens for reading and writing(no truncating, file pointer 
# at the beginning)
# w+ - opens for writing ( and thus truncates the file) and reading
# a+ - opens for appending(writing without truncating, only at the end of the 
# file, and the file pointer is at the end of the file) and reading

with open("my_file.txt", mode="a+") as file3:
    file3.write("\nHello world!")
    contents_file3 = file3.read()
    print(contents_file3)
