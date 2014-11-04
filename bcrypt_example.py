import bcrypt
import getpass
import sys

password = getpass.getpass("Enter new password: ")
retypepass = getpass.getpass("Retype new password: ")

if (password != retypepass):
    print("Passwords do not match")
    sys.exit()

# Hash a password for the first time, with a randomly-generated salt
hashedpw = bcrypt.hashpw(password, bcrypt.gensalt())


# Store and load 'hashedpw' for the user ...


# Check the password
password = getpass.getpass("Enter the password: ")
if bcrypt.hashpw(password, hashedpw) == hashedpw:
    print("It Matches!")
else:
    print("It Does not Match :(")
