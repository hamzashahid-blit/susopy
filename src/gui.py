# TODO: ALLOW CHANGE OF THEME BY CHANGE OF COLORS!

import tkinter as tk
from tkinter import ttk
from PIL import Image, ImageTk
import tksvg
import time


class COLOR:
    background = "#282828"
    foreground = "#ebdbb2"
    light_background = "#2c2c2c"
    regular_black = "#282828"
    regular_red = "#cc241d"
    regular_green = "#98971a"
    regular_yellow = "#d79921"
    regular_blue = "#458588"
    regular_magenta = "#b16286"
    regular_cyan = "#689d6a"
    regular_gray = "#a89984"
    bright_black = "#928374"
    bright_red = "#fb4934"
    bright_green = "#b8bb26"
    bright_yellow = "#fabd2f"
    bright_blue = "#83a598"
    bright_magenta = "#d3869b"
    bright_cyan = "#8ec07c"
    bright_gray = "#ebdbb2"

should_run = True
def close_app ():
    global should_run
    should_run = False
    root.destroy()

ALGORITHMS = ["Backtracking"]

root = tk.Tk()
root.config(background="#282828")
root.protocol("WM_DELETE_WINDOW", close_app)
root.geometry("420x420")
root.title("Susopy")
icon_image = tk.PhotoImage(file="../res/logo.png")
root.iconphoto(True, icon_image)

menubar = tk.Menu(root)
root.config(menu=menubar)

### Menu ###
file_menu = tk.Menu(menubar, tearoff=0)
menubar.add_cascade(label="File", menu=file_menu)
file_menu.add_command(label="New")
file_menu.add_command(label="Open")
file_menu.add_command(label="Save")
file_menu.add_separator()
file_menu.add_command(label="Exit", command=close_app)

edit_menu = tk.Menu(menubar, tearoff=0)
menubar.add_cascade(label="Edit", menu=edit_menu)
edit_menu.add_command(label="Cut")
edit_menu.add_command(label="Copy")
edit_menu.add_command(label="Paste")
edit_menu.add_separator()
edit_menu.add_command(label="Theme")

### PanedWindow ###
main_paned = tk.PanedWindow(root,
                            orient=tk.HORIZONTAL,
                            background=COLOR.bright_black,
                            bd=0,
                            showhandle=False,
                            sashwidth=10,
                            handlesize=10,
                            width=400)
main_paned.pack(fill=tk.BOTH, expand=True)

main_frame = tk.Frame(main_paned,
                      background=COLOR.background,
                      width=400)
tool_frame = tk.Frame(main_paned,
                      background=COLOR.background,
                      width=200)
tool_frame.columnconfigure(tuple(range(3)), weight=1)
tool_frame.rowconfigure(tuple(range(10)), weight=1)
main_paned.add(main_frame, minsize=300)
main_paned.add(tool_frame, minsize=400)

### TOOL PANE ###
tool_label = tk.Label(tool_frame,
                      text="Tool pane",
                      font=("Clear Sans", 20),
                      background=COLOR.background,
                      foreground=COLOR.foreground)
tool_label.grid(row=0, column=0, columnspan=3)

algorithm_label = tk.Label(tool_frame,
                           text="Algorithm: ",
                           font=("Clear Sans", 16),
                           background=COLOR.background,
                           foreground=COLOR.foreground)
algorithm_label.grid(row=1, column=0, stick=tk.EW)

style = ttk.Style()
# Without theme_use style.map() won't function as expected.
style.theme_use('clam')
# Style Combobox Listbox
root.option_add('*TCombobox*Listbox*Background', COLOR.background)
root.option_add('*TCombobox*Listbox*Foreground', COLOR.foreground)
root.option_add('*TCombobox*Listbox*selectBackground', COLOR.regular_gray)
root.option_add('*TCombobox*Listbox*selectForeground', COLOR.background)
root.option_add('*TCombobox*Listbox.font', ("Clear Sans", 16))   # apply font to combobox list
# Style Combobox entry field
style.map('TCombobox', fieldbackground=[('readonly', COLOR.background)])
style.map('TCombobox', selectbackground=[('readonly', COLOR.background)])
style.map('TCombobox', selectforeground=[('readonly', COLOR.foreground)])
style.map('TCombobox', background=[('readonly', COLOR.background)])
style.map('TCombobox', foreground=[('readonly', COLOR.foreground)])

# Set Dropdown Icon and Theme it's color to foreground color
def hex_to_rgb(hex_color): return tuple(int(hex_color.lstrip("#")[i:i+2], 16) for i in (0, 2, 4))
def get_arrow_down_image():
    raw_img = Image.open("../res/arrow-down-dark.png").resize((35, 35))
    img = raw_img.convert("RGBA")
    new_data = []
    for item in img.getdata():
        if item[3] > 0:
            r, g, b = hex_to_rgb(COLOR.foreground)
            new_data.append((r, g, b, 255))
        else:
            new_data.append(item)
    img.putdata(new_data)
    return img

arrow_down_photo = ImageTk.PhotoImage(get_arrow_down_image())
style.element_create('TCombobox.downarrow', 'image', arrow_down_photo)
style.layout(
    'TCombobox', [(
        'Combobox.field', {
            'sticky': tk.NSEW,
            'children': [(
                'TCombobox.downarrow', {
                    'side': 'right',
                    'sticky': tk.NS
                }
            ), (
                'Combobox.padding', {
                    'expand': '1',
                    'sticky': tk.NSEW,
                    'children': [(
                        'Combobox.textarea', {
                            'sticky': tk.NSEW
                        }
                    )]
                }
            )]
        }
    )]
)

algorithm = tk.StringVar(tool_frame)
algorithm_combobox = ttk.Combobox(tool_frame,
                                  textvariable=algorithm,
                                  state="readonly",
                                  values=ALGORITHMS,
                                  font=("Clear Sans", 16),
                                  justify="center")
algorithm.set(ALGORITHMS[0])
algorithm_combobox.bind("<<ComboboxSelected>>", lambda event: event.widget.selection_clear())
algorithm_combobox.grid(row=1, column=1, columnspan=2, sticky=tk.EW, padx=(0, 20))

### MAIN PANE ###
def resize_board(event):
    square_size = min(event.width, event.height)/9
    offset_y = (event.height / 2 - square_size * 9/2) * 0.75 # 15% shifted up for visual niceness
    offset_x = event.width / 2 - square_size * 9/2
    # Resize and move Squares
    for y in range(9):
        for x in range(9):
            main_canvas.coords(squares[y][x],
                               square_size*x, square_size*y,
                               square_size*(x+1), square_size*(y+1))
            main_canvas.coords(digits[y][x], square_size * (x + 1/2), square_size * (y + 1/2))
            # Dynamic font size
            fontsize = 20 if event.width < 500 else 35
            main_canvas.itemconfigure(digits[y][x], font=("Clear Sans", fontsize))
    for y in range(3):
        for x in range(3):
            main_canvas.coords(group_squares[x+(3*y)],
                               square_size*3*x, square_size*3*y,
                               square_size*3*(x+1), square_size*3*(y+1))
    # Center board
    [main_canvas.move(item, offset_x, offset_y) for item in main_canvas.find_all()]

def create_squares():
    return [[main_canvas.create_rectangle(10, 10, 30, 30, outline=COLOR.foreground) for x in range(9)] for y in range(9)]

def create_group_squares():
    return [main_canvas.create_rectangle(20, 20, 30, 30, outline=COLOR.foreground, width=3) for x in range(9)]

def create_digits():
    return [[main_canvas.create_text(20*y, 20*x, fill=COLOR.foreground, font=("Clear Sans", 35), text=str(x)) for x in range(9)] for y in range(9)]


main_canvas = tk.Canvas(main_frame,
                        background=COLOR.background,
                        borderwidth=0,
                        highlightthickness=0,)
title_label = tk.Label(main_frame, text="Susopy", font=("Clear Sans", 25), fg=COLOR.foreground, bg=COLOR.background)
title_label.pack()
main_canvas.pack(fill=tk.BOTH, expand=True)
main_canvas.bind('<Configure>', resize_board)


squares = create_squares()
group_squares = create_group_squares()
digits = create_digits()
while should_run:
    tool_label.config(text=f"({main_canvas.winfo_width()}, {main_canvas.winfo_height()})")
    root.update()
    time.sleep(0.001)

# board_frame = tk.Frame(main_frame)
# board_frame.pack(expand=True)
# for y in range(9):
#     for x in range(9):
#         tk.Label(board_frame,
#                  text="8",
#                  font=("Clear Sans", 10),
#                  highlightthickness=1,
#                  bg=COLOR.background,
#                  fg=COLOR.foreground).grid(row=y, column=x, ipadx=10, ipady=10)
