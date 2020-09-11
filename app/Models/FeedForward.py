import torch
import torch.nn as nn
import torch.nn.functional as F

input_shape = 1*28*28
hidden_shape = 512
output_shape = 10

class MNIST_FeedForward(nn.Module):
    def __init__(self):
        super(MNIST_FeedForward , self ).__init__()
        self.fc1 = nn.Linear(input_shape , hidden_shape)
        self.relu = nn.ReLU()
        self.fc2 = nn.Linear(hidden_shape , output_shape)

    def forward(self , images):
        print(images.shape)
        images = images.reshape(-1 , input_shape)
        hidden = self.fc1(images)
        relu = self.relu(hidden)
        output = self.fc2(relu)
        return output

