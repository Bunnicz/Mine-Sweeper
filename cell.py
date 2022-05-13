from tkinter import Button
import settings as st
import random


class Cell:
    all = []
    def __init__(self, x: int, y: int, is_mine: bool = False) -> None:
        self.is_mine = is_mine
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
            text=f"{self.x}, {self.y}",
        )
        btn.bind('<Button-1>', self.left_click_actions)  # Left Mouse Click
        btn.bind('<Button-3>', self.right_click_actions)  # Right Mouse Click
        self.cell_btn_object = btn
        
    def left_click_actions(self, event) -> None:
        if self.is_mine:
            self.show_mine()
        else:
            self.show_cell()
        
    def right_click_actions(self, event) -> None:
        print(event)
        print("right clicked!")
        
    def show_mine(self):
        # A logic to Interupt the game and display a message that player lost!
        self.cell_btn_object.configure(bg='red')
    
    def show_cell(slef):
        pass
        
    @staticmethod
    def randomize_mines():
        picked_cells = random.sample(
            Cell.all, st.MINES_COUNT
        )
        for picked_cell in picked_cells:
            picked_cell.is_mine = True

    @staticmethod
    def show_all_mines():
        for cell in Cell.all:
            if cell.is_mine:
                cell.cell_btn_object.configure(bg="yellow")
    
    def __repr__(self):
        return f"Cell({self.x}, {self.y})"