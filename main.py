import pyttsx3
import PyPDF2
from tkinter.filedialog import *

book = askopenfilename()

# If the user doesn't 
if not book:
    print("No file selected.")
    exit()

# Once the program has a file at hand, the program will use PdfReader to open and read the PDF.
pdfreader = PyPDF2.PdfReader(book)
# To find out how many pages are in the PDF.
pages = len(pdfreader.pages)

# The text-to-speech engine.
player = pyttsx3.init()


print("Choose the reading speed:")
print("1. Slow")
print("2. Normal")
print("3. Fast")
choice = input("Enter your choice: ")

# Set the speaking rate based on user choice
if choice == "1":
    player.setProperty("rate", 100)
    print("Set to Slow speed (100 wpm)")
elif choice == "2":
    player.setProperty("rate", 150)
    print("Set to Normal speed (150 wpm)")
elif choice == "3":
    player.setProperty("rate", 200)
    print("Set to Fast speed (200 wpm)")
else:
    print("Invalid choice.")
    player.setProperty("rate", 150)  # Default speed
    print("Set to Default speed (150 wpm)")


# Reads the PDF one page at a time.
for num in range(pages):
    page = pdfreader.pages[num]
    text = page.extract_text()

# Checks to see if there's an actual text to read from.
    if text:
        # Makes sure that the speech engine to say the text out loud.
        player.say(text)
        player.runAndWait()