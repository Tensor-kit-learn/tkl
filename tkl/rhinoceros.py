'''
Created on Fri Apr 30 17:05:49 2020 
@author: <Fahim Ferdous>
@Email: <liveviewer360@gmail.com>
'''
#Sets up input node
class add_input():
  def __init__(self,input):
    self.inp = input
  
  def get(self):
    return(self.inp)

#Sets up a hidden layer
class add_hidden_layer():
  def __init__(self,input,id=None):
    self.input = [input.get()]
    self.id = str(id)
    self.neuron_outs = []
  
  #Creates a neuron with the id of the node
  def add_neuron(self,activation,learning_rate=0,gamma=0.0,alpha=1.0):
    input_lar=[]
    input_lar.append(self.input)
    out = []
    for i in self.input:
      i = int(float(i))+gamma
      main_out = activation(int(i),alpha)
      out.append(main_out)  
      
    self.neuron_outs.append([float(str(out)[1:-1])])
    #return(float(str(out)[1:-1]))
  
  #Returns the output of the node
  def get(self):
    return(self.neuron_outs)

#Sets up the output node
class add_output():
  def __init__(self,hidden_layer,weights,biases):
    self.layer = hidden_layer.get()
    self._weights = weights
    self._biases = biases
    
  def get(self):
    out = [self.layer[i] * self._weights[i]+[self._biases] for i in range(len(self.layer))]
    out = (str(out).replace('[','').replace(']',''))
    y = list(map(float,out.split(',')))
    return(sum(y)-self._biases)

#for predicting
def predict(hidden_layer1,hidden_layer2,label1,label2,accuracy=False):
    ac = accuracy
    
    def _predict():
      if hidden_layer1.get() > hidden_layer2.get():
        return(label1)
          
      elif hidden_layer1.get() < hidden_layer2.get():
        return(label2)
          
      else:
        return(label1,label2)  
    
    def accuracy(out):
      accuracy = "{0:.0%}".format(out/500.0)
      acc = float(accuracy.strip(' \t\n\r%'))
      if acc>100:
        return('99.9%')
      else:
        return(accuracy) 
        
    def main():
      out1_accuracy = accuracy(hidden_layer1.get())
      out2_accuracy = accuracy(hidden_layer2.get())
        
      if ac == False:
        return(_predict())
          
      elif ac == True:
        __predict = _predict()
          
        if __predict == label1:
          return(__predict,out1_accuracy)
              
        elif predict == label2:
          return(__predict,out2_accuracy)        
          
        else:
            return(__predict,out2_accuracy,out1_accuracy)      
    
    return(main())


add_input = add_input
add_hidden_layer = add_hidden_layer
add_output = add_output
predict = predict
