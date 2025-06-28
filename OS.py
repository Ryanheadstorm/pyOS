import tkinter as tk
from tkinter import messagebox, filedialog, scrolledtext
import webbrowser
import random

user_db = {}

class CustomOS(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("PyOS")
        self.geometry("800x600")
        self.resizable(False, False)
        self.login_screen()

    def login_screen(self):
        self.clear()
        tk.Label(self, text="PyOS Login", font=("Arial", 24)).pack(pady=20)
        tk.Label(self, text="Username").pack()
        self.username = tk.Entry(self)
        self.username.pack()
        tk.Label(self, text="Password").pack()
        self.password = tk.Entry(self, show="*")
        self.password.pack()
        tk.Button(self, text="Login", command=self.verify_login).pack(pady=5)
        tk.Button(self, text="Create Account", command=self.create_account_screen).pack(pady=5)

    def verify_login(self):
        uname = self.username.get()
        pword = self.password.get()
        if uname in user_db and user_db[uname] == pword:
            self.loading_screen()
        else:
            messagebox.showerror("Login Failed", "Incorrect username or password.")

    def create_account_screen(self):
        self.clear()
        tk.Label(self, text="Create Account", font=("Arial", 24)).pack(pady=20)
        tk.Label(self, text="New Username").pack()
        self.new_username = tk.Entry(self)
        self.new_username.pack()
        tk.Label(self, text="New Password").pack()
        self.new_password = tk.Entry(self, show="*")
        self.new_password.pack()
        tk.Button(self, text="Create", command=self.create_account).pack(pady=5)
        tk.Button(self, text="Back to Login", command=self.login_screen).pack()

    def create_account(self):
        uname = self.new_username.get()
        pword = self.new_password.get()
        if uname in user_db:
            messagebox.showerror("Error", "Username already exists!")
        elif uname == "" or pword == "":
            messagebox.showerror("Error", "Username and password cannot be empty.")
        else:
            user_db[uname] = pword
            messagebox.showinfo("Success", "Account created successfully!")
            self.login_screen()

    def loading_screen(self):
        self.clear()
        tk.Label(self, text="Loading PyOS...", font=("Arial", 20)).pack(pady=250)
        self.after(2000, self.main_menu)

    def main_menu(self):
        self.clear()
        desktop = tk.Frame(self, bg="#3a3a3a")
        desktop.pack(expand=True, fill="both")

        taskbar = tk.Frame(self, bg="#1f1f1f", height=40)
        taskbar.pack(side="bottom", fill="x")

        tk.Label(desktop, text="Welcome to PyOS", font=("Arial", 18), bg="#3a3a3a", fg="white").pack(pady=10)

        # Buttons on the "taskbar"
        apps = [
            ("Web Browser", self.web_browser),
            ("Files App", self.file_explorer),
            ("Play Game", self.play_game),
            ("Logout", self.login_screen)
        ]

        for name, command in apps:
            btn = tk.Button(taskbar, text=name, command=command, bg="#2e2e2e", fg="white")
            btn.pack(side="left", padx=5, pady=5)

    def web_browser(self):
        self.clear()
        tk.Label(self, text="Web Browser", font=("Arial", 16)).pack(pady=5)
        entry = tk.Entry(self, width=50)
        entry.pack()
        tk.Button(self, text="Go", command=lambda: webbrowser.open(entry.get())).pack(pady=5)
        tk.Button(self, text="Back", command=self.main_menu).pack(pady=20)

    def file_explorer(self):
        self.clear()
        tk.Label(self, text="Files App", font=("Arial", 16)).pack(pady=5)
        text_area = scrolledtext.ScrolledText(self, width=70, height=20)
        text_area.pack()

        def open_file():
            filename = filedialog.askopenfilename()
            if filename:
                with open(filename, "r") as f:
                    content = f.read()
                text_area.delete(1.0, tk.END)
                text_area.insert(tk.END, content)

        def save_file():
            filename = filedialog.asksaveasfilename(defaultextension=".txt")
            if filename:
                with open(filename, "w") as f:
                    f.write(text_area.get(1.0, tk.END))

        tk.Button(self, text="Open", command=open_file).pack(pady=2)
        tk.Button(self, text="Save", command=save_file).pack(pady=2)
        tk.Button(self, text="Back", command=self.main_menu).pack(pady=20)

    def play_game(self):
        self.clear()
        tk.Label(self, text="Number Guessing Game", font=("Arial", 16)).pack(pady=5)
        self.target = random.randint(1, 100)
        self.guess_entry = tk.Entry(self)
        self.guess_entry.pack()

        def check_guess():
            try:
                guess = int(self.guess_entry.get())
                if guess < self.target:
                    messagebox.showinfo("Result", "Too low!")
                elif guess > self.target:
                    messagebox.showinfo("Result", "Too high!")
                else:
                    messagebox.showinfo("Result", "Correct!")
                    self.main_menu()
            except:
                messagebox.showerror("Error", "Please enter a number.")

        tk.Button(self, text="Guess", command=check_guess).pack(pady=5)
        tk.Button(self, text="Back", command=self.main_menu).pack(pady=20)

    def clear(self):
        for widget in self.winfo_children():
            widget.destroy()

if __name__ == "__main__":
    app = CustomOS()
    app.mainloop()
