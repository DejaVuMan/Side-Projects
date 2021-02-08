#      The goal of this small project is to successfully create a neural network capable of
# guessing what the result should be from previous information.
#
# EXAMPLE:
#       Inputs      Outputs
# 1     0 0 1       0
# 2     1 1 1       1
# 3     1 0 1       1
# 4     0 1 1       0
# 5?    1 0 0       ???
#            Guess This output
# In this example, if the first input is 1, the output should be 1.
#
# This is a Perceptron net? No inner layers.
#   INPUTS SYNAPSES NEURON      OUTPUT
#   x1 ----w1--------\
#                    /|\
#   x2---w2-------->|   |=======[==[]
#                   |   |
#   x3---w3--------/ \|/
#       wn is the weight of the synapse importance
#   xn is the input value
#           Neurons calculate the output by getting a weighted sum of the inputs, then getting normalized
#           In this example, we use the sigmoid function to normalize.

