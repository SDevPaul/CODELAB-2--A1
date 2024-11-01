from tkinter import *   # Import tkinter GUI
from tkinter import ttk     # Import ttk for advanced widgets

root = Tk()  # Create the main window
root.geometry('700x500')  # Window size
root['bg'] = 'lightblue'  # Window size

# Data storage for individual students
class StudentInfo:
    # Constructor for initializing student information
    def __init__(self, num, name, courseMark1, courseMark2, courseMark3, examMark):
        self.num = num  # Store the student number
        self.name = name  # Store the student name
        # Calculate the total course mark by summing the three course marks
        self.totalCourseMark = courseMark1 + courseMark2 + courseMark3
        self.examMark = examMark  # Store the exam mark
        # Calculate the total score as the sum of course and exam marks
        self.totalScore = self.totalCourseMark + examMark
        # Calculate the total percentage based on a maximum of 160 points
        self.totalPercentage = (self.totalScore / 160) * 100
        self.grade = self.calculate_grade()  # Determine the grade based on the percentage

    # Method to calculate the grade based on the percentage
    def calculate_grade(self):
        if self.totalPercentage >= 70:
            return "A"  # Return A for 70% and above
        elif 70 > self.totalPercentage >= 60:
            return "B"  # Return B for 60% to less than 70%
        elif 60 > self.totalPercentage >= 50:
            return "C"  # Return C for 50% to less than 60%
        elif 50 > self.totalPercentage >= 40:
            return "D"  # Return D for 40% to less than 50%
        else:
            return "F"  # Return F for below 40%

# Method to open the file and read student data
def file_open():
    sorted_list = []  # Create a list to hold student objects
    with open('studentMarks.txt') as file_handler:  # Open the student marks file
        content = file_handler.readlines()  # Read all lines from the file
        for line in content:  # Loop through each line in the file
            # Split the line into student details and convert marks to integers
            num, name, courseMark1, courseMark2, courseMark3, examMark = line.strip().split(',')
            # Create a StudentInfo object and append it to the sorted list
            sorted_list.append(StudentInfo(num, name, int(courseMark1), int(courseMark2), int(courseMark3), int(examMark)))
        return sorted_list  # Return the list of student objects

list = file_open()  # Load student data into a list

# Function to update the display box and disable it after editing
def update_display_box(content):
    display_box.config(state=NORMAL)  # Enable the display box for editing
    display_box.delete(1.0, END)  # Clear previous content
    display_box.insert(END, content)  # Insert new content into the display box
    display_box.config(state=DISABLED)  # Disable the display box to prevent editing

# Function to view all student records
def view_all():
    content = ""  # Initialize an empty string for displaying content
    for student in list:  # Loop through each student in the list
        # Format the content for each student
        content += (f"Student Name: {student.name}\n"
                    f"Student Number: {student.num}\n"
                    f"Coursework Total: {student.totalScore}\n"
                    f"Exam Mark: {student.examMark}\n"
                    f"Overall Percentage: {student.totalPercentage:.2f}%\n"
                    f"Grade: {student.grade}\n\n")
    update_display_box(content)  # Update the display box with the compiled content

# Function to show the student with the highest score
def highest_score():
    highest = max(list, key=lambda s: s.totalScore)  # Find the student with the maximum score
    content = (f"Student Name: {highest.name}\n"
               f"Student Number: {highest.num}\n"
               f"Coursework Total: {highest.totalScore}\n"
               f"Exam Mark: {highest.examMark}\n"
               f"Overall Percentage: {highest.totalPercentage:.2f}%\n"
               f"Grade: {highest.grade}\n\n")
    update_display_box(content)  # Update the display box with the highest score information

# Function to show the student with the lowest score
def lowest_score():
    lowest = min(list, key=lambda s: s.totalScore)  # Find the student with the minimum score
    content = (f"Student Name: {lowest.name}\n"
               f"Student Number: {lowest.num}\n"
               f"Coursework Total: {lowest.totalScore}\n"
               f"Exam Mark: {lowest.examMark}\n"
               f"Overall Percentage: {lowest.totalPercentage:.2f}%\n"
               f"Grade: {lowest.grade}\n\n")
    update_display_box(content)  # Update the display box with the lowest score information

# Function to view an individual student's record based on selection
def view_record():
    selected_student = stdnt_choice_box.get().capitalize()  # Get the selected student name
    for student in list:  # Loop through each student in the list
        # Check if the selected student matches the current student name
        if student.name.strip().capitalize() == selected_student:
            content = (f"Student Name: {student.name}\n"
                       f"Student Number: {student.num}\n"
                       f"Coursework Total: {student.totalScore}\n"
                       f"Exam Mark: {student.examMark}\n"
                       f"Overall Percentage: {student.totalPercentage:.2f}%\n"
                       f"Grade: {student.grade}\n\n")
            update_display_box(content)  # Update the display box with the selected student's information
            return  # Exit the function after displaying the student record

# Create frames for layout
row_one_frame = Frame(root, bg='lightblue')  # Frame for the first row of buttons

# Button to view all student records
view_all_btn = Button(row_one_frame, text="View All Records", command=view_all,
                      font=('Ariel', 12)).pack(side='left', padx=16)

# Button to show the student with the highest score
high_score_btn = Button(row_one_frame, text="Show Highest Score", command=highest_score,
                        font=('Ariel', 12)).pack(side='left', padx=16)

# Button to show the student with the lowest score
low_score_btn = Button(row_one_frame, text="Show Lowest Score", command=lowest_score,
                       font=('Ariel', 12)).pack(side='left', padx=16)

row_two_frame = Frame(root, bg='lightblue')  # Frame for the second row of inputs

# Label for viewing individual student records
l1 = Label(row_two_frame, text="View Individual Student Record:",
           font=('Roberto', 12), bg='lightblue').pack(side='left', padx=8)

# Combobox for selecting a student
stdnt_choice_box = ttk.Combobox(row_two_frame)
stdnt_choice_box.pack(side='left', padx=8)
stdnt_choice_box['values'] = [student.name for student in list]  # Populate combobox with student names

# Button to view a specific student's record
view_rec_btn = Button(row_two_frame, text="View Record", command=view_record,
                      font=('Ariel', 12)).pack(side='left', padx=8)

# Display box to show student information
display_box = Text(root, height=15, width=62, font=('Ariel', 11))
display_box.config(state=DISABLED)  # Disable the display box initially

# Layout the frames and widgets
Label(root, text="Student Manager", font=('Roberto', 20, 'bold'), bg='lightblue').pack(pady=12)  # Title label
row_one_frame.pack(pady=12)  # Pack the first row frame
row_two_frame.pack(pady=12)  # Pack the second row frame
display_box.pack()  # Pack the display box

root.mainloop()  # Start and Display the window
