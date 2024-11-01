from tkinter import *   # Import tkinter
import random   # Importing "random" library to be able to use the class and methods given from this library

root = Tk()     # Create Main Window
root.geometry("500x400")    # Window size
root.config(bg='lightblue')     # Window color background

current_question = 0  # Track the current question number
score = 0  # Store's the user's score
attempts = 0  # Track attempts for each question (max 2 attempts per question)

total_questions = 10  # Number of questions to ask
current_problem = None  # Store the current math problem


# Method to reset the previous quiz and go back the beginning
def reset_quiz():
    global current_question, score  # Ensures that the variables are updated throughout the program/globally
    # Resets to the initial value to get ready for the new game
    current_question = 0    # Changing the current question and score value
    score = 0               # to the initial value and then
    clear_frame(window_frame)   # Clears the previous frame then
    displayMenu()   # Displays the menu difficulty


# Method to set the selected difficulty
def setDifficulty(value):   # Takes a value then
    global difficulty_level
    difficulty_level = value  # Set the difficulty level and updates the variable globally
    ask_question(difficulty_level)  # Then starts asking the first question to the player


# A method that ask a new question and reset attempts
def ask_question(difficulty):
    global current_problem, attempts    # Updates the variables globally

    # If all questions have been asked, display the final results
    if current_question >= total_questions:
        displayResults()
        return

    # else reset attempts for the new question
    attempts = 0

    # Then generate random numbers and operation for the current problem
    two_random_integers = randomInt(difficulty)    # First it create a list that contains two random integers
    selected_operator = decideOperation()          # Then decides if the operator is addition or subtraction and then
    current_problem = (two_random_integers[0], two_random_integers[1],
                       selected_operator)                                   # It stores the current problem

    # Then clears the previous question and then displays the new question
    clear_frame(window_frame)   # Clearing the frame of the previous question
    displayProblem(two_random_integers[0], two_random_integers[1], selected_operator)   # Then displays the new question


# Method to determine the digit/s that will be displayed based on difficulty level.
def randomInt(difficulty):  # Takes the set value of the difficulty
    if difficulty == 1:     # When easy difficulty is selected
        return random.randint(1, 9), random.randint(1, 9)   # It gives one digit integers
    elif difficulty == 2:   # Else if its moderate, then
        return random.randint(10, 99), random.randint(10, 99)   # two digits will be returned
    elif difficulty == 3:   # Or if its advanced, then
        return random.randint(1000, 9999), random.randint(1000, 9999) # three digits will be returned instead


# Method that randomly choose between addition and subtraction
def decideOperation():
    return random.choice(['+', '-'])    # The random choice method randomly choose between addition or subtraction


# Method that displays the math question and accepts the user's answer.
def displayProblem(num1, num2, operator):   # This method takes the two random integers and the operator
    global current_question, feedback_label     # Updates the variables globally

    # Displays what question you are in and the question
    Label(window_frame, text=f"Question {current_question + 1}:", font=("Cambria", 18), bg='lightblue').pack(pady=10)
    Label(window_frame, text=f"What is {num1} {operator} {num2}?", font=("Cambria", 20), bg='lightblue').pack(pady=20)

    # Entry for the player answer
    answer_entry = Entry(window_frame, font=("Ariel", 16))
    answer_entry.pack(pady=10)
    # This Ensures the player does not need to keep manually clicking the entry after every answer
    answer_entry.focus_set()

    # Feedback label to show messages to the player
    feedback_label = Label(window_frame, font=("Cambria", 18), bg='lightblue')
    feedback_label.pack(pady=10)

    # Submit button to check the answer
    submit_button = Button(window_frame, text="Submit", font=("Ariel", 14),
                           command=lambda: check_answer(num1, num2, operator, answer_entry))
    submit_button.pack(pady=10)

    # Bind Enter key to the Submit button for player to not have to manually click the button with the cursor
    root.bind('<Return>', lambda event: submit_button.invoke())


# Method to check if the user's answer is correct and manage scoring
def check_answer(num1, num2, operator, answer_entry):   # Takes the question integer, operator, and the user's answer
    global score, attempts, current_question    # Updates variables globally

    # Get the answer from the entry
    answer = answer_entry.get()

    # Once the player gives the answer, it checks if the answer given can be converted to an integer
    try:
        answer = int(answer)    # If it can be converted to an integer then
        correct = isCorrect(num1, num2, operator, answer)   # it checks if the answer is correct

        if correct:     # If the answer is correct then it checks how many attempt it took
            if attempts == 0:   # If it's the first try then
                score += 10  # Player is awarded 10 points for the first attempt
            elif attempts == 1: # if not then
                score += 5  # Only 5 points for the second attempt

            current_question += 1  # Then updates the variable and move to the next question
            feedback_label.config(text="Correct!", fg="green")  # As well as displays that the answer is correct
            answer_entry.delete(0, END)  # And then clears the entry for new input
            # And passes the difficulty for the next question to ensure it's the same difficulty throughout the quiz
            root.after(1000, lambda: ask_question(difficulty_level))

        else:   # If you got your answer wrong then
            attempts += 1   # the attempt variable is updated then
            if attempts >= 2:   # Checks if this is the second or third attempt and
                current_question += 1  # move to the next question after 2 attempts

                # Displays that the answer is wrong
                feedback_label.config(text="Incorrect! Moving to the next question.", fg="red")
                answer_entry.delete(0, END)  # Then clear the entry for new input and
                root.after(1000, lambda: ask_question(difficulty_level))  # Pass the difficulty for the next question
            else:   # Though if you got the first one wrong it gives you one last attempt
                feedback_label.config(text="Try again!", fg="orange")   # And displays to try again

    except ValueError:  # If the answer cannot be converted into an integer then
        feedback_label.config(text="Please enter a valid number.", fg="red")    # The program ask for an integer
        answer_entry.delete(0, END)  # And then clear the entry for new input


# Check if the user's answer is correct
def isCorrect(num1, num2, operator, answer):    # Takes the current question integer, operator, and player answer
    if operator == '+':     # If the operator is addition
        return answer == num1 + num2    # Then it solves the question then checks if the answer is correct/equal
    else:   # Else if the operator is subtraction
        return answer == num1 - num2    # Solves the question then checks if the answer is correct/equal


# Clear the current frame's contents
def clear_frame(frame):

    # For all the children of the specified frame
    for widget in frame.winfo_children():
        widget.destroy()    # Is destroyed


# This method displays the user's final score after 10 questions
def displayResults():
    clear_frame(window_frame)   # Clears the previous frame
    # And then sets up the result to be displayed
    Label(window_frame, text="Quiz Completed!", font=("Cambria", 26), bg='lightblue').pack(pady=40)
    Label(window_frame, text=f"Your final score is: {score}/{total_questions * 10}",
          font=("Cambria", 20), bg='lightblue').pack(pady=20)

    # Gives the user their grade
    if score >= 90:
        grade = "A+"
    elif 90 > score >= 80:
        grade = "A"
    elif 80 > score >= 70:
        grade = "B"
    elif 70 > score >= 60:
        grade = "C"
    elif 60 > score >= 50:
        grade = "D"
    elif 50 > score >= 40:
        grade = "E"
    else:
        grade = "F"

    # Displays the grade
    Label(window_frame, text=f"Your grade is: {grade}", font=("Cambria", 20), bg='lightblue').pack(pady=20)

    # Displays Restart button to restart the quiz
    Button(window_frame, text="Restart Quiz", font=("Ariel", 16), command=reset_quiz).pack(pady=20)


# Start menu for difficulty selection
def displayMenu():
    # Displays the label and buttons
    Label(window_frame, text="Arithmetic Quiz", font=("Cambria", 26), bg='lightblue').pack(pady=40)

    Button(window_frame, text="Easy", command=lambda: setDifficulty(1),                 # Easy Difficulty Button
           font=("Ariel", 18), width=15, bg="#84DB79", fg="White").pack(pady=5)
    Button(window_frame, text="Moderate", command=lambda: setDifficulty(2),             # Moderate Difficulty Button
           font=("Ariel", 18), width=15, bg="#FCCA52", fg="White").pack(pady=5)
    Button(window_frame, text="Advanced", command=lambda: setDifficulty(3),             # Advanced Difficulty Button
           font=("Ariel", 18), width=15, bg="#FC5252", fg="White").pack(pady=5)


# Main window frame
window_frame = Frame(root, bg='lightblue')
window_frame.pack(fill=BOTH, expand=True)

displayMenu()  # Display the difficulty menu at the start

root.mainloop()     # Start and Display the window
