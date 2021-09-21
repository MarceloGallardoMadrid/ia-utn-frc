def vec_string_2_vec_float(vec_string):
    vec_float=[]
    for s in vec_string:
        vec_float.append(float(s))
    return vec_float
class Lector:
    def __init__(self,path):
        self.path=path
    def print_file(self):
        with open(self.path,"r") as archivo:
            for linea in archivo:
                print(linea)
    def leer_cant_lineas(self):
        f=open(self.path,"r")
        res=len(f.readlines())
        f.close()
        return res
    def leer_lineas(self):
        mtx=[]
        with open(self.path,"r") as archivo:
            row=[]
            for line in archivo:
                row=line.split()
                mtx.append(row)
                
        return mtx
        
    def leer_lineas_num(self,separetor):
        mtx=[]
        with open(self.path,"r") as archivo:
            row=[]
            for line in archivo:
                row=line.split(separetor)
                row=vec_string_2_vec_float(row)
                mtx.append(row)
                
        return mtx        
    def leer_lineas_max(self,lineas):
        mtx=[]
        i=0
        with open(self.path,"r") as archivo:
            row=[]
            for line in archivo:
                if(i<lineas):
                    row=line.split()
                    mtx.append(row)
                i+=1
        return mtx
    def leer_lineas_desde_hasta(self,desde,hasta):
        mtx=[]
        i=0
        with open(self.path,"r") as archivo:
            row=[]
            for line in archivo:
                if(i<hasta and i>=desde):
                    row=line.split()
                    mtx.append(row)
                i+=1
        return mtx
            
        
        