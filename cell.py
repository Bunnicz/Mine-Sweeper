from tkinter import Button, Label
import settings as st
import random
import ctypes


class Cell:
    all = []
    cell_count = st.CELL_COUNT
    cell_count_label_object = None

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
            width=12,
            height=4,
            #     text=f"{self.x}, {self.y}",
        )
        btn.bind("<Button-1>", self.left_click_actions)  # Left Mouse Click
        btn.bind("<Button-3>", self.right_click_actions)  # Right Mouse Click
        self.cell_btn_object = btn
    
    @staticmethod
    def create_cell_count_label(location):
        lbl = Label(
            location,
            bg='black',
            fg='white',
            text=f"Cells Left: {Cell.cell_count}",
            width=12,
            height=4,
            font=("", 30),
        )
        Cell.cell_count_label_object = lbl
    
    def left_click_actions(self, event) -> None:
        if self.is_mine:
            self.show_mine()
        else:
            # add showing all cells with 0
            if not self.is_opened:
                if self.surrounded_cells_mines_lenght == 0:
                    for cell_obj in self.surrounded_cells:
                        cell_obj.show_cell()
                self.show_cell()

    def right_click_actions(self, event) -> None:
        if not self.is_mine_candidate:
            self.cell_btn_object.configure(
                bg='orange',
            )
            self.is_mine_candidate = True
        else:
            self.cell_btn_object.configure(
                bg='SystemButtonFace',
            )
            self.is_mine_candidate = False

    def get_cell_by_axis(self, x: int, y: int):
        # Return a cell object based on the value of x, y
        for cell in Cell.all:
            if cell.x == x and cell.y == y:
                return cell

    def show_mine(self):
        # A logic to Interupt the game and display a message that player lost!
        self.cell_btn_object.configure(bg="red")

    @property
    def surrounded_cells(self):
        cells = [
            self.get_cell_by_axis(self.x - i, self.y - j)
            for i in range(-1, 2)
            for j in range(-1, 2)
            if not (i == 0 and j == 0)
        ]
        # for i in range(-1,2):
        #     for j in range(-1,2):
        #         if (i == 0 and j == 0): # or f"Cell({self.x - i}, {self.y - j})" not in Cell.all:
        #             continue
        #         surrounded_cells.append(self.get_cell_by_axis(self.x - i, self.y - j))
        cells = [cell for cell in cells if cell is not None]
        return cells

    @property
    def surrounded_cells_mines_lenght(self):
        counter = 0
        for cell in self.surrounded_cells:
            if cell.is_mine:
                counter += 1
        return counter

    def show_cell(self):
        if not self.is_opened:
            Cell.cell_count -= 1
            self.cell_btn_object.configure(text=self.surrounded_cells_mines_lenght)
            # Replace the text of cell count label with the newer count
            if Cell.cell_count_label_object:
                Cell.cell_count_label_object.configure(
                    text=f"Cells Left: {Cell.cell_count}",
                )
        # Mark the cell as opened (Use it as the last line of this method)
        self.is_opened = True
        
    @staticmethod
    def randomize_mines():
        picked_cells = random.sample(Cell.all, st.MINES_COUNT)
        for picked_cell in picked_cells:
            picked_cell.is_mine = True

    @staticmethod
    def show_all_mines():
        for cell in Cell.all:
            if cell.is_mine:
                cell.cell_btn_object.configure(bg="yellow")

    def __repr__(self):
        return f"Cell({self.x}, {self.y})"
