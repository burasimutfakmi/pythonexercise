#class Akin:
import threading
import time
#bacaklar = 2
    #ayaklar = 2
    #kollar = 2
    #eller = 2
    #dick = 1
    #def __init__(self,make,model,year,color):
#       self.make = make
#        self.model = model
#        self.year = year
#        self.color = color

    #def code(self):
        #print(self.model + " is coding!")

    #def codestop(self):
        #print(self.model + " stopped coding!")

#class Human:

    #alive = True

    #def code(self):
        #print("He is coding")

    #def eat(self):
        #print("he is eating")

    #def sleep(self):
        #print("he is sleeping")

# class Muzo(Human):
#     def muzo(self):
#         print("Ben muzoyum")
# class Akin(Human):
#     pass
# class Arda(Human):
#     def arda(self):
#         print("Ben ardayım")
#
# muzo = Muzo()
# akin = Akin()
# arda = Arda()


#arda.sleep()
#arda.arda()
#muzo.muzo()

# class Prey:
#
#     def flee(self):
#         print("This animal is fast and you can not catch it")
#
# class Predator:
#
#     def hunt(self):
#         print("This animal is hunting and is faster than you so tell your last words")
#
# class Fish(Prey,Predator):
#     pass
#
# fish = Fish()
# fish.hunt()
# class Car:
#
#     def turnon(self):
#         print("Car turned on")
#         return self
#
#     def turnoff(self):
#         print("Car turned off")
#         return self
#
#     def drive(self):
#         print("Car has been drived")
#         return self
#
#     def brake(self):
#         print("Car's breaks has been stepped on")
#         return self
#
# car = Car()
#
# car.turnon()\
#     .drive()\
#     .brake()\
#     .turnoff()
# class Dortgen:
#     def __init__(self, uzunluk, genislik):
#         self.uzunluk = uzunluk
#         self.genislik = genislik
#
# class Kare(Dortgen):
#     def __init__(self,uzunluk, genislik):
#         super().__init__(uzunluk,genislik)
#
#     def alan(self):
#         return self.uzunluk * self.genislik
#
# class Kup(Dortgen):
#     def __init__(self,uzunluk,genislik,yukseklik):
#         super().__init__(uzunluk,genislik)
#         self.yukseklik = yukseklik
#     def volume(self):
#         return self.uzunluk*self.genislik*self.yukseklik
#
# kup = Kup(3,3,3)
# kare = Kare(3,3)
#
# print(kare.alan())
# print(kup.volume())

# from abc import ABC, abstractmethod
#
# class Vehicle(ABC):
#
#     @abstractmethod
#     def go(self):
#         pass
#     @abstractmethod
#     def stop(self):
#         pass
#
# class Car(Vehicle):
#     def go(self):
#         print("You drive this car")
#
#     def stop(self):
#         print("You stopped this car")
#
# class Motor(Vehicle):
#     def go(self):
#         print("You drive this motorcycle")
#     def stop(self):
#         print("You stopped this motorcycle")
# motor = Motor()
# car = Car()
# motor.go()
# car.go()
# motor.stop()
# car.stop()





# class Car:
#     color = None
#
# class Motor:
#     color = None
#
# def change_color(vehicle,color):
#
#     vehicle.color = color
#     print(color)
#
# car_1 = Car()
# car_2 = Car()
# car_3 = Car()
#
# bike_1 = Motor()
# bike_2 = Motor()
# bike_3 = Motor()
#
# change_color(car_1,"red")
# change_color(car_2,"white")
# change_color(car_3,"blue")
# change_color(bike_1,"black")




# class Chicken:
#
#     def walk(self):
#         print("This chicken walks.")
#
#     def talk(self):
#         print("This chicken glucks.")
#
# class Duck:
#
#     def walk(self):
#         print("This duck walks.")
#
#     def talk(self):
#         print("This duck quacks")
#
# class Person:
#
#     def catch(self,a):
#         a.walk()
#         a.talk()
#         print("You got it!")
#
# chicken = Chicken()
# duck = Duck()
# person = Person()
#
# person.catch(chicken)





# foods = list()
# while food := input("what would you prefer?: ") != "quit":
#     foods.append(food)
# def loud(text):
#     return text.upper()
#
# def quiet(text):
#     return text.lower()
#
# def hello(func):
#     text = func("hello")
#     print(text)
#
#
# hello





# age_check = lambda age: print("you are an adult") if age>=18 else print("suck it")
# age_check(int(input("enter your age: ")))
# colors = ("blue", "red", "white", "black", "green")
#
# sort = sorted(colors,reverse=True)
#
# for i in sort:
#     print




# store = [("Jacket",20.00),
#          ("Pants",15.00),
#          ("Hoodie",18.00),
#          ("Don",25.00)]
#
# to_euro = lambda data:(data[0], data[1] * 0.82)
#
# eurostore = list(map(to_euro,store))
# for i in eurostore:
#     print(i)




# import functools
# factorial = [int(input("istediğiniz sayıları giriniz: "))]
# word = functools.reduce(lambda x,y: x*y,factorial)
# print




# notes = [100,90,70,50,20,10]
#
# passed_students = [i if i >= 60 else "FAILED" for i in notes]
# print(passed_students)



# dictionary = {"New York": 32, "Amsterdam": 67, "Tokyo": 79}
#
# dictionary_2 = {key: round((value-32)*(5/9)) for (key, value) in dictionary.items()}
# print(dictionary_2)



# cities = {"New York": 78, "Amsterdam": 210, "Somewhere in the uni": 8392, "Adana": 26, "Ankara": 837292}
# desc_cities = {key: ("Sıcak" if value >= 250 else "soğuk") for (key,value) in cities.items()}
# print(desc_cities)




# usernames = ["Akin", "Pritok", "akinbabajoe"]
# password = ("p@ssword", "guest", "akinbabajoe2123")
#
# users = dict(zip(usernames, password))
#
# for key,value in users.items():
#     print(key,":", value)
#
# login_date = ["1/1/2021", "1/2/2021", "1/3/2021"]
#
# logins = zip(usernames,password,login_date)
# for key,value,date in logins:
#     print




# print(time.ctime(0))
#
# print(time.time())
#
# print(time.localtime())
# import time
# time1 = (1988, 5, 21, 6, 0, 0, 0, 0, 0)
# print(time.asctime(time1))




# import threading
# import time
#
#
# def eat_breakfast():
#     time.sleep(3)
#     print("breakfast done")
#
# def drink_coffee():
#     time.sleep(4)
#     print("you drank coffee")
#
#
# def study():
#     time.sleep(5)
#     print("you have studied")
#
#
# x = threading.Thread(target=eat_breakfast,args=())
# x.start()
#
# y = threading.Thread(target=drink_coffee,args=())
# y.start()
#
# z = threading.Thread(target=study,args=())
# z.start()
#
# x.join()
# y.join()
# z.join()
#
# print(threading.active_count())
# print(threading.enumerate())
# print(time.perf_counter())





# from multiprocessing import Process, cpu_count
#
# def counter(num):
#     count = 0
#     while count<num:
#         count += 1
#         print(count)
#
#
# def main():
#
#     print(cpu_count())
#     a = Process(target=counter, args=(2500,))
#     b = Process(target=counter, args=(2500,))
#     c = Process(target=counter, args=(2500,))
#     d = Process(target=counter, args=(2500,))
#     e = Process(target=counter, args=(2500,))
#     f = Process(target=counter, args=(2500,))
#     g = Process(target=counter, args=(2500,))
#     h = Process(target=counter, args=(2500,))
#     I = Process(target=counter, args=(2500,))
#     j = Process(target=counter, args=(2500,))
#     k = Process(target=counter, args=(2500,))
#     l = Process(target=counter, args=(2500,))
#     m = Process(target=counter, args=(2500,))
#     n = Process(target=counter, args=(2500,))
#     o = Process(target=counter, args=(2500,))
#     p = Process(target=counter, args=(2500,))
#
#     b.start()
#     a.start()
#     c.start()
#     d.start()
#     e.start()
#     f.start()
#     g.start()
#     h.start()
#     I.start()
#     j.start()
#     k.start()
#     l.start()
#     m.start()
#     n.start()
#     o.start()
#     p.start()
#
#     a.join()
#     b.join()
#     c.join()
#     d.join()
#     e.join()
#     f.join()
#     g.join()
#     h.join()
#     I.join()
#     j.join()
#     k.join()
#     l.join()
#     m.join()
#     n.join()
#     o.join()
#     p.join()
#
#     print("finished in:" ,time.perf_counter(),"seconds")
#
#
# if __name__ == "__main__":
#     main
# from tkinter import *
#
# window = Tk()
#
# label = Label(window,text="Hello",background="magenta", fg="yellow", font=("Ariel",40), )
# label.place(x= 275,y= 275)
# window.geometry("600x600")
# window.title("Akin's Place")
# window.config(background="magenta")
#
# window.mainloop()

# from tkinter import *
#
# count = 0
# def click():
#     global count
#     count += 1
#     print(count)
# window = Tk()
#
# button = Button(window,text="Hello hi wisconsin",command=click, font=("Comic Sans", 30), background= "grey", foreground="black",
#                 activebackground="grey", activeforeground="white")
# button.pack()
#
# window.mainloop()





# from tkinter import *
# window = Tk()
#
# def submit():
#     username = entry.get()
#     print("hello my man " + username)
#
# def delete():
#     entry.delete(0,END)
#
# def backspace():
#     entry.delete(len(entry.get())-1 ,END)
# entry = Entry(window, font=("Arial", 30), bg="black", fg="light green")
#
# submit_button = Button(window,text="Submit", command=submit)
# submit_button.pack(side=(RIGHT))
#
# delete_button = Button(window,text="Delete", command=delete)
# delete_button.pack(side=(RIGHT))
#
# backspace_button = Button(window,text="Backspace", command=backspace)
# backspace_button.pack(side=(RIGHT))
#
# entry.pack(side=(LEFT))
#
# window.mainloop()







# from tkinter import *
#
# window = Tk()
#
#
# def display():
#     if(x.get() == 1):
#         print("You have agreed to be a man of the griffis ^^")
#     else:
#         print("If you are not an ally then you must be our enemy!")
# x= IntVar()
# check_button = Checkbutton(window,text="I agree that I indeed am a man of Griffith ,The White Hawk,", variable=x, onvalue=1,offvalue=0,command=display)
# check_button.pack()
#
# window.mainloop()
#
# from tkinter import *
#
# food = ["pizza", "sushi", "your mama"]
# window = Tk()
#
# x = IntVar()
# for index in range(len(food)):
#     radiobutton = Radiobutton(window,text=food[index], variable=x, value=index, padx= 25, pady= 30, font=("Comic Sans", 20))
#     radiobutton.pack(anchor=W)
#
#
# window.mainloop()







# from tkinter import *
#
# window = Tk()
#
# def submit():
#     print("The temperature is " + str(scale.get()) + "degrees C")
#     temp = scale.get()
#     if (temp == 0):
#         print("Water has frozen and now it is ice")
#     elif (temp == 100):
#         print("Water has boiled and now it is water steam")
# scale = Scale(window,from_=100,to=0, length=600, width=15, tickinterval= 10 , troughcolor="light blue", fg= "#FF1C00", bg="grey", font=("Ariel", 15))
# scale.pack()
#
# button = Button(window,text="Submit", command=submit)
# button.pack()
#
#
# window.mainloop()
# from tkinter import *
#
# window = Tk()
# entryBox = Entry(window)
# entryBox.pack()
#
# def submit():
#     print("You have ordered " + listbox.get(listbox.curselection())+ ", my dear friend")
#
# def add():
#     if (entryBox.get() == ""):
#         print("please choose what you will add")
#     else:
#         listbox.insert(listbox.size(),entryBox.get())
#         listbox.config(height=listbox.size())
#
# def delete():
#     listbox.delete(listbox.curselection())
#     listbox.config(height=listbox.size())
#
#
#
#
# listbox = Listbox(window,bg="#f7ffde", font=("Constantia", 35), width=15, selectmode=MULTIPLE)
# listbox.pack()
#
# listbox.insert(1,"Pasta")
# listbox.insert(2,"Sushi")
# listbox.insert(3,"Steak")
# listbox.insert(4,"Salad")
# listbox.insert(5,"Soup")
#
# listbox.config(height=listbox.size())
#
# submitButton = Button(window,text="Submit",command=submit)
# submitButton.pack()
#
# addButton = Button(window,text="Add",command=add)
# addButton.pack()
#
# deleteButton = Button(window, text="Delete", command=delete)
# deleteButton.pack()
#
#
# window.mainloop()




# from tkinter import *
#
# window = Tk()
# entryBox = Entry(window)
# entryBox.pack()
#
# def submit():
#     food = []
#
#     for index in listbox.curselection():
#         food.insert(index,listbox.get(index))
#     print("You have ordered: ")
#     for index in food:
#         print(index)
# def add():
#     if (entryBox.get() == ""):
#         print("please choose what you will add")
#     else:
#         listbox.insert(listbox.size(),entryBox.get())
#         listbox.config(height=listbox.size())
#
# def delete():
#     for index in reversed(listbox.curselection()):
#         listbox.delete(index)
#
#
#
#
# listbox = Listbox(window,bg="#f7ffde", font=("Constantia", 35), width=15, selectmode=MULTIPLE)
# listbox.pack()
#
# listbox.insert(1,"Pasta")
# listbox.insert(2,"Sushi")
# listbox.insert(3,"Steak")
# listbox.insert(4,"Salad")
# listbox.insert(5,"Soup")
#
# listbox.config(height=listbox.size())
#
# submitButton = Button(window,text="Submit",command=submit)
# submitButton.pack()
#
# addButton = Button(window,text="Add",command=add)
# addButton.pack()
#
# deleteButton = Button(window, text="Delete", command=delete)
# deleteButton.pack()
#
#
# window.mainloop()

# from tkinter import *
# from tkinter import messagebox
#
#
# def click():
#     if messagebox.askokcancel(title="Is this ok?",message="How about the thing?"):
#         print(messagebox.showinfo(message="You did it YEY :)"))
#     else:
#         print(messagebox.showinfo(message="You didn't do it why? :("))
#
# window = Tk()
#
# button = Button(window,command=click, text="click me")
# button.pack()
#
# window.mainloop()

#from tkinter import *
#from tkinter import messagebox

# if messagebox.askyesno(title="Evet mi hayır mı?",message="Guts'a berserker armoru veren kişi casca mıdır?"):
#     print(messagebox.showinfo(message="Yanlış bildiniz."))
# else:
#     print(messagebox.showinfo(message="Doğru cevap!"))





# from tkinter import *
# from tkinter import colorchooser
#
# window = Tk()
#
# def click():
#     color = colorchooser.askcolor()
#     colorhex = color[1]
#     window.config(bg=colorhex)
#     print(color)
# window.geometry("600x600")
# button = Button(text="click me!", command=click)
# button.pack()
#
#
# window.mainloop()


# from tkinter import *
#
# window = Tk()
#
#
# def submit():
#     textp = text.get("1.0", END)
#     print(textp)
# text = Text(window,bg="light yellow", font=("Ink free", 25),height=8,width=20)
# text.pack()
# button = Button(window,text= "click me!",command= submit, font=("Comic Sans", 25))
# button.pack()
# window.mainloop()

# from tkinter import *
# from tkinter import filedialog
#
# window = Tk()
#
# def openFile():
#     filepath = filedialog.askopenfilename()
#     file = open(filepath,"r")
#     print(file.read())
# button = Button(text="Open", command=openFile)
# button.pack()
# window.mainloop()

# from tkinter import *
# from tkinter import filedialog
#
# def savefile():
#     file = filedialog.asksaveasfile(defaultextension=".txt",filetypes=[("Text file", ".txt"),
#                                                                        ("HTML file", ".html"),
#                                                                        ("All files", ".*")])
#     fileinfo = text.get("1.0", END)
#     file.write(fileinfo)
#     file.close()
#
# window = Tk()
# button = Button(text="Save File", font=("Comic Sans", 20),command=savefile)
# button.pack()
# text = Text(window)
# text.pack()
#
#
# window.mainloop()

# from tkinter import *
#
# window = Tk()
#
# menubar = Menu(window)
# window.config(menu=menubar)
#
# def openfile():
#     print("File has been opened")
# def save():
#     print("File has been saved")
#
# filemenu = Menu(menubar,tearoff=False)
# menubar.add_cascade(label="File", menu=filemenu)
# filemenu.add_command(label="Open Files",command=openfile())
# filemenu.add_command(label="Save Files", command=save)
# filemenu.add_separator()
# filemenu.add_command(label="Exit", command=quit)


# window.mainloop()

# from tkinter import *
# from tkinter import ttk
#
# window = Tk()
#
# notebook = ttk.Notebook(window)
#
# tab1 = Frame(notebook)
# tab2 = Frame(notebook)
#
# notebook.add(tab1,text="Tab 1")
# notebook.add(tab2, text="Tab 2")
# notebook.pack(expand=True, fill="both")
#
# Label(tab1, text="Hello, this is tab1", width=50, height=25).pack()
# Label(tab2, text="Goodbye, this is tab2", width=50, height=25).pack()
#
# window.mainloop()

# from tkinter import *
# from tkinter.ttk import *
# import time
#
# window = Tk()
#
# percent = StringVar()
#
# def submit():
#     tasks = 10
#     x = 0
#     while (x<tasks):
#         time.sleep(1)
#         bar["value"]+=10
#         x+=1
#         percent.set(str(int((x/tasks)*100))+"%")
#         window.update_idletasks()
#
# bar =Progressbar(window,orient=VERTICAL, length=600)
# bar.pack()
#
# percentlabel = Label(window, textvariable=percent).pack()
# button = Button(window,text="download", command=submit).pack()
#
#
# window.mainloop()

# from tkinter import *
#
#
# def drag_start(event):
#     label.startX = event.x
#     label.startY = event.y
# def drag_motion(event):
#     x = label.winfo_x() - label.startX + event.x
#     y = label.winfo_y() - label.startY + event.y
#     label.place(x=x,y=y)
# window = Tk()
#
# label = Label(window,bg="red",width=10,height=5)
# label.place(x=0,y=0)
# label.bind("<Button-1>",drag_start)
# label.bind("<B1-Motion>",drag_motion)
#
# window.mainloop()

# import numpy as np
#
# a = np.array([[1,2,3,4,5,6,7],[8,9,10,11,12,13,14]])
# print(a[0, 1:6:1])

# def printHello():
#     print("hello")
#
# a = printHello()

import numpy as np
shopping_list = [2, "Banana", 2, "Tomatoes"]
shopping_list = np.array(shopping_list)
print(shopping_list)