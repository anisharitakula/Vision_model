import pytest
import sys
sys.path.append('./src')
print(sys.path)
from load_data import data_loading

@pytest.fixture
def input_data():
    trainloader=data_loading()
    first_batch_inputs, first_batch_labels = next(iter(trainloader))
    return first_batch_inputs





