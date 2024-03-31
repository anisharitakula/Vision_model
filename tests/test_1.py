import pytest
import torch
import sys
sys.path.append('./src')

from evaluate import evaluate

def test_outputs(input_data):
    predictions=evaluate(input_data)
    assert torch.equal(predictions,torch.tensor([3,6,9,0]))
