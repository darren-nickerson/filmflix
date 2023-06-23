from tkinter import *
from tkinter import ttk
from tkinter import messagebox
from controller import Controller
from initialize_database import initialize_database
from sql_handling import SQLHandling


class FilmFlixApp:
    def __init__(self):
        initialize_database()
        self.root = Tk()
        self.root.title("FilmFlix Database")
        self.create_menu()
        self.f_controller = Controller()
        self.connector = SQLHandling("filmflix.db")
        self.create_ui()
        self.add_records()

    def create_ui(self):
        self.set_window_centered()  # Center the window on the screen
        self.root.configure(padx=20, pady=20)

        # Add some style
        self.style = ttk.Style()
        self.style.theme_use("default")

        # Create the Treeview
        self.create_tree_view()
        self.create_buttons()

        # Create input boxes for record entry
        self.create_input_boxes()

    def focus_input(self):
        self.entry.focus_set()

    def create_menu(self):
        self.menubar = Menu(self.root)
        self.root.config(menu=self.menubar)

        self.file = Menu(self.menubar)

        self.menubar.add_cascade(label="File", menu=self.file)
        self.file.add_command(label="Exit Program", command=self.exit)

        self.reports = Menu(self.menubar)
        self.menubar.add_cascade(label="Reports", menu=self.reports)
        self.reports.add_command(
            label="Display all Films", command=self.all_film_report
        )
        self.reports.add_command(label="Search by Title", command=self.title_report)
        self.reports.add_command(label="Search by ID", command=self.id_report)
        self.reports.add_command(label="Search by Genre", command=self.genre_report)
        self.reports.add_command(
            label="Search by Wildcard", command=self.wildcard_report
        )

    def title_report(self):
        self.clear_input_boxes()
        self.lookup_title()

    def id_report(self):
        self.clear_input_boxes()
        self.lookup_id()

    def genre_report(self):
        self.clear_input_boxes()
        self.lookup_genre()

    def wildcard_report(self):
        self.clear_input_boxes()
        self.lookup_wildcard()

    def all_film_report(self):
        self.my_tree.delete(*self.my_tree.get_children())
        self.add_records()

    def exit(self):
        self.root.destroy()

    def search_genre(self):
        self.genre = self.genre_search_entry.get()
        self.genre_search.destroy()
        # Clear the existing items in the treeview
        self.my_tree.delete(*self.my_tree.get_children())
        records = self.f_controller.select_all_films_by_genre(self.genre)
        for count, record in enumerate(records):
            try:
                if count % 2 == 0:
                    self.my_tree.insert(
                        parent="",
                        index="end",
                        iid=count,
                        text="",
                        values=(
                            record[0],
                            record[2],
                            record[3],
                            record[4],
                            record[5],
                            record[6],
                        ),
                        tags=("evenrow",),
                    )
                else:
                    self.my_tree.insert(
                        parent="",
                        index="end",
                        iid=count,
                        text="",
                        values=(
                            record[0],
                            record[2],
                            record[3],
                            record[4],
                            record[5],
                            record[6],
                        ),
                        tags=("oddrow",),
                    )
            except IndexError:
                # Handle the IndexError as per your requirements
                print(f"Error: Invalid record at index {count}")

    def lookup_genre(self):
        self.genre_search = Toplevel(self.root)
        self.genre_search.title("Lookup Records")
        self.genre_search.resizable(False, False)

        # Calculate the position of the search window relative to the main window
        main_window_width = self.root.winfo_width()
        main_window_height = self.root.winfo_height()
        search_window_width = 300  # Adjust the width as needed
        search_window_height = 200  # Adjust the height as needed
        x = (
            self.root.winfo_rootx()
            + (main_window_width // 2)
            - (search_window_width // 2)
        )
        y = (
            self.root.winfo_rooty()
            + (main_window_height // 2)
            - (search_window_height // 2)
        )

        # Set the search window's geometry and position it relative to the main window
        self.genre_search.geometry(
            f"{search_window_width}x{search_window_height}+{x}+{y}"
        )

        # Label
        self.genre_search_frame = LabelFrame(self.genre_search, text="Search by Genre")
        self.genre_search_frame.pack(padx=10, pady=10)

        # Entry box
        self.genre_search_entry = Entry(self.genre_search_frame)
        self.genre_search_entry.pack(pady=20, padx=20)

        # Button
        self.genre_button = Button(
            self.genre_search, text="Search Records", command=self.search_genre
        )
        self.genre_button.pack(padx=20, pady=20)
        self.genre_search_entry.focus_set()

    def search_title(self):
        self.title = self.title_search_entry.get()
        self.title_search.destroy()
        # Clear the existing items in the treeview
        self.my_tree.delete(*self.my_tree.get_children())
        records = self.f_controller.select_film_by_title(self.title)

        for count, record in enumerate(records):
            try:
                if count % 2 == 0:
                    self.my_tree.insert(
                        parent="",
                        index="end",
                        iid=count,
                        text="",
                        values=(
                            record[0],
                            record[2],
                            record[3],
                            record[4],
                            record[5],
                            record[6],
                        ),
                        tags=("evenrow",),
                    )
                else:
                    self.my_tree.insert(
                        parent="",
                        index="end",
                        iid=count,
                        text="",
                        values=(
                            record[0],
                            record[2],
                            record[3],
                            record[4],
                            record[5],
                            record[6],
                        ),
                        tags=("oddrow",),
                    )
            except IndexError:
                # Handle the IndexError as per your requirements
                print(f"Error: Invalid record at index {count}")

    def lookup_title(self):
        self.title_search = Toplevel(self.root)
        self.title_search.title("Lookup Records")
        self.title_search.resizable(False, False)

        # Calculate the position of the search window relative to the main window
        main_window_width = self.root.winfo_width()
        main_window_height = self.root.winfo_height()
        search_window_width = 300  # Adjust the width as needed
        search_window_height = 200  # Adjust the height as needed
        x = (
            self.root.winfo_rootx()
            + (main_window_width // 2)
            - (search_window_width // 2)
        )
        y = (
            self.root.winfo_rooty()
            + (main_window_height // 2)
            - (search_window_height // 2)
        )

        # Set the search window's geometry and position it relative to the main window
        self.title_search.geometry(
            f"{search_window_width}x{search_window_height}+{x}+{y}"
        )

        # Label
        self.title_search_frame = LabelFrame(self.title_search, text="Search by Title")
        self.title_search_frame.pack(padx=10, pady=10)

        # Entry box
        self.title_search_entry = Entry(self.title_search_frame)
        self.title_search_entry.pack(pady=20, padx=20)

        # Button
        self.title_button = Button(
            self.title_search, text="Search Records", command=self.search_title
        )
        self.title_button.pack(padx=20, pady=20)
        self.title_search_entry.focus_set()

    def search_wildcard(self):
        self.wildcard = self.wildcard_search_entry.get()
        self.wildcard_search.destroy()
        # Clear the existing items in the treeview
        self.my_tree.delete(*self.my_tree.get_children())
        records = self.f_controller.select_all_films_by_wildcard(self.wildcard)

        for count, record in enumerate(records):
            try:
                if count % 2 == 0:
                    self.my_tree.insert(
                        parent="",
                        index="end",
                        iid=count,
                        text="",
                        values=(
                            record[0],
                            record[2],
                            record[3],
                            record[4],
                            record[5],
                            record[6],
                        ),
                        tags=("evenrow",),
                    )
                else:
                    self.my_tree.insert(
                        parent="",
                        index="end",
                        iid=count,
                        text="",
                        values=(
                            record[0],
                            record[2],
                            record[3],
                            record[4],
                            record[5],
                            record[6],
                        ),
                        tags=("oddrow",),
                    )
            except IndexError:
                # Handle the IndexError as per your requirements
                print(f"Error: Invalid record at index {count}")

    def lookup_wildcard(self):
        self.wildcard_search = Toplevel(self.root)
        self.wildcard_search.title("Lookup Records")
        self.wildcard_search.resizable(False, False)

        # Calculate the position of the search window relative to the main window
        main_window_width = self.root.winfo_width()
        main_window_height = self.root.winfo_height()
        search_window_width = 300  # Adjust the width as needed
        search_window_height = 200  # Adjust the height as needed
        x = (
            self.root.winfo_rootx()
            + (main_window_width // 2)
            - (search_window_width // 2)
        )
        y = (
            self.root.winfo_rooty()
            + (main_window_height // 2)
            - (search_window_height // 2)
        )

        # Set the search window's geometry and position it relative to the main window
        self.wildcard_search.geometry(
            f"{search_window_width}x{search_window_height}+{x}+{y}"
        )

        # Label
        self.wildcard_search_frame = LabelFrame(
            self.wildcard_search, text="Search by Wildcard"
        )
        self.wildcard_search_frame.pack(padx=10, pady=10)

        # Entry box
        self.wildcard_search_entry = Entry(self.wildcard_search_frame)
        self.wildcard_search_entry.pack(pady=20, padx=20)

        # Button
        self.wildcard_button = Button(
            self.wildcard_search, text="Search Records", command=self.search_wildcard
        )
        self.wildcard_button.pack(padx=20, pady=20)
        self.wildcard_search_entry.focus_set()

    from tkinter import messagebox

    def search_id(self):
        self.id = self.id_search_entry.get()
        self.id_search.destroy()
        # Clear the existing items in the treeview
        self.my_tree.delete(*self.my_tree.get_children())
        record = self.f_controller.select_film_by_id(self.id)

        if record:
            self.my_tree.insert(
                parent="",
                index="end",
                iid=0,
                text="",
                values=(
                    record[0],
                    record[2],
                    record[3],
                    record[4],
                    record[5],
                    record[6],
                ),
                tags=("evenrow",) if 0 % 2 == 0 else ("oddrow",),
            )
        else:
            messagebox.showerror(
                "Invalid Record", "No record found with the provided ID."
            )

    def lookup_id(self):
        self.id_search = Toplevel(self.root)
        self.id_search.title("Lookup Records")
        self.id_search.resizable(False, False)

        # Calculate the position of the search window relative to the main window
        main_window_width = self.root.winfo_width()
        main_window_height = self.root.winfo_height()
        search_window_width = 300  # Adjust the width as needed
        search_window_height = 200  # Adjust the height as needed
        x = (
            self.root.winfo_rootx()
            + (main_window_width // 2)
            - (search_window_width // 2)
        )
        y = (
            self.root.winfo_rooty()
            + (main_window_height // 2)
            - (search_window_height // 2)
        )

        # Set the search window's geometry and position it relative to the main window
        self.id_search.geometry(f"{search_window_width}x{search_window_height}+{x}+{y}")

        # Label
        self.id_search_frame = LabelFrame(self.id_search, text="Search by ID")
        self.id_search_frame.pack(padx=10, pady=10)

        # Entry box
        self.id_search_entry = Entry(self.id_search_frame)
        self.id_search_entry.pack(pady=20, padx=20)

        # Button
        self.id_button = Button(
            self.id_search, text="Search Records", command=self.search_id
        )
        self.id_button.pack(padx=20, pady=20)
        self.id_search_entry.focus_set()

    def create_tree_view(self):
        self.style.configure(
            "Treeview",
            background="D3D3D3",
            foreground="black",
            rowheight=25,
            fieldbackground="#D3D3D3",
        )
        self.style.map("Treeview", background=[("selected", "#347083")])

        # Create a Treeview frame
        self.tree_frame = Frame(self.root)
        self.tree_frame.pack(pady=10, fill=X, expand=True)

        # Create a Treeview scrollbar
        self.tree_scroll = Scrollbar(self.tree_frame)
        self.tree_scroll.pack(side=RIGHT, fill=Y)

        # Create the Treeview
        self.my_tree = ttk.Treeview(
            self.tree_frame, yscrollcommand=self.tree_scroll.set, selectmode="extended"
        )

        # Configure the Scrollbar
        self.tree_scroll.config(command=self.my_tree.yview)

        # Define Treeview columns
        self.my_tree["columns"] = (
            "Film ID",
            "Title",
            "Year Released",
            "Rating",
            "Duration",
            "Genre",
        )

        # Format our columns
        self.my_tree.column("#0", width=0, stretch=NO)
        self.my_tree.column("Film ID", anchor=CENTER, width=100)
        self.my_tree.column("Title", anchor=W, width=180)
        self.my_tree.column("Year Released", anchor=CENTER, width=140)
        self.my_tree.column("Rating", anchor=CENTER, width=100)
        self.my_tree.column("Duration", anchor=CENTER, width=100)
        self.my_tree.column("Genre", anchor=CENTER, width=140)

        # Pack the Treeview
        self.my_tree.pack(fill=BOTH, expand=True)

        # Create headings
        self.my_tree.heading("#0", text="", anchor="w")
        self.my_tree.heading("Film ID", text="Film ID", anchor="center")
        self.my_tree.heading("Title", text="Title", anchor="w")
        self.my_tree.heading("Year Released", text="Year Released", anchor="center")
        self.my_tree.heading("Rating", text="Rating", anchor="center")
        self.my_tree.heading("Duration", text="Duration", anchor="center")
        self.my_tree.heading("Genre", text="Genre", anchor="center")
        # Create striped row tags
        self.my_tree.tag_configure("oddrow", background="white")
        self.my_tree.tag_configure("evenrow", background="lightblue")

        # Bind the treeview
        self.my_tree.bind("<ButtonRelease-1>", self.select_record)

    def add_records(self):
        records = self.f_controller.select_all_films()
        for count, record in enumerate(records):
            try:
                if count % 2 == 0:
                    self.my_tree.insert(
                        parent="",
                        index="end",
                        iid=count,
                        text="",
                        values=(
                            record[0],
                            record[2],
                            record[3],
                            record[4],
                            record[5],
                            record[6],
                        ),
                        tags=("evenrow",),
                    )
                else:
                    self.my_tree.insert(
                        parent="",
                        index="end",
                        iid=count,
                        text="",
                        values=(
                            record[0],
                            record[2],
                            record[3],
                            record[4],
                            record[5],
                            record[6],
                        ),
                        tags=("oddrow",),
                    )
            except IndexError:
                # Handle the IndexError as per your requirements
                print(f"Error: Invalid record at index {count}")

    def check_selection(self):
        selected_item = self.my_tree.selection()
        if selected_item:
            self.add_button.config(state="disabled")
        else:
            self.add_button.config(state="normal")

    def refresh_treeview(self):
        # Clear the existing items in the treeview
        self.my_tree.delete(*self.my_tree.get_children())

    def create_input_boxes(self):
        self.data_frame = LabelFrame(self.root, text="Record")
        self.data_frame.pack(fill="x", expand="yes")

        # Film ID
        self.film_id_label = Label(self.data_frame, text="Film ID")
        self.film_id_label.grid(row=0, column=0, padx=10, pady=10)
        self.film_id_entry = ttk.Entry(self.data_frame, style="CustomEntry.TEntry")
        self.film_id_entry.grid(row=0, column=1, padx=10, pady=10)
        self.film_id_entry.configure(state="disable")

        # Title
        self.title_label = Label(self.data_frame, text="Title")
        self.title_label.grid(row=0, column=2, padx=10, pady=10)
        self.title_entry = Entry(self.data_frame)
        self.title_entry.grid(row=0, column=3, padx=10, pady=10)

        # Year Released
        self.yr_label = Label(self.data_frame, text="Year Released")
        self.yr_label.grid(row=0, column=4, padx=10, pady=10)
        self.yr_entry = Entry(self.data_frame)
        self.yr_entry.grid(row=0, column=5, padx=10, pady=10)

        # Rating
        self.rating_label = Label(self.data_frame, text="Rating")
        self.rating_label.grid(row=1, column=0, padx=10, pady=10)
        self.rating_entry = Entry(self.data_frame)
        self.rating_entry.grid(row=1, column=1, padx=10, pady=10)

        # Duration
        self.duration_label = Label(self.data_frame, text="Duration")
        self.duration_label.grid(row=1, column=2, padx=10, pady=10)
        self.duration_entry = Entry(self.data_frame)
        self.duration_entry.grid(row=1, column=3, padx=10, pady=10)

        # Genre
        self.genre_label = Label(self.data_frame, text="Genre")
        self.genre_label.grid(row=1, column=4, padx=10, pady=10)
        self.genre_entry = Entry(self.data_frame)
        self.genre_entry.grid(row=1, column=5, padx=10, pady=10)

        style = ttk.Style()
        style.configure("CustomEntry.TEntry", font=("Arial", 12), foreground="blue")

    def create_buttons(self):
        self.buttons_frame = LabelFrame(self.root, text="Commands")
        self.buttons_frame.pack(fill=BOTH, expand="yes")

        # Buttons
        self.clear_button = ttk.Button(
            self.buttons_frame,
            text="Clear Input",
            style="Clear.TButton",
            command=self.clear_input_boxes,
            width=15,  # Increase button width
        )
        self.clear_button.grid(row=0, column=3, padx=5)

        self.delete_button = ttk.Button(
            self.buttons_frame,
            text="Delete Record",
            style="Delete.TButton",
            command=lambda: self.delete_record(),
            width=15,  # Increase button width
        )
        self.delete_button.grid(row=0, column=1, padx=5)

        self.update_button = ttk.Button(
            self.buttons_frame,
            text="Update Record",
            style="Update.TButton",
            width=15,  # Increase button width
            command=lambda: self.update(),
        )
        self.update_button.grid(row=0, column=2, padx=5)

        self.add_button = ttk.Button(
            self.buttons_frame,
            text="Add Record",
            style="Add.TButton",
            command=lambda: self.insert(),
            width=15,  # Increase button width
        )
        self.add_button.grid(row=0, column=0, padx=5)

        # Center the buttons within the frame
        self.buttons_frame.grid_columnconfigure(0, weight=1)
        self.buttons_frame.grid_columnconfigure(1, weight=1)
        self.buttons_frame.grid_columnconfigure(2, weight=1)
        self.buttons_frame.grid_columnconfigure(3, weight=1)
        self.buttons_frame.grid_rowconfigure(0, weight=1)

        # Center buttons within the frame
        self.buttons_frame.pack_configure(anchor="center")

        # Configure custom styles
        self.root.style = ttk.Style()

        # Custom style for the delete button
        self.root.style.configure(
            "Delete.TButton",
            background="#f44336",  # Set a subtle red background color
            foreground="white",  # Set white text color
            font=("Helvetica", 12),  # Set a custom font
            width=12,  # Set a custom width
            pady=8,  # Set custom padding
        )

        # Custom style for the update button
        self.root.style.configure(
            "Update.TButton",
            background="#2196f3",  # Set a subtle blue background color
            foreground="white",  # Set white text color
            font=("Helvetica", 12),  # Set a custom font
            width=12,  # Set a custom width
            pady=8,  # Set custom padding
        )

        # Custom style for the clear button
        self.root.style.configure(
            "Clear.TButton",
            background="#ffeb3b",  # Set a subtle yellow background color
            foreground="black",  # Set black text color
            font=("Helvetica", 12),  # Set a custom font
            width=12,  # Set a custom width
            pady=8,  # Set custom padding
        )
        # Custom style for the add button
        self.root.style.configure(
            "Add.TButton",
            background="#4caf50",  # Set a subtle green background color
            foreground="white",  # Set white text color
            font=("Helvetica", 12),  # Set a custom font
            width=12,  # Set a custom width
            pady=8,  # Set custom padding
        )

        # Configure hover effect for all buttons
        self.root.style.map(
            "Delete.TButton",
            background=[
                ("active", "#e53935")
            ],  # Set a darker red hover background color
            foreground=[("active", "white")],  # Set white hover text color
        )

        self.root.style.map(
            "Update.TButton",
            background=[
                ("active", "#1976d2")
            ],  # Set a darker blue hover background color
            foreground=[("active", "white")],  # Set white hover text color
        )

        self.root.style.map(
            "Clear.TButton",
            background=[
                ("active", "#fdd835")
            ],  # Set a darker yellow hover background color
            foreground=[("active", "black")],  # Set black hover text color
        )

        self.root.style.map(
            "Add.TButton",
            background=[
                ("active", "#43a047")
            ],  # Set a darker green hover background color
            foreground=[("active", "white")],  # Set white hover text color
        )

    def set_window_centered(self):
        window_width = 950
        window_height = 600
        self.root.resizable(False, False)
        screen_width = self.root.winfo_screenwidth()
        screen_height = self.root.winfo_screenheight()
        x = (screen_width // 2) - (window_width // 2)
        y = (screen_height // 2) - (window_height // 2)
        self.root.geometry(f"{window_width}x{window_height}+{x}+{y}")

    def clear_input_boxes(self):
        # Clear the values of the input boxes
        self.film_id_entry.configure(state="normal")
        self.film_id_entry.delete(0, "end")
        self.title_entry.delete(0, "end")
        self.yr_entry.delete(0, "end")
        self.rating_entry.delete(0, "end")
        self.duration_entry.delete(0, "end")
        self.genre_entry.delete(0, "end")
        self.deselect_tree_view()
        self.film_id_entry.configure(state="disable")

    def delete_record(self):
        film_id = self.film_id_entry.get()
        if film_id:
            self.f_controller.delete_record(film_id)

            if film_id:
                messagebox.showinfo(
                    title="Success", message="Record Deleted", parent=self.root
                )
                self.film_id_entry.configure(state="normal")
                self.refresh_treeview()
                self.add_records()
                self.clear_input_boxes()
                self.film_id_entry.configure(state="disable")
                self.check_selection()
            else:
                messagebox.showinfo(
                    title="Error", message="Failed to delete record", parent=self.root
                )
        else:
            messagebox.showwarning(
                title="Error", message="Please enter a film ID", parent=self.root
            )

    def insert(self):
        result = self.f_controller.insert_film(
            self.title_entry.get(),
            self.yr_entry.get(),
            self.rating_entry.get(),
            self.duration_entry.get(),
            self.genre_entry.get(),
        )
        if isinstance(result, list):
            error_message = "\n".join(result)  # Concatenate errors with newlines
            messagebox.showwarning(
                title="error", message=error_message, parent=self.root
            )
        else:
            messagebox.showinfo(
                title="Record Submitted", message=result, parent=self.root
            )
            self.clear_input_boxes()
            self.refresh_treeview()
            self.add_records()

    def update(self):
        selected_record = self.my_tree.selection()

        if not selected_record:
            # Display error message for no record selected
            messagebox.showwarning(
                title="Error",
                message="No record selected for update.",
                parent=self.root,
            )
            return

        film_id = self.film_id_entry.get()
        title = self.title_entry.get()
        year_released = self.yr_entry.get()
        rating = self.rating_entry.get()
        duration = self.duration_entry.get()
        genre = self.genre_entry.get()

        result = self.f_controller.update_record(
            film_id,
            title,
            year_released,
            rating,
            duration,
            genre,
        )

        if isinstance(result, list):
            # Display error message
            error_message = "\n".join(result)
            messagebox.showerror(
                title="Error",
                message="An error occurred:\n" + error_message,
                parent=self.root,
            )

        else:
            # Display success message
            messagebox.showinfo(
                title="Success",
                message="" + result,
                parent=self.root,
            )
            self.refresh_treeview()
            self.add_records()
            self.clear_input_boxes()
            self.check_selection()

    def deselect_tree_view(self):
        selected_item = self.my_tree.selection()
        if selected_item:
            self.my_tree.selection_remove(selected_item)
            self.check_selection()

    def select_record(self, e):
        # Clear the values of the input boxes
        self.check_selection()
        self.film_id_entry.configure(state="normal")
        self.film_id_entry.delete(0, "end")
        self.title_entry.delete(0, "end")
        self.yr_entry.delete(0, "end")
        self.rating_entry.delete(0, "end")
        self.duration_entry.delete(0, "end")
        self.genre_entry.delete(0, "end")
        self.film_id_entry.configure(state="disable")

        # Grab record number
        selected = self.my_tree.focus()

        # Grab record values if available
        values = self.my_tree.item(selected, "values")
        if values:
            self.film_id_entry.configure(state="normal")
            # Insert values into input boxes
            self.film_id_entry.insert(0, values[0])
            self.title_entry.insert(0, values[1])
            self.yr_entry.insert(0, values[2])
            self.rating_entry.insert(0, values[3])
            self.duration_entry.insert(0, values[4])
            self.genre_entry.insert(0, values[5])
            self.film_id_entry.configure(state="disable")

    def run(self):
        self.root.mainloop()

    def __del__(self):
        self.connector.close_connection()


if __name__ == "__main__":
    app = FilmFlixApp()
    app.run()
