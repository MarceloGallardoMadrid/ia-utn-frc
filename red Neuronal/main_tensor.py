from main import *
from lectorcsv import *
import numpy as np
import pyrenn as prn
def model_simple_pyrenn():
    es=np.transpose(np.array([[0,0],[1,0],[0,1],[1,1]]))
    os=np.array([0,1,1,0])
    net=prn.CreateNN([2,2,1])
    net=prn.train_LM(es,os,net,verbose=True,k_max=100,E_stop=1e-2)
    print(prn.NNOut(es,net))
    
def model_ia_pyrenn():
    train_size=1000
    lec=Lector("X_norm")
    es=lec.leer_lineas_num_desde_hasta(0,train_size," ")
    es=np.transpose(np.array(es))
    lec=Lector("Y.csv")
    os=lec.leer_lineas_num_desde_hasta(0,train_size,",")
    new_os=[]
    for o in os:
        new_os.append(o[0])
    os=np.array(new_os)
    net=prn.CreateNN([4,10,10,10,10,10,10,10,10,10,1])
    print("training..")
    net=prn.train_LM(es,os,net,verbose=False,k_max=500,E_stop=1e-4)
    y=prn.NNOut(es,net)
    bin_y=[]
    for mini_y in y:
        if(mini_y<0.5):
            bin_y.append(0)
        else:
            bin_y.append(1)
    error=0
    i=0
    for o in os:
        if(i==0):
            error=abs(o-bin_y[i])
        else:
            error=(i-1)*error+abs(o-bin_y[i])
            error=error/i
        i+=1
    print("Error en los valores de entrenamiento: "+str(error))
    print("primer test")
    #otro set de testeo
    test_size=200
    test_offset=200
    lec=Lector("X_norm")
    es=lec.leer_lineas_num_desde_hasta(test_offset,test_offset+test_size," ")
    es=np.transpose(np.array(es))
    lec=Lector("Y.csv")
    os=lec.leer_lineas_num_desde_hasta(test_offset,test_offset+test_size,",")
    new_os=[]
    for o in os:
        new_os.append(o[0])
    os=np.array(new_os)
    y=prn.NNOut(es,net)
    bin_y=[]
    for mini_y in y:
        if(mini_y<0.5):
            bin_y.append(0)
        else:
            bin_y.append(1)
    error=0
    i=0
    for o in os:
        if(i==0):
            error=abs(o-bin_y[i])
        else:
            error=(i-1)*error+abs(o-bin_y[i])
            error=error/i
        i+=1
    print("Error en los valores de testeo: "+str(error))
    print("segundo test")
    #otro set de testeo
    test_size=500
    test_offset=500
    lec=Lector("X_norm")
    es=lec.leer_lineas_num_desde_hasta(test_offset,test_offset+test_size," ")
    es=np.transpose(np.array(es))
    lec=Lector("Y.csv")
    os=lec.leer_lineas_num_desde_hasta(test_offset,test_offset+test_size,",")
    new_os=[]
    for o in os:
        new_os.append(o[0])
    os=np.array(new_os)
    y=prn.NNOut(es,net)
    bin_y=[]
    for mini_y in y:
        if(mini_y<0.5):
            bin_y.append(0)
        else:
            bin_y.append(1)
    error=0
    i=0
    for o in os:
        if(i==0):
            error=abs(o-bin_y[i])
        else:
            error=(i-1)*error+abs(o-bin_y[i])
            error=error/i
        i+=1
    print("Error en los valores de testeo("+str(test_size)+"): "+str(error))
    #otro set de testeo
    test_size=1000
    test_offset=1000
    lec=Lector("X_norm")
    es=lec.leer_lineas_num_desde_hasta(test_offset,test_offset+test_size," ")
    es=np.transpose(np.array(es))
    lec=Lector("Y.csv")
    os=lec.leer_lineas_num_desde_hasta(test_offset,test_offset+test_size,",")
    new_os=[]
    for o in os:
        new_os.append(o[0])
    os=np.array(new_os)
    y=prn.NNOut(es,net)
    bin_y=[]
    for mini_y in y:
        if(mini_y<0.5):
            bin_y.append(0)
        else:
            bin_y.append(1)
    error=0
    i=0
    for o in os:
        if(i==0):
            error=abs(o-bin_y[i])
        else:
            error=(i-1)*error+abs(o-bin_y[i])
            error=error/i
        i+=1
    print("Error en los valores de testeo("+str(test_size)+"): "+str(error))
    #otro set de testeo
    print("tercer test")
    test_size=5000
    test_offset=5000
    lec=Lector("X_norm")
    es=lec.leer_lineas_num_desde_hasta(test_offset,test_offset+test_size," ")
    es=np.transpose(np.array(es))
    lec=Lector("Y.csv")
    os=lec.leer_lineas_num_desde_hasta(test_offset,test_offset+test_size,",")
    new_os=[]
    for o in os:
        new_os.append(o[0])
    os=np.array(new_os)
    y=prn.NNOut(es,net)
    bin_y=[]
    for mini_y in y:
        if(mini_y<0.5):
            bin_y.append(0)
        else:
            bin_y.append(1)
    error=0
    i=0
    for o in os:
        if(i==0):
            error=abs(o-bin_y[i])
        else:
            error=(i-1)*error+abs(o-bin_y[i])
            error=error/i
        i+=1
    print("Error en los valores de testeo ("+str(test_size)+"): "+str(error))
    #otro set de testeo
    print("cuarto test")
    test_size=10000
    test_offset=10000
    lec=Lector("X_norm")
    es=lec.leer_lineas_num_desde_hasta(test_offset,test_offset+test_size," ")
    es=np.transpose(np.array(es))
    lec=Lector("Y.csv")
    os=lec.leer_lineas_num_desde_hasta(test_offset,test_offset+test_size,",")
    new_os=[]
    for o in os:
        new_os.append(o[0])
    os=np.array(new_os)
    y=prn.NNOut(es,net)
    bin_y=[]
    for mini_y in y:
        if(mini_y<0.5):
            bin_y.append(0)
        else:
            bin_y.append(1)
    error=0
    i=0
    for o in os:
        if(i==0):
            error=abs(o-bin_y[i])
        else:
            error=(i-1)*error+abs(o-bin_y[i])
            error=error/i
        i+=1
    print("Error en los valores de testeo("+str(test_size)+"): "+str(error))

def main():
    model_simple_pyrenn()
if __name__=="__main__":
    main()