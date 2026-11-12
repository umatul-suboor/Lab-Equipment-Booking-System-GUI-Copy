import tkinter as tk
from tkinter import ttk, messagebox
from src.equipment import EQUIPMENT
from src.booking import create_booking, get_booking_records


BG = "#F3F6FB"
NAVY = "#172B4D"
NAVY_LIGHT = "#243D63"
BLUE = "#3977D5"
TEXT = "#243247"
MUTED = "#718096"
WHITE = "#FFFFFF"
GREEN = "#16865B"


class EquipmentBookingApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Lab Equipment Booking and Management System")
        self.root.geometry("1180x760")
        self.root.minsize(950, 650)
        self.root.configure(bg=BG)

        self.style = ttk.Style()
        self.style.theme_use("clam")
        self.configure_styles()

        self.sidebar = tk.Frame(root, bg=NAVY, width=230)
        self.sidebar.pack(side="left", fill="y")
        self.sidebar.pack_propagate(False)

        self.content = tk.Frame(root, bg=BG)
        self.content.pack(side="right", fill="both", expand=True)

        self.build_sidebar()
        self.show_dashboard()

    def configure_styles(self):
        self.style.configure(
            "Treeview", background=WHITE, foreground=TEXT,
            rowheight=34, fieldbackground=WHITE, font=("Segoe UI", 10)
        )
        self.style.configure(
            "Treeview.Heading", background="#E8EEF7",
            foreground=NAVY, font=("Segoe UI", 10, "bold"), padding=9
        )
        self.style.map("Treeview", background=[("selected", "#DCE9FC")])
        self.style.configure(
            "TCombobox", padding=7, font=("Segoe UI", 10)
        )

    def build_sidebar(self):
        tk.Label(
            self.sidebar, text="LAB EQUIPMENT", bg=NAVY, fg=WHITE,
            font=("Segoe UI", 17, "bold")
        ).pack(anchor="w", padx=22, pady=(30, 2))
        tk.Label(
            self.sidebar, text="BOOKING SYSTEM", bg=NAVY, fg="#B9C9DF",
            font=("Segoe UI", 9, "bold")
        ).pack(anchor="w", padx=23, pady=(0, 35))

        menu_items = [
            ("Dashboard", self.show_dashboard),
            ("Equipment", self.show_equipment),
            ("New Booking", self.show_new_booking),
            ("Booking Records", self.show_records),
        ]

        for label, command in menu_items:
            button = tk.Button(
                self.sidebar, text="  " + label, command=command,
                bg=NAVY, fg=WHITE, activebackground=NAVY_LIGHT,
                activeforeground=WHITE, relief="flat", anchor="w",
                font=("Segoe UI", 11), padx=18, pady=13, cursor="hand2"
            )
            button.pack(fill="x", padx=10, pady=3)

        tk.Frame(self.sidebar, bg="#385171", height=1).pack(
            fill="x", padx=18, pady=(30, 15)
        )
        tk.Label(
            self.sidebar, text="Desktop Application",
            bg=NAVY, fg="#B9C9DF", font=("Segoe UI", 9)
        ).pack(anchor="w", padx=22)
        tk.Label(
            self.sidebar, text="CLI mode: --cli",
            bg=NAVY, fg="#B9C9DF", font=("Segoe UI", 9)
        ).pack(anchor="w", padx=22, pady=5)

    def clear_content(self):
        for widget in self.content.winfo_children():
            widget.destroy()

    def page_heading(self, title, subtitle):
        header = tk.Frame(self.content, bg=BG)
        header.pack(fill="x", padx=32, pady=(27, 20))
        tk.Label(
            header, text=title, bg=BG, fg=NAVY,
            font=("Segoe UI", 22, "bold")
        ).pack(anchor="w")
        tk.Label(
            header, text=subtitle, bg=BG, fg=MUTED,
            font=("Segoe UI", 10)
        ).pack(anchor="w", pady=(5, 0))

    def card(self, parent, title, value, accent):
        panel = tk.Frame(parent, bg=WHITE, highlightthickness=1,
                         highlightbackground="#E5EAF2")
        tk.Label(
            panel, text=title, bg=WHITE, fg=MUTED,
            font=("Segoe UI", 10, "bold")
        ).pack(anchor="w", padx=18, pady=(17, 8))
        tk.Label(
            panel, text=str(value), bg=WHITE, fg=accent,
            font=("Segoe UI", 25, "bold")
        ).pack(anchor="w", padx=18, pady=(0, 16))
        return panel

    def make_table(self, parent, columns, headings, widths=None):
        table_frame = tk.Frame(parent, bg=WHITE)
        table = ttk.Treeview(
            table_frame, columns=columns, show="headings", height=9
        )
        for index, column in enumerate(columns):
            table.heading(column, text=headings[index])
            width = widths[index] if widths else 150
            table.column(column, width=width, anchor="center")
        scrollbar = ttk.Scrollbar(
            table_frame, orient="vertical", command=table.yview
        )
        table.configure(yscrollcommand=scrollbar.set)
        table.pack(side="left", fill="both", expand=True)
        scrollbar.pack(side="right", fill="y")
        return table_frame, table

    def show_dashboard(self):
        self.clear_content()
        self.page_heading(
            "Dashboard", "Overview of laboratory equipment and bookings"
        )

        total_types = len(EQUIPMENT)
        available = sum(item["available"] for item in EQUIPMENT.values())
        records = get_booking_records()
        total_bookings = len(records)
        pending = sum(1 for item in records if item["status"] == "Pending")

        cards = tk.Frame(self.content, bg=BG)
        cards.pack(fill="x", padx=32)
        card_data = [
            ("Equipment Types", total_types, BLUE),
            ("Available Items", available, GREEN),
            ("Total Bookings", total_bookings, "#7955B8"),
            ("Pending Bookings", pending, "#D18A24"),
        ]
        for index, (title, value, color) in enumerate(card_data):
            panel = self.card(cards, title, value, color)
            panel.grid(row=0, column=index, sticky="nsew",
                       padx=(0 if index == 0 else 10, 0), pady=3)
            cards.grid_columnconfigure(index, weight=1)

        section = tk.Frame(self.content, bg=WHITE,
                           highlightthickness=1,
                           highlightbackground="#E5EAF2")
        section.pack(fill="both", expand=True, padx=32, pady=25)
        tk.Label(
            section, text="Equipment Availability", bg=WHITE, fg=NAVY,
            font=("Segoe UI", 13, "bold")
        ).pack(anchor="w", padx=18, pady=17)

        frame, table = self.make_table(
            section, ("id", "name", "available"),
            ("Equipment ID", "Equipment Name", "Available Quantity"),
            (140, 300, 210)
        )
        frame.pack(fill="both", expand=True, padx=18, pady=(0, 18))
        for equipment_id, item in EQUIPMENT.items():
            table.insert(
                "", "end",
                values=(equipment_id, item["name"], item["available"])
            )

    def show_equipment(self):
        self.clear_content()
        self.page_heading(
            "Equipment", "View the equipment available in the laboratory"
        )
        panel = tk.Frame(self.content, bg=WHITE,
                         highlightthickness=1,
                         highlightbackground="#E5EAF2")
        panel.pack(fill="both", expand=True, padx=32, pady=5)
        frame, table = self.make_table(
            panel, ("id", "name", "available"),
            ("Equipment ID", "Equipment Name", "Available Quantity"),
            (160, 360, 220)
        )
        frame.pack(fill="both", expand=True, padx=20, pady=20)
        for equipment_id, item in EQUIPMENT.items():
            table.insert(
                "", "end",
                values=(equipment_id, item["name"], item["available"])
            )

    def show_new_booking(self):
        self.clear_content()
        self.page_heading(
            "New Booking", "Enter booking details and submit your request"
        )

        panel = tk.Frame(self.content, bg=WHITE,
                         highlightthickness=1,
                         highlightbackground="#E5EAF2")
        panel.pack(anchor="nw", padx=32, pady=5, fill="x")

        form = tk.Frame(panel, bg=WHITE)
        form.pack(fill="x", padx=28, pady=25)

        tk.Label(
            form, text="Equipment", bg=WHITE, fg=TEXT,
            font=("Segoe UI", 10, "bold")
        ).grid(row=0, column=0, sticky="w", pady=(0, 7))
        equipment_options = [
            f"{key} - {value['name']}" for key, value in EQUIPMENT.items()
        ]
        equipment_var = tk.StringVar()
        equipment_box = ttk.Combobox(
            form, textvariable=equipment_var, values=equipment_options,
            state="readonly", width=42
        )
        equipment_box.grid(row=1, column=0, sticky="w", pady=(0, 18))
        if equipment_options:
            equipment_box.current(0)

        available_var = tk.StringVar()
        tk.Label(
            form, textvariable=available_var, bg=WHITE, fg=GREEN,
            font=("Segoe UI", 9)
        ).grid(row=2, column=0, sticky="w", pady=(0, 15))

        tk.Label(
            form, text="Quantity", bg=WHITE, fg=TEXT,
            font=("Segoe UI", 10, "bold")
        ).grid(row=3, column=0, sticky="w", pady=(0, 7))
        quantity_entry = tk.Entry(
            form, font=("Segoe UI", 11), width=45,
            relief="solid", bd=1
        )
        quantity_entry.grid(row=4, column=0, sticky="w", pady=(0, 18))

        tk.Label(
            form, text="Booking Date (YYYY-MM-DD)", bg=WHITE, fg=TEXT,
            font=("Segoe UI", 10, "bold")
        ).grid(row=5, column=0, sticky="w", pady=(0, 7))
        date_entry = tk.Entry(
            form, font=("Segoe UI", 11), width=45,
            relief="solid", bd=1
        )
        date_entry.grid(row=6, column=0, sticky="w", pady=(0, 22))

        def update_available(event=None):
            selected = equipment_var.get().split(" - ")[0]
            if selected in EQUIPMENT:
                available_var.set(
                    f"Currently available: {EQUIPMENT[selected]['available']}"
                )

        equipment_box.bind("<<ComboboxSelected>>", update_available)
        update_available()

        def submit_booking():
            selected = equipment_var.get()
            if not selected:
                messagebox.showerror("Booking Error", "Please select equipment.")
                return

            equipment_id = selected.split(" - ")[0]
            try:
                quantity = int(quantity_entry.get().strip())
            except ValueError:
                messagebox.showerror(
                    "Booking Error", "Quantity must be a whole number."
                )
                return

            result = create_booking(
                equipment_id, quantity, date_entry.get().strip()
            )

            if result.startswith("Booking accepted"):
                messagebox.showinfo("Booking Successful", result)
                self.show_new_booking()
            else:
                messagebox.showerror("Booking Rejected", result)

        buttons = tk.Frame(form, bg=WHITE)
        buttons.grid(row=7, column=0, sticky="w")
        tk.Button(
            buttons, text="Submit Booking", command=submit_booking,
            bg=BLUE, fg=WHITE, activebackground="#2D65B7",
            activeforeground=WHITE, relief="flat",
            font=("Segoe UI", 10, "bold"), padx=18, pady=10,
            cursor="hand2"
        ).pack(side="left", padx=(0, 10))
        tk.Button(
            buttons, text="Clear", command=lambda: (
                quantity_entry.delete(0, "end"),
                date_entry.delete(0, "end")
            ),
            bg="#E8EEF7", fg=NAVY, relief="flat",
            font=("Segoe UI", 10, "bold"), padx=18, pady=10,
            cursor="hand2"
        ).pack(side="left")

    def show_records(self):
        self.clear_content()
        self.page_heading(
            "Booking Records", "Review booking requests submitted in this session"
        )
        panel = tk.Frame(self.content, bg=WHITE,
                         highlightthickness=1,
                         highlightbackground="#E5EAF2")
        panel.pack(fill="both", expand=True, padx=32, pady=5)
        frame, table = self.make_table(
            panel,
            ("booking_id", "equipment", "quantity", "date", "status"),
            ("Booking ID", "Equipment", "Quantity", "Booking Date", "Status"),
            (100, 220, 100, 170, 130)
        )
        frame.pack(fill="both", expand=True, padx=20, pady=20)

        records = get_booking_records()
        for record in records:
            table.insert(
                "", "end",
                values=(
                    record["booking_id"], record["equipment"],
                    record["quantity"], record["date"], record["status"]
                )
            )
        if not records:
            tk.Label(
                panel, text="No booking records found yet.",
                bg=WHITE, fg=MUTED, font=("Segoe UI", 10)
            ).pack(pady=(0, 15))


def run_gui():
    root = tk.Tk()
    EquipmentBookingApp(root)
    root.mainloop()
