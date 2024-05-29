# ------------------------------------------------------------------------------------------ #
# Title: Assignment06
# Desc: This assignment demonstrates using functions
# with structured error handling
# Change Log: (Who, When, What)
#   RRoot,1/1/2030,Created Script
#   Rachel Hostetler,05/25/2024,Assignment06
# ------------------------------------------------------------------------------------------ #
from codeop import Compile
from collections import defaultdict
import json

# Define the Data Constants
MENU: str = '''
---- Course Registration Program ----
  Select from the following menu:  
    1. Register a Student for a Course.
    2. Show current data.  
    3. Save data to a file.
    4. Exit the program.
----------------------------------------- 
'''
# Define the Data Constants
FILE_NAME: str = "Enrollments.json"

# Define the Data Variables and constants
menu_choice: str = ''  # Hold the choice made by the user.
students: list = [] 

# define FileProcessor class
class FileProcessor:
    """
    this class processes files, such as reading and writing data to files
    
    ChangeLog: (Who, When, What)
    RachelHostetler,5/25/2024,Created Class
    """
    
    # define functions
    @staticmethod
    def read_data_from_file(file_name: str, student_data: list):
        """
        this function reads data from the file
    
        ChangeLog: (Who, When, What)
        RachelHostetler,5/25/2024,Created function
        """   
        # When the program starts, read the file data into a list of lists (table)
        # Extract the data from the file
        try:
            file = open(file_name, "r")

            # JSON Answer
            student_data = json.load(file)

            file.close()
            
        except FileNotFoundError as e:
            IO.output_error_messages("File not found!", e)
            
        except Exception as e:
            IO.output_error_messages("Undefined Error!", e)
            
        finally:
            if file.closed == False:
                file.close()
        return student_data 

    @staticmethod
    def write_data_to_file(file_name: str, student_data: list):
        """
        this function writes data to the file
    
        ChangeLog: (Who, When, What)
        RachelHostetler,5/25/2024,Created function
        """   
        try:
            file = open(file_name, "w")

            # # JSON answer
            json.dump(student_data, file)

            file.close()
            
            IO.output_student_courses(student_data=student_data)
                
        except TypeError as e:
            IO.output_error_messages("check that data file is JSON format", e)
        except Exception as e:
            IO.output_error_messages("Undefined error!", e)
            
        finally:
            if file.closed == False:
                file.close()
            

# define IO class
class IO:
    """
    this class does inputs and outputs
    
    ChangeLog: (Who, When, What)
    RachelHostetler,5/25/2024,Created Class
    """
    
    # define functions
    @staticmethod    
    def output_error_messages(message: str, error: Exception = None):
        """ 
        shows output error message, has handing error
    
        ChangeLog: (Who, When, What)
        RachelHostetler,5/25/2024,Created function
        """
        print(message, end="\n")
        if error is not None:
                print("- Error - ")
                print(error, error.__doc__, type(error), sep='\n')

    @staticmethod
    def output_menu(menu: str):
        """ 
        displays menu options
        ChangeLog: (Who, When, What)
        RachelHostetler,5/25/2024,Created function
    
        """
        print(menu)
    
    @staticmethod
    def input_menu_choice():
        """ 
        input menu choices from user
        ChangeLog: (Who, When, What)
        RachelHostetler,5/25/2024,Created function
        """
       
        menu_choice = "0"
        try:
            menu_choice = input("Enter your menu choice number: ")
            if menu_choice not in ("1","2","3","4"):
                raise Exception("choose only 1, 2, 3, or 4")
        except Exception as e:
            IO.output_error_messages("undefined error!", e) 
        return menu_choice
    
    @staticmethod
    def output_student_courses(student_data: list):
        """ 
        this function shows the students and their enrolled courses
    
        ChangeLog: (Who, When, What)
        RachelHostetler,5/25/2024,Created function
        """     
        # Process the data to create and display a custom message
        print("-" * 50)
        for student in student_data:
            print(f'Student {student["FirstName"]} '
                  f'{student["LastName"]} is enrolled in {student["CourseName"]}')
        print("-" * 50)

    @staticmethod
    def input_student_data(student_data: list):
        """
        this function enters data about the student
    
        ChangeLog: (Who, When, What)
        RachelHostetler,5/25/2024,Created function
        """      
        try:
            student_first_name = input("Enter the student's first name: ")
            if not student_first_name.isalpha():
                raise ValueError("The last name should not contain numbers.")
            student_last_name = input("Enter the student's last name: ")
            if not student_last_name.isalpha():
                raise ValueError("The last name should not contain numbers.")
            course_name = input("Please enter the name of the course: ")
            student = {"FirstName": student_first_name,
                            "LastName": student_last_name,
                            "CourseName": course_name}
            student_data.append(student)
            print(f"You have registered {student_first_name} {student_last_name} for {course_name}.")
        except ValueError as e:
            IO.output_error_messages("Make sure input data is correct", e)
        except Exception as e:
            IO.output_error_messages("Undefined error!", e)
        return student_data
    
            
students = FileProcessor.read_data_from_file(file_name = FILE_NAME, student_data = students)

# Present and Process the data
while (True):

    IO.output_menu(menu = MENU)

    # Present the menu of choices
    menu_choice = IO.input_menu_choice()

    # Input user data
    if menu_choice == "1":  # This will not work if it is an integer!
           
        students = IO.input_student_data(student_data = students)
        continue

    # Present the current data
    elif menu_choice == "2":

        IO.output_student_courses(student_data = students)
        continue

    # Save the data to a file
    elif menu_choice == "3":
        
        FileProcessor.write_data_to_file(file_name = FILE_NAME, student_data = students)
        continue

    # Stop the loop
    elif menu_choice == "4":
        break  # out of the loop
    else:
        print("Please only choose option 1, 2, or 3")

print("Program Ended")
