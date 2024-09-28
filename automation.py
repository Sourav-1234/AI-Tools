import tkinter as tk 
from tkinter import Entry,Label,Button
import webbrowser

#Defining the main window below for taking the tkinter root object
root=tk.Tk()
root.title('YOUR AUTOMATION AI ASSISTANT')


#aDDING DECORATIVES FOR THE BACKGROUND AND THE
root.configure(bg='blue')

#Define the function for you tube Search

def search_youtube():
    query=entry.get()
    url=f"https://www.youtube.com/results?search_query={query}" 
    webbrowser.open(url)


#Define the Function to search for the Google 
def search_google():
    query=entry.get()
    url=f"https://www.google.com/search?q={query}" 
    webbrowser.open(url)


#Define the Fucntion for the Instagram
def search_instagram():
    Username=entry.get().replace('@',"")

    url=f"www.instagram.com/{Username}/"
    webbrowser.open(url)


#Define the Function for Linked in
def search_linkedin():
    query=entry.get()
    word=query.split()
    hyphenated_name="-".join(word)
    url=f"https://www.linkedin.com/in/{hyphenated_name}/" 
    webbrowser.open(url)



#Create an Input Field for the
Label(root,text="Enter your command").pack(pady=10)
entry=Entry(root,width=50)
entry.pack(pady=10)

Button(root,text="Search on Youtube",command=search_youtube).pack(pady=5)
Button(root,text="Search on Google",command=search_google).pack(pady=5)
Button(root,text="Search on Instagram",command=search_instagram).pack(pady=5)
Button(root,text="Search on Linkedin",command=search_linkedin).pack(pady=5)

#Running the main loop with
root.mainloop()


