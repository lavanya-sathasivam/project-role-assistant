import torch
import torch.nn as nn
import torch.optim as optim
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import OneHotEncoder ,StandardScaler
from sklearn.metrics import accuracy_score
import joblib

df=pd.read_csv("neural_dataset.csv")
encoder=OneHotEncoder(sparse_output=False)
interest_enc=encoder.fit_transform(df[["Interest"]])
joblib.dump(encoder,"encoder.pkl")
numeric=df[["Programming","Communication","ProblemSolving","Leadership","Experience","TechnicalDepth"]]
scaler = StandardScaler()
numeric_scaled = scaler.fit_transform(numeric)
joblib.dump(scaler, "scaler.pkl")
X = pd.concat([pd.DataFrame(numeric_scaled), pd.DataFrame(interest_enc)],axis=1).values
y=df["Role"].values

X_train,X_test,y_train,y_test=train_test_split(X,y,test_size=0.2,random_state=42,stratify=y)
X_train=torch.tensor(X_train,dtype=torch.float32)
X_test=torch.tensor(X_test,dtype=torch.float32)
y_train=torch.tensor(y_train,dtype=torch.long)
y_test=torch.tensor(y_test,dtype=torch.long)

class RoleNet(nn.Module):
    def __init__(self,input_size):
        super(RoleNet, self).__init__()
        self.fc1=nn.Linear(input_size, 64)
        self.fc2=nn.Linear(64, 32)
        self.fc3=nn.Linear(32, 16)
        self.fc4=nn.Linear(16, 6)
        self.relu=nn.ReLU()
        self.dropout=nn.Dropout(0.3)
    def forward(self, x):
        x=self.relu(self.fc1(x))
        x=self.dropout(x)
        x=self.relu(self.fc2(x))
        x=self.dropout(x)
        x=self.relu(self.fc3(x))
        x=self.dropout(x)
        x=self.fc4(x)
        return x
input_size=X_train.shape[1]
model=RoleNet(input_size)
class_counts=torch.bincount(y_train)
class_weights=1.0/class_counts.float()
class_weights=class_weights/class_weights.sum()
loss=nn.CrossEntropyLoss(weight=class_weights)
optimizer=optim.Adam(model.parameters(),lr=0.0005)
epoch=200
for i in range(epoch):
    model.train()
    output=model(X_train)
    l=loss(output,y_train)
    optimizer.zero_grad()
    l.backward()
    optimizer.step()
    if (i+1)%20==0:
        _, preds= torch.max(output,1)
        train_acc=(preds==y_train).float().mean()
        print(f"Epoch [{i+1}/{epoch}], Loss: {l.item():.4f}, Train Acc: {train_acc*100:.2f}%")
model.eval()
with torch.no_grad():
    test_outputs=model(X_test)
    a,predicted=torch.max(test_outputs,1)
    acc=accuracy_score(y_test.numpy(),predicted.numpy())
print(f"\nTest Accuracy: {acc*100:.2f}%")
torch.save(model.state_dict(), "neural_model.pth")
print("Model saved successfully.")