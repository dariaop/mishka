import tkinter as tk
import random

window = tk.Tk()
hp4 = 200
hp5 = 200
point = 0

def close(a, b, c, d, i, f):
    a['state'] = tk.DISABLED
    b['state'] = tk.DISABLED
    c['state'] = tk.DISABLED
    d['state'] = tk.DISABLED
    i['state'] = tk.DISABLED
    f['state'] = tk.DISABLED
def peremens(name, x):
    f = open(name, "r")
    x = f.readline()
    f.close()
    return x

def createNewWindow():
    w1 = tk.Toplevel(window)
    w1.title("Создать персонажа")
    w1.geometry('900x600')
    w1.config(bg="#8FBC8F")
    lbl = tk.Label(w1, text="Создайте своего персонажа",bg="#8FBC8F", font=("Arial Bold", 25))
    lbl.grid(row=0, column=0)
    # фио
    fiot = tk.Label(w1, text="ФИО", bg="#8FBC8F", font=("Arial Bold", 15))
    fiot.grid(row=1, column=0)
    fio = tk.Entry(w1, width=30)
    fio.grid(row=1, column=1)
    # пол
    pol = tk.Label(w1, text="ПОЛ", bg="#8FBC8F", font=("Arial Bold", 15))
    pol.grid(row=2, column=0)
    pol1 = tk.Entry(w1, width=30)
    pol1.grid(row=2, column=1)
    # рост
    rost = tk.Label(w1, text="РОСТ" ,bg="#8FBC8F", font=("Arial Bold", 15))
    rost.grid(row=3, column=0)
    ros = tk.Entry(w1, width=30)
    ros.grid(row=3, column=1)
    # вес
    p = tk.Label(w1, text="ВЕС", bg="#8FBC8F", font=("Arial Bold", 15))
    p.grid(row=4, column=0)
    p1 = tk.Entry(w1, width=30)
    p1.grid(row=4, column=1)

    def getInput():
        a =fio.get()
        b =pol1.get()
        c = int(ros.get())
        d1 = p1.get()
        d = int(p1.get())
        hp3 = (d/((c**2)/1000))*100
        if b == "m":
            hp3 +=30


        global fios
        fios = a
        f = open("fios.txt", "w")
        f.write(str(fios))
        f.close()
        global c1
        c1 = str(c)
        f = open("rost.txt", "w")
        f.write(c1)
        f.close()
        global ves
        ves = str(d)
        f = open("ves.txt", "w")
        f.write(ves)
        f.close()
        global hp31
        hp31 = str(hp3)
        f = open("hp.txt", "w")
        f.write(hp31)
        f.close()
    b1 = tk.Button(w1,text="Создать", bg="Crimson", width=20, height=1, font=(100), command=getInput)
    b1.grid(row=5, column=3)
    b2 = tk.Button(w1, text="Начать игру", bg="Crimson", width=20, height=1, font=(100), command=createNewWindow2)
    b2.grid(row=6, column=3)

def createNewWindow1():

    def clicked():
        global hp3
        global hp4
        if hp3 >=h and hp4 >=h:
            a = 1
            b = random.randint(1, 3)
            if a != b:
                hp3 = hp3 - h
            else:
                hp3 = hp3 - ((h * 30) // 100)
            c.set(hp3)
        elif hp3 < h:
            c.set("Ты проиграл")
            global mhp
            f = open("hp.txt", "r")
            a = f.readline()
            mhp = int(float(a))
            hp3 = mhp
            print(mhp)
            f.close()
            global hp5
            hp4 = hp5
            close(g1, g2, t1, t2, n1,n2)

            global point
            point = point + 1
            f = open("point.txt", "w")
            f.write(str(point))
            f.close()

            ex1 = tk.Button(w3,text="Выход", bg="Crimson", width=20, height=1, font=(100), command=w3.destroy)
            ex1.grid(row=6, column=2)
        elif hp4 < h:
            d.set("Ты выиграл")
            point = point + 5
            f = open("point.txt", "w")
            f.write(str(point))
            f.close()
            ex1 = tk.Button(w3, text="Выход", bg="Crimson", width=20, height=1, font=(100), command=w3.destroy)
            ex1.grid(row=6, column=2)
            f = open("hp.txt", "r")
            a = f.readline()
            mhp = int(float(a))
            hp3 = mhp
            print(mhp)
            f.close()
            hp4 = hp5
            close(g1, g2, t1, t2, n1, n2)

    def clicked1():
        global hp3
        global hp4
        a = 2
        b = random.randint(1, 3)
        if hp3 >= h and hp4 >= h:
            if a != b:
                hp3 = hp3 - h
            else:
                hp3 = hp3 - ((h * 30) // 100)
            c.set(hp3)
        elif hp3 < h:
            c.set("Ты проиграл")
            global point
            point = point + 1
            f = open("point.txt", "w")
            f.write(str(point))
            f.close()
            ex1 = tk.Button(w3, text="Выход", bg="Crimson", width=20, height=1, font=(100), command=w3.destroy)
            ex1.grid(row=6, column=2)
            global mhp
            f = open("hp.txt", "r")
            a = f.readline()
            mhp = int(float(a))
            hp3 = mhp
            print(mhp)
            f.close()
            hp4 = hp5
            close(g1, g2, t1, t2, n1, n2)
        elif hp4 < h:
            d.set("Ты выиграл")

            point = point + 5
            f = open("point.txt", "w")
            f.write(str(point))
            f.close()
            ex1 = tk.Button(w3, text="Выход", bg="Crimson", width=20, height=1, font=(100), command=w3.destroy)
            ex1.grid(row=6, column=2)
            f = open("hp.txt", "r")
            a = f.readline()
            mhp = int(float(a))
            hp3 = mhp
            print(mhp)
            f.close()
            hp4 = hp5
            close(g1, g2, t1, t2, n1, n2)

    def clicked2():
        global hp3
        global hp4
        a = 3
        b = random.randint(1, 3)
        if hp3 >= h and hp4 >= h:
            if a != b:
                hp3 = hp3 - h
            else:
                hp3 = hp3 - ((h * 30) // 100)
            c.set(hp3)
        elif hp3 < h:
            c.set("Ты проиграл")

            global point
            point = point + 1
            f = open("point.txt", "w")
            f.write(str(point))
            f.close()
            ex1 = tk.Button(w3, text="Выход", bg="Crimson", width=20, height=1, font=(100), command=w3.destroy)
            ex1.grid(row=6, column=2)
            hp4 = hp5
            global mhp
            f = open("hp.txt", "r")
            a = f.readline()
            mhp = int(float(a))
            hp3 = mhp
            print(mhp)
            f.close()
            close(g1, g2, t1, t2, n1, n2)
        elif hp4 < h:
            d.set("Ты выиграл")

            point = point + 5
            f = open("point.txt", "w")
            f.write(str(point))
            f.close()
            ex1 = tk.Button(w3, text="Выход", bg="Crimson", width=20, height=1, font=(100), command=w3.destroy)
            ex1.grid(row=6, column=2)
            f = open("hp.txt", "r")
            a = f.readline()
            mhp = int(float(a))
            hp3 = mhp
            print(mhp)
            f.close()
            hp4 = hp5
            close(g1, g2, t1, t2, n1, n2)

    def clicked3():
        global hp4
        global hp3
        a = 1
        b = random.randint(1, 3)
        if hp3 >= h and hp4 >= h:
            if a != b:
                hp4 = hp4 - h
            else:
                hp4 = hp4 - ((h * 30) // 100)
            d.set(hp4)
        elif hp3 < h:
            c.set("Ты проиграл")

            global point
            point = point + 1
            f = open("point.txt", "w")
            f.write(str(point))
            f.close()
            ex1 = tk.Button(w3, text="Выход", bg="Crimson", width=20, height=1, font=(100), command=w3.destroy)
            ex1.grid(row=6, column=2)
            global mhp
            f = open("hp.txt", "r")
            a = f.readline()
            mhp = int(float(a))
            hp3 = mhp
            print(mhp)
            f.close()
            global hp5
            hp4 = hp5
            close(g1, g2, t1, t2, n1, n2)
        elif hp4 < h:
            d.set("Ты выиграл")

            point = point + 5
            f = open("point.txt", "w")
            f.write(str(point))
            f.close()
            ex1 = tk.Button(w3, text="Выход", bg="Crimson", width=20, height=1, font=(100), command=w3.destroy)
            ex1.grid(row=6, column=2)
            f = open("hp.txt", "r")
            a = f.readline()
            mhp = int(float(a))
            hp3 = mhp
            print(mhp)
            f.close()
            hp4 = hp5
            close(g1, g2, t1, t2, n1, n2)

    def clicked4():
        global hp4
        global hp3
        a = 1
        b = random.randint(1, 3)
        if hp3 >= h and hp4 >= h:
            if a != b:
                hp4 = hp4 - h
            else:
                hp4 = hp4 - ((h * 30) // 100)
            d.set(hp4)
        elif hp3 < h:
            c.set("Ты проиграл")

            global point
            point = point + 1
            f = open("point.txt", "w")
            f.write(str(point))
            f.close()
            ex1 = tk.Button(w3, text="Выход", bg="Crimson", width=20, height=1, font=(100), command=w3.destroy)
            ex1.grid(row=6, column=2)
            global mhp
            f = open("hp.txt", "r")
            a = f.readline()
            mhp = int(float(a))
            hp3 = mhp
            print(mhp)
            f.close()
            global hp5
            hp4 = hp5
            close(g1, g2, t1, t2, n1, n2)
        elif hp4 < h:
            d.set("Ты выиграл")

            point = point + 5
            f = open("point.txt", "w")
            f.write(str(point))
            f.close()
            ex1 = tk.Button(w3, text="Выход", bg="Crimson", width=20, height=1, font=(100), command=w3.destroy)
            ex1.grid(row=6, column=2)
            f = open("hp.txt", "r")
            a = f.readline()
            mhp = int(float(a))
            hp3 = mhp
            print(mhp)
            f.close()
            hp4 = hp5
            close(g1, g2, t1, t2, n1, n2)

    def clicked5():
        global hp4
        global hp3
        a = 1
        b = random.randint(1, 3)
        if hp3 >= h and hp4 >= h:
            if a != b:
                hp4 = hp4 - h
            else:
                hp4 = hp4 - ((h * 30) // 100)
            d.set(hp4)
        elif hp3 < h:
            c.set("Ты проиграл")

            global point
            point = point + 1
            f = open("point.txt", "w")
            f.write(str(point))
            f.close()
            ex1 = tk.Button(w3, text="Выход", bg="Crimson", width=20, height=1, font=(100), command=w3.destroy)
            ex1.grid(row=6, column=2)
            global mhp
            f = open("hp.txt", "r")
            a = f.readline()
            mhp = int(float(a))
            hp3 = mhp
            print(mhp)
            f.close()
            global hp5
            hp4 = hp5
            close(g1, g2, t1, t2, n1, n2)
        elif hp4 < h:
            d.set("Ты выиграл")

            point = point + 5
            f = open("point.txt", "w")
            f.write(str(point))
            f.close()
            ex1 = tk.Button(w3, text="Выход", bg="Crimson", width=20, height=1, font=(100), command=w3.destroy)
            ex1.grid(row=6, column=2)
            f = open("hp.txt", "r")
            a = f.readline()
            mhp = int(float(a))
            hp3 = mhp
            print(mhp)
            f.close()
            hp4 = hp5
            close(g1, g2, t1, t2, n1, n2)

    w3 = tk.Toplevel(window)
    w3.geometry('900x600')
    w3.title("PlayFight")
    w3.config(bg="#8FBC8F")
    c = tk.StringVar()
    d = tk.StringVar()
    c.set(hp3)
    d.set(hp4)

    nm1 = tk.Label(w3, text="PlayFight",bg="#8FBC8F", font=("Arial Bold", 80))
    nm1.grid(row=0, column=1)
    hp1 = tk.Label(w3, textvariable=c,bg="#8FBC8F", font=("Arial Bold", 50))
    hp1.grid(row=1, column=1)
    hp2 = tk.Label(w3, textvariable=d,bg="#8FBC8F", font=("Arial Bold", 50))
    hp2.grid(row=1, column=2)

    at = tk.Label(w3, text="Защита",bg="#8FBC8F", font=("Arial Bold", 40))
    at.grid(row=2, column=1)

    g1 = tk.Button(w3, text="Голова", width=30,bg="Crimson", height=1, command=clicked)
    g1.grid(row=3, column=1)

    t1 = tk.Button(w3, text="Тело", width=30,bg="Crimson", height=1, command=clicked1)
    t1.grid(row=4, column=1)

    n1 = tk.Button(w3, text="Ноги", width=30,bg="Crimson", height=1, command=clicked2)
    n1.grid(row=5, column=1)

    za = tk.Label(w3, text="Атака",bg="#8FBC8F", font=("Arial Bold", 40))
    za.grid(row=2, column=2)

    g2 = tk.Button(w3, text="Голова", width=30,bg="Crimson", height=1, command=clicked3)
    g2.grid(row=3, column=2)

    t2 = tk.Button(w3, text="Тело", width=30,bg="Crimson", height=1, command=clicked4)
    t2.grid(row=4, column=2)

    n2 = tk.Button(w3, text="Ноги", width=30,bg="Crimson", height=1, command=clicked5)
    n2.grid(row=5, column=2)

def createNewWindow3():

    def bust1():
        global point
        if point >= 5:
            global h
            h+=5
            c.set(h)
            point-=5
            f = open("ves.txt", "w")
            f.write(str(h))
            f.close()

    def bust2():
        global point
        if point >= 5:
            global hp3
            hp3+=5
            hp3= float(hp3)
            d.set(hp3)
            point-=5
            f = open("hp.txt", "w")
            f.write(str(hp3))
            f.close()


    w4 = tk.Toplevel(window)
    w4.geometry('900x600')
    w4.title("PlayFight")
    w4.config(bg="#8FBC8F")
    global h
    peremens("ves.txt",h)
    k =tk.StringVar()
    k.set(point)
    c = tk.StringVar()
    c.set(h)
    global hp3
    d = tk.StringVar()
    d.set(hp3)
    nm = tk.Label(w4, text="Тренировка", bg="#8FBC8F", font=("Arial Bold", 60))
    nm.grid(row=0, column=1)
    points1 = tk.Label(w4, text="point:", bg="#8FBC8F", font=("Arial Bold", 40))
    points1.grid(row=1, column=2)
    points = tk.Label(w4, textvariable=k, bg="#8FBC8F", font=("Arial Bold", 40))
    points.grid(row=1, column=3)
    ex= tk.Button(w4,text="<-", width=5, height=5,  bg="Crimson", command=w4.destroy)
    ex.grid(row=0, column=0)
    sila = tk.Label(w4, text="сила", bg="#8FBC8F", font=("Arial Bold", 30))
    sila.grid(row=2, column=0)
    colvo1 = tk.Label(w4, textvariable=c, bg="#8FBC8F", font=("Arial Bold", 30))
    colvo1.grid(row=3, column=0, sticky= "e")
    sil = tk.Button(w4, text="трен.", width=30, height=1, bg="Crimson", command= bust1)
    sil.grid(row=3, column=1,sticky= "w")

    zdor = tk.Label(w4, text="здоровье", bg="#8FBC8F", font=("Arial Bold", 30))
    zdor.grid(row=4, column=0)
    colvo2 = tk.Label(w4, textvariable=d, bg="#8FBC8F", font=("Arial Bold", 30))
    colvo2.grid(row=5, column=0, sticky= "e")
    zd = tk.Button(w4, text="трен.", width=30, height=1, bg="Crimson", command= bust2)
    zd.grid(row=5, column=1, sticky= "w")

    '''sila = tk.Label(w4, text="сила", bg="#8FBC8F", font=("Arial Bold", 40))
    sila.grid(row=2, column=0)
    colvo1 = tk.Label(w4, textvariable=c, bg="#8FBC8F", font=("Arial Bold", 40))
    colvo1.grid(row=3, column=0)
    sil = tk.Button(w4, text="трен.", width=30, height=1, bg="Crimson")
    sil.grid(row=3, column=1)'''


def createNewWindow2():
    global fio
    f = open("fios.txt", "r")
    fio = f.readline()
    f.close()
    #print(fio)
    global hp3
    f = open("hp.txt", "r")
    hp = f.readline()
    hp3 = int(float(hp) // 1)
    f.close()
    #print(hp3)
    global rost
    f = open("rost.txt", "r")
    rost1 = f.readline()
    rost = int(rost1)
    f.close()
    #print(rost)
    global h
    f = open("ves.txt", "r")
    h1 = f.readline()
    h = int(h1)
    f.close()
    #print(h)

    w2 = tk.Toplevel(window)
    w2.geometry('900x600')
    w2.title("PlayFight")
    w2.config(bg="#8FBC8F")
    nm = tk.Label(w2,text="PlayFight", bg="#8FBC8F", font=("Arial Bold", 80))
    nm.grid(row=0, column=0)

    bi = tk.Button(w2,text="Быстрый матч", bg="Crimson", width=30, height=1, font=(100), command=createNewWindow1)
    bi.grid(row=1, column=0)

    kar= tk.Button(w2,text="Карьера", width=30, bg="Crimson", height=1, font=(100))
    kar.grid(row=2, column=0)

    tr = tk.Button(w2,text="Тренировка", width=30, bg="Crimson", height=1, font=(100), command = createNewWindow3)
    tr.grid(row=3, column=0)

    ex1 = tk.Button(w2,text="Выйти", font=(100), bg="Crimson", command=window.quit)
    ex1.grid(row=4, column=0)
    '''tablo= tk.Label(w2,text="ФИО: \nПОЛ: \nСИЛА: \nЗДОРОВЬЕ: \nИНТЕЛЛЕКТ:", font=("Arial Bold", 15))
    tablo.grid(row=1, column=1)'''


window.geometry('900x600')
window.title("PlayFight")
window.config(bg="#8FBC8F")
label = tk.Label(text="PlayFight", fg="Black", bg="#8FBC8F", font=("Arial Bold", 80))
label.pack()
# создать персонаж
begin = tk.Button(text="Создать персонажа", width=30, bg="Crimson", height=1, font=(100), command=createNewWindow)
begin.pack()
# загрузить
safe = tk.Button(text="Загрузить персонажа", bg="Crimson", width=30, height=1, font=(100), command=createNewWindow2)
safe.pack()
# выход
ex = tk.Button(text="Выйти", font=(100), bg="Crimson", command=window.quit)
ex.pack()

window.mainloop()