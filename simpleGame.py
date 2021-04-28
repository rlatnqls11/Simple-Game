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













    
