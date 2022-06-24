import numpy as np



def sigmoid(x,y=None):
    return 1.0 / (1 + np.exp(-x))
  

def ReLU(x,y=None):
    return x * (x > 0)


def leaky_ReLU(x,y=None):
    if x <= 0.0:
      return(0.01*x)
    else:
      return(x)  


def dReLU(x,y=None):
    return 1 if x > 0 else 0
  

def swish(x,y=None):
    return x * 1 / (1 + np.exp(-x))
  
   
def softmax(x,y=None):
    e_to_the_y_j = np.exp(x)
    return e_to_the_y_j / np.sum(e_to_the_y_j)
    
   
def tanh(x,y=None):
    return (np.exp(x) - np.exp(-x)) / (np.exp(x) + np.exp(-x))
  
 
def dtanh(x,y=None):
    def tanh(x):
        return (np.exp(x) - np.exp(-x)) / (np.exp(x) + np.exp(-x))
    return 1 - np.power(tanh(x), 2)
  
 
def elu(x,alpha=1.0):
    return x if x >= 0 else alpha*(x^x -1)
  

def delu(x,alpha=1.0):
    return 1 if x > 0 else alpha*np.exp(x)
  

def base(x,y=None):
    return(x*1)


def linear(x,y=None):
    return(4*x)


def binary(x,y=None):
    if x<0:
        return(0)
    else:
        return(1)