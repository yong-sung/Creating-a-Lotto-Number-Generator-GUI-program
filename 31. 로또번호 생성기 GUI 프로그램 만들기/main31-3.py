import tkinter
import tkinter.font
import random

lotto_num = range(1,46) # 1부터 45까지 숫자를 리스트로 만듬.

def buttonClick():
    for i in range(5):
        lottoPick = map(str, random.sample(lotto_num,6)) # 'lotto_num'에서 6개의 무작위 숫자를 선택
        lottoPick = ','.join(lottoPick)
        lottoPick = str(i+1) + "회: " + lottoPick
        print(lottoPick)
        listbox.insert(i, lottoPick)
    listbox.pack() # tkinter에서 위젯을 화면에 배치하는 메소드
    
window=tkinter.Tk()
window.title("lotto")
window.geometry("400x200+800+300") # 크기를 400x200으로 설정, 위치를 800, 300으로 설정
window.resizable(False, False) # 사이즈 조절 안함

# 버튼에 "번호확인"이라는 텍스트를 표시, 너비는 15로 설정. 클릭 시 buttonClick 함수가 실행되도록 command 옵션을 설정
button = tkinter.Button(window, overrelief="solid",text="번호확인", width=15, command=buttonClick, repeatdelay=1000, repeatinterval=100)

button.pack()

font = tkinter.font.Font(size = 20)

# tkinter.Listbox를 사용하여 목록 위젯을 생성. 다중 선택이 가능하도록 selectmode를 'extended'로 설정하고, 높이는 5로 설정
listbox = tkinter.Listbox(window, selectmode='extended', height=5, font=font)

listbox.insert(0, "1회:")
listbox.insert(0, "2회:")
listbox.insert(0, "3회:")
listbox.insert(0, "4회:")
listbox.insert(0, "5회:")
listbox.pack()

window.mainloop() # window.mainloop()를 호출하여 윈도우를 루프로 유지하여 사용자 입력을 처리