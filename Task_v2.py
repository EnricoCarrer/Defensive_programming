# This program gives 2 options to the user:
#   option1: enter two numbers and an operation sign. The program will print the result and write the equations to a file (I used the file "equations.txt" wihich is also saved in this folder).
#   option2: enter a file name. The program will read the equations on the file and print them. 
# The program uses defensive programmming (loops, if-else, try-except) to handle unespected events and user inputs.

# Note on external sources: I couldn't figure out how to use the "try-except" block in this scenario so I asked ChatGPT and after a few trials and errors 
#   I managed to get it right. I also got information on writing to a file from https://thenewstack.io/yet-more-python-for-beginners-saving-input-to-a-file/


# Introduction and intructions for the user
print ("You have two options: \nOption1 - enter two numbers and an operation sign. The program will solve the equation and write it on a file.\nOption2 - enter a file name. The program will print the content of the file.")


# Use a while loop to keep prompting the user until a valid input is entered (either '1' or '2')
while True:
    user_choice = input("Please enter '1' for option1 or enter '2' for option2: ")
    if user_choice in ['1', '2']:
        break
    else:
        print ("Invalid input. Try again.")

# Define what happens if the user chose option1
if user_choice == '1':

    # Use a while loop and a try-except block for the input of the operands, so the program keeps prompting the user until a valid number is entered.
    while True:
        try:
            num1 = float(input("Please enter the first number: "))
            num2 = float(input("Please enter the second number: "))
            break
        except ValueError:
            print("Invalid input: that does not look like a number.")

    # Use a while loop with an if-else block for the input of the operation sign, so the program keeps prompting the user until a valid sign is entered.
    while True:
        operation_sign = input("Please enter an operation sign (+, -, *, /): ")
        if operation_sign in ["+", "-", "*", "/"]:
            break
        else:
            print("Invalid input: that does not look like an operation sign.")

    # Solve the equation (based on the operation sign) by creating two variables needed later
    if operation_sign == '+':
        result = round(num1 + num2, 2)      # use the round function to limit the decimals
        equation = f"{num1} + {num2} = {result}"
    if operation_sign == '-':
        result = round(num1 - num2, 2)
        equation = f"{num1} - {num2} = {result}"
    if operation_sign == '*':
        result = round(num1 * num2, 2)
        equation = f"{num1} * {num2} = {result}"
    if operation_sign == '/':
        try:
            result = round(num1 / num2, 2)
            equation = f"{num1} / {num2} = {result}"
        except ZeroDivisionError :
            result = "Error - a number cannot be divided by zero."
            equation = f"{num1} / {num2} = {result}"

    # Print the result
    print ("The result of your equation is:",result, "\nThis equation has been written to the file 'equations.txt'.")    

    # Write the equation to a file 
    #   (I picked the 'with' statement from ChatGPT and the open-write-close structure from:
    #   https://thenewstack.io/yet-more-python-for-beginners-saving-input-to-a-file/.
    #   The second argument 'a' (Append) in the 'open' command will create the file if it doesn't 
    #   exist and will add a new equation to the file rather than overwrite the previous one :-)
    with open("equations.txt", 'a') as file:
        file.write(equation + "\n")
        file.close()

# Define what happens if the user chose option2   
if user_choice == '2':
    
    # Ask user to type the file name and use defensive coding (while loop + try&except) so that if file does not exists,  
    #   the user is asked to try again until a valid file name is entered.
    while True:
        file_name = input('Please enter the name of the file you want to open (example: "equations.txt"): ')
        try:
            # the following 'with' block opens, read, print and finally close the file. 
            with open(file_name, 'r') as file:
                # as suggested by Chris during a live lesson, reading and printing lines rather than the whole file is recommended as some file formats would not be printed if read with a more general 'print(file.read())' 
                lines = file.readlines()
                for line in lines:      
                    print(line.strip())       
                file.close()
            break
        except FileNotFoundError:
            print ("The file does not exist. Try again.")
