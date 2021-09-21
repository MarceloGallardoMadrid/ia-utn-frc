import math
class Matrix:
    def __init__(self,rows,cols):
        self.rows=rows
        self.cols=cols
        self.mtx=[]
    #cada lista dentro de la lista de vectores forma una fila
    #habria que verificar que el tamaño corresponda con el de las rows y cols
    def set_mtx(self,lista_vectores):
        for vec in lista_vectores:
            self.mtx.append(vec)
    #doble for trata de evitarlo
    def trans(self):
        t=Matrix(self.cols,self.rows)
        mtx=[]
        for c in range(self.cols):
            vec=[]
            for r in range(self.rows):
                vec.append(self.mtx[r][c])
            mtx.append(vec)
        t.set_mtx(mtx)
        return t
    def escalar_mult(self,esc):
        o=Matrix(self.rows,self.cols)
        mtx=[]
        for r in range(self.rows):
            vec=[]
            for c in range(self.cols):
                num=self.mtx[r][c]*esc
                vec.append(num)
            mtx.append(vec)
        o.set_mtx(mtx)
        return o
    def comb_mult_vec(self,vec):
        res=[]
        
        for j in range(self.cols):
            celda=vec[j]
            for i in range(self.rows):
                celda+=self.mtx[i][j]
            res.append(celda)
        return res
            
    #Esta multiplicacion representa el calculo de combinatoria entre 2 matrices
    #4 for da un toque de miedo 
    def comb_mult(self,other):
        #o_c other colums
        mtx=[]
        for o_c in range(other.cols):
            #o_r other rows
            col=[]
            
            for o_r in range(other.rows):
                #other celda
                o_celda=other.mtx[o_r][o_c]
                #s_c self cols
                for s_r in range(self.rows):
                    num=o_celda*self.mtx[s_r][o_r]
                    col.append(num)
            mtx.append(col)
        new_matrix=Matrix(other.cols,other.rows*self.rows)
        new_matrix.set_mtx(mtx)
        new_matrix=new_matrix.trans()
        return new_matrix
    #Multiplicacion de matrix con un vector columna en la que cada escalar de una fila del vector se multiplica por toda la fila homologa de la matrix
    def dist_mult(self,vec):
        m=Matrix(self.rows,self.cols)
        mtx=[]
        for r in range(self.rows):
            row=[]
            for c in range(self.cols):
                num=vec[r]*self.mtx[r][c]
                row.append(num)
            mtx.append(row)
        m.set_mtx(mtx)
        return m
    def toString(self):
        m="[\n"
        for r in range(self.rows):
            m+="[ "
            for c in range(self.cols):
                m+=str(mtx[r][c])+" "
            m+="]\n"
        m+="\n ]"
        return m
    def __str__(self):
        m="[\n"
        for r in range(self.rows):
            m+="[ "
            for c in range(self.cols):
                m+=str(self.mtx[r][c])+" "
            m+="]\n"
        m+="\n ]"
        return m        
    def row(self,idx):
        rw=[]
        for c in range(self.cols):
            rw.append(self.mtx[idx][c])
        return rw
    #si bien es una lista se debe tener en cuenta que representa una columna de la matrix
    def col(self,idx):
        cl=[]
        for r in range(self.rows):
            cl.append(self.mtx[r][idx])
        return cl
class Vector:
    def __init__(self,vec):
        self.vec=vec
    def __sub__(self,other):
        vec=[]
        for i in range(len(self.vec)):
            num=self.vec[i]-other.vec[i]
            vec.append(num)
        return Vector(vec)