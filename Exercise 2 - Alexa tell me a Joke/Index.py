from tkinter import *   # Import tkinter GUI
import random   # Importing "random" library to be able to use the class and methods given from this library

root = Tk()      # Create Main Window
root.geometry("425x500")    # Window size
root['bg'] = 'lightblue'    # Window color background

current_joke = []  # Store the current joke setup and punchline


# A method to display the message to the chat box
def send_message(joke_container):   # Takes the current joke

    message = v.get().strip()  # Gets user message
    chatbox.config(state=NORMAL)  # Enables editing temporarily
    chatbox.insert(END, "You: " + message + "\n")   # Inserts user message to the chat box
    chatbox.config(state=DISABLED)  # Disables editing again
    textbox.delete(0, END)  # Deletes the message in the entry box

    # Check if the user prompts "Alexa tell me a joke"
    if message.lower().startswith("alexa tell me a joke"):  # If yes
        alexa_jokes()   # Then Alexa will tell a joke

    # And if a joke has been set up and the user type any of the starting prompt to show the punchline
    elif joke_container and (message.lower().startswith("what")
                           or message.lower().startswith("why")
                           or message.lower().startswith("how")):

        chatbox.config(state=NORMAL)    # Enables editing temporarily
        chatbox.insert(END, "Alexa: " + current_joke[1] + "\n")     # Alexa tells the punchline
        chatbox.config(state=DISABLED)  # Disables editing again

    elif message.lower() == 'quit':     # If the user type quit then the program closes
        root.destroy()  # Closes the program
    else:   # If the user did not prompt asking Alexa to tell them a joke then
        chatbox.config(state=NORMAL)    # Enables editing temporarily
        # Alexa provides an instruction to the user
        chatbox.insert(END, "Alexa: Sorry, I didn't understand that.\n\t(Type 'Alexa tell me a joke')\n")
        chatbox.config(state=DISABLED)  # Disables editing again


# Method for alexa to give a joke from the file
def alexa_jokes():
    global current_joke     # Ensures that the variable is updated throughout the program/globally

    with open("randomJokes.txt") as jokes_file:     # Opening the file as jokes_file variable

        jokes_list = jokes_file.readlines()  # Read all lines from the file into a list
        random_joke = random.choice(jokes_list)  # Pick a random line from the jokes list
        question_answer = random_joke.split('?')  # Split the sentence at the '?' symbol

        # Sort the question and answer
        question = question_answer[0] + '?'     # Adds a question mark to the question
        answer = question_answer[1].strip()     # Ensure that there are no extra whitespaces
        current_joke = (question, answer)  # Store the current joke (setup and punchline)

        # Display the setup of the joke
        chatbox.config(state=NORMAL)    # Enables editing temporarily
        # Alexa providing the joke with an instruction how to get the punchline
        chatbox.insert(END, "Alexa: " + question + "\n\t(Type 'what', 'how', or 'why' to see the punchline)\n")
        chatbox.config(state=DISABLED)  # Disables editing again


v = StringVar()     # To store the string that is inputed to the entry

# Create a frame to hold the chat box and scrollbar
frame = Frame(root)
frame.pack(pady=10)

# Create the chatbox (Text widget)
chatbox = Text(frame, height=23, width=50, wrap='word', borderwidth=5, relief='groove')
chatbox.config(state=DISABLED)  # Disable editing

# Create a scrollbar for the chatbox
scrollbar = Scrollbar(frame, command=chatbox.yview)
chatbox.config(yscrollcommand=scrollbar.set)

# Pack the chatbox and scrollbar side by side
chatbox.pack(side=LEFT, fill=BOTH, expand=True)
scrollbar.pack(side=RIGHT, fill=Y)

# Create the input textbox
textbox = Entry(root, width=65, textvariable=v, borderwidth=5, relief='groove')
textbox.pack(padx=10, ipadx=10, ipady=2)

# Bind the Return key to send a message
root.bind('<Return>', lambda event: send_message(current_joke))

# Send button
Button(root, text="Send Message", command=send_message).pack(pady=8)

root.mainloop()     # Start and Display the window
