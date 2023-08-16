import json
import random
import tkinter as tk
from tkinter import messagebox, simpledialog

# Load data from words.json
with open("words.json", "r") as json_file:
    dictionary = json.load(json_file)

def search_word():
    word = simpledialog.askstring("Search Word", "Enter the word you want to search for:").lower()
    definition = dictionary.get(word, "Word not found in the dictionary.")
    messagebox.showinfo("Search Result", f"Definition of '{word}': {definition}")

def add_word():
    word = simpledialog.askstring("Add Word", "Enter the new word:")
    definition = simpledialog.askstring("Add Word", "Enter the definition of the word:")
    result = add_word_to_dictionary(word, definition)
    messagebox.showinfo("Add Word Result", result)

def add_word_to_dictionary(word, definition):
    if word not in dictionary:
        dictionary[word] = definition
        with open("words.json", "w") as json_file:
            json.dump(dictionary, json_file, indent=4)
        return f"'{word}' added to the dictionary."
    else:
        return f"'{word}' already exists in the dictionary."

def display_words():
    starting_letter = simpledialog.askstring("Display Words", "Enter the starting letter:").lower()
    words_with_starting_letter = [word for word in dictionary if word.startswith(starting_letter)]
    
    root_display = tk.Toplevel()
    root_display.title(f"Words Starting with '{starting_letter}'")
    
    listbox = tk.Listbox(root_display)
    listbox.pack(fill=tk.BOTH, expand=True)
    
    for word in words_with_starting_letter:
        listbox.insert(tk.END, word)

def get_word_of_the_day():
    random_word = random.choice(list(dictionary.keys()))
    definition = dictionary[random_word]
    messagebox.showinfo("Word of the Day", f"Word of the Day: '{random_word}'\nDefinition: {definition}")

# Create the main GUI window
root = tk.Tk()
root.title("Dictionary Program")
root.geometry("400x300")  # Set the initial size of the window

# Create buttons for each function with improved layout
search_button = tk.Button(root, text="Search Word", command=search_word)
search_button.pack(pady=10)

add_button = tk.Button(root, text="Add Word", command=add_word)
add_button.pack(pady=10)

display_button = tk.Button(root, text="Display Words", command=display_words)
display_button.pack(pady=10)

word_of_day_button = tk.Button(root, text="Word of the Day", command=get_word_of_the_day)
word_of_day_button.pack(pady=10)

exit_button = tk.Button(root, text="Exit", command=root.quit)
exit_button.pack(pady=20)

# Run the GUI event loop
root.mainloop()
