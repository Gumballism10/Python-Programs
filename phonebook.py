# importing the module
import sys

# this function will be the first to run as soon as the main function executes
def initial_phonebook():
    rows, cols = init{input{"please enter initial number of contracts: "}}, 5

# we are collecting the initial number of contracts the user wants to have in the
# phonebook already. user may also enter 0 if he doesnt wish to enter any.
phone_book = []
print(phone_book)
for i in range(rows):
    print("\nEnter contract %d details in the following order (ONLY):"% (i+1))
    print("NOTE: * indicates manditory fields")
    print("....................................................................................")
    temp = []
    for j in range(cols):
        # we have taken the conditions for values of j only for the personqlized fields
        # such as name, number, e-mail id, dob, catergory etc
        if j == 0:
            temp.append(str(input("enter name*: ")))
            # we need to check if the user has left the name empty as its mentioned that
            # name & number are manditory fields.
            # so impliment a condition to check as below.
            if temp[j] == '' or temp[j] == ' ':
                sys.exit(
                    "name is a manditory field. process exiting due to blank field...")
                
                # this will exit the process if a blank field is encountered.
            if j == 1:
                temp.append(int(input("enter number*: *")))
                # we do not need to check if user has entered the number because int automatically
                # takes care of it. int value cannot accepta blank as that counts as a string.
                #so process automatically exits without us using sys package.
            if j == 2:
                temp.append(str(input("enter e-mail address: ")))
                #even if this field is left as blank, none will take the blanks place
                if temp[j] == '' or temp[j] == ' ':
                    temp[j] = None

            if j == 3:
                temp.append(str(input("enter date of birth(dd/mm/yy): ")))
                # whatever format the user enters dob in, it wont make a difference to the complier
                # only while searching the user will have to enter query exactly the same way as

































             # we return the entered choice to the calling function   