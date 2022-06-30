# -*- coding: utf-8 -*-
"""
Created on Wed Jun 29 18:03:00 2022

@author: JADER MANOSALVA
"""
import pandas as pd
import os #Se importa para limpiar la consola
import matplotlib.pyplot as plt #Modulo importado para operaciones
import numpy as np #importamos el modulo numpy y le danos un apodo dentro del programa
from scipy import stats #de scipy importamos el modulo stats, para datos mas estadisticos
from tabulate import tabulate
from os import path
from random import shuffle
print("---------------------------------------------------------------------------")           
print ("\n ¡BIENVENIDO A ESTE PROGRAMA \n")
print("---------------------------------------------------------------------------")            
print("nota: Recomendamos que el archivo gapminder lo conserve en la misma carpeta"
      "en la que desarrolla este programa",'\n')
dire=path.abspath('gapminder.xlsx')
df=pd.read_excel(dire)
"""Cambiamos los valores a na en lifeExp, pop y gdpPercap"""
z=0
while z != 4:
    print("---------------------------------------------------------------------------")            
    print ("\n                        MENÙ PRINCIPAL                                \n")
    print("---------------------------------------------------------------------------")            
    print ("De las siguientes opciones:","\n",
       "1. Ejercicio 1 del taller 3","\n",
       "2. Ejercicio 2 del taller 3","\n",
       "3. Ejercicio 3 del taller 3","\n",
       "4. Salir","\n")
    print ("\n NOTA: Si la opción que desea seleccionar es: Salir (4), indique el numero correspondiente y precione dos veces enter.")
    z=float(input ("Elija la opción 1, 2, 3 o 4, según desee conocer los dato: "))
    if z == 1:
        w = 0
        while w != 6:
            print("---------------------------------------------------------------------------")
            print ("\n MENU DEL EJERCICIO 1 \n")
            print ("---------------------------------------------------------------------------",
            "De las siguientes opciones:","\n",
               "1. Exportar gapminder con valores en NaN","\n",
               "2. Importar gapminder","\n",
               "3. Grafica de dispersión de lifeExp vs pop","\n",
               "4. Grafica de dispersión de gdpPercap vs pop","\n",
               "5. Diagrama de cajas de gdpPercap por continentes en los años 1990-2007","\n"
               "6. Salir","\n")
            print("nota: si desea salir de este sub menú elija la opción 6 y precione 3 veces enter.")
            w=int(input ("Elija la opción que desea: \n"))
            #Este if corresponde al primer punto, donde se exportan los datos gapminder con 
            #algunos valores en gdpPercap, LifeExp y pop en NA
            if w == 1:
                 """Cambiamos los valores a na en lifeExp, pop y gdpPercap"""
                 dim=df.shape
                 porc=int(dim[0]*0.1)
                 """lifeExp"""
                 indices1=np.random.permutation(dim[0])
                 indices1=indices1[:porc]
                 df.loc[indices1,'lifeExp']=np.nan
                 """pop"""
                 indices2=np.random.permutation(dim[0])
                 indices2=indices2[:porc]
                 df.loc[indices2,'pop']=np.nan
                 """gdpPercap"""
                 indices3=np.random.permutation(dim[0])
                 indices3=indices3[:porc]
                 df.loc[indices3,'gdpPercap']=np.nan
                 """Exportamos el archivo con los valores de na incluidos"""
                 nam=input("Por favor ingrese el nombre con el cual desea guardar el archivo:\n")
                 nam=nam +".xlsx"
                 df.to_excel(nam, sheet_name="Datos")
                 print("Gapminder exportado")
            elif w==2:
                """Importamos el archivo con los valores de na incluidos"""
                df1=pd.read_excel(nam)
                print("Gapminder importado")
                a=input("Presione enter")
            elif w==3:
                """Con este elifvisualizamos la grafica de dispersión convirtiendo los valores NA al promedio"""
                df1.loc[indices1,'lifeExp']=np.nanmean(df.iloc[:,3])
                df1.loc[indices2,'pop']=np.nanmean(df.iloc[:,4])
                df1.loc[indices3,'gdpPercap']=np.nanmean(df.iloc[:,5])
                """Creamos el diagrama de dispersión para gdpPercap vs lifeExp"""
                plt.scatter(df1['lifeExp'],df1['pop'], color='r')
                plt.xlabel('LifeExp')
                plt.ylabel('Población')
                plt.title('LifeExp vs Población')
                plt.show()
            elif w==4:
                """Creamos el diagrama de dispersión para gdpPercap vs pop"""
                plt.scatter(np.log(df1['gdpPercap']),df1['pop'], color='b')
                plt.xlabel('log(gdpPercap)')
                plt.ylabel('Población')
                plt.title('GdpPercap vs Población')
                plt.show()
            elif w==5:
                """Creamos el diagrama de cajas para gdpPercap discriminados por continentes 
                desde1990 a 2007"""
                df1=df1[df1['year']>1990]
                df1=df1[df1['year']<2007]
                df1.boxplot(column="gdpPercap", by='continent', fontsize=10)
                plt.xlabel("Continentes")
                plt.ylabel('GdpPercap')
                plt.title('GdpPercap por Población')
                plt.show()
            input()
            os.system("cls")
    elif z==2:
        """Segundo punto del taller3"""
        """En primer lugar le pedimos al usuario que digite la media, la desviación 
        estandar y la longitud de los datos con la que desea trabajr los experimentos"""
        print("Por favor ingrese los datos con los que desea trabajar:")
        ld=int(input("Por favor ingrese la cantidad de datos con los cuales desea trabajar los experimentos:\n"))
        m1=float(input("Por favor ingrese la media para el experimento_a:\n"))
        m2=float(input("Por favor ingrese la media para el experimento_b:\n"))
        d1=float(input("Por favor ingrese la desviación estandar para el experimento_a:\n"))
        d2=float(input("Por favor ingrese la desviación estandar para el experimento_b:\n"))
        ExpA=pd.DataFrame(d1*np.random.randn(ld)+m1)
        ExpB=pd.DataFrame(d2*np.random.randn(ld)+m2)
        ExpA.to_csv("Experimento_a.csv")
        ExpB.to_csv("Experimento_b.csv")
        x=0
        while x != 5:
            print("---------------------------------------------------------------------------")
            print("MENU DEL EJERCICIO 2", '\n',
            "---------------------------------------------------------------------------", 
                  "1. Importar los experimentos a & b", '\n',
                  "2. Determinar si las medias de los experimentos a & b son estadisticamente significativas", '\n',
                  "3. Correlación Pearson & Spearman de los experimentos a & b", '\n',
                  "4. Grafica de dispersión de los experimentos con linea de tendencia", '\n',
                  "5. Salir", '\n')
            print("nota: si desea salir de este sub menú elija la opción 5 y precione 3 veces enter.")
            x=int(input ("Elija la opción que desea: \n"))
            if x==1:
                """Este if importa los experimentos"""
                Ex1=pd.read_csv("Experimento_a.csv")
                Ex2=pd.read_csv("Experimento_b.csv")
                print("Experimentos importados")
            elif x==2:
                est=stats.ttest_ind(Ex1.iloc[:,1],Ex2.iloc[:,1])
                print("El p valor es:",est[1])
                
                if est[1]>0.5:
                    print("Las medias no presentan diferencias estadisticamente significativas")
                else:
                    print("Las medias presentan diferencias estadisticamente significativas")
                a=input("Presione enter")
            elif x==3:
                print("La correlación Pearson de los experimentos es:",'\n')
                p=Ex1.iloc[:,1].corr(Ex2.iloc[:,1], method='pearson')
                print(p,'\n')
                print("La correlación Spearman de los experimentos es:",'\n')
                s=Ex1.iloc[:,1].corr(Ex2.iloc[:,1], method='spearman')
                print(s,'\n')
            elif x==4:
                sumx=sum(Ex1.iloc[:,1])
                sumy=sum(Ex2.iloc[:,1])
                sumx2=sum(Ex1.iloc[:,1]*Ex1.iloc[:,1])
                sumy2=sum(Ex2.iloc[:,1]*Ex2.iloc[:,1])
                sumxy=sum(Ex1.iloc[:,1]*Ex2.iloc[:,1])
                promx=sumx/ld
                promy=sumy/ld
                m=(sumx*sumy - ld*sumxy)/(sumx**2 - ld*sumx2)
                b=promy - m*promx
                plt.plot(Ex1.iloc[:,1],Ex2.iloc[:,1], 'o', label='Datos')
                plt.plot(Ex1.iloc[:,1],m * Ex1.iloc[:,1] + b, label='Ajuste')
                plt.xlabel('Experimento_A')
                plt.ylabel('Experimento_B')
                plt.title('Diagrama de dispersión entre los experimentos A & B')
                plt.grid()
                plt.legend(loc=4)
                plt.show()
            input()
            os.system("cls")
    elif z == 3:
        val=0
        while val != 5:
            print("---------------------------------------------------------------------------")
            print("                        MENÙ DE GRAFICOS EJERCICIO 3                              ")
            print("---------------------------------------------------------------------------")
            print("1. Graficar la función de densidad de una distribución uniforme")
            print("2. Graficar la función de densidad de una distribución Bernoulli")
            print("3. Graficar la función de densidad de una distribución Poisson")
            print("4. Graficar la función de densidad de una distribución Exponencial")
            print("--------------------------------------------------------------------------")
            print("5. SALIR DEL PROGRAMA")
            #Este comando le permite al usuario elegir que grafica desea visualizar
            val=  int(input("¿Qué gráfico desea ver?: "))
            if val == 1:
                    #Grafica función de distribución Uniforme ()
                    #Se importan las librerias
                  from scipy.stats import uniform
                  def uniform_pdf(x, a, b):
                    if a <= x <= b: #La función de densidad debe cumplir esto
                      return 1/(b-a)
                    else:
                      return 0
                  x = 0.3 
                  a =  int(input("Ingrese el valor deL evento a: ")) #El usuario puede  asignar el valor que desee observar
                  b =  int(input("Ingrese el valor del evento b: "))
                  print(uniform_pdf(x, a, b))
                  fig, ax = plt.subplots(figsize=(12,6))
                  ax.plot(np.linspace(a-1, b+1, num=10000),[uniform_pdf(x,a,b) for x in np.linspace(a-1, b+1, num=10000)], lw=10)
                  ax.plot(np.linspace(a-1, b+1, num=10000),[uniform_pdf(x,a,b) for x in np.linspace(a-1, b+1, num=10000)], lw=3)
                  plt.show() 
                    #https://docs.scipy.org/doc/scipy/reference/generated/scipy.stats.uniform.html#scipy.stats.uniform
            elif val == 2:
                    #Grafica función de distribución Bernoulli ()
                  #Se importan las librerias 
                  from scipy.stats import bernoulli
                  import seaborn as sb
                  p=0.5
                  #Mostrar la función de masa de probabilidad ( pmf)
                  x = np.arange(bernoulli.ppf(0.01, p),
                                bernoulli.ppf(0.99, p))
                  fig, ax = plt.subplots(figsize=(12,6))
                  ax.plot(x, bernoulli.pmf(x, p), 'bo', ms=8, label='Bernoulli pmf')
                  ax.vlines(x, 0, bernoulli.pmf(x, p), colors='y', lw=5, alpha=0.5)
                  ax.legend(loc='best', frameon=False)
                  plt.show() #Se realiza la grafica de la distribución de Bernoulli    
                    #https://docs.scipy.org/doc/scipy/reference/generated/scipy.stats.bernoulli.html#scipy.stats.bernoulli
            elif val == 3:
                    #Grafica función de distribución Poisson 
                    #Se importan las librerias
                  from scipy.stats import poisson
                  import seaborn as sb
                  mu = 0.8
                  x = np.arange(poisson.ppf(0.01, mu),
                                poisson.ppf(0.99, mu))
                  fig, ax = plt.subplots(figsize=(12,6))
                  ax.plot(x, poisson.pmf(x, mu), 'bo', ms=8, label='Poisson pmf')
                  ax.vlines(x, 0, poisson.pmf(x, mu), colors='g', lw=5, alpha=0.5)
                  ax.legend(loc='best', frameon=False)
                  plt.show()   
                    #https://docs.scipy.org/doc/scipy/reference/generated/scipy.stats.poisson.html
            elif val == 4:
                    #Grafica función de deistribucion Exponencial ()
                    #Se importan las librerias
                  from scipy.stats import expon
                  import matplotlib.pyplot as plt
                  #Muestre la función de densidad de probabilidad ( pdf)
                  x = np.linspace(expon.ppf(0.01),
                                  expon.ppf(0.99), 100)
                  fig, ax = plt.subplots(figsize=(12,6))
                  ax.plot(x, expon.pdf(x),
                        'r-', lw=5, alpha=0.6, label='Exponencial pdf')
                  ax.legend(loc='best', frameon=False)
                  plt.show()
                    #https://docs.scipy.org/doc/scipy/reference/generated/scipy.stats.expon.html#scipy.stats.expon
            input()   
            os.system("cls")
    input()   
    os.system("cls")
print("Muchas gracias por usar nuestro programa")
                
                