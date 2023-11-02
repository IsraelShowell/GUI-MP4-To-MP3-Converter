#Creator: Israel Showell
#Date Created: 11-2-23
#Allows a user to convert an mp4 file to an mp3 file by entering a path to the directory where the file is located.
#The mp3 file will be generated in the directory where the Python script is.

# Imports the tkinter library for GUI
import tkinter as tk
from tkinter import messagebox

#Imports the moviepy.editor that controls the conversion
from moviepy.editor import *


def convertMP4():
    
    Conv = Conv_entry.get() #Gets the text stored in the text area
    
    print(Conv) #Prints the entered path.

    # Loads the mp4 file
    video = VideoFileClip(Conv)

    # Extracts audio from video
    video.audio.write_audiofile(Conv + ".mp3")



# Creates the main window
root = tk.Tk()
root.title("GUI MP4 to MP3 Converter")  # Sets the window title

# Creates input fields and labels
Conv_label = tk.Label(root, text="Enter the path to your mp4 file:")  # Create a label
#Note, the path to the file should be inputted like this:
#C:/Users/User1/Downloads/file.mp4
Conv_label.pack()  # Packs the label into the window
Conv_entry = tk.Entry(root)  # Creates an input field to enter the path to the file
Conv_entry.pack()  # Packs the input field into the window


run_button = tk.Button(root, text="Convert MP4", command=convertMP4)  # Creates a button that calls the function
run_button.pack()  # Packs the button into the window

root.mainloop()




