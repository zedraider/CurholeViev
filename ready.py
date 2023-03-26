import random
import threading
import time
from tkinter import *

## Create main window
root = Tk()
root.title("CurholeViev") # устанавливаем название окна
root.geometry("400x600")
root.minsize(250,600) # устанавливаем минимальный размер окна 
root.resizable(width=True, height=True) # выключаем возможность изменять окно



label2 = Label(font=(None, 10))
#label2.grid(row=1,column=1)
label2.pack()

label3 = Label(font=(None, 10))
#label3.grid(row=1,column=2)
label3.pack()



label4 = Label(font=(None, 10))
#label4.grid(row=1,column=2)
label4.pack()

Newlabel1 = Label(font=(None, 10))
#label4.grid(row=1,column=3)
Newlabel1.pack()

Labelgold = Label(root, bg="gold", width=20)
Labelgold.pack()



#Закрыть программу на кнопку меню.
def close_win():
     root.destroy()
#Закрыть программу на кнопку в окне.
def close_win_but(event):
     root.destroy()


#have the button run a function like this.
def mainthread():
    threading.Thread(target=buttonOne).start()

def scalget():
	return sca1.get()
def scalget2():
	return sca12.get()
def scalget3():
	return sca13.get()
def textget():
	return int(str(ent.get()))
def textget2():
	return int(str(ent2.get()))


## MY!!! Function run in thread
def button_clicked():
	xmath = scalget2()
	maxma = textget2()
	ss = 0
	g = scalget3()
	x = 1
	i = 0
	dep = textget()
	lose = 0
	def rand():
		a = (random.randint(1,100))
		return a
	while (dep > 1):
		i = i + 1
		label2['text'] = "РАУНД", i, "Депозит", dep
		time.sleep(scalget())
		while (rand() > 50):
			i = i + 1
			time.sleep(scalget())
			label2['text'] = "РАУНД", i, "Депозит", dep
			dep = dep - x
			x = x*(xmath)
			if (maxma!=0):
				if (x > maxma):
					x = 1 
			label2['text'] = "РАУНД", i, "Депозит", dep
			Labelgold['text'] = "ставка:", x
			if(x <= dep):
				label3['text'] = "проиграли! Удваиваем!"
				label2['text'] = "РАУНД", i, "Депозит", dep
				dep = dep - g
				ss = ss + g
				Newlabel1['text'] = "Забираем", g, "заработали", ss
			else:
				lose = 1
				break
		if(lose == 1):
			break
		dep = dep + x
		label2['text'] = "РАУНД", i, "Депозит", dep
		label3['text'] = "Выйграли!"
		x = 1
		dep = dep - g
		ss = ss + g
		Newlabel1['text'] = "Забираем", g, "заработали", ss
		
	label3['text'] = "Всё! Их нет!!! Ты всё продул! Осталось:"
	label44['text'] = ss + dep
## Function run in thread

## In the main thread, do usual stuff


#label2 = Label(root, text="HELLO", bg="red", width=8).pack()



#строчка
sca1 = Scale(root,orient=HORIZONTAL,length=300,
          from_=0,to=0.5,tickinterval=100,resolution=0.01)
sca1.pack()

#Текст перед окном ввода
label5 = Label(font=(None, 10))
label5['text'] = "Введите депозит"
label5.pack()

#text intern
ent = Entry(root,width=20) # Однострочное текстовое поле
ent.insert(END, '1000')
ent.pack()



#Текст перед окном ввода множителя
label6 = Label(font=(None, 10))
label6['text'] = "Введите множитель (2 для классической системы)"
label6.pack()

#text intern
sca12 = Scale(root,orient=HORIZONTAL,length=100, from_=0,to=3,tickinterval=100,resolution=0.1)
sca12.set(2)
sca12.pack()

#Текст перед окном ввода заработка
label66 = Label(font=(None, 10))
label66['text'] = "Введите сколько забирать со любой сделки"
label66.pack()
#text intern
sca13 = Scale(root,orient=HORIZONTAL,length=200, from_=0,to=3,tickinterval=100,resolution=0.1)
sca13.set(0)
sca13.pack()


#Текст перед окном ввода множителя
label7 = Label(font=(None, 10))
label7['text'] = "Введите максимальную ставку.(0 - не ограничена)"
label7.pack()

#text intern
ent2 = Entry(root,width=20) # Однострочное текстовое поле
ent2.insert(END, '512')
ent2.pack()

label44 = Label(root, bg="green", width=20)
label44.pack()

#запуск потока
def asd2(event):
	threading.Thread(target=button_clicked).start()

def asd3(event):
	threading.Thread(target=button_clicked).terminate()

#Кнопки запуска и выхода

but2 = Button(root) # Создание виджет
but2["text"] = "Старт" # Установка свойств виджет
but2.bind("<Button-1>",asd2) #Событие нажатия левой кнопкой мыши 
but2["font"]="Arial 12"
but2.pack() # Размещение виджет. Если не вставить эту строчку кода, то кнопка в окне так и не появится, хотя она есть в программе.

but2 = Button(root) # Создание виджет
but2["text"] = "Стоп" # Установка свойств виджет
but2.bind("<Button-1>",asd3) #Событие нажатия левой кнопкой мыши 
but2["font"]="Arial 12"
but2.pack() # Размещение виджет. Если не вставить эту строчку кода, то кнопка в окне так и не появится, хотя она есть в программе.
#Кнопки OFF

but2 = Button(root) # Создание виджет
but2["text"] = "Выход" # Установка свойств виджет
but2.bind("<Button-1>",close_win_but) #Событие нажатия левой кнопкой мыши 
but2["font"]="Arial 12"
but2.pack() # Размещение виджет. Если не вставить эту строчку кода, то кнопка в окне так и не появится, хотя она есть в программе.
#Кнопки OFF


#MENU

def about():
     win = Toplevel(root)
     lab = Label(win,text="CurholeViev is private Advomain programm. \n Don't use it.")
     lab.pack()
     
main_menu = Menu()

file_menu = Menu(tearoff=0)
file_menu.add_command(label="Exit",command=close_win)
 
help_menu = Menu(tearoff=0)
help_menu.add_command(label="About",command=about)
 
main_menu.add_cascade(label="File", menu=file_menu)
main_menu.add_cascade(label="Help",menu=help_menu)

root.config(menu=main_menu)

#MENU OFF

root.mainloop()