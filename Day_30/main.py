#try catch and finally exceptions
try:
    file = open("a_file.txt")
    a_dictionary = {"key" : "value"}
    print(a_dictionary["sdfsdf"])
except FileNotFoundError:
    file = open("a_file.txt", "w")
    file.write("Something")
except KeyError as error_msg:
    print(f"The key {error_msg} does not exist")
else:
    content = file.read()
    print(content)
finally:
    raise KeyError
    file.close()
    print("file was closed")