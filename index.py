# main framework of the application

from tkinter import *
from tkinter import messagebox

root = Tk()
# root.geometry("500x700")

width = root.winfo_screenwidth()
height = root.winfo_screenheight()
root.geometry("%dx%d" % (width, height))
root.title('Employee Management System')
root.config(bg="#bebeb6")


# ==================== Login Page ===========================

def clear_frames(frame_name):
    for frame in frame_name.winfo_children():
        frame.destroy()


def first_page():

    def home_page():
        home_frame = Frame(main_frame)
        lb = Label(home_frame, text='Home Page\n\nPage: 1', font=('Bold', 30))
        lb.pack()

        home_frame.pack(pady=20)

    def menu_page():
        menu_frame = Frame(main_frame)
        lb = Label(menu_frame, text='Menu Page\n\nPage: 2', font=('Bold', 30))
        lb.pack()

        menu_frame.pack(pady=20)

    def contact_page():
        contact_frame = Frame(main_frame)
        lb = Label(contact_frame, text='Contact Page\n\nPage: 3',
                   font=('Bold', 30))
        lb.pack()

        contact_frame.pack(pady=20)

    def about_page():
        about_frame = Frame(main_frame)
        lb = Label(about_frame, text='about Page\n\nPage: 4',
                   font=('Bold', 30))
        lb.pack()

        about_frame.pack(pady=20)

    def hide_indicate():
        home_indicate.config(bg="#c3c3c3")
        menu_indicate.config(bg="#c3c3c3")
        contact_indicate.config(bg="#c3c3c3")
        about_indicate.config(bg="#c3c3c3")

    def delete_pages():
        for frame in main_frame.winfo_children():
            frame.destroy()

    def indicate(lb, page):
        hide_indicate()
        lb.config(bg="#158aff")
        delete_pages()
        page()
    # creating options frame on left

    options_frame = Frame(root, bg="#c3c3c3")

    home_btn = Button(options_frame, text="HOME", font=('Bold', 15), fg="#158aff",
                      bd=0, bg="#c3c3c3", command=lambda: indicate(home_indicate, home_page))
    home_btn.place(x=10, y=50)

    home_indicate = Label(options_frame, text="", bg="#c3c3c3")
    home_indicate.place(x=3, y=50, width=5, height=35)

    menu_btn = Button(options_frame, text="MENU", font=('Bold', 15), fg="#158aff",
                      bd=0, bg="#c3c3c3", command=lambda: indicate(menu_indicate, menu_page))
    menu_btn.place(x=10, y=100)

    menu_indicate = Label(options_frame, text="", bg="#c3c3c3")
    menu_indicate.place(x=3, y=100, width=5, height=35)

    contact_btn = Button(options_frame, text="CONTACT", font=('Bold', 15), fg="#158aff",
                         bd=0, bg="#c3c3c3", command=lambda: indicate(contact_indicate, contact_page))
    contact_btn.place(x=10, y=150)

    contact_indicate = Label(options_frame, text="", bg="#c3c3c3")
    contact_indicate.place(x=3, y=150, width=5, height=35)

    about_btn = Button(options_frame, text="ABOUT", font=('Bold', 15), fg="#158aff",
                       bd=0, bg="#c3c3c3", command=lambda: indicate(about_indicate, about_page))
    about_btn.place(x=10, y=200)

    about_indicate = Label(options_frame, text="", bg="#c3c3c3")
    about_indicate.place(x=3, y=200, width=5, height=35)

    options_frame.pack(side=LEFT)
    options_frame.pack_propagate(False)
    options_frame.configure(width=150, height=400)

    # showing work frame
    main_frame = Frame(root, highlightbackground='black', highlightthickness=2)
    main_frame.pack(side=LEFT)
    main_frame.pack_propagate(False)
    main_frame.configure(height=400, width=500)


def login():
    userid = entry1.get()
    password = entry2.get()

    if (userid == "" or password == ""):
        messagebox.showinfo("", "Blank Fields not Allowed")
    elif (userid == "user" and password == "user"):   # setting test id and password
        clear_frames(root)
        first_page()
    elif (userid == "admin" and password == "admin"):
        clear_frames(root)
        first_page()
    else:
        messagebox.showinfo("", "Incorrect User Details")


login_frame = Frame(root, highlightthickness=2)

login_frame.place(relx=.5, rely=.5, anchor=CENTER)
login_frame.configure(height=300, width=400)

global entry1
global entry2

Label(login_frame, text="User Id", font=("BOLD", 18)).place(x=20, y=40)
Label(login_frame, text="Password", font=("BOLD", 18)).place(x=20, y=90)

entry1 = Entry(login_frame, bd=5, font=(18), borderwidth=5, relief=FLAT)
entry1.place(x=150, y=40)

entry2 = Entry(login_frame, bd=5, show="*",
               font=(18), borderwidth=5, relief=FLAT)
entry2.place(x=150, y=90)

Button(login_frame, text="Login", command=login, height=2, font=("BOLD", 18),
       width=15, bd=4).place(x=90, y=150)


# ===================== first page ===========================


# options side bar


# options_frame.pack(side=LEFT)
# options_frame.pack_propagate(False)
# options_frame.configure(width=150, height=400)


# main frame

# main_frame = Frame(root, highlightbackground='black', highlightthickness=2)

# main_frame.pack(side=LEFT)
# main_frame.pack_propagate(False)
# main_frame.configure(height=400, width=500)

root.mainloop()

root.mainloop()
