'''
Created on Tue Nov 29 16:52:42 2020 
@author: <Fahim Ferdous>
@Email: <liveviewer360@gmail.com>
'''
import tkl.activations

#Adds an input neuron to our neural-network
def add_input(input):
  try:
    return([float(input)])
    del input
  except TypeError:
    return(input)
    del input[:]
    
#Adds a neuron to our neural-network
def add_neuron(input_layer,activation,learning_rate=.001,gamma=0.0,alpha=1.0):
    input_lar=[]
    input_lar.append(input_layer)
    Il = input_layer
    out = []
    for i in Il:
        i = str(i)
        main_out = activation(float(i),alpha+gamma)
        out.append(main_out)
    return(out,learning_rate)
    del out[:]
    del Il
    del input_lar[:]
    
#Sets up the weights for our neural-network
def add_weights(x):
  return(x)
  del x
  

#Adds an output neuron to our neural-network
def add_output(neuron,weights,biases,activation=tkl.activations.base):
    Out_ = []
    try:
        neuron = neuron[0]
        for num1 in neuron:
            for num2 in weights:
              x = float(num1)*num2+biases
              Out_.append(x)
              break
        pass
    
    except:
        Out_.append(neuron[0]*weights+biases)
    
    return(activation(sum(Out_)))
    #del out

#for predicting
def predict(output1,output2,label1,label2,accuracy=False):
    def __predict__():
      if output1 > output2:
        return(label1)
        
      elif output1 < output2:
        return(label2)
        
      else:
          return(label1,label2)  
          
    def __main__():
      def __accuracy__(out):
        accuracy = "{0:.0%}".format(out/500.0)
        acc = float(accuracy.strip(' \t\n\r%'))
        if acc>100:
          return('99.9%')
        else:
          return(accuracy)   
        
      out1_accuracy = __accuracy__(output1)
      out2_accuracy = __accuracy__(output2)
      
      if accuracy == False:
        return(__predict__())
        
      elif accuracy == True:
        predict = __predict__()
        
        if predict == label1:
          return(predict,out1_accuracy)
          
        elif predict == label2:
          return(predict,out2_accuracy)        
      
        else:
            return(predict,out2_accuracy,out1_accuracy)
      
    return(__main__())




