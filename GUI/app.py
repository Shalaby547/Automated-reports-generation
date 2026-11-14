import customtkinter as ctk
from main_window import MainWindow


class App(ctk.CTk):

    def __init__(self):
        super().__init__()

        self.title("Student Reports Generator")
        self.geometry("1000x650")

        self.main_window = MainWindow(self)
        self.main_window.pack(fill="both", expand=True)