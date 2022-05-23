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

    top_frame = Frame(
        root,
        # bg="red",  # change later to black
        width=st.WIDTH,
        height=utils.height_prct(25),
    )
    top_frame.place(x=0, y=0)

    game_tittle = Button(
        top_frame,
        text=":)",
        width=2,
        height=1,
        font=("", 17),
    )
    game_tittle.place(x=utils.width_prct(40), y=utils.height_prct(5))

    center_frame = Frame(
        root,
        bg="black",  # change later to black
        width=st.WIDTH,
        height=utils.height_prct(75),
    )
    center_frame.place(x=utils.width_prct(15), y=utils.height_prct(25))

    # Create grid of cells objects
    for x in range(st.GRID_SIZE):
        for y in range(st.GRID_SIZE):
            c = Cell(x, y)
            c.create_btn_object(center_frame)
            c.cell_btn_object.grid(column=x, row=y)

    # Create cell count label
    Cell.create_cell_count_label(top_frame)
    Cell.cell_count_label_object.place(x=utils.width_prct(5), y=utils.height_prct(5))

    # Create game time label
    Cell.create_time_label(top_frame)
    Cell.game_time_label_object.place(x=utils.width_prct(67), y=utils.height_prct(5))

    # Init start time and start counting
    Cell.start_time = time.time()
    Cell.count_elapsed_time()

    Cell.randomize_mines()

    # for debug only
    # Cell.show_all_mines()
    
    # Run the window
    root.mainloop()
