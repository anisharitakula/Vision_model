import torch
from model import Net
import torch.nn.functional as F

def evaluate(input):
    net= Net()
    net.load_state_dict(torch.load('./models/model_1.pth'))
    with torch.no_grad():
        probabilities = F.softmax(net(input),dim=1)
        predictions= torch.argmax(probabilities,dim=1)
        print(predictions)
        return predictions
