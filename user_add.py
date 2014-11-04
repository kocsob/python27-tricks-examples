import getpass
import sys

def yn_choice(message, default='y'):
    choices = 'Y/n' if default.lower() in ('y', 'yes') else 'y/N'
    choice = raw_input("%s [%s] " % (message, choices))
    values = ('y', 'yes', '') if default == 'y' else ('y', 'yes')
    return choice.strip().lower() in values


username = raw_input("Enter username: ")

valid_pass = False
while (valid_pass == False):
    password = getpass.getpass("Enter new password: ")
    retypepass = getpass.getpass("Retype new password: ")

    if (password == retypepass):
        valid_pass = True
    else:
        print("Sorry, passwords do not match")
        if (yn_choice("Try again?", 'n') == False):
            sys.exit()

print("Adding the user information for %s:" % username)

valid_info = False
while (valid_info == False):
    full_name = raw_input("\tFull name: ")
    room_number = raw_input("\tRoom number: ")
    work_phone = raw_input("\tWork phone: ")
    home_phone = raw_input("\tHome phone: ")
    email = raw_input("\tE-mail: ")
    
    if (yn_choice("Is the information correct?", 'y') == True):
        valid_info = True
    else:
        if (yn_choice("Try again?", 'n') == False):
            sys.exit()

# Store the user informations ...