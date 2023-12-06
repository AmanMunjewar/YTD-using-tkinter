from sys import exception
import tkinter
import customtkinter
from numpy import pad
from pytube import YouTube
from yaml import StreamEndEvent

def startDownload():
    try:
        ytLink = str(link.get())
        ytObject = YouTube(ytLink)
        video = ytObject.streams.get_highest_resolution() 
        
        if video != None:
            video.download()
        else:
            print("Invalid link")
    except:
        print("Error incountered")
    print("Successful download")

# Stting up the environment
customtkinter.set_appearance_mode("System")
customtkinter.set_default_color_theme("blue")

# Setting up the app frame
app = customtkinter.CTk()
app.geometry("720x480")
app.title("YouTube downloader")

# Add UI element
title = customtkinter.CTkLabel(app, text="Enter the YouTube link")
title.pack(padx=10, pady=10)

# Take link from the user
url_var = tkinter.StringVar()
link = customtkinter.CTkEntry(app, width=350, height=40, textvariable=url_var, placeholder_text="Enter the link here")
link.pack()

# Create the download button
button = customtkinter.CTkButton(app, text="Download", command=startDownload)
button.pack(padx=10, pady=10)

# Run app
app.mainloop()