import torch
import torch.nn as nn
import numpy as np
import joblib
import pandas as pd

class RoleNet(nn.Module):
    def __init__(self, input_size):
        super(RoleNet, self).__init__()
        self.fc1=nn.Linear(input_size, 64)
        self.fc2=nn.Linear(64, 32)
        self.fc3=nn.Linear(32, 16)
        self.fc4=nn.Linear(16, 6)
        self.relu=nn.ReLU()
    def forward(self, x):
        x=self.relu(self.fc1(x))
        x=self.relu(self.fc2(x))
        x=self.relu(self.fc3(x))
        x=self.fc4(x)
        return x
encoder=joblib.load("encoder.pkl")
scaler=joblib.load("scaler.pkl")
input_size=10
model=RoleNet(input_size)
model.load_state_dict(torch.load("neural_model.pth"))
model.eval()
rolemap={0:"Developer",1:"Designer",2:"Researcher",3:"Tester",4:"DevOps",5:"Manager"}
 
def predict_role(programming ,communication, problem_solving, leadership, experience, technical_depth, interest):
    numeric = pd.DataFrame([{"Programming": programming, "Communication": communication, "ProblemSolving": problem_solving, "Leadership": leadership, "Experience": experience, "TechnicalDepth": technical_depth }])
    numeric_scaled=scaler.transform(numeric)
    interest_encoded=encoder.transform(pd.DataFrame([{"Interest": interest}]))
    features= np.concatenate([numeric_scaled, interest_encoded], axis=1)
    features= torch.tensor(features, dtype=torch.float32)

    with torch.no_grad():
        output =model(features)
        probabilities= torch.softmax(output,dim=1)
        predicted_class= torch.argmax(probabilities).item()
        confidence =probabilities[0][predicted_class].item()
    role =rolemap[predicted_class]
    return role, round(confidence*100,2)
