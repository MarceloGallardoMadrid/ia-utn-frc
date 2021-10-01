import numpy as np
from math import *
from random import random

class Irreg_matrix:
    def __init__(self):
        #matrices cuyas filas son np.array de 1 fila y n columnas
        self.mtx=[]
        #Como es una matrix entonces, tiene 2 dimensiones, pero en este array guardo los tamaños por fila
        self.shape=[]
    def __getitem__(self,idx):
        return self.mtx[idx]
    def add_row(self,np_array):
        shape=np_array.shape[1]
        self.shape.append(shape)
        self.mtx.append(np_array)
    
    
    
        
def sigmoide(x):
    x=max(-400,x)
    return 1/(1+exp(-x))
def der_sigmoide(x):
    return sigmoide(x)*(1-sigmoide(x))
def tanh(x):
    x=max(-400,x)
    return (exp(x)-exp(-x))/(exp(x)+exp(-x))
def der_tanh(x):
    return 1-pow(tanh(x),2)
def float2bin(x):
    if(x>0.5):
        return 1
    else:
        return 0
def print_pesos(pesos,umbrales):
    for c in range(len(pesos)):
        m=""
        for n in range(len(pesos[c])):
            m+="u: "+str(umbrales[c][n])
            for p in range(len(pesos[c][n])):
                m+="p_"+str(p)+": "+str(pesos[c][n][p])
            m+="\n"
        print(m)
        print("\n")
def deepcopy_numeros(lista):
    new_lista=[]
    for n in lista:
        new_lista.append(n)
    return new_lista
def deepcopy_lista_numeros(matrix):
    new_mtx=[]
    for r in matrix:
        new_lista=deepcopy_numeros(r)
        new_mtx.append(new_lista)
    return new_mtx
def rnd_peso():
    return -1+2*random()
def apply_act_func(f,lista):
    new_lista=[]
    for n in lista:
        new_lista.append(f(n))
    return new_lista

def calculo_error(vec_esperado,vec_estimado):
    if(len(vec_esperado)!=len(vec_estimado)):
        return
    else:
        suma=0
        for i in range(len(vec_esperado)):
            suma+=pow(vec_esperado[i]-vec_estimado[i],2)
        suma=0.5*suma
        return suma
def calc_grad_error(vec_esperado,vec_estimado):
    if(len(vec_esperado)!=len(vec_estimado)):
        return
    else:
        gradiente=[]
        for i in range(len(vec_esperado)):
            gradiente.append(-(vec_esperado[i]-vec_estimado[i]))
        
        return gradiente

def hadaman_mult(mtx_1,mtx_2):
    #todo es np.array([vec_1,....,vec_n])
    #aunque sea np.array([[esc]])
    mtx_res=np.multiply(np.array(mtx_1),np.array(mtx_2))
    #devuelve una matriz del mismo tamaño que el shape
    
    rows=mtx_res.shape[0]
    
    cols=mtx_res.shape[1]
    
    mtx=[]
    for r in range(rows):
        row=[]
        for c in range(cols):
            row.append(mtx_res[r][c].item())
        mtx.append(row)
    return mtx
def mtx_mult(mtx_1,mtx_2):
    #todo es np.array([vec_1,....,vec_n])
    #aunque sea np.array([[esc]])
    np_mtx_1=np.array(mtx_1)
    np_mtx_2=np.array(mtx_2)
    if(len(mtx_1[0])==1 or len(mtx_2[0])==1):
        np_mtx_res=np.multiply(np_mtx_1,np_mtx_2)
    else:
        np_mtx_res=np.matmul(np_mtx_1,np_mtx_2)
    mtx_res=[]
    for r in range(len(np_mtx_res)):
            row=[]
            for c in range(len(np_mtx_res[0])):
                row.append(np_mtx_res[r][c].item())
            mtx_res.append(row)
    return mtx_res
def mtx_mult_vec(vec_1,vec_2):
    np_mtx_1=np.transpose(np.array(vec_1))
    np_mtx_2=np.array(vec_2)
    if(len(vec_1[0])==1 or len(vec_2[0])==1):
        np_mtx_res=np.multiply(np_mtx_1,np_mtx_2)
    else:
        np_mtx_res=np.matmul(np_mtx_1,np_mtx_2)
    mtx_res=[]
    for r in range(len(np_mtx_res)):
            row=[]
            for c in range(len(np_mtx_res[0])):
                row.append(np_mtx_res[r][c].item())
            mtx_res.append(row)
    return mtx_res
def esc_mtx(esc,mtx):
    mtx_res=[]
    for r in range(len(mtx)):
        row=[]
        for c in range(len(mtx[0])):
            num=esc*mtx[r][c]
            row.append(num)
        mtx_res.append(row)
    return mtx_res
def trasponer(mtx):
    rows=len(mtx)
    cols=len(mtx[0])
    t_mtx=[]
    for c in range(cols):
        row=[]
        for r in range(rows):
            row.append(mtx[r][c])
        t_mtx.append(row)
    return t_mtx

class NN:
    '''Implementacion de una red neuronal
        args:
            red_config:establece la arquitectura de la red, donde el primera elemento indica la cantidad de entradas
        la implementacion esta basada en el siguiente github que para mi tiene errores
        https://github.com/filipecalasans/mlp
        pero funciona a niveles didacticos
    '''
    def __init__(self,red_config):
       #vector que define la arquitectura de la red neuronal
       self.red_config=red_config
       #indice de la ultima capa para hacer mas faciles los calculos
       self.ultima_capa=len(red_config)-1
       #vector de matrices que definen los pesos por capa, cada fila representa un neurona y cada celda un peso
       self.pesos=[]
       #vector de listas cada elemento de una lista representa el bias de una nuerona
       #para cada fila de la lista de matrices de pesos existe un umbral asociados
       
       self.umbrales=[]
       #ambas listas anteriores son np.array
       self.create_pesos_umbrales()
    def create_pesos_umbrales(self):
        red_config=self.red_config
        #debe haber al menos 2 elementos en el red config
        if(len(red_config)<=1):
            return 
        
        for i in range(1,len(red_config)):
            capa=[]
            umbrales=[]
            num_entradas=red_config[i-1]
            num_neuronas=red_config[i]
            for n_n in range(num_neuronas):
                umbrales.append(rnd_peso())
                n=[]
                for n_e in range(num_entradas):
                    n.append(rnd_peso())
                capa.append(n)
            #hago estos deepcopy por si solo copian los punteross
            new_umb=deepcopy_numeros(umbrales)
            
            new_capa=deepcopy_lista_numeros(capa)
            self.umbrales.append(new_umb)
            self.pesos.append(new_capa)
    def fit(self,entry_set,output_set,max_epochs,e_error,tasa_aprendizaje=0.3,verbose=False):
        error=1
        iteraciones=0
        dist_error=1
        max_dist_error=e_error*0.0001
        #Por ahora la unica adaptacion de la tasa de aprendizaje es que cada 81 iteraciones
        #la divido 3/4 ¿Por que?Para jugar pero me gustaria un metodo menos arbitrarios,algo con el momentum
        while(True):
            last_error=error
            error=0
            for entrada_i in range(len(entry_set)):
                self.deltas=[]
                #calculo de las salida
                salida=self.output(entry_set[entrada_i])
                salida_esperada=output_set[entrada_i]
                #calculo de los errores
                entry_error=calculo_error(salida_esperada,salida)
                grad_error=calc_grad_error(salida_esperada,salida)
                #primero calculo los deltas y despues modifico
                #Los deltas tienen un sentido inversa a las capas porque se 
                delta_output=hadaman_mult([grad_error],self.derivadas_x_capa_x_neurona[self.ultima_capa-1])
                self.deltas.append(delta_output)
                for c in range(self.ultima_capa-2,-1,-1):
                    delta_size=len(self.deltas)
                    delta=hadaman_mult(mtx_mult(self.pesos[c+1],trasponer(self.deltas[delta_size-1])),self.derivadas_x_capa_x_neurona[c])
                    self.deltas.append(deepcopy_numeros(delta))
                #Se actualizan los pesos
                for c in range(len(self.pesos)):
                    mtx_entrada=mtx_mult_vec(self.deltas[self.ultima_capa-c-1],trasponer([self.last_entries_capa[c]]))
                    mtx_entrada=esc_mtx(tasa_aprendizaje,mtx_entrada)
       
                    delta=esc_mtx(tasa_aprendizaje,self.deltas[self.ultima_capa-c-1])
                    
                    delta=delta[0]
                    for n in range(len(self.pesos[c])):
                        self.umbrales[c][n]-=tasa_aprendizaje*delta[n]
                        for p in range(len(self.pesos[c][n])):
                            self.pesos[c][n][p]-=tasa_aprendizaje*mtx_entrada[n][p]
                      
                    
                error+=entry_error
            # if(iteraciones%100==0):
                # #una manera muy chota de adaptacion pero es un comnienzo
                # tasa_aprendizaje=tasa_aprendizaje*3/4
            dist_error=abs(error-last_error)
            if(verbose):
                print("iteraciones: "+str(iteraciones)+" error: "+str(error))
            if(iteraciones>=max_epochs):
                print("maximo iteraciones: "+str(iteraciones)+" error: "+str(error))
                break
            if(dist_error<=max_dist_error):
                print("maxima distancia error, iteraciones: "+str(iteraciones)+" error: "+str(error))
                break
            if(error<=e_error):
                print("Llegado al error deseado, iteraciones: "+str(iteraciones)+" error: "+str(error))
                break
            iteraciones+=1
    #feed forward
    def output(self,entry):
        #vector que representa las entradas por cada capa
        #donde cada lista de entrada esta asociada a la capa que los recibe
        #es util para el calculo de las derivadas
        
        self.last_entries_capa=[]
        #vector que almacena la primera derivada en cadena de cada neurona para el calculo de los pesos 
        self.derivadas_x_capa_x_neurona=[]
        salida_lista=entry
        
        #c de capa pero tiene los mismos elementos que la lista umbrales
        for c in range(len(self.umbrales)):
            self.last_entries_capa.append(deepcopy_numeros(salida_lista))
            new_salida=[]
            derivada_x_neurona=[]
            #n de neurona
            for n in range(len(self.pesos[c])):
                salida_neurona=self.umbrales[c][n]
                
                #p de pesos
                for p in range(len(self.pesos[c][n])):
                    salida_neurona+=self.pesos[c][n][p]*salida_lista[p]
                    
                
                new_salida.append(sigmoide(salida_neurona))
                derivada_x_neurona.append(der_sigmoide(salida_neurona))
           
            self.derivadas_x_capa_x_neurona.append([deepcopy_numeros(derivada_x_neurona)])
            salida_lista=deepcopy_numeros(new_salida)
        return salida_lista