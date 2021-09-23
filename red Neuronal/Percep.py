
from math import *
from random import *
def sigmoide(x):
    x=max(-200,x)
    return 1/(1+exp(-x))
def der_sigmoide(X):
    return sigmoide(x)*(1-simoide(x))
def tanh(x):
    x=max(-200,x)
    return (exp(x)-exp(-x))/(exp(x)+exp(-x))
def der_tanh(x):
    return 1-pow(tanh(x),2)
def float2bin(x):
    if(x>0.5):
        return 1
    else:
        return 0
class Neurona:
    '''Implementacion de una neurona para una red backpropagation
        arg:
            num_entradas:cuantas entradas tendra la neurona
            tasa_aprendizaje:factor por el que se multiplicara el error
    '''
    def __init__(self,num_entradas,tasa_aprendizaje):
        self.num_entradas=num_entradas
        self.tasa_aprendizaje=tasa_aprendizaje
        self.pesos=[]
        self.create_weights()
    #se inicializan los pesos de manera aleatoria
    def create_weights(self):
        self.bias=-1+2*random()
        for i in range(self.num_entradas):
            self.pesos.append(-1+2*random())
    #se da una salida segun la entrada y la funcionde acttivacion
    #se debe guardar la entrada para el backpropagation
    #y la salida tambien
    def output(self,vec_entrada):
        nsum=self.bias
        self.last_input=vec_entrada
        i=0
        for p in self.pesos:
            nsum+=p*vec_entrada[i]
            i+=1
        self.nsum=nsum
        return tanh(nsum)
    #metodo para ajustar los pesos, el der_error es la derivada del error segun la neurona
    def fit(self,der_error):
        self.bias=self.bias+self.tasa_aprendizaje*der_error*der_tanh(self.nsum)
        i=0
        for i in range(self.num_entradas):
            self.pesos[i]=self.pesos[i]+self.tasa_aprendizaje*der_error*der_tanh(self.nsum)*self.last_input[i]
            i+=1
    #metodo para calcular la derivada de error segun esta neurona
    def der_error_neuron(self,capa_siguiente,idx_neurona):
        der_error=0
        for next_n in  capa_siguiente.neuronas[i]:
            #Estas muy cerca tenes que encontrar la manera de acumular los val
            der_error+=VAL*der_tanh(next_n.nsum)*next_n.pesos[idx_neurona]
            i+=1
        return der_error
class Capa:
    '''Implementacion de la capa de una red neuronal
    args:
        num_entradas:cuantas neuronas tiene la capa anterior
        num_neuronas: cauntas neuronas tiene esta capa
        tasa_aprendizaje:factor de actualizacion de los pesos
    '''
    def __init__(self,num_entradas,num_neuronas,tasa_aprendizaje):
        self.num_entradas=num_entradas
        self.num_neuronas=num_neuronas
        self.neuronas=[]
        self.create_neuronas(tasa_aprendizaje)
    #inicializacion de las neuronas
    def create_neuronas(self,tasa_aprendizaje):
        for i in range(self.num_neuronas):
            self.neuronas.append(Neurona(self.num_entradas,tasa_aprendizaje))
    #feed forward
    def output(self,vec_entrada):
        salida=[]
        for n in self.neuronas:
            salida.append(n.output(vec_entrada))
        return salida
    #backpropagation
    def fit(self,vec_der_error):
        i=0
        for n in self.neuronas:
            #el vec_der_error es un vector que almacena las derivadas parciales del error segun cada neurona de esta capa
            if(type(vec_der_error)!=type([])):
                vec_der_error=[vec_der_error]
            n.fit(vec_der_error[i])
            i+=1
    #en este metodo se calcula vector de derivadas parciales la capa mas cerca del input        
    #el metodo varia si es la capa de salida o una capa escondidad
    #si vec_der_error es None entonces es la capa de salida sino es una capa escondida
    def cal_vec_der_error(self,capa_siguiente):
        #caso de la capa de salida. el vec_der_error es -(valor_esperdo-valor_obtenido)
        if(vec_der_error!=None):

            self.vec_der_error=vec_der_error
        #caso de una capa que no es la salida.Cada valor en este vec_der_error representa 
        #la derivada del error segun la neurona idx_neurona, cada neurona sera capaz de calcular su derivada parcial
    
        vec_der_error=[]
        idx_neurona=0
        for n in self.neuronas:
            #cada neurona se encarga de calcular su derivada parcial para el error, para ello requiere la capa siguiente
            #por eso es backpropagation
            vec_der_error.append(n.der_error_neuron(capa_siguiente,idx_neurona))
            idx_neurona+=1
        #aca se setea el valor
        self.vec_der_error=vec_der_error
            
class MultilayerPerceptron:
    '''Implementacion del perceptron multiplicapa
        args:
            red_config reprensenta la arquitectura de la red donde el primer valor define el numero de atributos de la entrada
    '''
    def __init__(self,red_config,tasa_aprendizaje=0.3):
        self.red_config=red_config
        self.create_capas(tasa_aprendizaje)
    def create_capas(self,tasa_aprendizaje):
        self.capas=[]
        num_capas=len(self.red_config)
        #Se le resta uno ya que el primer valor reprensenta el numero de entrada|
        for i in range(1,num_capas):
            self.capas.append(Capa(self.red_config[i-1],self.red_config[i],tasa_aprendizaje))
    #implementacion feedforward por eso la salida de una capa es la entrada de la siguiente
    def output(self,vec_entrada):
        i=0
        salida=self.capas[i].output(vec_entrada)
        i+=1
        for i in range(len(self.red_config)-1):
            salida=self.capas[i].output(salida)
        #antes de devolver la salida debo estandarizarla de 0 a 1
        #como la salida esta determinada por tanh entonces los valores comprenden de -1 a 1 
        #la formula de estandarizacion (valor-(min_value))/(max_value-min_value)
        new_salida=[]
        for s in salida:
            new_salida.append((s+1)/2)
        return new_salida
    '''Implementacion del backpropagation 
        args:
            ess:conjunto de entradas cada fila representa un set de entrada que corresponde a una fila del vector de salidas esperado
                los datos de este conjunto deben estar entre 0 a 1
            os:conjunto de valores en forma de lista de salida esperado, se pide que sea entre 0 y 1
            
            max_epochs:maximo de iteraciones permitidas
            e_error:maximo de error tolerable permite cortar el entrenamiento
            max_dist_error:mide el cambio de  error, sirve para el cambio de error entre epoch,por si no cambia mucho cortar
            verbose:habilita mostrar el entremiento por pantalla
    '''
    def fit(self,ess,os,max_epochs,e_error,verbose=False,max_dist_error=None):
        iteraciones=0
        error=1
        dist_error=1
        hay_dist_error=max_dist_error!=None
        true_while=iteraciones<=max_epochs and error>e_error
        if(hay_dist_error):
            true_while=true_while and dist_error>max_dist_error
        while(true_while):
            error=0
            i=0
            for entrada in ess:
                if(i==0):
                    error=abs(os[i]-float2bin(self.output(entrada)[0]))
                else:
                    error=error*(i-1)+abs(os[i]-float2bin(self.output(entrada)[0]))
                    error=error/i
                
                i+=1
            if(verbose):
                print("iteracion: "+str(iteraciones)+" error: "+str(error))
            
            iteraciones+=1
            true_while=iteraciones<=max_epochs and error>e_error
            if(hay_dist_error):
                true_while=true_while and dist_error>max_dist_error
            if(not(true_while)):
                if(iteraciones>max_epochs):

                    print("iteracion: "+str(iteraciones)+" error: "+str(error))
            
                    print("Se supero el numero de epochs")
                if(error<=e_error):

                    print("iteracion: "+str(iteraciones)+" error: "+str(error))

                    print("se alcanzo del nivel de error")
                break
            else:
                i=0
                for entrada in ess:
                    der_error=-(os[i]-self.output(entrada)[0])
                    ultima_capa=len(self.red_config)-2
                    self.capas[ultima_capa].fit(der_error)
                    #el metodo calcular vector error donde cada elemento representa esta asociado a una neurona de la capa anterior
                    for i in range(len(self.red_config)-3,1,-1):
                       #una capa requiere del vector error de derivadas parciales de la capa siguiente para actualizar sus pesos
                       self.capas[i].cal_vec_der_error(self.capas[i+1])

                       self.capas[i].fit(self.capas[i].vec_der_error)
                    if((len(self.red_config)-1)>2):
                        self.capas[i].cal_vec_der_error(self.capas[i+1])

                        self.capas[1].fit(self.capas[1].vec_der_error)
                        