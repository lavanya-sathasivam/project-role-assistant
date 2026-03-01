import torch
import torch.nn as nn
import torch.optim as optim
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import OneHotEncoder
from sklearn.metrics import accuracy_score
import joblib

df=pd.read_csv("neural_dataset.csv")
encoder=OneHotEncoder(sparse_output=False)
interest_enc=encoder.fit_transform(df[["Interest"]])
joblib.dump(encoder,"encoder.pkl")
numeric=df[["Programming","Communication","ProblemSolving","Leadership","Experience","TechnicalDepth"]]
X=pd.concat([pd.DataFrame(numeric),pd.DataFrame(interest_enc)],axis=1).values
y=df["Role"].values

X_train,X_test,y_train,y_test=train_test_split(X,y,test_size=0.2,random_state=42)
X_train=torch.tensor(X_train,dtype=torch.float32)
X_test=torch.tensor(X_test,dtype=torch.float32)
y_train=torch.tensor(y_train,dtype=torch.long)
y_test=torch.tensor(y_test,dtype=torch.long)

class RoleNet(nn.Module):
    def __init__(self):
        super(RoleNet, self).__init__()
        self.fc1=nn.Linear(10, 32)
        self.fc2=nn.Linear(32, 16)
        self.fc3=nn.Linear(16, 6)
        self.relu=nn.ReLU()
    def forward(self, x):
        x=self.relu(self.fc1(x))
        x=self.relu(self.fc2(x))
        x=self.fc3(x)
        return x
model=RoleNet()
loss=nn.CrossEntropyLoss()
optimizer=optim.Adam(model.parameters(),lr=0.001)
epoch=50
for i in range(epoch):
    model.train()
    output=model(X_train)
    l=loss(output,y_train)
    optimizer.zero_grad()
    l.backward()
    optimizer.step()
    if (i+1)%10==0:
        print(f"Epoch [{i+1}/{epoch}], Loss: {l.item():.4f}")
model.eval()
with torch.no_grad():
    test_outputs=model(X_test)
    a,predicted=torch.max(test_outputs,1)
    acc=accuracy_score(y_test,predicted)
print("y_test shape:", len(y_test))
print("predicted shape:", len(predicted))
print(f"\nTest Accuracy: {acc*100:.2f}%")
torch.save(model.state_dict(), "neural_model.pth")
print("Model saved successfully.")