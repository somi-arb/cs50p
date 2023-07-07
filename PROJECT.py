import tkinter as tk
import customtkinter
from PIL import ImageTk, Image
import random

customtkinter.set_appearance_mode("system")
customtkinter.set_default_color_theme("green")

app = customtkinter.CTk()
app.geometry("600x440")
app.title('Login')

list_of_ideas = [
    "Go camping in the wilderness",
    "Have a picnic at the park",
    "Learn to surf",
    "Visit a new city",
    "Go hiking in the mountains",
    "Take a road trip with friends",
    "Attend a music festival",
    "Explore a national park",
    "Volunteer for a local charity",
    "Try a new water sport",
    "Go stargazing",
    "Have a barbecue party",
    "Learn to cook a new dish",
    "Visit an amusement park",
    "Take a scenic bike ride",
    "Learn to play a musical instrument",
    "Try rock climbing",
    "Take a yoga class",
    "Have a beach bonfire",
    "Go on a hot air balloon ride",
    "Visit a vineyard and go wine tasting",
    "Take a helicopter tour",
    "Try stand-up paddleboarding",
    "Attend an outdoor concert",
    "Go on a wildlife safari",
    "Explore a local farmer's market",
    "Take a photography workshop",
    "Go snorkeling or scuba diving",
    "Attend a sports game",
    "Learn to dance a new style",
    "Take a pottery or art class",
    "Visit a botanical garden",
    "Try zip-lining",
    "Go horseback riding",
    "Have a movie marathon night",
    "Learn to make homemade ice cream",
    "Take a river rafting adventure",
    "Attend a cooking or mixology class",
    "Visit a museum or art gallery",
    "Go on a kayaking trip",
    "Take a day trip to an island",
    "Have a DIY project day",
    "Try indoor skydiving",
    "Go on a ghost tour",
    "Learn a new language",
    "Have a picnic by the lake",
    "Try paddleboard yoga",
    "Go on a wine and cheese tasting tour",
    "Visit a famous landmark in your country",
    "Try indoor rock climbing",
    "Take a scenic train ride",
    "Go on a zip line canopy tour",
    "Explore a local street food market",
    "Have a water balloon fight",
    "Learn to juggle",
    "Try a new hairstyle or haircut",
    "Take a pottery painting class",
    "Have a picnic in a botanical garden",
    "Learn to make sushi",
    "Go on a sunset cruise",
    "Have a karaoke night",
    "Try a new workout or fitness class",
    "Take a bike tour of the city",
    "Visit a local historical site",
    "Go on a food tasting tour",
    "Attend a comedy show",
    "Learn to meditate or practice mindfulness",
    "Try a new fashion trend",
    "Have a themed costume party",
    "Take a scenic helicopter tour",
    "Go on a wine and painting class",
    "Volunteer at an animal shelter",
    "Try a new type of cuisine",
    "Visit a waterfall and go for a swim",
    "Take a pottery wheel class",
    "Go on a sunrise hike",
    "Have a game night with friends",
    "Try indoor trampoline jumping",
    "Learn to make homemade pizza",
    "Take a salsa or tango dance class",
    "Go on a photography scavenger hunt",
    "Visit a local food festival",
    "Try paddleboard fishing",
    "Have a DIY spa day at home",
    "Take a cooking class with a renowned chef",
    "Go on a sailing adventure",
    "Attend a cultural festival",
    "Try a new water activity like jet skiing or wakeboarding",
    "Take a scenic helicopter tour",
    "Have a picnic in a lavender field",
    "Learn to do a handstand or cartwheel",
    "Try a new type of art, such as glassblowing or pottery throwing",
    "Take a day trip to a nearby island or beach town",
    "Have a themed movie marathon at home",
    "Try a new outdoor fitness activity, such as parkour or aerial yoga",
    "Visit a local farm and pick your own fruits or vegetables",
    "Go on a hot air balloon ride at sunrise or sunset",
    "Take a cooking class focused on a specific cuisine or dish",
    "Explore a local nature reserve or wildlife sanctuary",
    "Have a relaxing day at a spa or wellness retreat"
]

def on_button_click():
    random.shuffle(list_of_ideas)
    idea = list_of_ideas[0]
    idea_label.configure(text=idea)

def button_function():
    app.destroy()
    w = customtkinter.CTk()
    w.geometry("920x480")
    w.title('Welcome')
    image = Image.open("final_project.py/pattern.png")
    img1 = ImageTk.PhotoImage(image)
    l1 = customtkinter.CTkLabel(master=w, image=img1)
    l1.pack()
    l1 = customtkinter.CTkLabel(master=w, text="NEW IDEAS FOR THE DAY", font=('Century Gothic', 60))
    l1.place(relx=0.5, rely=0.3, anchor=tk.CENTER)
    l2 = customtkinter.CTkButton(master=w, text="Explore", font=('Century Gothic', 50), command=on_button_click)
    l2.place(relx=0.4, rely=0.45)
    global idea_label
    idea_label = customtkinter.CTkLabel(master=w, text="", font=('Century Gothic', 60))
    idea_label.place(relx=0.5, rely=0.7, anchor=tk.CENTER)
    w.mainloop()

image = Image.open("final_project.py/pattern.png")
img1 = ImageTk.PhotoImage(image)

l1 = customtkinter.CTkLabel(master=app, image=img1)
l1.pack()

frame = customtkinter.CTkFrame(master=l1, width=320, height=360, corner_radius=15)
frame.place(relx=0.5, rely=0.5, anchor=tk.CENTER)

l2 = customtkinter.CTkLabel(master=frame, text="Log into your Account", font=('Century Gothic', 20))
l2.place(x=50, y=45)

entry1 = customtkinter.CTkEntry(master=frame, width=220, placeholder_text='Username')
entry1.place(x=50, y=110)

entry2 = customtkinter.CTkEntry(master=frame, width=220, placeholder_text='Password', show="*")
entry2.place(x=50, y=165)

l3 = customtkinter.CTkLabel(master=frame, text="Forget password?", font=('Century Gothic', 12))
l3.place(x=155, y=195)

button1 = customtkinter.CTkButton(master=frame, width=220, text="Login", command=button_function, corner_radius=6)
button1.place(x=50, y=240)

app.mainloop()