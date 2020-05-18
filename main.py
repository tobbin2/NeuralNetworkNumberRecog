import numpy as np

class NeuralNetwork:

    def __init__(self, inputs, outputs):
        #inputs
        self.inputs = inputs

        #outputs
        self.outputs = outputs

        #weights one layer
        self.weights = np.zeros((self.inputs[0].size , 1))
        self.weightsL2 = np.zeros((self.inputs[0].size / 2, 1))


    def sigmoid(self, x, deriv=False):
        if(deriv == True):
            return x * ( 1 - x )
        return 1 / (1 + np.exp(-x))

    
def sigmoid(self, x, deriv=False):
        if deriv == True:
            return x * (1 - x)
        return 1 / (1 + np.exp(-x))

def feed_forward(self):
    self.hidden = self.sigmoid(np.dot(self.inputs, self.weights))

def backpropagation(self):
    self.error  = self.outputs - self.hidden #calc error
    delta = self.error * self.sigmoid(self.hidden, deriv=True) #calc error and deriv of hidden from feed_forward
    self.weights += np.dot(self.inputs.T, delta) #append it to weights for next iteration

def train(self, epochs=25000):
    for epoch in range(epochs):

        self.feed_forward()
        self.backpropagation()    

        self.error_history.append(np.average(np.abs(self.error)))
        self.epoch_list.append(epoch)

def predict(self, new_input):
    prediction = self.sigmoid(np.dot(new_input, self.weights))
    return prediction

    


