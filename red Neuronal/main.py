from perceptron import *
from Palabra import *
from Matrix import *
from simpleperceptron import *
from lectorcsv import *
from escritorcsv import *
from math import *
from time import time
ran=1000
rnd=0.001
#puedo deducir este algoritmo en la entrada de los profes y en ese caso como lo resuelvo
def entradas_rnd_2():
    entradas=[]
    for i in range(ran):
        if(i%10==0):
            entradas.append([0,0,0,0])
        elif(i%10==1):
            entradas.append([1,0,1,0])
        elif(i%10==2):
            entradas.append([0,1,0,1])
        elif(i%10==3):
            entradas.append([1,1,1,1])
        elif(i%10==4):
            entradas.append([1,1,0,0])
        elif(i%10==5):
            entradas.append([0,1,1,0])
        elif(i%10==6):
            entradas.append([1,1,0,1])
        elif(i%10==7):
            entradas.append([1,0,0,1])
        elif(i%10==8):
            entradas.append([0,1,1,1])
        else:
            entradas.append([1,0,1,1])
    return entradas
def salidas_rnd_2():
    salidas=[]
    for i in range(ran):
        if(i%10==0):
            if(random()<rnd):
                salidas.append([0])
            else:
                salidas.append([1])
        elif(i%10==1):
            if(random()<rnd):
                salidas.append([1])
            else:
                salidas.append([0])
        elif(i%10==2):
            if(random()<rnd):
                salidas.append([0])
            else:
                salidas.append([1])
        elif(i%10==3):
            if(random()<rnd):
                salidas.append([0])
            else:
                salidas.append([1])
        elif(i%10==4):
            if(random()<rnd):
                salidas.append([1])
            else:
                salidas.append([0])
        elif(i%10==5):
            if(random()<rnd):
                salidas.append([0])
            else:
                salidas.append([1])
        elif(i%10==6):
            if(random()<rnd):
                salidas.append([0])
            else:
                salidas.append([1])
        elif(i%10==8):
            if(random()<rnd):
                salidas.append([1])
            else:
                salidas.append([0])
        else:
            if(random()<rnd):
                salidas.append([0])
            else:
                salidas.append([1])
    return salidas

def entradas_rnd():
    entradas=[]
    for i in range(ran):
        if(i%4==0):
            entradas.append([0,0,0])
        elif(i%4==1):
            entradas.append([1,0,0])
        elif(i%4==2):
            entradas.append([0,1,0])
        else:
            entradas.append([1,0,1])
    return entradas
def salidas_rnd():
    salidas=[]
    for i in range(ran):
        if(i%4==0):
            if(random()<rnd):
                salidas.append([0])
            else:
                salidas.append([1])
        elif(i%4==1):
            if(random()<rnd):
                salidas.append([1])
            else:
                salidas.append([0])
        elif(i%4==2):
            if(random()<rnd):
                salidas.append([0])
            else:
                salidas.append([1])
        else:
            if(random()<rnd):
                salidas.append([0])
            else:
                salidas.append([1])
    return salidas
def xs_norm_esp():
    lec=Lector("X_1")
    es=lec.leer_lineas_num(",")
    es=normalizar_mtx_esp(es)
    #es=normalizar_mtx_bin(es)
    return es

def ys():
    salidas=[[0],[1],[1],[0]]
    return salidas
def xs():
    entradas=[]
    entradas.append([0,0,0])
    entradas.append([0,0,1])
    entradas.append([1,0,1])
    entradas.append([1,1,0])
    
    return entradas
def xs_files():
    lec=Lector("X.csv")
    es=lec.leer_lineas_num(",")
    #es=normalizar_mtx(0,1,es)
    #es=normalizar_mtx_bin(es)
    return es
def ys_files():
    lec=Lector("Y.csv")
    os=lec.leer_lineas_num(",")
    #os=normalizar_mtx(0,1,os)
    #os=normalizar_mtx_bin(os)
    return os
def test_output_perc():
    es=xs()
    redConfig=[1,1]
    p=Perceptron(redConfig,1,1)
    for e in es:
        print(e)
        print(p.output(e))
    print(p.toString())
def test_percep():
    es=xs_norm_esp()
    os=ys_files()

    red_config=[4,4,5,10,10,10,4,5,1]
    p=Perceptron(4,red_config,0.1,0.05)
    print(p.toString())
    print("learn")
    star_time=time()
    p.learn(es,os)
    end_time=time()
    print("tiempo transcurrido: "+str(end_time-star_time))
    error=0
    i=0
    for e in es:
        num=abs(p.bin_output(e)[0]-os[i][0])
        if(i==0):
            error=num
        else:
            error=((i-1)*error+num)/i
        i+=1
    print("error: "+str(error))
    print(p.toString())
def learn_percep():
    es=entradas_rnd_2()
    os=salidas_rnd_2()
    redConfig=[4,5,5,1]
    p=Perceptron(4,redConfig,0.1,0.05)
    print(p.toString())
    print("learn")
    star_time=time()
    p.learn(es,os)
    end_time=time()
    print("tiempo transcurrido :"+str(end_time-star_time))
    print(p.toString())
    i=0
    for e in es:
        num=abs(p.bin_output(e)[0]-os[i][0])
        if(i==0):
            error=num
        else:
            error=((i-1)*error+num)/i
        i+=1
    print("error: "+str(error))
    #i=0
    #for e in es:
    #    print(e)
    #    print(os[i])
    #    print(p.bin_output(e))
    #    i+=1
def test_mtx():
    m1=Matrix(2,3)
    m2=Matrix(3,2)
    mtx_1=[]
    mtx_2=[]
    for r in range(2):
        row=[]
        for c in range(3):
            pal=Palabra("s:"+str(r)+str(c))
            row.append(pal)
        mtx_1.append(row)
    for r in range(3):
        row=[]
        for c in range(2):
            pal=Palabra("o:"+str(r)+str(c))
            row.append(pal)
        mtx_2.append(row)
    m1.set_mtx(mtx_1)
    m2.set_mtx(mtx_2)
    print(str(m1))
    print(str(m2))
    #m_res=m1.trans()
    m_res=m1.comb_mult(m2)
    print(str(m_res))
def write_ones_zeros_files():
    es=xs_files()
def write_entries():
    es=xs_norm_esp()
    esc=Escritor("X_norm_esp")
    esc.escribir_matrix(es)
def write_files():
    es=xs_files()
    print(len(es))
    os=ys_files()
    mat=Matrix(len(es),len(es[0]))
    mat.set_mtx(es)
    print(mat.rows)
    col_1=mat.col(0)
    col_2=mat.col(1)
    col_3=mat.col(2)
    col_4=mat.col(3)
    mtx_1=[]
    mtx_2=[]
    mtx_3=[]
    mtx_4=[]
    for i in range(len(es)):
        row_1=[]
        row_2=[]
        row_3=[]
        row_4=[]
        row_1.append(col_1[i])
        row_1.append(os[i][0])
        mtx_1.append(row_1)
        
        row_2.append(col_2[i])
        row_2.append(os[i][0])
        mtx_2.append(row_2)

        row_3.append(col_3[i])
        row_3.append(os[i][0])
        mtx_3.append(row_3)

        row_4.append(col_4[i])
        row_4.append(os[i][0])        
        mtx_4.append(row_4)

    mtx_1=sorted(mtx_1,key=lambda linea:linea[0]) 
    esc=Escritor("X_1_Y")
    esc.escribir_matrix(mtx_1)
    mtx_2=sorted(mtx_2,key=lambda linea:linea[0]) 
    esc=Escritor("X_2_Y")
    esc.escribir_matrix(mtx_2)
    mtx_3=sorted(mtx_3,key=lambda linea:linea[0]) 
    esc=Escritor("X_3_Y")
    esc.escribir_matrix(mtx_3)
    mtx_4=sorted(mtx_4,key=lambda linea:linea[0]) 
    esc=Escritor("X_4_Y")
    esc.escribir_matrix(mtx_4)
def write_bin_files():
    es=xs_norm_esp()
    os=ys_files()
    mat=Matrix(len(es),len(es[0]))
    mat.set_mtx(es)
    
    col_1=mat.col(0)
    col_2=mat.col(1)
    col_3=mat.col(2)
    col_4=mat.col(3)
    mtx_1=[]
    mtx_2=[]
    mtx_3=[]
    mtx_4=[]
    for i in range(len(es)):
        row_1=[]
        row_2=[]
        row_3=[]
        row_4=[]

        row_1.append(col_1[i])
        row_1.append(os[i][0])
        mtx_1.append(row_1)
        row_2.append(col_2[i])
        row_2.append(os[i][0])
        mtx_2.append(row_2)

        row_3.append(col_3[i])
        row_3.append(os[i][0])
        mtx_3.append(row_3)
        row_4.append(col_4[i])
        row_4.append(os[i][0])        
        mtx_4.append(row_4)
    mtx_1=sorted(mtx_1,key=lambda linea:linea[0]) 
    esc=Escritor("X_1_Y_bin")
    esc.escribir_matrix(mtx_1)
    mtx_2=sorted(mtx_2,key=lambda linea:linea[0]) 
    esc=Escritor("X_2_Y_bin")
    esc.escribir_matrix(mtx_2)
    mtx_3=sorted(mtx_3,key=lambda linea:linea[0]) 
    esc=Escritor("X_3_Y_bin")
    esc.escribir_matrix(mtx_3)
    mtx_4=sorted(mtx_4,key=lambda linea:linea[0]) 
    esc=Escritor("X_4_Y_bin")
    esc.escribir_matrix(mtx_4)
def write_norm_files():
    es=xs_files()
    es=normalizar_norm_mtx(es)
    os=ys_files()
    mat=Matrix(len(es),len(es[0]))
    mat.set_mtx(es)
    
    col_1=mat.col(0)
    col_2=mat.col(1)
    col_3=mat.col(2)
    col_4=mat.col(3)
    mtx_1=[]
    mtx_2=[]
    mtx_3=[]
    mtx_4=[]
    for i in range(len(es)):
        row_1=[]
        row_2=[]
        row_3=[]
        row_4=[]

        row_1.append(col_1[i])
        row_1.append(os[i][0])
        mtx_1.append(row_1)
        row_2.append(col_2[i])
        row_2.append(os[i][0])
        mtx_2.append(row_2)

        row_3.append(col_3[i])
        row_3.append(os[i][0])
        mtx_3.append(row_3)
        row_4.append(col_4[i])
        row_4.append(os[i][0])        
        mtx_4.append(row_4)
    mtx_1=sorted(mtx_1,key=lambda linea:linea[0]) 
    esc=Escritor("X_1_Y_norm_euc")
    esc.escribir_matrix(mtx_1)
    mtx_2=sorted(mtx_2,key=lambda linea:linea[0]) 
    esc=Escritor("X_2_Y_norm_euc")
    esc.escribir_matrix(mtx_2)
    mtx_3=sorted(mtx_3,key=lambda linea:linea[0]) 
    esc=Escritor("X_3_Y_norm_euc")
    esc.escribir_matrix(mtx_3)
    mtx_4=sorted(mtx_4,key=lambda linea:linea[0]) 
    esc=Escritor("X_4_Y_norm_euc")
    esc.escribir_matrix(mtx_4)
def learn_simple():
    es=xs()
    os=[1,0,1,0]
    p=SimplePerceptron(2,1.1,0.01)
    print(p.toString())
    print("learn")
    i=0
    for e in es:
        print(e)
        print(os[i])
        print(p.output(e))
        i+=1
    p.learn(es,os)
    print(p.toString())
    i=0
    for e in es:
        print(e)
        print(os[i])
        print(p.output(e))
        i+=1

def main():
    test_percep()
if __name__=="__main__":
    main()