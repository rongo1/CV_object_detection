import torch 
import torch.nn as nn 

from utils import intersection_over_union


class YoloLoss(nn.Module):
    def __init__(self, S = 7, B = 2, C = 20):
        super(YoloLoss, self).__init__()
        self.mse = nn.MSELoss(reduction=loss)
        self.S = S
        self.B = B
        self.C = C
        self.lambda_noobj = 0.5
        self.lambda_coord = 5
    

