from tkinter import *
from tkinter import ttk

root = Tk()
root.geometry('700x500')
root['bg'] = 'lightblue'

# Data storage for individual students
class StudentInfo:

    def __init__(self, num, name, courseMark1, courseMark2, courseMark3, examMark):
        self.num = num
        self.name = name
        self.totalCourseMark = courseMark1 + courseMark2 + courseMark3
        self.examMark = examMark
        self.totalScore = self.totalCourseMark + examMark
        self.totalPercentage = (self.totalScore / 160) * 100
        self.grade = self.calculate_grade()

    def calculate_grade(self):
        if self.totalPercentage >= 70:
            return "A"
        elif 70 > self.totalPercentage >= 60:
            return "B"
        elif 60 > self.totalPercentage >= 50:
            return "C"
        elif 50 > self.totalPercentage >= 40:
            return "D"
        else:
            return "F"

def file_open():
    sorted_list = []
    with open('studentMarks.txt') as file_handler:
        content = file_handler.readlines()
        for line in content:
            num, name, courseMark1, courseMark2, courseMark3, examMark = line.strip().split(',')
            sorted_list.append(StudentInfo(num, name,
                                           int(courseMark1), int(courseMark2), int(courseMark3), int(examMark)))
        return sorted_list


list = file_open()

# Function to update the display box and disable it after
def update_display_box(content):
    display_box.config(state=NORMAL)  # Enable the display box for editing
    display_box.delete(1.0, END)  # Clear previous content
    display_box.insert(END, content)  # Insert new content
    display_box.config(state=DISABLED)  # Disable the display box again


def view_all():
    content = ""
    for student in list:
        content += (f"Student Name: {student.name}\n"
                    f"Student Number: {student.num}\n"
                    f"Coursework Total: {student.totalScore}\n"
                    f"Exam Mark: {student.examMark}\n"
                    f"Overall Percentage: {student.totalPercentage}%\n"
                    f"Grade: {student.grade}\n\n")
    update_display_box(content)


def highest_score():
    highest = max(list, key=lambda s: s.totalScore)
    content = (f"Student Name: {highest.name}\n"
               f"Student Number: {highest.num}\n"
               f"Coursework Total: {highest.totalScore}\n"
               f"Exam Mark: {highest.examMark}\n"
               f"Overall Percentage: {highest.totalPercentage}%\n"
               f"Grade: {highest.grade}\n\n")
    update_display_box(content)


def lowest_score():
    lowest = min(list, key=lambda s: s.totalScore)
    content = (f"Student Name: {lowest.name}\n"
               f"Student Number: {lowest.num}\n"
               f"Coursework Total: {lowest.totalScore}\n"
               f"Exam Mark: {lowest.examMark}\n"
               f"Overall Percentage: {lowest.totalPercentage}%\n"
               f"Grade: {lowest.grade}\n\n")
    update_display_box(content)


def view_record():
    selected_student = stdnt_choice_box.get().capitalize()
    for student in list:
        if student.name.strip().capitalize() == selected_student:
            content = (f"Student Name: {student.name}\n"
                       f"Student Number: {student.num}\n"
                       f"Coursework Total: {student.totalScore}\n"
                       f"Exam Mark: {student.examMark}\n"
                       f"Overall Percentage: {student.totalPercentage}%\n"
                       f"Grade: {student.grade}\n\n")
            update_display_box(content)
            return  # Exit after displaying the selected student


# Widgets

row_one_frame = Frame(root, bg='lightblue')

view_all_btn = Button(row_one_frame, text="View All Records", command=view_all,
                      font=('Ariel', 12)).pack(side='left', padx=16)

high_score_btn = Button(row_one_frame, text="Show Highest Score", command=highest_score,
                        font=('Ariel', 12)).pack(side='left', padx=16)

low_score_btn = Button(row_one_frame, text="Show Lowest Score", command=lowest_score,
                       font=('Ariel', 12)).pack(side='left', padx=16)

row_two_frame = Frame(root, bg='lightblue')

l1 = Label(row_two_frame, text="View Individual Student Record:",
           font=('Roberto', 12), bg='lightblue').pack(side='left', padx=8)

stdnt_choice_box = ttk.Combobox(row_two_frame)
stdnt_choice_box.pack(side='left', padx=8)
stdnt_choice_box['values'] = [student.name for student in list]

view_rec_btn = Button(row_two_frame, text="View Record", command=view_record,
                      font=('Ariel', 12)).pack(side='left', padx=8)

# Display box
display_box = Text(root, height=15, width=62)
display_box.config(state=DISABLED)  # Disable the display box initially

# Layout the frames and widgets
Label(root, text="Student Manager", font=('Roberto', 20, 'bold'), bg='lightblue').pack(pady=12)
row_one_frame.pack(pady=12)
row_two_frame.pack(pady=12)
display_box.pack()

root.mainloop()
