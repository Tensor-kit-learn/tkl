'''
Created on Tue Dec 26 10:39:17 2020 
@author: <Fahim Ferdous>
@Email: <liveviewer360@gmail.com>
'''
import tkl.activations as activations


#Sets up the input neuron
def add_input(input):
  try:
    inp = int(input)
    return[inp]
  
  except TypeError:
    return(input)


#Sets up the hidden layer    
def add_hidden_layer(inputs=()):
  listed_inputs = str(inputs)[1:-1].replace('[','').replace(']','')
  listed_inputs = list(map(float,listed_inputs.split(',')))
  return(listed_inputs)


#Sets up the neuron  
def add_neuron(hidden_layer,activation,learning_rate=0,gamma=0.0,alpha=1.0):
  input_lar=[]
  input_lar.append(hidden_layer)
  Il = hidden_layer
  out = []
  for i in Il:
    i = int(float(i))
    main_out = activation(int(i),alpha+gamma)
    out.append(main_out)  
  return(out)


#Sets up the weights for our neural-network
def add_weights(x):
    if x == False:
      return(0)
      
    else:
        return(x)

#Sets up the learning rate for our neuron 
def learning_rate(rate):
  _rate =  rate=float(rate)
  return(_rate)       


#Adds an output neuron to our neural-network
def add_output(neuron,weights,biases,activation=activations.base):
  Out_ = []
  for num1 in range(len(neuron)):
    for num2 in range(len(weights)):
      x = neuron[num1]*weights[num2]
      Out_.append(x)
      break
  pass
      
  return(activation(sum(Out_)+biases))
  del Out_[:]


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
  
  