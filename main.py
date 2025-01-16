"""This function handles the transfer process for the user."""
# TODO: Import the Checking, Savings, and Validation classes
def main():
    checking_account = Checking()
    savings_account = Savings()
    
    # Implement login and transaction handling logic here


# TODO: These should be imported from the appropriate file in the BankingClasses directory.
def main():
    checking_account = Checking()
    savings_account = Savings()
    
    # Implement login and transaction handling logic here


# TODO: Import the handle_deposit, handle_withdrawal, handle_transfer, and balances functions
max_attempts = 3
attempts = 0

while attempts < max_attempts:
    email = input("Enter your email: ")
    password = input("Enter your password: ")

    # Validate email and password
    
        
        # Proceed with the application logic (e.g., show account balances)
    
if attempts == max_attempts:
    print("Maximum login attempts reached. Exiting the program.")

# TODO: These should be imported from the appropriate file in the BankingFunctions directory.

def main():
    """
    This function is the entry point of the banking system.
    It prompts the user to enter their email and password for authentication.
    If the email and password are valid, the default balances are shown.
    It then presents a menu of options to the user,
    allowing them to make deposits, withdrawals, or transfers between accounts.
    """
    email = input("Enter your email: ")
    print("Your password should be at least 8 characters long,\n"
           "contain at least one uppercase and lowercase letter,\n"
           "one number, and one of the following special characters:!@#$%^&*.")
    password = input("Enter your password: ")

    # TODO: Initialize the attempts variable to 1.
    attempts = 1

# Start the while loop
while attempts <= 3:  # Change to <= to allow for 3 attempts
    email = input("Enter your email: ")
    password = input("Enter your password: ")

    # Replace the following lines with your validation logic
    if Validation.validate_email(email) and Validation.validate_password(password):
        print("Login successful!")
        # Proceed with the application logic (e.g., show account balances)
        break  # Exit the loop if login is successful
    else:
        print("Invalid email or password. Please try again.")
        attempts += 1  # Increment the attempts counter

# Check if the maximum attempts were reached
if attempts > 3:
    print("Maximum login attempts reached. Exiting the program.")
    # TODO: Create a while loop to validate the email and password.
    max_attempts = 3
attempts = 0


    

    # Validate email and password
    
        # Proceed with the application logic (e.g., show account balances)
       


    # TODO: The while loop should run as long as the attempts variable is less than 3.
   

while attempts < 3:  # Loop will run while attempts is less than 3
        email = input("Enter your email: ")
        password = input("Enter your password: ")

        # Here, you would typically validate the email and password
        if validate_credentials(email, password):  # Assume this function checks credentials
            print("Login successful!")
            
        else:
            attempts += 1  # Increment the attempts counter
            print(f"Invalid credentials. You have {3 - attempts} attempts left.")

        print("Maximum login attempts reached. Exiting the program.")

def validate_credentials(email, password):

# Start the while loop

    

    # Replace the following lines with your validation logic
 
       
        # Proceed with the application logic (e.g., show account balances)
        
   
       
       

# Check if the maximum attempts were reached

   

        # TODO: Validate the email and password using the Validation class.
        attempts = 1
    

 
        email = input("Enter your email: ")
        password = input("Enter your password: ")

        # Validate email and password
        if Validation.validate_email(email) and Validation.validate_password(password):
            print("Login successful!")
            # Proceed with showing account balances or other functionalities
            
        else:
            print("Invalid email or password. Please try again.")
            attempts += 1

    
        print("Maximum login attempts reached. Exiting the program.")
        exit()

            # If the email and password are invalid,
            # print a message and prompt the user to enter their email and password again.



        # TODO: Otherwise, break out of the loop.

    # TODO: If the maximum number of attempts is reached, print a message and exit the program.

    # Set up accounts with default balances.


    # Print a message for the user inform them of their checking and savings balances
   
    # TODO: Use the get_balance method to retrieve the current balance of each account.

    # TODO: Write while loop to present options for the user.
    # TODO: Present a menu of options to the user.
    # TODO: Allowing them to make deposits, withdrawals, or transfers between accounts.

        # TODO: Create a list of valid choices.

            # TODO: Use if/elif conditional statements to check the user's choice.
            # TODO: If the choice is in the list of valid choices, call the appropriate function.
            # TODO: Pass in the checking_account and savings_account objects.


        # TODO: If the user enters an invalid choice, print a message.

        attempts = 0  # Initialize the attempts variable

    

def validate_credentials(email, password):
    # Placeholder for actual validation logic
    return email == "user@example.com" and password == "password123"

# Call the login function
login()
