![template](https://user-images.githubusercontent.com/79488582/120871148-de31ac00-c568-11eb-91ee-d9a8690f8af7.png)


# What is Tkl
Tkl is a machine learning (ML) platform developed in python. It is an easy-to-use lite weight ML framework. It can run on low-end pc, tablets, androide devices etc.

# Why Tkl?
```
Tkl is a very lite weight machine learning libary it runs off the `CPU`. 
*The current version (v 1.19 alplha) does not support the `GPU`
```

# Installation
```
[tkl-lite]: https://drive.google.com/file/d/1EPojFMeBpxBwtM6hRvZxzTlImn7tkYaB/view?usp=sharing (Great option for androide devices.)
[tkl-full]: https://drive.google.com/drive/folders/1NcWBs7T9J1kGEyddR7MuRZFWtQaFDdfl?usp=sharing (Great option for PC's)
```

# Run `TKL` in your browser!
https://trinket.io/library/trinkets/4ed462b480

# Try your first Tkl program (example code)
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

# How to install on PC
```
1) download `[tkl-full].zip` from `https://drive.google.com/drive/folders/1NcWBs7T9J1kGEyddR7MuRZFWtQaFDdfl?usp=sharing`
2) unzip the file you installed (tkl-full.zip)
3) Move unzipped folder to the right path:

#ANACONDA
If you are using conda, place the unzipped files folder in the directory: `C:\ProgramData\Anaconda3\Lib`

#IDLE
If you are using IDLE, place the unzipped files folder in the directory: `C:\Users\{SYSYTEM USRNAME}\AppData\Local\Programs\Python\Python39\Lib`

```

# How to install on android and ios
```
1) download `[tkl-lite].py` from `https://drive.google.com/file/d/1EPojFMeBpxBwtM6hRvZxzTlImn7tkYaB/view?usp=sharing`
2) open the IDE of your choice, check if tkl is working using `import tkl`
```

# Credits
**Fahim Ferdous (Developer of Tkl)**
