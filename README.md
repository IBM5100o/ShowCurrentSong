首先這個東西應該有更好的方法，不過我就是根據自己的需求自己寫一個  
可以當作參考，改成適合你們自己的，或是找其他方法  

由於我個人習慣在本地端放音樂，通常是用PotPlayer  
直播時想顯示目前歌曲，就用Python寫了這個東西  
目標有兩個，一是取得歌曲名稱，二是顯示於視窗提供擷取  
不多說直接上code  
```
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
```
首先要先解釋一下，PotPlayer的視窗標題格式是長這樣: 檔案名稱 - PotPlayer  
例如: 化物語-OP.flac - PotPlayer  
上面的code就是去拿這個東西，然後把副檔名後面的東西砍掉，最後回傳名稱  
我的音樂只有mp3、m4a、flac這三種，所以就寫死了  
如此一來第一步就完成了，接著就是做視窗  
```
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
```
視窗我是用tkinter，字體大小顏色那些可以自己去調，比較重要的是refresher  
由於換歌時，顯示名稱也要更新，refresher就是在做這件事  
我是設定3秒(3000毫秒) 更新一次，如此一來第二步也完成了  
結果長這樣:  
![](https://hackmd.io/_uploads/Sk46Q4g1T.png)  
然後用直播軟體擷取這個視窗就完事了，記得不要把視窗最小化，不然會卡住  
另外我一開始是用PyCharm寫的，不過建議跑的時候用cmd，節省資源  
![](https://hackmd.io/_uploads/BkcNYVey6.png)  
基本上就是常規操作，先進虛擬環境，然後python main.py就好  
大概是這樣，下次見888888