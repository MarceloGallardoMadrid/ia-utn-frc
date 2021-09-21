from random import *
from lectorcsv import *
class Escritor:
    def __init__(self,path):
        self.path=path
    def escribir_lineal(self):
        m=""
        for i in range(100):
            row=""
            for j in range(50):
                if(j!=0):
                    row+=" "
                row+=str(100*i+j)
            
            row+="\n"
            m+=row
        f=open(self.path,"w")
        f.write(m)
        f.close()
        
    def escribir_lineas_rnd(self):
        m=""
        for i in range(100):
            row=""
            for j in range(50):
                if(j!=0):
                    row+=" "
                row+=str(random())
            
            row+="\n"
            m+=row
        f=open(self.path,"w")
        f.write(m)
        f.close()
    def copia_archivo(self,original):
        f=open(self.path,"w")
        with open(original,"r") as archivo:
            for line in archivo:
                if (line.strip()!=""):
                    f.write(line)
        f.close()
    def escribir_vector(self,vec):
        m=""
        rows=len(vec)
        for i in range(rows):
            m+=str(vec[i])+"\n"
            
        f=open(self.path,"w")
        f.write(m)
        f.close()        
    def escribir_matrix(self,matrix):
        m=""
        rows=len(matrix)
        cols=len(matrix[0])
        for i in range(rows):
            row_s=""
            for j in range(cols):
                if(j!=0):
                    row_s+=" "
                row_s+=str(matrix[i][j])
            row_s+="\n"
            m+=row_s
            
        f=open(self.path,"w")
        f.write(m)
        f.close()
            
            
    def dividir_archivo(self,ratio,original,copia=False):
        path_file_1=original+"_1"
        path_file_2=original+"_2"
        if(copia):
            path_file_1+="_copia"
            path_file_2+="_copia"
        lec=Lector(original)
        lineas=lec.leer_cant_lineas()
        lineas_file_1=round(lineas*ratio)
        esc_1=Escritor(path_file_1)
        esc_2=Escritor(path_file_2)
        mtx_file_1=lec.leer_lineas_max(lineas_file_1)
        mtx_file_2=lec.leer_lineas_desde_hasta(lineas_file_1,lineas)
        esc_1.escribir_matrix(mtx_file_1)
        esc_2.escribir_matrix(mtx_file_2)
        