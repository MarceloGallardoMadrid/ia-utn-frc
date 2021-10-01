import numpy as np
import NN as nn
from NN import *
def simple_nn_xor():
    print("simple perceptron")
    net=nn.NN([2,3,3,3,3,3,1])
    es=[[1,1],[0,1],[1,0],[0,0]]
    os=[[0],[1],[1],[0]]
    for e in es:
        print(net.output(e))
    print("learn")
    net.fit(es,os,500,0.1,0.5,True)
    for e in es:
        print(net.output(e))
def mult_test():
    vec_1=[1,1]
    vec_2=[2,3]
    #print(hadaman_mult(vec_1,vec_2))
    mtx=[[1,0],[0,1]]
    mtx_2=[[1,2],[3,4]]
    print(mtx_mult_vec_vec(vec_1,vec_2))
    print(mtx_mult(mtx,mtx_2))
def main():
    simple_nn_xor()
if __name__=="__main__":
    main()