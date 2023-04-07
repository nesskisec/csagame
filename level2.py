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
        self.current_room = None
        self.create_rooms()
        self.current_room = self.rooms[0]

        self.app = app

        self.lbl_room = ctk.CTkLabel(self.app, text=self.current_room.name)
        self.lbl_room.pack()

        self.lbl_desc = ctk.CTkLabel(self.app, text=self.current_room.description)
        self.lbl_desc.pack()

        self.lbl_items = ctk.CTkLabel(self.app, text="You see the following items:")
        self.lbl_items.pack()

        self.lbl_inventory = ctk.CTkLabel(self.app, text="")
        self.lbl_inventory.pack()

        self.lbl_help = ctk.CTkLabel(self.app, text="Enter 'help' for a list of commands.")
        self.lbl_help.pack()

        self.lbl_input = ctk.CTkLabel(self.app, text="What do you want to do?")
        self.lbl_input.pack()

        self.entry = ctk.CTkEntry(self.app)
        self.entry.pack()
        self.entry.focus_set()

        self.btn_submit = ctk.CTkButton(self.app, text="Submit", command=self.get_user_input)
        self.btn_submit.pack()

        self.app.bind("<Return>", lambda event: self.get_user_input())

        self.print_inventory()

    def create_rooms(self):
        self.rooms = [
            Room("Lobby", "You are in the lobby. There is a receptionist desk here.", [], {"north": 1, "east": 2}),
            Room("Server Room", "You are in a room full of servers. It is very noisy in here.", ["USB drive"],
                 {"south": 0}),
            Room("Conference Room", "You are in a conference room. There is a projector and a whiteboard here.", [],
                 {"west": 0, "north": 3}),
            Room("CEO's Office", "You are in the CEO's office. There is a large desk and a bookshelf here.", ["key"],
                 {"south": 2, "east": 4}),
            Room("IT Department", "You are in the IT department. There are computers and monitors everywhere.", [],
                 {"west": 3})
        ]

    def print_room(self):
        self.lbl_room.configure(text=self.current_room.name)
        self.lbl_desc.configure(text=self.current_room.description)
        self.print_items()

    def print_items(self):
        items_str = ", ".join(self.current_room.items)
        if items_str:
            self.lbl_items.configure(text="You see the following items: " + items_str)
        else:
            self.lbl_items.configure(text="There are no items in this room.")

    def print_inventory(self):
        if len(self.inventory) > 0:
            inventory_str = ", ".join(self.inventory)
            self.lbl_inventory.configure(text="Inventory: " + inventory_str)
        else:
            self.lbl_inventory.configure(text="You don't have any items in your inventory.")

    def get_user_input(self):
        user_input = self.entry.get()
        self.entry.delete(0, tk.END)
        self.process_input(user_input)

    def process_input(self, user_input):
        if user_input == "help":
            message = "Possible commands:\n\n" \
                      "north, east, south, west\n" \
                      "take [item name]\n" \
                      "use [item name]\n" \
                      "inventory"
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
                self.lbl_input.configure(text="That item is not in this room.")
        elif user_input.startswith("use "):
            item_name = user_input[4:]
            if item_name in self.inventory:
                if self.current_room.name == "CEO's Office" and item_name == "key":
                    self.lbl_input.configure(text="Congratulations! You have found the secret document and won the game!")
                    self.btn_submit.configure(state=tk.DISABLED)
                else:
                    self.lbl_input.configure(text="You cannot use that item here.")
            else:
                self.lbl_input.configure(text="That item is not in your inventory.")
        elif user_input == "inventory":
            self.print_inventory()
        else:
            self.lbl_input.configure(text="Invalid command. Please try again.")
