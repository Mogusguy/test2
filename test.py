from tkinter import *
import random
import json
import os

# Function to load names from the JSON file
def load_names():
    if os.path.exists("names.json"):
        with open("names.json", "r") as f:
            return json.load(f)
    return reset_names()  # Reset if the file doesn't exist

# Function to save names to the JSON file
def save_names(names):
    with open("names.json", "w") as f:
        json.dump(names, f)

# Function to reset names to the default list
def reset_names():
    default_names = ["Liam", "Noah", "Oliver", "Elijah", "James",
                     "William", "Benjamin", "Lucas", "Henry", "Alexander"]
    save_names(default_names)
    return default_names

# Function to randomly select a name
def random_name():
    names = load_names()
    if names:  # Check if names are not empty
        text.config(text="Hi " + random.choice(names))
    else:
        text.config(text="No names available!")  # Handle case where no names are present

# Function to delete the displayed name
def delete():
    text.pack_forget()

# Function to generate a random name
def name_gen():
    text.pack()
    random_name()

# Function to add a new name to the list
def add_name():
    new_name = entry.get().strip()
    if new_name:
        names = load_names()
        if new_name not in names:
            names.append(new_name)
            save_names(names)
            entry.delete(0, END)
        else:
            entry.delete(0, END)

# Initializing the main window
window = Tk()
window.geometry("600x600")

# Create a label to display text
text = Label(window, text="", font=("Impact", 20))
text.pack(pady=10)

# Create buttons and entry fields
Button(window, text="Do an action", command=name_gen).pack(pady=10)
entry = Entry(window)
entry.pack(pady=10)
Button(window, text="Add Name", command=add_name).pack(pady=10)

window.mainloop()
