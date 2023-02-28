# main framework of the application

from tkinter import *
from tkinter import messagebox

import psycopg2

# ==================== Login Page ===========================


class System:

    def __init__(self, root) -> None:
        self.root = root
        width = root.winfo_screenwidth()
        height = root.winfo_screenheight()
        self.root.geometry("%dx%d" % (width, height))
        self.root.title('Employee Management System')
        self.root.config(bg="#bebeb6")

        self.login_menu()

        # self.conn = psycopg2.connect(
        #     host="localhost",
        #     database="employee",
        #     user="postgres",
        #     password="password")

    @staticmethod
    def clear_frames(frame_name):
        for frame in frame_name.winfo_children():
            frame.destroy()

    # login menu

    def login_menu(self):
        def login():
            userid = entry1.get()
            password = entry2.get()

            if (userid == "" or password == ""):
                messagebox.showinfo("", "Blank Fields not Allowed")
            elif (userid == "user" and password == "user"):   # setting test id and password
                self.clear_frames(self.root)
                home_frame = Frame(self.root, highlightthickness=2)
                home_frame.place(relx=.5, rely=.5, anchor=CENTER)
                home_frame.configure(height=700, width=900)
                user = User("user", "pass", 123, home_frame)
            elif (userid == "admin" and password == "admin"):
                self.clear_frames(self.root)
                home_frame = Frame(self.root, highlightthickness=2)
                home_frame.place(relx=.5, rely=.5, anchor=CENTER)
                home_frame.configure(height=700, width=900)
                admin = Admin("admin", "pass", 123, home_frame)
            else:
                messagebox.showinfo("", "Incorrect User Details")

        login_frame = Frame(self.root, highlightthickness=2)

        login_frame.place(relx=.5, rely=.5, anchor=CENTER)
        login_frame.configure(height=300, width=400)

        global entry1
        global entry2

        Label(login_frame, text="User Id", font=("BOLD", 18)).place(x=20, y=40)
        Label(login_frame, text="Password",
              font=("BOLD", 18)).place(x=20, y=90)

        entry1 = Entry(login_frame, bd=5, font=(18),
                       borderwidth=5, relief=FLAT)
        entry1.place(x=150, y=40)

        entry2 = Entry(login_frame, bd=5, show="*",
                       font=(18), borderwidth=5, relief=FLAT)
        entry2.place(x=150, y=90)

        Button(login_frame, text="Login", command=login, height=2, font=("BOLD", 18),
               width=15, bd=4).place(x=90, y=150)

    def home_page(self):

        pass


class User:
    def __init__(self, first, last, num, root):
        self.first = first
        self.last = last
        self.num = num
        self.root = root
        self.home_page()

    def home_page(self):

        # creating options frame on left
        self.options_frame = Frame(self.root, bg="#c3c3c3")

        # log out btn
        self.logOut_btn = Button(self.options_frame, text="Log Out", font=('Bold', 15), fg="#158aff",
                                 bd=0, bg="#c3c3c3", command=lambda: self.indicate(self.logOut_indicate, self.logOut_page))
        self.logOut_btn.place(x=10, y=50)

        self.logOut_indicate = Label(self.options_frame, text="", bg="#c3c3c3")
        self.logOut_indicate.place(x=3, y=50, width=5, height=35)

        # profile btn
        self.profile_btn = Button(self.options_frame, text="Profile", font=('Bold', 15), fg="#158aff",
                                  bd=0, bg="#c3c3c3", command=lambda: self.indicate(self.profile_indicate, self.profile_page))
        self.profile_btn.place(x=10, y=100)

        self.profile_indicate = Label(
            self.options_frame, text="", bg="#c3c3c3")
        self.profile_indicate.place(x=3, y=100, width=5, height=35)

        # messages btn
        self.messages_btn = Button(self.options_frame, text="Messages", font=('Bold', 15), fg="#158aff",
                                   bd=0, bg="#c3c3c3", command=lambda: self.indicate(self.messages_indicate, self.messages_page))
        self.messages_btn.place(x=10, y=150)

        self.messages_indicate = Label(
            self.options_frame, text="", bg="#c3c3c3")
        self.messages_indicate.place(x=3, y=150, width=5, height=35)

        # tasks btn
        self.tasks_btn = Button(self.options_frame, text="Tasks Page", font=('Bold', 15), fg="#158aff",
                                bd=0, bg="#c3c3c3", command=lambda: self.indicate(self.tasks_indicate, self.tasks_page))
        self.tasks_btn.place(x=10, y=200)

        self.tasks_indicate = Label(self.options_frame, text="", bg="#c3c3c3")
        self.tasks_indicate.place(x=3, y=200, width=5, height=35)

        self.options_frame.pack(side=LEFT)
        self.options_frame.pack_propagate(False)
        self.options_frame.configure(width=250, height=700)

        # showing work frame
        self.main_frame = Frame(self.root, highlightbackground='black',
                                highlightthickness=2)

        self.main_frame.pack(side=LEFT)
        self.main_frame.pack_propagate(False)
        self.main_frame.configure(height=700, width=650)

    def logOut_page(self):
        logOut_frame = Frame(self.main_frame)
        lb = Label(logOut_frame, text='Home Page\n\nPage: 1',
                   font=('Bold', 30))
        lb.pack()
        # myscrollbar = Scrollbar(logOut_frame, orient="vertical")
        # myscrollbar.pack(side="right", fill="y")

        logOut_frame.pack(pady=20)

    def profile_page(self):
        profile_frame = Frame(self.main_frame)
        lb = Label(profile_frame, text='Menu Page\n\nPage: 2',
                   font=('Bold', 30))
        # myscrollbar = Scrollbar(profile_frame, orient="vertical")
        # myscrollbar.pack(side="right", fill="y")
        lb.pack()

        profile_frame.pack(pady=20)

    def messages_page(self):
        messages_frame = Frame(self.main_frame)
        lb = Label(messages_frame, text='Contact Page\n\nPage: 3',
                   font=('Bold', 30))
        lb.pack()

        messages_frame.pack(pady=20)

    def tasks_page(self):
        tasks_frame = Frame(self.main_frame)
        lb = Label(tasks_frame, text='about Page\n\nPage: 4',
                   font=('Bold', 30))
        lb.pack()

        tasks_frame.pack(pady=20)

    def hide_indicate(self):
        self.logOut_indicate.config(bg="#c3c3c3")
        self.profile_indicate.config(bg="#c3c3c3")
        self.messages_indicate.config(bg="#c3c3c3")
        self.tasks_indicate.config(bg="#c3c3c3")

    @staticmethod
    def delete_pages(frame_name):
        for frame in frame_name.winfo_children():
            frame.destroy()

    def indicate(self, lb, page):
        self.hide_indicate()
        lb.config(bg="#158aff")
        User.delete_pages(self.main_frame)
        page()

    # creating home frame for options and main menu


class Admin(User):
    def __init__(self, root) -> None:
        super().__init__(root)


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
if __name__ == "__main__":
    root = Tk()
    obj = System(root)
    root.mainloop()
