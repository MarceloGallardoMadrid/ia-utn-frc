from random import random
import math
from Matrix import *
def media(vec):
    return sum(vec)/float(len(vec))
def sigmoide(x):
    x=max(-200,x)
    res=1/(1+math.exp(-x))
    return res
def derSigmoide(x):
    res =sigmoide(x)
    return res*(1-res)
def dotProduct(xs,ys):
    sum=0
    n=len(xs)
    for i in range(n):
        sum+=xs[i]*ys[i]
    return sum
def escProduct(esc,xs):
    n=len(xs)
    for i in range(n):
        xs[i]=xs[i]*esc
def euclidian_norm(vec_1,vec_2):
    if(type(vec_1)==int):
        return abs(vec_1-vec_2)
    else:
        suma=0
        for i in range(len(vec_1)):
 
            suma+=pow(vec_1[i]-vec_2[i],2)
        return pow(suma,1/2)
def normalizar_mtx_esp(mtx):
    rows=len(mtx)
    cols=len(mtx[0])
    col_1=[]
    col_2=[]
    col_3=[]
    col_4=[]
    for i in range(rows):
        col_1.append(mtx[i][0])
        col_2.append(mtx[i][1])
        col_3.append(mtx[i][2])
        col_4.append(mtx[i][3])
    col_1=normalizar_vec_uni_bin(col_1)
    col_2=normalizar_vec_uni_bin(col_2)
    col_3=normalizar_vec_uni_bin(col_3)
    col_4=normalizar_vec_pois_bin(col_4)
    new_mtx=[]
    for i in range(rows):
        row=[]
        row.append(col_1[i])
        row.append(col_2[i])
        row.append(col_3[i])
        row.append(col_4[i])
        new_mtx.append(row)
    return new_mtx
def normalizar_norm(vec):
    maximo=max(vec)
    new_vec=[]
    for i in range(len(vec)):
        new_vec.append(vec[i]/maximo)
    norm=0
    for v in new_vec:
        norm+=v*v
    norm=maximo*pow(norm,1/2)
    for i in range(len(new_vec)):
        new_vec[i]=vec[i]/norm
    return new_vec
def normalizar_norm_mtx(mtx):
    rows=len(mtx)
    cols=len(mtx[0])
    col_1=[]
    col_2=[]
    col_3=[]
    col_4=[]
    for i in range(rows):
        col_1.append(mtx[i][0])
        col_2.append(mtx[i][1])
        col_3.append(mtx[i][2])
        col_4.append(mtx[i][3])
    col_1=normalizar_norm(col_1)
    col_2=normalizar_norm(col_2)
    col_3=normalizar_norm(col_3)
    col_4=normalizar_norm(col_4)
    new_mtx=[]
    for i in range(rows):
        row=[]
        row.append(col_1[i])
        row.append(col_2[i])
        row.append(col_3[i])
        row.append(col_4[i])
        new_mtx.append(row)
    return new_mtx    
def normalizar_vec_pois_bin(vec):
    minimo=min(vec)
    prom=media(vec)
    new_vec=[]
    for n in vec:
        if((n-minimo)>=(0.65*prom)):
            new_vec.append(1)
        else:
            new_vec.append(0)
    return new_vec
def normalizar_vec_uni_bin(vec):
    minimo=min(vec)
    maximo=max(vec)
    new_vec=[]
    intervalo=(maximo-minimo)
    for n in vec:
        if(n>=(0.5*intervalo+minimo)):
            new_vec.append(1)
        else:
            new_vec.append(0)
    return new_vec
def normalizar_vec(min_val,max_val,vec):
    minimo=min(vec)
    maximo=max(vec)
    intervalo=(maximo-minimo)
    new_vec=[]
    for v in vec:
        new_vec.append(min_val+(max_val-min_val)*(v-minimo)/intervalo)
    return new_vec
def normalizar_vec_bin(vec):
    vec=normalizar_vec(0,1,vec)
    for v in vec:
        num=1
        if(v<0.5):
            num=0
        new_vec.append(num)
    return new_vec
def normalizar_mtx(min_val,max_val,mtx):
    minimo=min(mtx[0])
    maximo=max(mtx[0])
    for vec in mtx:
        min_vec=min(vec)
        max_vec=max(vec)
        if(min_vec<minimo):
            minimo=min_vec
        if(max_vec>maximo):
            maximo=max_vec
    new_mtx=[]
    intervalo=(maximo-minimo)
    for i in range(len(mtx)):
        row=[]
        for j in range(len(mtx[0])):
            cell=min_val+(max_val-min_val)*((mtx[i][j]-minimo)/intervalo)
            row.append(cell)
        new_mtx.append(row)
    return new_mtx
    
def normalizar_mtx_bin(mtx):
    mtx=normalizar_mtx(0,1,mtx)
    new_mtx=[]
    for i in range(len(mtx)):
        row=[]
        for j in range(len(mtx[0])):
            cell=0
            if(mtx[i][j]>0.5):
                cell=1
            
            row.append(cell)
        new_mtx.append(row)
    return new_mtx
class Neurona:
    def __init__(self,numEntradas,alfa):
        self.pesos=[]
        self.numEntradas=numEntradas
        num=random()
        self.bias=-1+2*num
        self.alfa=alfa
        self.entradas=[]
        for i in range(numEntradas):
            num=-1+2*random()
            self.pesos.append(num)
    def output(self,entradas):
        ssum=self.bias
        self.entradas=entradas
        for i in range(self.numEntradas):
            ssum=ssum+entradas[i]*self.pesos[i]
        res=sigmoide(ssum)
        self.delta=res*(1-res) 
        self.salida=res
        return res
    #der_error es el valor numerico de la derivada del error segun la neurona
    def fit(self,der_error):
        i=0
        der_error=der_error[0]
        for i in range(len(self.pesos)):
            #es menos por que se dirige al lado contrario del error
            self.pesos[i]=self.pesos[i]+self.alfa*der_error*self.delta*self.entradas[i]
            i+=1
        self.bias=self.bias+self.alfa*der_error*self.delta
        
    def toString(self):
        m="u: "+str(round(self.bias,2))
        for p in self.pesos:
            m+=" p: "+str(round(p,2))
        return m
    
class Capa:
    def __init__(self,numEntradas,numNeuronas,alfa):
        self.neuronas=[]
        self.numEntradas=numEntradas
        self.salidas=[]
        self.last_input=[]
        self.capa_anterior=None
        self.capa_siguiente=None
        self.deltas=[]
        self.numNeuronas=numNeuronas
        self.matrix_pesos_derivada=Matrix(numNeuronas,numEntradas)
        self.vec_der_error=[]
        for i in range(numNeuronas):
            self.neuronas.append(Neurona(numEntradas,alfa))
    def set_vec_der_error(self,vec):
        self.vec_der_error=vec
    def set_capa_anterior(self,capa):
        self.capa_anterior=capa
    def set_capa_siguiente(self,capa):
        set_capa_siguiente=capa
    def output(self,entradas):
        salidas=[]
        self.last_input=entradas

        for i in range(self.numNeuronas):
            res=self.neuronas[i].output(entradas)
            salidas.append(res)
        return salidas
    def set_pesos_derivada(self):
        pass
    def calculate_deltas(self):
        dels=[]
        for n in self.neuronas:
            dels.append(n.delta)
        return dels
    #El error es un numero
    def fit(self,error):
        self.deltas=self.calculate_deltas()
        if(self.capa_siguiente==None):
            #La primera capa solo deberia actualizar los pesos
            #Primera capa de la salida a la entrada
            list_error=[error]
            for n in self.neuronas:
                n.fit(list_error)
            self.matrix_pesos_derivada=self.create_matrix_pesos_derivada()
            if(self.capa_anterior!=None):
                self.capa_anterior.set_vec_der_error(self.create_vec_der_error(self.matrix_pesos_derivada))
                self.capa_anterior.fit(error)           
        #la ultima capa solo se actualiza con el error
        elif(self.capa_anterior==None):
             self.fit_neurons(self.vec_der_error)

        else:
            self.fit_neurons(self.vec_der_error)
            self.matrix_pesos_derivada=self.create_matrix_pesos_derivada()
            vec=self.matrix_pesos_derivada.comb_mult_vec(self.vec_der_error)
            self.capa_anterior.set_vec_der_error(vec)
            self.capa_anterior.fit(error)
    def toString(self):
        m="";
        for n in self.neuronas:
            m+="|"+n.toString()+"\t"
        return m
    def fit_neurons(self,vec):
        for i in range(self.numNeuronas):
            n=self.neuronas[i]
            cl=vec[i]
            n.fit(cl)
    def create_matrix_pesos_derivada(self):
        m=Matrix(self.numNeuronas,self.numEntradas)
        mtx=[]
        for n in self.neuronas:
            row=[]
            for p in n.pesos:
                row.append(p)
            mtx.append(row)
        m.set_mtx(mtx)
        m=m.dist_mult(self.deltas)
        return m
    def create_vec_der_error(self,mtx):
        vec=[]
        for i in range(mtx.rows):
            celda=0
            for j in range(mtx.cols):
                celda+=mtx.mtx[i][j]
            vec.append(celda)
        return vec
#La variable alfa representa la tasa de aprendizajea
#max_error representa el maximo de error tolerable
#red_config representa como se distribuiran las neuronas en las capas        
#num_entradas representan el numero de entradas para aprender
#deberian ser configurable el min cambio de pesos y el min cambio de error
class Perceptron:
    def __init__(self,num_entradas,red_config,alfa,max_error):    
        self.entradas=[]
        #La primera capa debe coincidir con las entradas y la ultima con lpresenta la tasa de aprendizajea salida
        self.capas=[]
        self.pesos=[]
        self.num_entradas=num_entradas
        self.max_error=max_error
        self.alfa=alfa
        self.red_config=red_config;
        self.capas=[]
        self.min_cambio=0.1
        self.min_cambio_error=0.01
        n=len(red_config)
        for i in range(len(red_config)):
           if(i==0):
            capa=Capa(num_entradas,red_config[0],alfa)
           else:
            capa=Capa(red_config[i-1],red_config[i],alfa)
           if(i!=0):
            capa.set_capa_anterior(self.capas[i-1])
           self.capas.append(capa)
        for i in range(n-1):
            self.capas[i].set_capa_siguiente(self.capas[i+1])
    def output(self,entradas):
        salida=self.capas[0].output(entradas) 
        for i in range(1,len(self.red_config)):
            salida=self.capas[i].output(salida)
        return salida
    def bin_output(self,entradas):
        salida=self.capas[0].output(entradas)
        for i in range(1,len(self.red_config)):
            salida=self.capas[i].output(salida)
        salida_bin=[]
        for sal in salida:
            if(sal<0.5):
                salida_bin.append(0)
            else:
                salida_bin.append(1)
        return salida_bin
    #xss representa el conjunto de lista de entradas y ys la lista de salidas esperadas
    def learn(self,xss,ys):
        its=200
        it=0
        err=self.measure_error(xss,ys)
        vec=self.list_pesos()
        cambio_pesos=1
        dist_error=1
        while(err>self.max_error and it<its and cambio_pesos>self.min_cambio and dist_error>self.min_cambio_error ):    
            error_anterior=err
            numEntries=len(xss)
            self.pesos=vec
            for i in range(numEntries):
                
                self.output(xss[i])
                self.fit(xss[i],ys[i])
            err=self.measure_error(xss,ys)
            vec=self.list_pesos()
            cambio_pesos=euclidian_norm(self.pesos,vec)
            dist_error=abs(err-error_anterior)
            it+=1
        if(cambio_pesos<=self.min_cambio):
            print("Se encontro un minimo local")
        if(dist_error<=self.min_cambio_error):
            print("no hay mucho cambio de error")
            print("dist_error: "+str(dist_error))
        if(it>=its):
            print("no se que paso")
            print("hicieron falta: "+str(it)+" iteraciones")
        else:
            print("hicieron falta: "+str(it)+" iteraciones")
    #y hat representa la salida esperada que por ahora es un solo valor por entrada
    def measure_error(self,entradas,y_hat):
        sum_error=0
        for i in range(len(entradas)):
            
            err=euclidian_norm(self.output(entradas[i]),y_hat[i])
            sum_error+=err
        sum_error=pow(sum_error,1/2)
        return sum_error
    #xs es una lista de entradas  y corresponde a la salida correspondiente,(a priori sera con una salida(
    def fit(self,xs,y):
        
        salida=self.output(xs)
        for i in range(len(salida)):        
            error=y[i]-salida[i]         
            n=len(self.red_config)
            self.capas[n-1].fit(error)
    def list_pesos(self):
        pesos=[]
        for c in self.capas:
            for n in c.neuronas:
                for p in n.pesos:
                    pesos.append(p)
        return pesos
    def toString(self):
        m="*"
        for c in self.capas:
            m+=c.toString()+"\n"+"*"
        return m
    
    