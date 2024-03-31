import sys
import torch
sys.path.append('./src')

from load_data import data_loading

trainloader=data_loading()

def test_input():
    input,label=next(iter(trainloader))
    assert torch.equal(label,torch.tensor([9,7,8,2]))

