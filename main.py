import pyttsx3
import PyPDF2
from tkinter.filedialog import *

book = askopenfilename()

pdfreader = PyPDF2.PdfReader(book)
pages = len(pdfreader.pages)


player = pyttsx3.init()

# Get the current speaking rate and print for debugging
current_rate = player.getProperty('rate')
print(f"Current speaking rate: {current_rate}")


print("Choose the reading speed:")
print("1. Slow")
print("2. Normal")
print("3. Fast")
choice = input("Enter your choice: ")

if choice == "1":
    player.setProperty("Rate", 100)
elif choice == "2":
    player.setProperty("Rate", 150)
elif choice == "3":
    player.setProperty("Rate", 200)
else:
    print("Invalid choice.")  
    player.setProperty("rate", 150)  # Default speed

# Check if the speed has been updated
updated_rate = player.getProperty('rate')
print(f"Updated speaking rate: {updated_rate}")

# Read the PDF out loud
for num in range(pages):
    page = pdfreader.pages[num]
    text = page.extract_text()


for num in range(pages):
    page = pdfreader.pages[num]
    text = page.extract_text()
    

    
    if text:
        player.say(text)
        player.runAndWait()