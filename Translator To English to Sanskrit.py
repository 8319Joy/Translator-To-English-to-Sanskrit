#!/usr/bin/env python
# coding: utf-8

# # Translator To English to Sanskrit
Creating a program that translates English to Sanskrit is a complex task due to the intricacies of both languages, including grammar, syntax, and cultural context. However, I can guide you through a basic implementation using Python and a relevant library or approach.

Here’s a simple example of how you might create a basic English to Sanskrit translator. Note that this won't be a fully functional translator but can serve as a foundational template. For actual translation, you would typically need a comprehensive dictionary and grammatical rules.

Basic Python Implementation
First, you will need a dictionary of English-Sanskrit word pairs. Here’s a simplified version:
# In[2]:


# English to Sanskrit dictionary
english_to_sanskrit_dict = {
    "hello": "नमस्ते",
    "world": "जगत्",
    "goodbye": "अलविदा",
    "thank you": "धन्यवाद",
    "yes": "हाँ",
    "no": "नहीं",
    "please": "कृपया",
    "friend": "मित्र",
    "love": "प्रेम",
    "knowledge": "ज्ञान",
    "peace": "शांति",
    "life": "जीवन",
    "death": "मृत्यु",
    "water": "जल",
    "fire": "आग्नि",
    "earth": "पृथ्वी",
    "sky": "आसमान",
}

# Function to translate English to Sanskrit
def translate_to_sanskrit(english_word):
    return english_to_sanskrit_dict.get(english_word.lower(), "Translation not found.")

# Sample usage
if __name__ == "__main__":
    words_to_translate = ["hello", "world", "thank you", "friend", "life", "unknown"]
    
    for word in words_to_translate:
        translation = translate_to_sanskrit(word)
        print(f"{word} -> {translation}")


# In[10]:


import tkinter as tk
from tkinter import messagebox

# Sample dictionary for translation
translation_dict = {
    "hello": "नमस्ते",
    "world": "जगत्",
    "goodbye": "अलविदा",
    "thank you": "धन्यवाद",
    # Add more translations as needed
    "yes": "हाँ",
    "no": "नहीं",
    "please": "कृपया",
    "friend": "मित्र",
    "love": "प्रेम",
    "knowledge": "ज्ञान",
    "peace": "शांति",
    "life": "जीवन",
    "death": "मृत्यु",
    "water": "जल",
    "fire": "आग्नि",
    "earth": "पृथ्वी",
    "sky": "आसमान",
}

def translate():
    try:
        english_text = entry.get().lower()
        # Translate the text using the dictionary
        sanskrit_translation = translation_dict.get(english_text, "Translation not found.")
        
        # Display the result in the label
        result_label.config(text=sanskrit_translation)
    except Exception as e:
        messagebox.showerror("Error", str(e))

# Create the main application window
root = tk.Tk()
root.title("English to Sanskrit Translator")

# Create and place the entry widget for user input
entry = tk.Entry(root, width=50)
entry.pack(pady=20)

# Create and place the translate button
translate_button = tk.Button(root, text="Translate", command=translate)
translate_button.pack(pady=10)

# Create and place the label for displaying the result
result_label = tk.Label(root, text="", font=("Helvetica", 14))
result_label.pack(pady=20)

# Start the Tkinter event loop
root.mainloop()

Explanation of the Code:
Dictionary Structure: The dictionary english_to_sanskrit_dict contains English words as keys and their Sanskrit translations as values.
Translation Function: The function translate_to_sanskrit takes an English word as input, converts it to lowercase (to ensure case insensitivity), and retrieves the Sanskrit equivalent from the dictionary. If the word is not found, it returns "Translation not found."
Sample Usage: The sample usage at the bottom demonstrates how to use the translation function. You can replace the words_to_translate list with any words you want to translate.
# In[ ]:




