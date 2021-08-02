![template](https://user-images.githubusercontent.com/79488582/120871148-de31ac00-c568-11eb-91ee-d9a8690f8af7.png)


# What is Tkl
Tkl is a machine learning platform coded in python, it uses an easy-to-use framework. It's also very lite weight, which means it can run on low-end pc, tablets, phones, etc...



# Why Tkl?
```
Tkl is a very lite weight machine learning libary it runs off the `CPU`. 
*Currently has no support for `GPU`
```

# Installation
```
[tkl-lite]: https://drive.google.com/file/d/1EPojFMeBpxBwtM6hRvZxzTlImn7tkYaB/view?usp=sharing (Great option for phones, tablets, etc)
[tkl-full]: N/A(Great option for PC's)
```


```
**How to install on PC** : 
1). install `[tkl-full]` from `https://`
2). unzip the file you installed (tkl-full.zip)

#ANACONDA
If you are using conda, Place the unziped file in the directory: `C:\ProgramData\Anaconda3\Lib`

#IDLE
If you are using IDLE, Place the unziped file in the directory: `C:\Users\{SYSYTEM USRNAME}\AppData\Local\Programs\Python\Python39\Lib`

```



# Try your first Tkl program
```python
from tkl import *
import random


#// setting up the inputs
input1 = NN.add_input(random.uniform(0, 1))
input2 = NN.add_input(random.uniform(0, 1))
input3 = NN.add_input(random.uniform(0, 1))
input4 = NN.add_input(random.uniform(0, 1))

#// setting up the layers  
neuron1 = NN.add_neuron(input1,activations.ReLU,0.0001,alpha=2.0,gamma=-1.2)
neuron2 = NN.add_neuron(input2,activations.ReLU,0.001,alpha=2.0,gamma=-1.2)
neuron3 = NN.add_neuron(input3,activations.ReLU,0.001,alpha=2.0,gamma=-1.2)
neuron4 = NN.add_neuron(input4,activations.ReLU,0.001,alpha=2.0,gamma=-1.2)
#//seting up the outputs

output1 = NN.add_output(neuron1,[1.1,2,-2,1],1)
output2 = NN.add_output(neuron2,[0.2,2,-2,1],1)
output3 = NN.add_output(neuron3,[0.3,2,-2,1],1)

```
# Modules support
|  Name | Version | Description |
| ------------- | ------------- | ------------- |
| `tkl.NN()`  |1.1.4|   `create simple neural networks`|
| `tkl.activations()` |1.2.7| `activation functions for the neural network` |
| `tkl.koala()`  |1.1.3|   `create deep networks `|
| `tkl.islands()` |1.1.2|   `dataset for tkl`|
| `tkl.tkboard()`  |1.1.1|   `create simple graphs based on neural network`|
| `tkl.train()`  |0.1.0|   `trains a Neural network/Deep network`|
| `tkl.rhinoceros()`  |0.0.1|   `create neural networks & deep networks`|

# Release Note
```
[1.11]:[base/root of tkl, added NN]
[1.12]:[tkl.koala was added]
[1.13]:[tkl.activations were added]
[1.14]:[tkl.koala removed for maintenance]
[1.15]:[tkl.koala was updated and added back]
[1.16]:[tkl.islands was added]
[1.17]:[tkl.islands,tkl.koala were improved]
[1.18]:[BUG fixes,fixed tkl.NN, koala improved,added tkboard]
[1.19]:[Added Train,Rhinoceros tkl.NN.add_input()/tkl.koala.add_input() array can be used]
```



# Credits

**Fahim Ferdous (Creator of Tkl)**


