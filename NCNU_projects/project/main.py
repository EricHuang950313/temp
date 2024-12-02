# import tkinter as tk
import ttkbootstrap as ttk
from ttkbootstrap.constants import *
from branch.migong import Solver
from branch.control import Control

class MazeApp(Solver, Control):
    def __init__(self, root):
        self.root = root
        self.jsonFileLocation = "./branch/maps.json"
        self.setup_ui()
        self.mapp = 1

    def setup_ui(self):
        self.root.title("Migongs")
        self.root.geometry("600x600")
        self.root.resizable(False, False)
        self.root.grid_columnconfigure(0, weight=1)

        # Create a Notebook
        notebook = ttk.Notebook(self.root)
        notebook.grid(row=0, column=0, sticky="nsew", padx=10, pady=10)
        self.create_tabs(notebook)
    
    def create_tabs(self, notebook):
        # Create frames for using tabs
        tabA = ttk.Frame(notebook)
        tabB = ttk.Frame(notebook)
        tabA.grid_columnconfigure(0, weight=1)
        tabB.grid_columnconfigure(0, weight=1)

        notebook.add(tabA, text="Solve Maze")
        notebook.add(tabB, text="Try Maze")

        self.setup_solve_tab(tabA)
        self.setup_try_tab(tabB)

    def setup_solve_tab(self, tabA):
        # label
        tabA_label = ttk.Label(tabA, text="Solve", font=("Times", 36))
        tabA_label.grid(row=0, column=0, padx=10, pady=10)

        # Create an outline menu button for theme selection
        theme_button = ttk.Menubutton(tabA, text="Select a theme", bootstyle="info-outline")
        theme_button.grid(row=0, column=1, padx=10, pady=10)
        # Create a menu for the theme button
        self.theme_menu = ttk.Menu(theme_button)
        # Populate the menu with available themes
        for theme in self.root.style.theme_names():
            self.theme_menu.add_command(label=theme, command=lambda t=theme: self.change_theme(t))
        # Attach the menu to the menu button
        theme_button["menu"] = self.theme_menu

        # Introduction (Part 1)
        text_solve = '''
        The program will solve the migongs using the Depth-First Search
        (DFS) algorithm.

        Three predefined migongs configurations are available: 
        Map1, Map2, and Map3.
        
        The user can select which migong the program should solve.
        '''

        tabA_widgetA = ttk.Labelframe(tabA, text="Introduction")
        tabA_widgetA.grid(row=2, column=0, columnspan=2, padx=10, pady=10, sticky="nsew")
        tabA_widgetA_text = ttk.Label(tabA_widgetA, text=text_solve)
        tabA_widgetA_text.grid(row=2, column=0, columnspan=2, padx=10, pady=10, sticky="nsew")

        # Run (Part 2)
        # Styled Widgets section
        tabA_widgetB = ttk.Labelframe(tabA, text="Run The Program")
        tabA_widgetB.grid(row=3, column=0, columnspan=2, padx=10, pady=10, sticky="nsew")

        # solve
        self.solve_button = ttk.Button(tabA_widgetB, text="Solve Maze", command=self.solve_maze)
        self.solve_button.grid(row=1, column=0, padx=20, pady=20)

        # map choosing
        # create a Menubutton
        self.map_button = ttk.Menubutton(tabA_widgetB, text="Map 1")
        self.map_button.grid(row=1, column=1, padx=20, pady=20)

        # Create a menu for the Menubutton
        self.map_menu = ttk.Menu(self.map_button, tearoff=0)

        # Add options to the menu
        for i in range(1, 4):
            self.map_menu.add_command(label=f"Map {i}", command=lambda i=i: self.set_map(i))
        
        self.map_button["menu"] = self.map_menu
        
    
    def setup_try_tab(self, tabB):
        # label
        tabB_label = ttk.Label(tabB, text="Try", font=("Times", 36))
        tabB_label.grid(row=0, column=0, padx=10, pady=10)

        # Create an outline menu button for theme selection
        theme_button = ttk.Menubutton(tabB, text="Select a theme", bootstyle="info-outline")
        theme_button.grid(row=0, column=1, padx=10, pady=10)
        # Create a menu for the theme button
        self.theme_menu = ttk.Menu(theme_button)
        # Populate the menu with available themes
        for theme in self.root.style.theme_names():
            self.theme_menu.add_command(label=theme, command=lambda t=theme: self.change_theme(t))
        # Attach the menu to the menu button
        theme_button["menu"] = self.theme_menu

        # Introduction (Part 1)
        text_try = '''
        Provide an opportunity for the user to attempt solving the migongs.

        Three predefined migongs configurations are available:
        Map1, Map2, and Map3.

        The migong to be solved will be selected randomly.
        '''

        tabB_widgetA = ttk.Labelframe(tabB, text="Introduction")
        tabB_widgetA.grid(row=2, column=0, columnspan=2, padx=10, pady=10, sticky="nsew")
        tabB_widgetA_text = ttk.Label(tabB_widgetA, text=text_try)
        tabB_widgetA_text.grid(row=2, column=0, columnspan=2, padx=10, pady=10, sticky="nsew")

        # Run (Part 2)
        # Styled Widgets section
        tabB_widgetB = ttk.Labelframe(tabB, text="Run The Program")
        tabB_widgetB.grid(row=3, column=0, columnspan=2, padx=10, pady=10, sticky="nsew")

        # try
        self.try_button = ttk.Button(tabB_widgetB, text="Try Maze", command=self.try_maze)
        self.try_button.grid(row=1, column=0, padx=20, pady=20)   
    

    # Define a function to change the theme
    def change_theme(self, selected_theme):
        self.root.style.theme_use(selected_theme)

    def set_map(self, map_number):
        self.mapp = map_number
        self.map_button.config(text=f"Map {map_number}")

    def solve_maze(self):
        # ./branch/migong.py
        solver = Solver(i_start=1, j_start=1, i_end=8, j_end=8, readFile=self.jsonFileLocation, mapp=self.mapp)
        solver.start()

    def try_maze(self):
        # ./branch/control.py
        trier = Control(readFile=self.jsonFileLocation)
        trier.start()


# Run the mazeApp application
if __name__ == "__main__":
    root = ttk.Window(themename="morph")
    app = MazeApp(root)
    root.mainloop()
