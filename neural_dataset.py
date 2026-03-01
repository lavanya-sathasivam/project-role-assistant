import pandas as pd
import random
def generate():
    programming=random.randint(1,10)
    communication=random.randint(1,10)
    problem_solving=random.randint(1,10)   
    leadership=random.randint(1,10)
    experience=random.randint(0,5)
    technical_depth=random.randint(1,10)
    interest=random.choice(["Coding","Design","Research","Management"])

    if interest=="Coding" and programming>7:
        role=0
    elif interest=="Design":
        role=1 
    elif interest=="Research" and problem_solving>6:
        role=2
    elif technical_depth<4:
        role=3
    elif communication>7:
        role=4
    elif leadership>7:
        role=5
    else:
        role=random.randint(0,5)
    return [programming,communication,problem_solving,leadership,experience,technical_depth,interest,role]

data=[generate() for _ in range(3000)]
columns=["Programming","Communication","ProblemSolving","Leadership","Experience","TechnicalDepth","Interest","Role"]
df=pd.DataFrame(data,columns=columns)
df.to_csv("neural_dataset.csv",index=False)
print("Dataset generated successfully.")