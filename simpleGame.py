# Simple game in python

import tkinter as tk

from tkinter import messagebox
 
ans = [
		#1
		("① 대구대학교는 몇년도에 개교했는가?","1956년"),
		#2
		("② 대구대학교의 공식캐릭터로 오른쪽 밑에 있는 캐릭터의 이름은 무엇인가?","두두"),
		#3
		("③ 대구대의 교목은 무엇인가?","소나무"),
                #4
                ("④ 대구대학교의 교화는 무엇인가?","백일홍"),
                #5
                ("⑤ 다음 중 대구대학교로 오는 버스가 아닌것은?(1,2,3,4 중 택1)\n   1. 708\n   2. 818\n   3. 814\n   4. 651 ","4"),
                #6
		("⑥ 대구대학교의 설립자는 누구인가?","이영식 목사"),
		#7
		("⑦ 대구대학교의 건학이념은 무엇인가?","사랑 빛 자유"),
		#8
		("⑧ 다음 중 대구대학교에 존재하는 장소가 아닌것은?(1,2,3,4 중 택1)\n   1. 두류공원\n   2. 글로벌라운지\n   3. 점자도서관\n   4. 창파도서관 ","1"),
                #9
                ("⑨ 대구대학교 안에서 즐길 수 있는 스포츠로 옳지 않은것은?(1,2,3,4 중 택1)\n   1. 탁구\n   2. 스키\n   3. 골프\n   4. 수영","2"),
                #10
                ("⑩ 대구대학교의 교훈은 무엇인가?","큰 뜻을 품어라")
 
]

numdom = len(ans)
score = 0
totalQuestions = 0

def d1():
	global totalQuestions, score, entry
	if totalQuestions == numdom:
	    text.pack_forget()
	    entry.pack_forget()
	    percent = (score/totalQuestions) * 100
		
	    button['text'] = f"평균: {percent}%\n 점수:{score}점\n 합격여부를 확인할려면 클릭하세요"
	    button['command'] = game_over
	    button.pack()
	    return
	    
	if totalQuestions == 0:
	    answer_widget()
		
	text['height'] = 7
	text['bg'] = 'white'
	text['width'] = 80
	text.delete("1.0",tk.END)
	text.insert("1.0",ans[totalQuestions][0])
	button.pack_forget()
	totalQuestions+=1

def game_over():
	global score
	if score >=7:
	    print("당신은 합격입니다! 대구대학교에 대한 지식이 풍부하군요!")
	else:
	    print("당신은 불합격입니다. 대구대학교에 대해 더 자세히 공부해 보세요!")
	window.destroy()
 
def answer_widget():
	global entry
	entry = tk.Entry(window, textvariable=ans, bg="yellow", font="Arial 20")
	entry.pack()
	entry.bind("<Return>", lambda x: check())
	entry.focus()
 
def empty_textbox():
	ans.set("")
	d1()
 
def check():
	global n, score
	text.delete("1.0",tk.END)
	
	if ans.get() == [totalQuestions-1][1]:
		text.insert(tk.END, "정답입니다! :) ")
		score+=1
		text['bg'] = "green"
	else:
		text.insert(tk.END, "오답입니다 :( ")
		text['bg'] = "red"
	text.after(1000, empty_textbox)

def clickButton() :
        messagebox.showinfo("도움말","게임시작을 누른 후, 빈칸에 답을 적고 엔터를 눌러!\n혹시라도 퀴즈가 어렵다면 오른쪽의 호랑이 캐릭터를 눌러봐!")

def duduButton() :
        messagebox.showinfo("힌트요정의 일기장","""안녕! 내 이름은 두두야! 나는 소나무와 백일홍을 가장 좋아해.\n내가 다니는 학교는 1956년에 처음 생겼고, 708, 818, 814 버스를 타면 놀러올 수 있어!
우리 학교는 이영식 목사님이 처음 지었고 사랑 빛 자유가 건학이념이래! 아 맞다. 교훈은 '큰 뜻을 품어라'야!\n우리학교에도 두류공원이 있었으면 좋겠어 ㅠㅠ 있었으면 스키도 탈 수 있었을껀데..""")
                                           
 
window = tk.Tk()
window.title("대구대 Quiz!!!")
window.geometry("1000x500")
window['bg'] = '#FFDCDC'

image = tk.PhotoImage(file="다운로드.png")
image_button = tk.Button(window, image = image, command=duduButton)
image_button.pack()

label = tk.Label(window, text = "대구대 Quiz", bg="green", font="Arial 48")
label.pack()

rules = """이 게임은 대구대학교를 잘 모르는 신입생들을 위해 대구대학교에 대한 퀴즈를 내서 대구대학교를 홍보하기 위해 제작되었습니다.

모든 퀴즈의 답은 한국어로 입력하셔야 되며, 단위가 있다면 모두 적어주셔야 정답으로 처리됩니다.

모두 만점을 받을 수 있길 기원합니다.

"""
text = tk.Text(window, bg="white",height=7,font="Arial 20")
text.insert("1.0", rules)
text.pack()

b1 = tk.Button(window, text="(도움말)", bg="white", fg="red", command=clickButton, font="Arial 10")
b1.place(x=0, y=472)
b1.pack

button = tk.Button(window, text="게임시작", bg="black", fg="white", command=d1, font="Arial 20")
button.pack()

image_button.place(x=780, y=300)
ans = tk.StringVar()
window.mainloop()











    
