import pyautogui
import tkinter as tk


def get_music_name():
    pot = pyautogui.getWindowsWithTitle("PotPlayer")
    if pot == []:
        name = 'Current Song:'
    else:
        name = pot[0].title
        idx = name.find(".mp3")
        if idx == -1:
            idx = name.find(".m4a")
            if idx == -1:
                idx = name.find(".flac")
        name = 'Current Song: ' + name[:idx]
    return name


def draw():
    global lbl_text
    fm_cal = tk.Frame(win, bg='#222222', width=1400, height=100)
    fm_cal.pack(fill=tk.BOTH)
    lbl_text = tk.Label(fm_cal, bg='#222222', fg='white',
                        text=get_music_name(), font=('Microsoft YaHei', 24),
                        padx=10, pady=10)
    lbl_text.pack(side=tk.LEFT, padx=30)


def refresher():
    global lbl_text
    lbl_text.configure(text=get_music_name())
    win.after(3000, refresher)


win = tk.Tk()
win.title("Music Name")
win.geometry('1400x100')
win.resizable(False, False)

draw()
refresher()
win.mainloop()
