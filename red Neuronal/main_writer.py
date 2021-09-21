from perceptron import *
from Palabra import *
from Matrix import *
from simpleperceptron import *
from lectorcsv import *
from escritorcsv import *
from math import *
from time import time
from main import *

def write_copias():
    esc=Escritor("X_1")
    esc.dividir_archivo(1/100,"X_1",True)
def write_ones_zeros_files_file(nombreX,nombreY,ratio):
    esc=Escritor("X_1")
    esc.dividir_archivo(ratio,nombreX,True)
    esc=Escritor("Y_1")
    esc.dividir_archivo(ratio,nombreY,True)
    lec=Lector(nombreX+"_1_copia")
    es=lec.leer_lineas_num(",")
    lec=Lector(nombreY+"_1_copia")
    os=lec.leer_lineas_num(",")
    es=xs_files()
    os=ys_files()
    es_c_1_1=[]
    es_c_1_0=[]
    es_c_2_1=[]
    es_c_2_0=[]
    es_c_3_1=[]
    es_c_3_0=[]
    es_c_4_1=[]
    es_c_4_0=[]
    for i in range(len(os)):
        bin_val=os[i][0]
        if(bin_val==1):
            es_c_1_1.append(es[i][0])
            es_c_2_1.append(es[i][1])
            es_c_3_1.append(es[i][2])
            es_c_4_1.append(es[i][3])
        else:
            es_c_1_0.append(es[i][0])
            es_c_2_0.append(es[i][1])
            es_c_3_0.append(es[i][2])
            es_c_4_0.append(es[i][3])
    es_c_1_1=sorted(es_c_1_1)
    es_c_1_0=sorted(es_c_1_0)
    es_c_2_1=sorted(es_c_2_1)
    es_c_2_0=sorted(es_c_2_0)
    es_c_3_1=sorted(es_c_3_1)
    es_c_3_0=sorted(es_c_3_0)
    es_c_4_1=sorted(es_c_4_1)
    es_c_4_0=sorted(es_c_4_0)
    esc=Escritor(nombreX+"c_1_1")
    esc.escribir_vector(es_c_1_1)
    esc=Escritor(nombreX+"c_1_0")
    esc.escribir_vector(es_c_1_0)
    esc=Escritor(nombreX+"c_2_1")
    esc.escribir_vector(es_c_2_1)    
    esc=Escritor(nombreX+"c_2_0")
    esc.escribir_vector(es_c_2_0)
    esc=Escritor(nombreX+"c_3_1")
    esc.escribir_vector(es_c_3_1)
    esc=Escritor(nombreX+"c_3_0")
    esc.escribir_vector(es_c_3_0)
    esc=Escritor(nombreX+"c_4_1")
    esc.escribir_vector(es_c_4_1)    
    esc=Escritor(nombreX+"c_4_0")
    esc.escribir_vector(es_c_4_0)   
def write_ones_zeros_files():
    es=xs_files()
    os=ys_files()
    es_c_1_1=[]
    es_c_1_0=[]
    es_c_2_1=[]
    es_c_2_0=[]
    es_c_3_1=[]
    es_c_3_0=[]
    es_c_4_1=[]
    es_c_4_0=[]
    for i in range(len(os)):
        bin_val=os[i][0]
        if(bin_val==1):
            es_c_1_1.append(es[i][0])
            es_c_2_1.append(es[i][1])
            es_c_3_1.append(es[i][2])
            es_c_4_1.append(es[i][3])
        else:
            es_c_1_0.append(es[i][0])
            es_c_2_0.append(es[i][1])
            es_c_3_0.append(es[i][2])
            es_c_4_0.append(es[i][3])
    es_c_1_1=sorted(es_c_1_1)
    es_c_1_0=sorted(es_c_1_0)
    es_c_2_1=sorted(es_c_2_1)
    es_c_2_0=sorted(es_c_2_0)
    es_c_3_1=sorted(es_c_3_1)
    es_c_3_0=sorted(es_c_3_0)
    es_c_4_1=sorted(es_c_4_1)
    es_c_4_0=sorted(es_c_4_0)
    esc=Escritor("X_1_c_1_1")
    esc.escribir_vector(es_c_1_1)
    esc=Escritor("X_1_c_1_0")
    esc.escribir_vector(es_c_1_0)
    esc=Escritor("X_1_c_2_1")
    esc.escribir_vector(es_c_2_1)    
    esc=Escritor("X_1_c_2_0")
    esc.escribir_vector(es_c_2_0)
    esc=Escritor("X_1_c_3_1")
    esc.escribir_vector(es_c_3_1)
    esc=Escritor("X_1_c_3_0")
    esc.escribir_vector(es_c_3_0)
    esc=Escritor("X_1_c_4_1")
    esc.escribir_vector(es_c_4_1)    
    esc=Escritor("X_1_c_4_0")
    esc.escribir_vector(es_c_4_0)
def main():
    write_ones_zeros_files_file("X","Y",1/100)
if __name__=="__main__":
    main()