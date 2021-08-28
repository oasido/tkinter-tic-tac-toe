from tkinter import *
from tkinter import messagebox

root = Tk()
root.title("Tic-Tac-Toe")


def reset_game():
    global b1, b2, b3, b4, b5, b6, b7, b8, b9
    global clicked, count
    clicked = True
    count = 0

    # The buttons
    b1 = Button(
        root,
        text=" ",
        font=("Helvetica", 20),
        height=3,
        width=6,
        bg="SystemButtonFace",
        command=lambda: b_click(b1),
    )
    b2 = Button(
        root,
        text=" ",
        font=("Helvetica", 20),
        height=3,
        width=6,
        bg="SystemButtonFace",
        command=lambda: b_click(b2),
    )
    b3 = Button(
        root,
        text=" ",
        font=("Helvetica", 20),
        height=3,
        width=6,
        bg="SystemButtonFace",
        command=lambda: b_click(b3),
    )
    b4 = Button(
        root,
        text=" ",
        font=("Helvetica", 20),
        height=3,
        width=6,
        bg="SystemButtonFace",
        command=lambda: b_click(b4),
    )
    b5 = Button(
        root,
        text=" ",
        font=("Helvetica", 20),
        height=3,
        width=6,
        bg="SystemButtonFace",
        command=lambda: b_click(b5),
    )
    b6 = Button(
        root,
        text=" ",
        font=("Helvetica", 20),
        height=3,
        width=6,
        bg="SystemButtonFace",
        command=lambda: b_click(b6),
    )
    b7 = Button(
        root,
        text=" ",
        font=("Helvetica", 20),
        height=3,
        width=6,
        bg="SystemButtonFace",
        command=lambda: b_click(b7),
    )
    b8 = Button(
        root,
        text=" ",
        font=("Helvetica", 20),
        height=3,
        width=6,
        bg="SystemButtonFace",
        command=lambda: b_click(b8),
    )
    b9 = Button(
        root,
        text=" ",
        font=("Helvetica", 20),
        height=3,
        width=6,
        bg="SystemButtonFace",
        command=lambda: b_click(b9),
    )

    # The grid layout
    b1.grid(row=0, column=0)
    b2.grid(row=0, column=1)
    b3.grid(row=0, column=2)

    b4.grid(row=1, column=0)
    b5.grid(row=1, column=1)
    b6.grid(row=1, column=2)

    b7.grid(row=2, column=0)
    b8.grid(row=2, column=1)
    b9.grid(row=2, column=2)


# X starts first
clicked = True
count = 0


# Button clicked
def b_click(b):
    global clicked, count

    if b["text"] == " " and clicked is True:
        b["text"] = "X"
        clicked = False
        count += 1
        check_win()
    elif b["text"] == " " and clicked is False:
        b["text"] = "O"
        clicked = True
        count += 1
        check_win()
    else:
        messagebox.showerror(
            "Tic-Tac-Toe Error",
            "Too late friend, you can't select that one!\n Pick another one.",
        )


def check_win():
    global winner
    winner = False

    # Check for X's win
    if b1["text"] == "X" and b2["text"] == "X" and b3["text"] == "X":
        b1.config(bg="red")
        b2.config(bg="red")
        b3.config(bg="red")
        winner = True
        messagebox.showinfo("Tic Tac Toe", "CONGRATULATIONS!  X Wins!!")
        disable_all_buttons()
    elif b4["text"] == "X" and b5["text"] == "X" and b6["text"] == "X":
        b4.config(bg="red")
        b5.config(bg="red")
        b6.config(bg="red")
        winner = True
        messagebox.showinfo("Tic Tac Toe", "CONGRATULATIONS!  X Wins!!")
        disable_all_buttons()

    elif b7["text"] == "X" and b8["text"] == "X" and b9["text"] == "X":
        b7.config(bg="red")
        b8.config(bg="red")
        b9.config(bg="red")
        winner = True
        messagebox.showinfo("Tic Tac Toe", "CONGRATULATIONS!  X Wins!!")
        disable_all_buttons()

    elif b1["text"] == "X" and b4["text"] == "X" and b7["text"] == "X":
        b1.config(bg="red")
        b4.config(bg="red")
        b7.config(bg="red")
        winner = True
        messagebox.showinfo("Tic Tac Toe", "CONGRATULATIONS!  X Wins!!")
        disable_all_buttons()

    elif b2["text"] == "X" and b5["text"] == "X" and b8["text"] == "X":
        b2.config(bg="red")
        b5.config(bg="red")
        b8.config(bg="red")
        winner = True
        messagebox.showinfo("Tic Tac Toe", "CONGRATULATIONS!  X Wins!!")
        disable_all_buttons()

    elif b3["text"] == "X" and b6["text"] == "X" and b9["text"] == "X":
        b3.config(bg="red")
        b6.config(bg="red")
        b9.config(bg="red")
        winner = True
        messagebox.showinfo("Tic Tac Toe", "CONGRATULATIONS!  X Wins!!")
        disable_all_buttons()

    elif b1["text"] == "X" and b5["text"] == "X" and b9["text"] == "X":
        b1.config(bg="red")
        b5.config(bg="red")
        b9.config(bg="red")
        winner = True
        messagebox.showinfo("Tic Tac Toe", "CONGRATULATIONS!  X Wins!!")
        disable_all_buttons()

    elif b3["text"] == "X" and b5["text"] == "X" and b7["text"] == "X":
        b3.config(bg="red")
        b5.config(bg="red")
        b7.config(bg="red")
        winner = True
        messagebox.showinfo("Tic Tac Toe", "CONGRATULATIONS!  X Wins!!")
        disable_all_buttons()

    # Check for O's win
    elif b1["text"] == "O" and b2["text"] == "O" and b3["text"] == "O":
        b1.config(bg="red")
        b2.config(bg="red")
        b3.config(bg="red")
        winner = True
        messagebox.showinfo("Tic Tac Toe", "CONGRATULATIONS!  O Wins!!")
        disable_all_buttons()
    elif b4["text"] == "O" and b5["text"] == "O" and b6["text"] == "O":
        b4.config(bg="red")
        b5.config(bg="red")
        b6.config(bg="red")
        winner = True
        messagebox.showinfo("Tic Tac Toe", "CONGRATULATIONS!  O Wins!!")
        disable_all_buttons()

    elif b7["text"] == "O" and b8["text"] == "O" and b9["text"] == "O":
        b7.config(bg="red")
        b8.config(bg="red")
        b9.config(bg="red")
        winner = True
        messagebox.showinfo("Tic Tac Toe", "CONGRATULATIONS!  O Wins!!")
        disable_all_buttons()

    elif b1["text"] == "O" and b4["text"] == "O" and b7["text"] == "O":
        b1.config(bg="red")
        b4.config(bg="red")
        b7.config(bg="red")
        winner = True
        messagebox.showinfo("Tic Tac Toe", "CONGRATULATIONS!  O Wins!!")
        disable_all_buttons()

    elif b2["text"] == "O" and b5["text"] == "O" and b8["text"] == "O":
        b2.config(bg="red")
        b5.config(bg="red")
        b8.config(bg="red")
        winner = True
        messagebox.showinfo("Tic Tac Toe", "CONGRATULATIONS!  O Wins!!")
        disable_all_buttons()

    elif b3["text"] == "O" and b6["text"] == "O" and b9["text"] == "O":
        b3.config(bg="red")
        b6.config(bg="red")
        b9.config(bg="red")
        winner = True
        messagebox.showinfo("Tic Tac Toe", "CONGRATULATIONS!  O Wins!!")
        disable_all_buttons()

    elif b1["text"] == "O" and b5["text"] == "O" and b9["text"] == "O":
        b1.config(bg="red")
        b5.config(bg="red")
        b9.config(bg="red")
        winner = True
        messagebox.showinfo("Tic Tac Toe", "CONGRATULATIONS!  O Wins!!")
        disable_all_buttons()

    elif b3["text"] == "O" and b5["text"] == "O" and b7["text"] == "O":
        b3.config(bg="red")
        b5.config(bg="red")
        b7.config(bg="red")
        winner = True
        messagebox.showinfo("Tic Tac Toe", "CONGRATULATIONS!  O Wins!!")
        disable_all_buttons()


def disable_all_buttons():
    b1.config(state="disabled")
    b2.config(state="disabled")
    b3.config(state="disabled")
    b4.config(state="disabled")
    b5.config(state="disabled")
    b6.config(state="disabled")
    b9.config(state="disabled")
    b7.config(state="disabled")
    b8.config(state="disabled")


def about():
    messagebox.showinfo("About", "Gemaakt door Ofek.")


# Creating the menu
the_menu = Menu(root)
root.config(menu=the_menu)

# Adding functions and the cascade to the menu
options_menu = Menu(the_menu, tearoff=False)
the_menu.add_cascade(label="Options", menu=options_menu)
options_menu.add_command(label="Restart", command=reset_game)

about_menu = Menu(the_menu, tearoff=False)
the_menu.add_cascade(label="Help", menu=about_menu)
about_menu.add_command(label="About", command=about)

reset_game()

root.mainloop()
