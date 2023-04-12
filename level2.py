import customtkinter as ctk
import tkinter as tk


class Room:
    def __init__(self, name, description, items, exits):
        self.name = name
        self.description = description
        self.items = items
        self.exits = exits

    def __str__(self):
        return self.name


class Level2:

    def __init__(self, app):
        self.inventory = []
        self.progress = 0
        self.create_rooms()
        self.current_room = self.rooms[0]

        self.app = app

        self.lbl_room = ctk.CTkLabel(self.app, text=self.current_room.name+"\n\n", font=('font.ttf', 50))
        self.lbl_room.place(relx=0.5, rely=0.1, anchor='n')

        self.lbl_desc = ctk.CTkLabel(self.app, text=self.current_room.description+"\n", font=('font.ttf', 20))
        self.lbl_desc.place(relx=0.5, rely=0.2, anchor='n')

        self.lbl_items = ctk.CTkLabel(self.app, text="You see the following items:")
        self.lbl_items.place(relx=0.5, rely=0.3, anchor='n')

        self.lbl_inventory = ctk.CTkLabel(self.app, text="")
        self.lbl_inventory.place(relx=0.5, rely=0.4, anchor=tk.CENTER)

        self.lbl_help = ctk.CTkLabel(self.app, text="\n\nEnter 'help' for a list of commands.")
        self.lbl_help.place(relx=0.5, rely=0.5, anchor=tk.CENTER)

        self.lbl_input = ctk.CTkLabel(self.app, text="\n\nWhat do you want to do?\n")
        self.lbl_input.place(relx=0.5, rely=0.6, anchor=tk.CENTER)

        self.entry = ctk.CTkEntry(self.app, width=220, height=50, placeholder_text="Enter your command here.")
        self.entry.place(relx=0.5, rely=0.7, anchor=tk.CENTER)

        self.btn_submit = ctk.CTkButton(self.app, width=220, height=50, text="Submit", command=self.get_user_input)
        self.btn_submit.place(relx=0.5, rely=0.77, anchor=tk.CENTER)

        self.entry.bind('<Return>', lambda event: self.get_user_input())

        self.print_inventory()

    def create_rooms(self):
        self.rooms = [
            Room("Lobby", "You are in the lobby. There is a receptionist desk here.\n\n", [], {"north": 1, "east": 2, "west": 3}),

            Room("Reception Area", "You are in the reception area. There is a waiting area and a phone here.\n\n",
                 ["phone"], {"south": 0, "west": 4, "east": 6, "north": 5}),

            Room("Storage Room", "You are in a small storage room. There are boxes and files everywhere.\n\n",
                 ["flash drive"], {"east": 0}),

            Room("Mailroom", "You are in the mailroom. There are letters and packages here.\n\n", [], {"west": 0}),

            Room("Finance Department", "You are in the finance department. There are calculators and spreadsheets here.\n\n", [],
                 {"east": 1, "south": 7, "west": 13, "north": 5}),

            Room("Marketing Department", "You are in the marketing department. There are posters and banners here.\n\n", [],
                 {"south": 1, "east": 8, "west": 4, "north": 9}),

            Room("Legal Department", "You are in the legal department. There are law books and contracts here.\n\n", [],
                 {"west": 1, "south": 10, "east": 16, "north": 9}),

            Room("IT Department", "You are in the IT department. There are computers and monitors everywhere.\n\n", [],
                 {"east": 12, "north": 4, "west": 13, "south": 17}),

            Room("Cafeteria", "You are in the cafeteria. There is a buffet and tables here.\n\n", [], {"west": 5, "north": 9}),

            Room("Break Room", "You are in the break room. There is a fridge and a coffee machine here.\n\n",
                 ["coffee"],
                 {"south": 8, "west": 5, "east": 6}),

            Room("HR Office", "You are in the HR office. There are files and papers all over the place.\n\n",
                 ["ID card"],
                 {"north": 6, "east": 11}),

            Room("Training Room", "You are in the training room. There are tables and chairs here.\n\n", ["USB drive"],
                 {"west": 10}),

            Room("Server Room", "You are in a room full of servers. It is very noisy in here.\n\n", [], {"west": 7, "south": 17}),

            Room("Boardroom", "You are in the boardroom. There is a long table and chairs here.\n\n", [],
                 {"east": 4, "north": 14, "south": 7}),

            Room("CEO's Office", "You are in the CEO's office. There is a large desk and a bookshelf here.\n\n",
                 [],
                 {"south": 13, "west": 15}),

            Room("Executive Bathroom", "You are in the executive bathroom. There is a sink and a toilet here.\n\n", ["key"],
                 {"east": 14}),

            Room("Conference Room", "You are in a conference room. There is a projector and a whiteboard here.\n\n", [],
                 {"east": 6}),

            Room("Security Room", "You are in the security room. There are cameras and monitors here.\n\n", [],
                 {"north": 12, "west": 7})
        ]

    def print_room(self):
        self.lbl_room.configure(text=self.current_room.name)
        self.lbl_desc.configure(text=self.current_room.description)
        self.print_items()

    def print_items(self):
        items_str = ", ".join(self.current_room.items)
        if items_str:
            self.lbl_items.configure(text="You see the following items: " + items_str + "\n\n")
        else:
            self.lbl_items.configure(text="There are no items in this room.\n\n")

    def print_inventory(self):
        if len(self.inventory) > 0:
            inventory_str = ", ".join(self.inventory)
            self.lbl_inventory.configure(text="\n\nInventory: " + inventory_str + "\n\n")
        else:
            self.lbl_inventory.configure(text="\nYou don't have any items in your inventory.\n\n")

    def get_user_input(self):
        user_input = self.entry.get()
        self.entry.delete(0, tk.END)
        self.process_input(user_input)

    def process_input(self, user_input):
        if user_input == "help":
            message = "\nPossible commands:\n\n" \
                      "north, east, south, west\n" \
                      "take [item name]\n" \
                      "use [item name]\n" \
                      "inventory\n\n"
            self.lbl_help.configure(text=message)
        elif user_input in self.current_room.exits:
            next_room = self.rooms[self.current_room.exits[user_input]]
            self.current_room = next_room
            self.progress += 1
            self.print_room()
        elif user_input.startswith("take "):
            item_name = user_input[5:]
            if item_name in self.current_room.items:
                self.current_room.items.remove(item_name)
                self.inventory.append(item_name)
                self.print_items()
                self.print_inventory()
            else:
                self.lbl_input.configure(text="\n\nThat item is not in this room.\n\n")
        elif user_input.startswith("use "):
            item_name = user_input[4:]
            if item_name in self.inventory:
                if self.current_room.name == "CEO's Office" and item_name == "key":
                    self.lbl_input.configure(text="You have found a cable hidden.")
                    self.btn_submit.configure(state=tk.DISABLED)
                elif self.current_room.name == "Server Room" and item_name == "USB drive":
                    self.lbl_input.configure(text="You used the USB Drive and have infected the computers with Ransomware.\nGame Over!", text_color="red")
                    self.btn_submit.configure(state=tk.DISABLED)
                else:
                    self.lbl_input.configure(text="\n\nYou cannot use that item here.\n\n")
            else:
                self.lbl_input.configure(text="\n\nThat item is not in your inventory.\n\n")
        elif user_input == "inventory":
            self.print_inventory()
        else:
            self.lbl_input.configure(text="\n\nInvalid command. Please try again.\n\n")
