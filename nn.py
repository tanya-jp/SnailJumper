import numpy as np


class NeuralNetwork:

    def __init__(self, layer_sizes):
        """
        Neural Network initialization.
        Given layer_sizes as an input, you have to design a Fully Connected Neural Network architecture here.
        :param layer_sizes: A list containing neuron numbers in each layers. For example [3, 10, 2] means that there are
        3 neurons in the input layer, 10 neurons in the hidden layer, and 2 neurons in the output layer.
        """
        # TODO (Implement FCNNs architecture here)
        self.w = []
        self.b = []
        center = 0
        margin = 1

        # allocate random normal W matrix and zero b vector for each layer.
        for i in range(1, len(layer_sizes)):
            # draw random samples from a normal (Gaussian) distribution
            w = np.random.normal(center, margin, size=(layer_sizes[i], layer_sizes[i - 1]))
            self.w.append(w)
            # zero bias vector
            b = np.zeros((layer_sizes[i], 1))
            self.b.append(b)


    def activation(self, x, activation_function="sigmoid"):
        """
        The activation function of our neural network, e.g., Sigmoid, ReLU.
        :param x: Vector of a layer in our network.
        :return: Vector after applying activation function.
        """
        # TODO (Implement activation function here)
        if activation_function == "ReLU":
            return max(0, x)
        elif activation_function == "softmax":
            return np.exp(x) / np.exp(x).sum()
        else:
            return 1 / (1 + np.exp(-x))


    def forward(self, x):
        """
        Receives input vector as a parameter and calculates the output vector based on weights and biases.
        :param x: Input vector which is a numpy array.
        :return: Output vector
        """
        # TODO (Implement forward function here)

        for i in range(len(self.w)):
            x = self.activation(self.w[i] @ x + self.b[i], "softmax")
        return x

