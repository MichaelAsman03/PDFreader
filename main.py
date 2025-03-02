import pyttsx3
import PyPDF2
from tkinter.filedialog import *

book = askopenfilename()

pdfreader = PyPDF2.PdfReader(book)
pages = len(pdfreader.pages)


player = pyttsx3.init()

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


for num in range(pages):
    page = pdfreader.pages[num]
    text = page.extract_text()
    

    
    if text:
        player.runAndWait()