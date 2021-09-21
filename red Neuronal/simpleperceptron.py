from math import *
from random import *
def sig(x):
    x=max(-500,x)
    return 1/(1+exp(-x))
class SimplePerceptron:
    def __init__(self,num_entradas,alfa,max_error):
        self.num_entradas=num_entradas
        self.pesos=[]
        num=random()
        self.bias=num
        self.alfa=alfa
        self.max_error=max_error
        
        for i in range(num_entradas):
            num=random()
            self.pesos.append(num)
    def output(self,entrada):
        suma=0
        self.last_input=entrada
        for i in range(self.num_entradas):
            suma=suma+self.pesos[i]*entrada[i]
        suma=suma+self.bias
        res=sig(suma)
        self.delta=res*(1-res)
        return res
    def measure_error(self,vec_1,vec_2):
        error=0
        for i in range(len(vec_1)):
            error=pow(vec_1[i]-vec_2[i],2)
        error=pow(error,1/2)
        return error
    def fit(self,entrada,salida):
        error=salida-self.output(entrada)
        for i in range(len(self.pesos)):
            self.pesos[i]=self.pesos[i]+self.alfa*error*self.delta*entrada[i]
        self.bias=self.bias+self.alfa*error*self.delta
    def learn(self,entradas,salidas):
        its=100000
        it=0
        salidas_out=[]
        for i in range(len(entradas)):
            salidas_out.append(self.output(entradas[i]))
        error=self.measure_error(salidas_out,salidas)
        while(error>self.max_error and it<its):
            for i in range(len(entradas)):
                self.fit(entradas[i],salidas[i])
            
            it+=1
        if(it>=its):
            print("algo salio mal")
        else:
            print("salio bien")
    def toString(self):
        m="|b: "+str(self.bias)
        for p in self.pesos:
            m+=" p: "+str(p)
        return m