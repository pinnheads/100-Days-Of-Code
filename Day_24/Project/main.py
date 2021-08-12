#TODO: Create a letter using starting_letter.txt 
#for each name in invited_names.txt
#Replace the [name] placeholder with the actual name.
#Save the letters in the folder "ReadyToSend".

formatted_names = []
template_text = []
with open("/home/pinnheads/Documents/100DaysOfCode/Day_24/Project/Input/Names/invited_names.txt", "r") as names:
    invited_names = names.readlines()
    for name in invited_names:
        name = name.strip("\n")
        formatted_names.append(name)
with open("/home/pinnheads/Documents/100DaysOfCode/Day_24/Project/Input/Letters/starting_letter.txt") as template:
    template_text = template.readlines()
    

for name in formatted_names:
    with open(f"/home/pinnheads/Documents/100DaysOfCode/Day_24/Project/Output/ReadyToSend/{name}.txt", "a+") as new_letter:
        for line in template_text:
            line = line.replace("[name]", name)
            new_letter.write(line)




    
#Hint1: This method will help you: https://www.w3schools.com/python/ref_file_readlines.asp
    #Hint2: This method will also help you: https://www.w3schools.com/python/ref_string_replace.asp
        #Hint3: THis method will help you: https://www.w3schools.com/python/ref_string_strip.asp
