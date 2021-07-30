from tkinter import ttk, messagebox
from math import sqrt
import tkinter as tk
import pandas as pd

class ArquitecuraC:
    def __init__(self):
        self.Main_Window = tk.Tk()
        self.Main_Window.geometry("360x230")
        self.Main_Window.title("Aquitectura de Computadoras")
        self.Main_Window.resizable(0, 0)
        self.Menu()
        self.Main_Window.mainloop()

    def Menu(self):
        WindowsP = self.Main_Window

        Lb_Menu = ttk.Label(WindowsP, text="\n M E N U ~ P R I N C I P A L")
        Lb_Menu.place(x=78, y=10)
        Lb_Menu.config(font=("Verdana", 10))

        Lb_Menu2 = ttk.Label(
            WindowsP, text="1. Fibonacci \n2. Tablas de Multilplicación \n3. Formula General \n4.Salir")
        Lb_Menu2.place(x=80, y=50)
        Lb_Menu2.config(font=("Verdana", 10))

        Lb_Titulo = ttk.Label(WindowsP, text="Opción: ")
        Lb_Titulo.place(x=45, y=150)
        Lb_Titulo.config(font=("Verdana", 11))

        Entry_Dat = ttk.Entry(WindowsP)
        Entry_Dat.place(x=110, y=151)

        Btn_Prin = ttk.Button(WindowsP, text="Entrar",command=lambda: self.SubMenu(Entry_Dat.get()))
        Btn_Prin.place(x=250, y=149)

    def SubMenu(self, Op_Seleccionado):
        Windos_P = self.Main_Window
        Op_Seleccionado = int(Op_Seleccionado)
        # Verificacion de dato ingresado
        if Op_Seleccionado <= 0 or Op_Seleccionado > 4:
            messagebox.showinfo(message="No Existe el Valor Ingresado", title="Aviso-Valores")
        else:
            # Seleccionar metodo
            if Op_Seleccionado == 1:
                self.Met_Fibonacci()
            elif Op_Seleccionado == 2:
                self.Met_TablasM()
            elif Op_Seleccionado == 3:
                self.Met_FormulaGen()
            elif Op_Seleccionado == 4:
                self.Met_Salir(Windos_P)

# ------- METODOD DE LA FIBONACCI ---------
    def Met_Fibonacci(self):
        Window_Fibo = tk.Tk()
        Window_Fibo.title("Fibonacci")
        Window_Fibo.geometry("340x150")
        
        Lb_DatSerie = ttk.Label(Window_Fibo, text="No. Veces: ")
        Lb_DatSerie.place(x=20,y=20)
        Lb_DatSerie.config(font=("Verdana",10))

        Entry_Fibo = ttk.Entry(Window_Fibo)
        Entry_Fibo.place(x=100, y=20)

        Btn_Serie = ttk.Button(Window_Fibo,text="Generar",command=lambda:self.Fibonacci_Secuen(Window_Fibo,Entry_Fibo.get()))
        Btn_Serie.place(x=245, y=19)

        Window_Fibo.mainloop()

    def Fibonacci_Secuen(self,Posicion,Cant_Veces):
        Cant_Veces = int(Cant_Veces)
        
        if Cant_Veces <= 1:
            messagebox.showinfo(message="Tiene que ser un valor > 1", title="Aviso-Valores")
            Posicion.destroy()
        else:
            Window_Fibo2 = tk.Tk()
            Window_Fibo2.title("Fibonacci")
            Window_Fibo2.geometry("340x150")

            def Fibo_Process(n):
                a = 0
                b = 1

                for i in range(n):
                    c = a + b
                    a = b
                    b = c
                return b

            Datos_S = []
            for a in range(Cant_Veces):
                Datos_S.append(Fibo_Process(a))
                Lb_Serie = ttk.Label(Window_Fibo2, text=("Serie:",Datos_S))
                Lb_Serie.place(x=20, y=40)
                Lb_Serie.config(font=("Verdana",12))

            Window_Fibo2.mainloop()
            
# ------- METODOD DE TABLAS DE MULTIPLICACION ---------
    def Met_TablasM(self):
        Window_Table = tk.Tk()
        Window_Table.title("Tabla de Multiplicacion")
        Window_Table.geometry("200x150")
        
        Lb_Titulo = ttk.Label(Window_Table,text="Seleccione la Tabla:").place(x=50,y=10)

        List_Valores = (1,2,3,4,5,6,7)
        List_Tabla = ttk.Combobox(Window_Table,values=List_Valores,width=15)
        List_Tabla.place(x=40,y=40)

        Btn_Selec = ttk.Button(Window_Table,text="Generar",command=lambda:self.Generar_Tab(Window_Table,List_Tabla.get())).place(x=50,y=80)

        Window_Table.mainloop()

    def Generar_Tab(self,Posicion,V_Selec):
        V_Selec = int(V_Selec)

        Val_Base = []
        Val_Multi = []
        Simbo = []
        Simbo2 = []
        Result = []

        for i in range(1,11):
            Mult = V_Selec*i
            Val_Base.append(V_Selec)
            Simbo.append("x")
            Val_Multi.append(i)
            Simbo2.append("=")
            Result.append(Mult)
        
        Dat_Tabla = pd.DataFrame(Val_Base,columns=["Base"])
        Dat_Tabla[""] = Simbo
        Dat_Tabla["Multi"] = Val_Multi
        Dat_Tabla[" "] = Simbo2
        Dat_Tabla["Resultado"] = Result

        self.Tab_General(Dat_Tabla)
    
    def Tab_General(self,Tabla):
        Window_Table2 = tk.Tk()
        Window_Table2.title("Tabla de Multiplicacion")
        Window_Table2.geometry("350x300")

        Tabla_Gen = ttk.Treeview(Window_Table2)
        Tabla_Gen.place(relheight=.80, relwidth=.90, x=15, y=20)
        
        Tabla_Gen["column"] = list(Tabla.columns)
        Tabla_Gen["show"] = "headings"

        for column in Tabla_Gen["column"]:
            Tabla_Gen.heading(column, text=column)
            Tabla_Gen.column(column, width=10, anchor="c")

        df_Tombola = Tabla.to_numpy().tolist()
        for row in df_Tombola:
            Tabla_Gen.insert("", "end", values=row)

        Window_Table2.mainloop()

# ------- METODOD DE LA FORMULA GENERAL ---------
    def Met_FormulaGen(self):
        Window_Formula = tk.Tk()
        Window_Formula.title("Formula General")
        Window_Formula.geometry("350x200")

        Lb_A = ttk.Label(Window_Formula, text="Valor de a: ")
        Lb_A.place(x=15, y=20)
        Lb_A.config(font=("Verdana", 11))

        Lb_B = ttk.Label(Window_Formula, text="Valor de b: ")
        Lb_B.place(x=15, y=50)
        Lb_B.config(font=("Verdana", 11))

        Lb_C = ttk.Label(Window_Formula, text="Valor de c: ")
        Lb_C.place(x=15, y=80)
        Lb_C.config(font=("Verdana", 11))

        Entry_A = ttk.Entry(Window_Formula)
        Entry_A.place(x=110, y=21)

        Entry_B = ttk.Entry(Window_Formula)
        Entry_B.place(x=110, y=50)

        Entry_C = ttk.Entry(Window_Formula)
        Entry_C.place(x=110, y=80)

        Btn_Selec2 = ttk.Button(Window_Formula,text="Calcular", width=18,
            command=lambda:self.Calcular_Form(Window_Formula,Entry_A.get(), Entry_B.get(), Entry_C.get())).place(x=100,y=120)

        Window_Formula.mainloop()

    def Calcular_Form(self,Posicion,v_A,v_B,v_C):
        v_A = int(v_A)
        v_B = int(v_B)
        v_C = int(v_C)

        try:
            if v_A != 0:
                Val_X1 = (-v_B + sqrt((v_B**2)-(4*v_A*v_C)))/(2*v_A)
                Val_X2 = (-v_B - sqrt((v_B**2)-(4*v_A*v_C)))/(2*v_A)
                
                if Val_X1==0 and Val_X2==0:
                    Lb_Resut = ttk.Label(Posicion, text=("Solucion: X1:",round(Val_X1,4)))
                    Lb_Resut.place(x=10, y=160)
                    Lb_Resut.config(font=("Verdana",10))
                else:
                    Lb_Resut2 = ttk.Label(Posicion, text=("Resultados:","X1:",round(Val_X1,4),"X2:",round(Val_X2,4)))
                    Lb_Resut2.place(x=10, y=160)
                    Lb_Resut2.config(font=("Verdana",10))
            else:
                if v_B != 0: 
                    v_X = -v_C/v_B
                    Lb_Resut3 = ttk.Label(Posicion, text=("Resultados:","X:",round(v_X,4)))
                    Lb_Resut3.place(x=10, y=160)
                    Lb_Resut3.config(font=("Verdana",10))
                else:
                    if v_C != 0:
                        messagebox.showinfo(message="Ecuacion sin Solucion", title="Error-Ecuacion")
                        Posicion.destroy()
                    else:
                        messagebox.showinfo(message="Ecuacion con Infinitas Soluciones", title="Error-Ecuacion")
                        Posicion.destroy()
        except:
            messagebox.showinfo(message="No se Puede Realizar la Ecuacion", title="Error-Ecuacion")
            Posicion.destroy()

#------- METODO PARA FINALIZAR EL PROGRAMA -------
    def Met_Salir(self, Posicion):
        Posicion.destroy()

ap = ArquitecuraC()
