# import ctypes
import random
import sys
import time
import tkinter.messagebox
from tkinter import *
from typing import List

import settings as st


class Cell:
    all = []
    cell_count = st.CELL_COUNT
    cell_count_label_object = None
    start_time = 0
    game_time = f"{0:03}"
    game_time_label_object = None
    mine_clicked = False

    def __init__(self, x: int, y: int, is_mine: bool = False) -> None:
        self.is_mine = is_mine
        self.is_opened = False
        self.is_mine_candidate = False
        self.cell_btn_object = None
        self.x = x
        self.y = y

        # Append the object to the Cell.all list
        Cell.all.append(self)

    def create_btn_object(self, location) -> None:
        btn = Button(
            location,
            width=2,
            height=1,
        )
        btn.bind("<Button-1>", self.left_click_actions)  # Left Mouse Click
        btn.bind("<Button-3>", self.right_click_actions)  # Right Mouse Click
        self.cell_btn_object = btn

    @staticmethod
    def create_cell_count_label(location):
        # Config in show_cell function
        lbl = Label(
            location,
            text=f"{Cell.cell_count}",
            width=3,
            height=1,
            font=st.LBL_FONT,
            bg="black",
            fg="red",
        )
        Cell.cell_count_label_object = lbl

    @staticmethod
    def create_time_label(location):
        lbl_time = Label(
            location,
            text=f"{Cell.game_time}",
            width=4,
            height=1,
            font=st.LBL_FONT,
            bg="black",
            fg="red",
        )
        Cell.game_time_label_object = lbl_time

    @staticmethod
    def count_elapsed_time():
        # Updates game time label every 1 sec if game haven't finished
        Cell.game_time = f"{int(time.time() - Cell.start_time):003}"
        Cell.game_time_label_object.config(text=Cell.game_time)
        if Cell.cell_count != st.MINES_COUNT and not Cell.mine_clicked:
            Cell.game_time_label_object.after(1000, Cell.count_elapsed_time)

    @staticmethod
    def show_mine():
        for cell in Cell.all:
            if cell.is_mine:
                cell.cell_btn_object.configure(bg="red", relief="sunken")

    def left_click_actions(self, event) -> None:
        self.is_opened = True
        if self.is_mine:
            Cell.mine_clicked = True  # Var for stopping timer only!
            self.show_mine()
            tkinter.messagebox.showinfo(
                "Game Over",
                f"You clicked on a mine.\nGame finished in {Cell.game_time} sec",
            )
            sys.exit()
        else:

            if self.surrounded_cells_mines_lenght == 0:
                for cell_obj in self.surrounded_cells:
                    if not cell_obj.is_opened:
                        cell_obj.left_click_actions("<Button-1>")
                    cell_obj.show_cell()
            self.show_cell()

            # If Mines count is equal to the cells left count, player won
            if Cell.cell_count == st.MINES_COUNT:
                tkinter.messagebox.showinfo(
                    "Game Over",
                    f"Congratulations! You won the game!\nGame finished in {Cell.game_time} sec!",
                )
                sys.exit()

        # Cancel left and Right click events if cell is already opened:
        # self.cell_btn_object.unbind("<Button-1>")
        # self.cell_btn_object.unbind("<Button-3>")

    def show_cell(self):
        if self.is_opened:
            x = 0
            self.configure_cell_btn_object_text()
            for cell_obj in Cell.all:
                if cell_obj.is_opened:
                    x += 1
            Cell.cell_count = st.CELL_COUNT - x
            # Replace the text of cell count label with the newer count
            if Cell.cell_count_label_object:
                Cell.cell_count_label_object.configure(
                    text=f"{Cell.cell_count}",  # Reapeted in label init
                )

    def right_click_actions(self, event) -> None:
        if not self.is_mine_candidate and not self.is_opened:
            self.cell_btn_object.configure(
                bg="orange",
            )
            self.is_mine_candidate = True
        else:
            self.cell_btn_object.configure(
                bg="SystemButtonFace",
            )
            self.is_mine_candidate = False

    def get_cell_by_axis(self, x: int, y: int):
        # Return a cell object based on the value of x, y
        for cell in Cell.all:
            if cell.x == x and cell.y == y:
                return cell

    @property
    def surrounded_cells(self) -> List:
        cells = [
            self.get_cell_by_axis(self.x - i, self.y - j)
            for i in range(-1, 2)
            for j in range(-1, 2)
            if not (i == 0 and j == 0)
        ]
        cells = [cell for cell in cells if cell is not None]

        return cells

    @property
    def surrounded_cells_mines_lenght(self) -> int:
        counter = 0
        for cell in self.surrounded_cells:
            if cell.is_mine:
                counter += 1
        return counter

    def configure_cell_btn_object_text(self):
        # configure cell text depending on surronding mine cells
        cell_fg_list = [
            "#0000ff",
            "#009933",
            "#ff0000",
            "#000066",
            "#990000",
            "#00ffff",
            "#000000",
            "#808080",
        ]
        cell_text = self.surrounded_cells_mines_lenght
        cell_fg = "white"
        if cell_text == 0:
            cell_text = None
        # Cell fg colour for numbers from 1 to 8
        for i in range(7):
            if cell_text == i + 1:
                cell_fg = cell_fg_list[i]

        self.cell_btn_object.configure(
            text=cell_text, fg=cell_fg, relief="sunken", bg="SystemButtonFace"
        )

    @staticmethod
    def randomize_mines():
        picked_cells = random.sample(Cell.all, st.MINES_COUNT)
        for picked_cell in picked_cells:
            picked_cell.is_mine = True

    @staticmethod
    def show_all_mines():
        # Show all mines for debug only!
        for cell in Cell.all:
            if cell.is_mine:
                cell.cell_btn_object.configure(bg="yellow")

    def __repr__(self):
        return f"Cell({self.x}, {self.y})"
