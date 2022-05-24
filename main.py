import time
from tkinter import *

import settings as st
import utils
from cell import Cell

if __name__ == "__main__":
    root = Tk()
    root.title("Minesweeper")
    root.iconbitmap("images\Minesweeper_Icon2.ico")
    # root.configure(bg="black")
    root.geometry(f"{st.WIDTH}x{st.HEIGHT}")
    root.resizable(False, False)  # width, height

    # Create top frame for cell count, emoji face button and timer
    top_frame = Frame(root, width=st.WIDTH, height=utils.height_prct(25))
    top_frame.place(x=0, y=0)

    # Create main frame for the minesweeper game with buttons as cells
    main_frame = Frame(root, width=st.WIDTH, height=utils.height_prct(75))
    main_frame.place(x=utils.width_prct(15), y=utils.height_prct(25))

    # Create grid of cells objects
    for x in range(st.GRID_SIZE):
        for y in range(st.GRID_SIZE):
            c = Cell(x, y)
            c.create_btn_object(main_frame)
            c.cell_btn_object.grid(column=x, row=y)

    # Create cell count label
    Cell.create_cell_count_label(top_frame)
    Cell.cell_count_label_object.place(x=utils.width_prct(5), y=utils.height_prct(5))

    # Create emoji face button
    Cell.create_face_btn_object(top_frame)
    Cell.face_btn_object.place(x=utils.width_prct(40), y=utils.height_prct(5))

    # Create game time label
    Cell.create_time_label(top_frame)
    Cell.game_time_label_object.place(x=utils.width_prct(67), y=utils.height_prct(5))

    # Init start time and start counting
    Cell.start_time = time.time()
    Cell.count_elapsed_time()

    # Randomly choose mines and asign them to cell objects
    Cell.randomize_mines()

    # Show all generated mines - for debug only -
    # Cell.show_all_mines()

    # Run the window
    root.mainloop()
