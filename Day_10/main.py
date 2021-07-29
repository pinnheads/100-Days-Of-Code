# Functions with outputs
def format_name(fName, lName):
    formated_name = fName.title() + ' ' + lName.title()
    return formated_name

my_name = format_name("UtSAV", "DeEP")
print(my_name)

# Functions with multiple return values
def format_name(fName, lName):
    '''
    Take a first and last name and format it to return the title case version of the name.
    '''
    if fName == "" or lName == "":
        return "No Valid input Provided"
    else:
        formated_name = fName.title() + ' ' + lName.title()
        return formated_name

my_name = format_name(input("What is your first name?"), input("What is your last name?"))
print(my_name)