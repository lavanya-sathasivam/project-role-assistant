import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.neural_network import MLPClassifier
from sklearn.preprocessing import StandardScaler
from sklearn.pipeline import Pipeline
import pickle

df=pd.read_csv("dataset.csv")
X=df.drop("role",axis=1)
y=df["role"]

X_train,X_test,y_train,y_test=train_test_split(X,y,test_size=0.2,random_state=42)
model=Pipeline([
    ("scaler",StandardScaler()),
    ("mlp",MLPClassifier(hidden_layer_sizes=(32,16),max_iter=1000,random_state=42))
])

model.fit(X_train,y_train)
accuracy=model.score(X_test,y_test)
print("Model Accuracy:",accuracy)

with open("model.pkl","wb") as f:
    pickle.dump(model,f)
print("Model saved as model.pkl")