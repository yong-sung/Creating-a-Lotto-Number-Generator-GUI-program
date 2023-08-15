import tkinter
import tkinter.font
import random

lotto_num = range(1,46) # 1부터 45까지 숫자를 리스트로 만듬.

def buttonClick():
    print(random.sample(lotto_num,6))
    
window=tkinter.Tk()
window.title("lotto")
window.geometry("400x200+800+300")
window.resizable(False, False) # 사이즈 조절 안함

button = tkinter.Button(window, overrelief="solid",text="번호확인", width=15, command=buttonClick, repeatdelay=1000, repeatinterval=100)
button.pack()

window.mainloop()