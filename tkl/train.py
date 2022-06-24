import time

def adjust_weights(neuron,weights,biases,target,delay=3.5):
  def __output__(weights):
    Out_ = []
    for num1 in neuron[0]:
      for num2 in weights:
        x = float(num1)*num2+biases
        Out_.append(x)
        break
    pass
    return((sum(Out_)))
    del Out_[:]
    
  def fail_safe(W_list):
    w_set = set(W_list)
    contains_duplicates = len(W_list) != len(w_set)
    if contains_duplicates == True:
      return(W_list[len(W_list)-1])
    else:
      del W_list[:len(W_list)-5]
      #print(W_list)
      return(False)
      
    del w_set[:]
  
  def gravitational_algorithm(weights):
    WEIGHTS = [float(str(i)+".0"+str(i)) for i in range(0, len(weights))]
    progression_rate = 0.001
    div_state = 0
    count = 0
    W_LIST = [] #contains all the weights
    while True:
      my_logic = __output__(WEIGHTS)
      time.sleep(delay)
      
      #Fail safe system
      FS = fail_safe(W_LIST)
      
      if FS != False:
        return(FS)
        break
      
      else:
        W_LIST.append(str(WEIGHTS))
        
      # Generation divider
      if count >= 260000:
        count = 0
        div_state += 10
        progression_rate = progression_rate/int(div_state)
       
        
      #negitive neuron output
      if 0 > float(str(neuron[0])[1:-1]):
        if my_logic > target:
          for i in range(len(WEIGHTS)):
            WEIGHTS[i] += float(progression_rate)
        
        elif my_logic < target:
          for i in range(len(WEIGHTS)):
            WEIGHTS[i] -= float(progression_rate)        
        
        elif my_logic == target:
          break
        
      #positive neuron output  
      else:
        if my_logic > target:
          for i in range(len(WEIGHTS)):
            WEIGHTS[i] -= float(progression_rate)
        
        elif my_logic < target:
          for i in range(len(WEIGHTS)):
            WEIGHTS[i] += float(progression_rate)
      
        elif my_logic == target:
          break        

      count+=1
      
    return(WEIGHTS)
    
    
  return(gravitational_algorithm(weights))
