import numpy as np

def sigmoid(x):
    return 1 / (1 * np.exp(-x))

def sigmoid_deriv(x):
    return x * (1 - x)


training_input = np.array([[0, 0, 1],  # 0
                           [1, 1, 1],  # 1
                           [1, 0, 1],  # 1
                           [0, 1, 1]])  # 0

training_out = np.array([[0, 1, 1, 0]]).T  # Expected results from array for training

np.random.seed(1)

synapse_weights = 2 * np.random.random((3, 1)) - 1

print('Random Starting Synapse Weight: ')
print(synapse_weights)

for iterate in range(20000):
    input_layer = training_input
    output = sigmoid(np.dot(input_layer, synapse_weights))

    error = training_out - output
    adjust = error * sigmoid_deriv(output)
    synapse_weights += np.dot(input_layer.T, adjust)

print('Synapse weight after training: ')
print(synapse_weights)


print('Outputs after training: ')
print(output)
