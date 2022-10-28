import os
import tkinter as tk
from tkinter import ttk, filedialog, messagebox

text_content = dict()


def create_file(content="", title="Untitled"):
    container = ttk.Frame(notebook)
    container.pack()
    text_area = tk.Text(container)
    text_area.insert("end", content)
    text_area.pack(side="left", fill="both", expand=True)
    notebook.add(container, text=title)
    notebook.select(container)

    text_content[str(text_area)] = hash(content)

    scroll_bar = ttk.Scrollbar(container, orient="vertical", command=text_area.yview)
    scroll_bar.pack(side="right", fill="y")
    text_area["yscrollcommand"] = scroll_bar.set


def get_text_widget():
    tab_widget = root.nametowidget(notebook.select())
    text_widget = tab_widget.winfo_children()[0]
    return text_widget


def close_current_tab():
    current = get_text_widget()
    if current_tab_unsaved() and not confirm_close():
        return

    notebook.forget(current)


def current_tab_unsaved():
    text_widget = get_text_widget()
    content = text_widget.get("1.0", "end-1c")
    return hash(content) != text_content[str(text_widget)]


def confirm_close():
    return messagebox.askyesno(
        message="you have unsaved changes, do you want to close?",
        icon="question",
        title="confirm close."
    )


def confirm_quit():
    unsaved = False
    for tab in notebook.tabs():
        tab_widget = root.nametowidget(tab)
        text_widget = tab_widget.winfo_children()[0]
        content = text_widget.get("1.0", "end-1c")

        if hash(content) != text_content[str(text_widget)]:
            unsaved = True
            break

    if unsaved and not confirm_close():
        return

    root.destroy()


def checking_for_changes():
    current = get_text_widget()
    content = current.get("1.0", "end-1c")
    name = notebook.tab("current")["text"]

    if hash(content) != text_content[str(current)]:
        if name[-1] != "*":
            notebook.tab("current", text=name + "*")
    elif name[-1] == "*":
        notebook.tab("current", text=name[:-1])


def save_file():
    file_path = filedialog.asksaveasfilename()

    try:
        filename = os.path.basename(file_path)
        text_widget = get_text_widget()
        content = text_widget.get("1.0", "end-1c")
        with open(file_path, "w") as file:
            file.write(content)

    except (AttributeError, FileNotFoundError):
        print("Save operation cancelled")
        return

    notebook.tab("current", text=filename)
    text_content[str(text_widget)] = hash(content)


def open_file():
    file_path = filedialog.askopenfilename()

    try:
        filename = os.path.basename(file_path)
        with open(file_path, "r") as file:
            content = file.read()

    except (AttributeError, FileNotFoundError):
        print("Opening file cancelled.")
        return

    create_file(content, filename)


def show_about_info():
    messagebox.showinfo(
        title="About",
        message="Hello this my first application coded with Python.\n"
                "Hope you find it usefully with your works. assuming it works xD.\n"
                "Credits goes to Teclado Udemy GUI Development course, doing such amazing"
                "work with this application.\n\n"
                "To contact and support: "
                "amzakaria94@gmail.com"
    )


root = tk.Tk()
root.title("ZEditor.")
root.option_add("*tearOff", False)

main = ttk.Frame(root)
main.pack(padx=1, pady=(4, 0), fill="both", expand=True)

menuBar = tk.Menu()
root.config(menu=menuBar)

file_menu = tk.Menu(menuBar)
help_menu = tk.Menu(menuBar)

menuBar.add_cascade(menu=file_menu, label="File")
menuBar.add_cascade(menu=help_menu, label="Help")

file_menu.add_command(label="New File", command=create_file, accelerator="Ctrl+N")
file_menu.add_command(label="Open File", command=open_file, accelerator="Ctrl+O")
file_menu.add_command(label="Save File", command=save_file, accelerator="Ctrl+S")
file_menu.add_command(label="Close Current tab", command=open_file, accelerator="Ctrl+R")
file_menu.add_command(label="Exit", command=confirm_quit, accelerator="Ctrl+Q")

help_menu.add_command(label="About", command=show_about_info)

notebook = ttk.Notebook(main)
notebook.pack(fill="both", expand=True)
create_file()

root.bind("<KeyPress>", lambda event: checking_for_changes())
root.bind("<Control-n>", lambda event: create_file())
root.bind("<Control-o>", lambda event: open_file())
root.bind("<Control-s>", lambda event: save_file())
root.bind("<Control-r>", lambda event: close_current_tab())
root.bind("<Control-q>", lambda event: confirm_quit())

root.mainloop()

# Here we could end our program safly
