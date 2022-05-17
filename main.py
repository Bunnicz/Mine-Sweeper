from tkinter import *
from cell import Cell

import settings as st
import utils

if __name__ == "__main__":
    root = Tk()
    # Overide the settings of the window
    root.configure(bg="black")
    root.geometry(f"{st.WIDTH}x{st.HEIGHT}")
    root.title("Minesweeper Game")
    root.resizable(False, False)  # width, height

    top_frame = Frame(
        root,
        bg="red",  # change later to black
        width=st.WIDTH,
        height=utils.height_prct(25),
    )
    top_frame.place(x=0, y=0)

    left_frame = Frame(
        root,
        bg="blue",  # change later to black
        width=utils.width_prct(25),
        height=utils.height_prct(75),
    )
    left_frame.place(x=0, y=utils.height_prct(25))

    center_frame = Frame(
        root,
        bg="gray",  # change later to black
        width=utils.width_prct(75),
        height=utils.height_prct(75),
    )
    center_frame.place(x=utils.width_prct(25), y=utils.height_prct(25))

    for x in range(st.GRID_SIZE):
        for y in range(st.GRID_SIZE):
            c = Cell(x, y)
            c.create_btn_object(center_frame)
            c.cell_btn_object.grid(column=x, row=y)

    # Cell the label from Cell class
    Cell.create_cell_count_label(left_frame)
    Cell.cell_count_label_object.place(
        x=0, y=0,
    )

    Cell.randomize_mines()
    

    Cell.show_all_mines()
    # Run the window
    root.mainloop()
