from tkinter.ttk import Scrollbar 
import platform
from numpy.polynomial import Polynomial as P
from tkinter import Frame, Label, Message, StringVar, Canvas
from numpy import polynomial
import numpy as np
import math
from math import *
import matplotlib
matplotlib.use("TkAgg")
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg, NavigationToolbar2TkAgg
import matplotlib.pyplot as plt
from numpy import linspace,sin,shape
from pandas import DataFrame
import numexpr as ne
import matplotlib

from scipy.interpolate import interp1d
from tkinter import *
from tkinter import ttk
import tkinter as tk
from matplotlib.figure import Figure
from tkinter.constants import *
import json
import pygame

pygame.init()
crash_sound = pygame.mixer.Sound("bgm.wav")


LARGE_FONT = ("Verdana", 12)

s1 = ""
s2 = ''
imp = []
n = 0
expr_trap = ""
h = 0
pontos = []
f_pontos = []
trapezio = 0
polino = ""
pn = ""
raiz = ""
def set_strings(): # ainda n sei como vo usar mas ta aew
    global s1
    global s2
    s1 = e1.get()
    s2 = e2.get()


def janelinha(title="Entrada",title2="Input"): # janelhina generica, uso: sei la bixo
    master = Tk()
    Label(master, text=title).grid(row=0)
    Label(master, text=title2).grid(row=1)

    e1 = Entry(master)
    e2 = Entry(master)

    e1.grid(row=0, column=1)
    e2.grid(row=1, column=1)

    Button(master, text='Fechar', command=master.quit).grid(
        row=3, column=0, sticky=W, pady=4)
    Button(master, text='OK', command=set_strings).grid(
        row=3, column=1, sticky=W, pady=4)

    s = e1.get()
    mainloop()

# def plot():
#     # TODO aqui ele plota com os treco da global var


class trap_show(tk.Frame):  # mostra o resulta pra trape
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        global pontos
        global f_pontos
        global trapezio
        label = tk.Label(self, text="Pontos \t F(x)", font=LARGE_FONT)
        label.pack(pady=10, padx=10)

        label_t = tk.Label(self, text="Valor do Trapezio: {}".format(trapezio), font=LARGE_FONT)
        label_t.pack(pady=10, padx=10)



# def popup():
#     popup = tk.Tk()
#     popup.wm_title(trapezio)
#     e1 = Entry(popup)
#     e1.pack()
#     label1 = Label(popup, Text="TEst", font=("Verdana", 12))
#     # label1.pack(side="top", fill="x", pady=10)
#     but = ttk.Button(popup, Text="Kill", command=popup.destroy)
#     but.pack()

# def janelinha_trape(): # backend do frontend do backend
#     master = Tk()
#     Label(master, text="Insira os valores de A e B separados").grid(row=0)
#     Label(master, text='Numero de pontos tabelados').grid(row=1)
#     Label(master, text='Informe a funcao em python').grid(row=2)

#     e1 = Entry(master)
#     e2 = Entry(master)
#     e3 = Entry(master)

#     e1.grid(row=0, column=1)
#     e2.grid(row=1, column=1)
#     e3.grid(row=2, column=1)

#     Button(master, text='Fechar', command=master.quit).grid( # fecha
#         row=3, column=0, sticky=W, pady=4)
#     Button(master, text='CALC', command=trapezio_info).grid( # calcula
#         row=3, column=1, sticky=W, pady=4)
#     Button(master, text='REVELA O PODER', command=trap_show).grid( # mostra
#         row=3, column=2, sticky=W, pady=4)

#     s = e1.get()
#     mainloop()


class janelinha_trape(tk.Frame):  # backend do frontend do backend

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        m = self
        # master = 
        label_ab = tk.Label(self, text="Insira os valores de A e B separados")
        label_ab.pack(pady=10, padx=10)

        label_n = tk.Label(
            self, text='Numero de pontos tabelados')
        label_n.pack(pady=11, padx=11)
        label_f = tk.Label(
            self, text='Informe a funcao em python')
        label_f.pack(pady=12, padx=12)        
        master = Tk()
        # print(type(self))
        e1 = Entry(master)
        e1.pack()
        e2 = ttk.Entry(master)
        e2.pack()
        e3 = ttk.Entry(master)
        e3.pack()

        e1.grid(row=0, column=1)
        e2.grid(row=1, column=1)
        e3.grid(row=2, column=1)
        
        def trapezio_info():  # isso seta os var pro trape
            nonlocal self
            global imp
            global n
            global expr_trap
            global h
            global pontos
            global trapezio

            imp = e1.get().split()
            n = int(e2.get())
            expr_trap = e3.get()
            print(imp)
            print(n)
            print(expr_trap)
            trapezio = trapy()
            data = {}
            with open('data.txt') as fp:
                data = json.load(fp)
            ip = 0

            popup = tk.Tk()
            popup.wm_title(trapezio)
            label1 = ttk.Label(popup, Text=str(trapezio), font=("Verdana", 12))
            label1.pack(side="top", fill="x", pady=10)
            but = ttk.Button(popup, Text="Kill", command=popup.destroy)
            but.pack()
            # tk.Label(self, Text="TRAPEZIO: {}".format(trapezio)).pack()
            # for key in data.keys:
            #     if key != "valor":
            #         pass
            #     else:
            #         for ponto in data['Xi']:
            #             tk.Label(self, Text="x: {} \t f(x): {}".format(ponto, data['F(Xi)'][ip]))
            #             ip += 1
            


        button1 = ttk.Button(self, text="Hommie",
                             command=lambda: controller.show_frame(StartPage))
        button1.pack()
        
        button2 = ttk.Button(self, text="CALCULAR",
                             command=trapezio_info)
        button2.pack()

        button3 = ttk.Button(self, text="Mostrar",
                             command=lambda: controller.show_frame(trap_show))
        button3.pack()
        # Button(master, text='CALC', command=trapezio_info).grid(  # calcula
        #     row=3, column=1, sticky=W, pady=4)
        # Button(master, text='REVELA O PODER', command=trap_show).grid(  # mostra
        #     row=3, column=2, sticky=W, pady=4)

def trapy():
    global h
    global imp
    with open('data.txt', 'w') as fp:
        fp.write("")
    # inp = input("Informe o A e o B da integração\n").split()
    # janelinha_trape("Informe o A e o B da integração",
    #                 "Numero de Pontos tabelados", " Informe o função f(x) para ser integrada")
    ab = [float(x) for x in imp]
    # n = int(input("Numero de Pontos tabelados \n"))
    h = round((ab[1] - ab[0])/(n-1), 1)
    print("h=(b-a)/n-1")
    print("{} = ({}-{})/{}-1".format("h", ab[1], ab[0], n))
    global pontos
    for i in range(n):
        if i == 0:
            pontos.append(ab[0])
        elif i == (n-1):
            pontos.append(ab[1])
        else:
            pontos.append(pontos[i-1]+h)
    pontos = [round(ponto, 1) for ponto in pontos]
    print("Espaçamento: {} \nPontos: {}".format(h, pontos))
    # print(" Informe o função f(x) para ser integrada \n")
    # expr_trap = input()
    global f_pontos
    
    for x in range(len(pontos)):
        t = x
        x = pontos[x]
        print(i, end=" ")
        f_pontos.append(eval(expr_trap))
        print(f_pontos[t])
        x = t
    f_pontos = [round(ponto, 7) for ponto in f_pontos]
    P = []
    I = []
    print(n)
    for i in range(n):
        if(i % 2 == 0 and i != 0 and f_pontos[i] != f_pontos[-1]):
            print
            P.append(f_pontos[i])
        elif (f_pontos[i] != f_pontos[-1] and i % 2 != 0):
            I.append(f_pontos[i])
    E = (f_pontos[0] + f_pontos[-1])
    p, i = np.sum(P), np.sum(I)
    print("trapezio= h[E/2 + P + I]")
    print("{}[{}/2 + {} + {}]".format(h, E, p, i))
    global trapezio
    trapezio = h*(E/2 + p + i)
    # trap = np.trapz(f_pontos, x=pontos, dx=h)
    lis = []
    lis_f = []
    for ponto in pontos:
        lis.append(ponto)
        lis_f.append(f_pontos[pontos.index(ponto)])
    data = {"Xi": lis, "F(Xi)": lis_f}
    data["valor"] = trapezio
    with open('data.txt', 'a') as fp:
        json.dump(data, fp)
    df = DataFrame(data=data)
    # plt.scatter(data["Xi"], data['F(xi)'])
    plt.show()
    ax = df.plot.bar(x="Xi", y="F(Xi)", rot=ab[0])
    print("trapezio manual: {} ".format(trapezio))
    return trapezio


def newtao():
    # Definindo inpu
    pontos = []  # lista dos ponto
    k = 0
    while True:
        k += 1
        while True:
            print("informe X e f(x) pro ", k, "º ponto")
            l = input()
            if not l:  # termina quando n bota nd
                break
            l = l.split()  # casta pruma lista
            if len(l) == 2:
                break
            else:
                print("Deu ruim")
        if not l:
            break
        for i in range(len(l)):  # formata pra pontos
            l[i] = float(l[i])
        pontos.append(l)

    l = []
    for i in range(len(pontos)):
        l.append(pontos[i][1])
    tabela = []  # tabelas pra dif div
    tabela.append(l)
    # fax os calculo do tipo f(x1, x2, x3)
    for i in range(len(pontos) - 1):
        l = []
        for j in range(len(pontos) - i - 1):
            dif = (tabela[i][j + 1] - tabela[i][j]) / \
                (pontos[j + 1 + i][0] - pontos[j][0])
            l.append(dif)
        tabela.append(l)
    difdiv = []
    for i in range(len(tabela)):
        difdiv.append(tabela[i][0])

    # somas os treco
    suma = 0
    for i in range(1, len(pontos)):
        produt = 1
        for k in range(i):  # produto
            # tava no livro c calculo, eh vdd isso
            produt *= (P([-pontos[k][0], 1]))
        suma += difdiv[i] * produt
    Pn = difdiv[0] + suma
    funcao = list(Pn)  # casta pra lista, mas sem racismo
    # po man, isso de deixa le os breguete numa boa
    texto = ""
    for i in range(len(funcao)):
        if funcao[i] == 0:
            continue
        elif i == 0:
            texto += str(funcao[i])
        else:
            texto += " + " + str(funcao[i])
            texto += ("*x^%o" % (i))
    print("Pn(x) :")
    print(texto)
    s = input(
        "Deseja calcular Pn(x) dado um valor de x? \n [S/N]").lower()
    if s == "s":
        print("Pn(x) em qual ponto?")
        p = float(input())
        print("Pn(%a) é igual a %a" % (p, Pn(p)))
        with open("newton.txt", 'w') as fp:
            fp.write("Polinomio: {} \n".format(texto))
            fp.write('Raizes: {} \n'.format(polynomial.polynomial.polyroots(list(Pn))))
            fp.write("Pn(%a) é igual a %a" % (p, Pn(p)))
    print("Raízes de Pn(x): ", polynomial.polynomial.polyroots(list(Pn)))
    # calculando f(x) nos pontos dados através de Pn(x)
    print("(x,Pn(x))")
    for i in range(len(pontos)):
        print("(%a,%a)" % (pontos[i][0], round(Pn(pontos[i][0]), 4)))
    with open("newton.txt", 'w') as fp:
            fp.write("Polinomio: {} \n".format(texto))
            fp.write('Raizes: {} \n'.format(polynomial.polynomial.polyroots(list(Pn))))
            for i in range(len(pontos)):
                fp.write("(%a,%a)" % (pontos[i][0], round(Pn(pontos[i][0]), 4)))
    

class App(tk.Tk):

    def __init__(self, *args, **kwargs):

        tk.Tk.__init__(self, *args, **kwargs)

        tk.Tk.wm_title(self, "RIC_ARO projeto sanguinolento-v7.2")

        container = tk.Frame(self)
        container.pack(side="top", fill="both", expand=True)
        container.grid_rowconfigure(0, weight=1)
        container.grid_columnconfigure(0, weight=1)

        self.frames = {}

        for F in (StartPage, janelinha_trape, trap_show, PageTwo, PageThree):

            frame = F(container, self)

            self.frames[F] = frame

            frame.grid(row=0, column=0, sticky="nsew")

        self.show_frame(StartPage)

    def show_frame(self, cont):

        frame = self.frames[cont]
        frame.tkraise()


class StartPage(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        label = tk.Label(self, text="Start Page", font=LARGE_FONT)
        label.pack(pady=10, padx=10)
        pygame.mixer.music.stop()
        button = ttk.Button(self, text="Trapezio",
                            command=lambda: controller.show_frame(janelinha_trape))
        button.pack()

        button2 = ttk.Button(self, text="Interpolação Newton",
                             command=lambda: controller.show_frame(PageTwo))
        button2.pack()

        button3 = ttk.Button(self, text="Graph Page",
                             command=lambda: controller.show_frame(PageThree))
        button3.pack()


class PageOne(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        label = tk.Label(self, text="Page One!!!", font=LARGE_FONT)
        label.pack(pady=10, padx=10)

        button1 = ttk.Button(self, text='CARALHOOO',
                             command=lambda: controller.show_frame(StartPage))
        button1.pack()

        button2 = ttk.Button(self, text="Page Two",
                             command=lambda: controller.show_frame(PageTwo))
        button2.pack()

# class NewtonPage(tk.Frame):
#     def __init__(self, parent,controller):
#         tk.Frame.__init__(self, parent)
#         l = []
#         label_poli = tk.Label(self, Text=l[0], font=LARGE_FONT)
#         label_poli.pack(pady=10, padx=10)
#         label_x = tk.Label(self, Text=l[1], font=LARGE_FONT)
#         label_x.pack(pady=10, padx=10)
#         label_y = tk.Label(self, Text=l[2], font=LARGE_FONT)
#         label_y.pack(pady=10, padx=10)


class PageTwo(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        label = tk.Label(self, text="Newton Interpolation Yeye", font=LARGE_FONT)
        label.pack(pady=10, padx=10)

        #pygame
        pygame.mixer.Sound.play(crash_sound)


        # entry1 = ttk.Entry(self)
        # entry1.pack()
        

        # def get_val():
        #     with open('butons.txt', 'w') as fp:
        #         fp.write(e1.get())

        def set_all():
            with open('newton.txt') as fp:
                global polino
                global pn
                global raiz
                dat = fp.readlines()
                polino = dat[0]
                pn = dat[2]
                raiz = dat[1]


        button1 = ttk.Button(self, text="Back to Home",
                             command=lambda: controller.show_frame(StartPage))
        button1.pack()

        button2 = ttk.Button(self, text="save",command=lambda: controller.show_frame(set_all))
        button2.pack()

        # button3 = ttk.Button(self, text="Show", command=lambda: controller.show_frame(NewtonPage))
        # button3.pack()

class PageThree(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        label = tk.Label(self, text="Graph Page!", font=LARGE_FONT)
        label.pack(pady=10, padx=10)

        button1 = ttk.Button(self, text="Back to Home",
                             command=lambda: controller.show_frame(StartPage))
        button1.pack()

        f = Figure(figsize=(5, 5), dpi=100)
        a = f.add_subplot(111)
        a.plot([1, 2, 3, 4, 5, 6, 7, 8], [5, 6, 1, 3, 8, 9, 3, 5])

        canvas = FigureCanvasTkAgg(f, self)
        canvas.show()
        canvas.get_tk_widget().pack(side=tk.BOTTOM, fill=tk.BOTH, expand=True)

        toolbar = NavigationToolbar2TkAgg(canvas, self)
        toolbar.update()
        canvas._tkcanvas.pack(side=tk.TOP, fill=tk.BOTH, expand=True)


app = App()
app.mainloop()


