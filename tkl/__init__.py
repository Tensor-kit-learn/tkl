"""
Tkl is a high level machine-learning library that includes of:

* NN
* Activation functions
* Koala
* Islands
* tkboard
* Train
* Rhinoceros

Created on Tue Nov 24 21:39:02 2020 
@author: <Fahim Ferdous>
"""
from tkl.NN import add_input
from tkl.NN import add_neuron
from tkl.NN import add_output
from tkl.NN import add_weights
from tkl.koala import add_input
from tkl.koala import add_hidden_layer
from tkl.koala import add_neuron
from tkl.koala import add_output
from tkl.koala import add_weights
from tkl.activations import sigmoid
from tkl.activations import ReLU
from tkl.activations import leaky_ReLU
from tkl.activations import dReLU
from tkl.activations import swish
from tkl.activations import softmax
from tkl.activations import tanh
from tkl.activations import dtanh
from tkl.activations import elu
from tkl.activations import delu
from tkl.activations import base
from tkl.activations import linear
from tkl.activations import binary
from tkl.islands import dataset
from tkl.islands import predictors
from tkl.tkboard import init
from tkl.tkboard import render
from tkl.rhinoceros import add_input
from tkl.rhinoceros import add_hidden_layer
from tkl.rhinoceros import add_output
from tkl.train import adjust_weights


def __version__():
  versions = ['1.2.0','1.1.4','1.2.7','1.1.3','1.1.2','1.1.1','0.1.0','0.0.1']
  labels = ["tkl","tkl.NN","tkl.activations","tkl.koala","tkl.islands","tkl.tkboard","tkl.train","tkl.rhinoceros"]
  for v in range(len(versions)):
      print(str(labels[v])+"=="+str(versions[v]))