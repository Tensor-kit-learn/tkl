import numpy.random as random
import re

class dataset:
    #Creates a dataset
    def create(name):
      name = name.lower()
      if '.txt' in name:
        raise Exception('please do not add any sort of file extensions')
        
      else:
        dataset = open((str(name)+'.txt'),'a')
        return(dataset)
    
    #writes records/data in the dataset
    def write(file,class_name,T_F,current_time=False):
      import time
      def __write__(dataset,CN,TF,CT):
            out = 0
            if T_F==True:out = True
            else:out=False
            
            if CT == True:
              t = time.localtime()
              c_time = time.strftime("%H:%M:%S", t)
              data_cell = dataset.write('['+str(c_time)+'|'+str(CN)+'|'+str(out)+'] \n')
              
            elif CT == False:
              data_cell = dataset.write('['+str(time.time())+'|'+str(CN)+'|'+str(out)+'] \n')
              
      file = file+'.txt'
      name = open(file,'a')
      if T_F == True:
        __write__(name,class_name,T_F,current_time)
      
      elif T_F == False:
        false_class_name = str(class_name)+'f'
        __write__(name,false_class_name,T_F,current_time)
          
      
      return(name)
    
    #clears dataset
    def clear(dataset,auto_warning=False):
      
      if auto_warning == False:
        raise Warning('[Auto warning]: if you clear your dataset noting can be found again.')
      
      if auto_warning == True:
        dataset = open(dataset,'w')
        dataset.write('')
    
    #reads dataset
    def read(dataset):
      dataset = dataset+'.txt'
      with open(dataset,'r') as ds:
        return(ds.read())
    
    #loas dataset for the predictor
    def load(dataset, class_names):
        find = class_names
        with open(dataset, 'r') as txt:
            contents = txt.read()
        
        word_counts = {}
        tokens = re.findall('\w+', contents)
        tokens = [token.lower() for token in tokens]
        find = [s.strip().lower() for s in find]
        
        for f in find:
          count = 0
          for t in tokens:
            if t == f:count +=1
          word_counts[f] = count
            
        return word_counts
    
    


class predictors:
    #Charles gives a weighted output based on your file/dataset
    def Charles(loaded_dataset):
      try:
        data = loaded_dataset
        results = random.choice([k for k in data for dummy in range(data[k])])
        return(results)
          
      except Exception:
        raise Warning('Unable to load dataset properly')  
        
