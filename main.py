from tkinter import *
import settings as st
import utils




root = Tk()
# Overide the settings of the window
root.configure(bg="black")
root.geometry(f'{st.WIDTH}x{st.HEIGHT}')
root.title("Minesweeper Game")
root.resizable(False, False) # width, height

top_frame = Frame(
    root,
    bg="red", # change later to black
    width=st.WIDTH,
    height=utils.height_prct(25)
    )
top_frame.place(x=0, y=0)

left_frame = Frame(
    root,
    bg='blue', # change later to black
    width=utils.width_prct(25),
    height=utils.height_prct(75)
)
left_frame.place(x=0, y=utils.height_prct(25))

# Run the window
root.mainloop()
