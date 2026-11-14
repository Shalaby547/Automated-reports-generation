
import customtkinter as ctk
from tkinter import messagebox


class MainWindow(ctk.CTkFrame):

    def __init__(self, master):
        super().__init__(master)

        self.grid_columnconfigure((0, 1), weight=1)

        # Header
        self.title_label = ctk.CTkLabel(
            self,
            text="Student Reports Generator",
            font=("Arial", 28, "bold")
        )
        self.title_label.pack(pady=(30, 5))

        self.subtitle_label = ctk.CTkLabel(
            self,
            text="Configure your report settings",
            font=("Arial", 14)
        )
        self.subtitle_label.pack(pady=(0, 25))

        # Group Selection
        self.group_label = ctk.CTkLabel(
            self,
            text="Select Group"
        )
        self.group_label.pack(anchor="w", padx=100)

        self.group_frame = ctk.CTkFrame(self)
        self.group_frame.pack(fill="x", padx=100, pady=(5, 15))

        self.group_menu = ctk.CTkOptionMenu(
            self.group_frame,
            values=["Select Group"]
        )
        self.group_menu.pack(
            side="left",
            fill="x",
            expand=True,
            padx=10,
            pady=10
        )

        self.add_group_button = ctk.CTkButton(
            self.group_frame,
            text="+ Add Group",
            command=self.add_group
        )
        self.add_group_button.pack(
            side="right",
            padx=10,
            pady=10
        )

        # Month Selection
        self.month_label = ctk.CTkLabel(
            self,
            text="Select Month"
        )
        self.month_label.pack(anchor="w", padx=100)

        self.month_menu = ctk.CTkOptionMenu(
            self,
            values=[
                "January", "February", "March",
                "April", "May", "June",
                "July", "August", "September",
                "October", "November", "December"
            ]
        )
        self.month_menu.pack(fill="x", padx=100, pady=(5, 15))

        # Quizzes and Monthly Exam
        self.options_frame = ctk.CTkFrame(self)
        self.options_frame.pack(fill="x", padx=100, pady=5)

        self.options_frame.grid_columnconfigure(
            (0, 1), weight=1
        )

        self.quizzes_label = ctk.CTkLabel(
            self.options_frame,
            text="Number of Quizzes"
        )
        self.quizzes_label.grid(
            row=0, column=0, padx=10, pady=5
        )

        self.quizzes_menu = ctk.CTkOptionMenu(
            self.options_frame,
            values=["1", "2", "3", "4"]
        )
        self.quizzes_menu.grid(
            row=1, column=0, padx=10, pady=5, sticky="ew"
        )

        self.exam_label = ctk.CTkLabel(
            self.options_frame,
            text="Monthly Exam"
        )
        self.exam_label.grid(
            row=0, column=1, padx=10, pady=5
        )

        self.exam_menu = ctk.CTkOptionMenu(
            self.options_frame,
            values=["Yes", "No"]
        )
        self.exam_menu.grid(
            row=1, column=1, padx=10, pady=5, sticky="ew"
        )

        # Sessions
        self.sessions_label = ctk.CTkLabel(
            self,
            text="Number of Sessions"
        )
        self.sessions_label.pack(pady=(15, 5))

        self.sessions_menu = ctk.CTkSegmentedButton(
            self,
            values=["4", "8"]
        )
        self.sessions_menu.pack(pady=5)

        # Action Buttons
        self.generate_button = ctk.CTkButton(
            self,
            text="Generate Reports",
            height=40,
            command=self.generate_reports
        )
        self.generate_button.pack(fill="x", padx=100, pady=(25, 8))

        self.pdf_button = ctk.CTkButton(
            self,
            text="Convert to PDF",
            height=40,
            fg_color="gray",
            command=self.convert_to_pdf
        )
        self.pdf_button.pack(fill="x", padx=100, pady=5)

    def add_group(self):
        messagebox.showinfo(
            "Add Group",
            "We will connect this button to AddGroupDialog."
        )

    def generate_reports(self):
        messagebox.showinfo(
            "Generate Reports",
            "We will connect this button to the report generator."
        )

    def convert_to_pdf(self):
        messagebox.showinfo(
            "Convert to PDF",
            "We will connect this button to the PDF converter."
        )
