import torch
import torch.nn as nn
import torch.nn.functional as F

input_size = 1*28*28
num_classes = 10

class MNISTModel(nn.Module):
    def __init__(self):
        super().__init__()
        self.linear = nn.Linear(input_size , num_classes)
    
    def forward(self , xb):
        xb = xb.reshape(-1 , input_size)
        out = self.linear(xb)
        return out