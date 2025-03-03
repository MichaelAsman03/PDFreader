import pyttsx3
import PyPDF2
from tkinter.filedialog import *

book = askopenfilename()


if not book:
    print("No file selected.")
    exit()

pdfreader = PyPDF2.PdfReader(book)
pages = len(pdfreader.pages)


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


# Read the PDF out loud
for num in range(pages):
    page = pdfreader.pages[num]
    text = page.extract_text()


    if text:
        player.say(text)
        player.runAndWait()