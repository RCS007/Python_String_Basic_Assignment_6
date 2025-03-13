# Question 6

# Ask the user to enter their first name. If the length of their first name is under five characters, ask them to
# enter their surname and join them together (without a space) and display the name in upper case. If the
# length of the first name is five or more characters, display their first name in lower case.

# Ask the user to enter their first name
first_name = input("Enter your first name: ")

# Check the length of the first name
if len(first_name) < 5:
    # If the first name has fewer than 5 characters, ask for their surname
    surname = input("Enter your surname: ")
    # Join first name and surname without a space and display in uppercase
    full_name = (first_name + surname).upper()
    print(f"Your name: {full_name}")
else:
    # If the first name has 5 or more characters, display it in lowercase
    print(f"Your name: {first_name.lower()}")