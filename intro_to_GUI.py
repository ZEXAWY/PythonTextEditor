import tkinter as tk
from tkinter import ttk

# def greet():
#     print(f"Hello, {user_name.get() or 'why wont you add your name?'}!")


root = tk.Tk()
root.title("MyApp")
# first_Button = ttk.Button(root, text="first", command=greet)
# first_Button.pack(side="left", fill="x", expand=True)
# root_Quit = ttk.Button(root, text="Quit", command=root.destroy)
# root_Quit.pack(side="right", fill="x", expand=True)
"""
Defining a Label:
"""
# user_name = tk.StringVar()
# name_label = ttk.Label(root, text="Name: ")
# name_label.pack(side="left", padx=(0, 10))
# name_entry = ttk.Entry(root, width=10, textvariable=user_name)
# name_entry.pack(side="left")
# name_entry.focus()
#
# greet_button = ttk.Button(root, text="press me", command=greet)
# greet_button.pack(side="left", fill="x", expand=True)
"""
Label positions:
"""
# tk.Label(root, text="Label 1", bg="green").pack(side="top", fill="both", expand=True)
# tk.Label(root, text="Label 2", bg="red").pack(side="top", fill="both", expand=True)
# tk.Label(root, text="Label left", bg="grey").pack(
#     side="left", fill="both", expand=True
# )
"""
Playing a little with frames:
"""
main = ttk.Frame(root)  # Defining a variable that will contain the frame
main.pack(side="left", fill="both", expand=True)  # Packing the frame Location.

tk.Label(main, text="Label 1", bg="green").pack(side="top", fill="both", expand=True)
tk.Label(main, text="Label 2", bg="red").pack(side="top", fill="both", expand=True)
tk.Label(root, text="Label left", bg="grey").pack(
    side="left", fill="both", expand=True)


root.mainloop()
