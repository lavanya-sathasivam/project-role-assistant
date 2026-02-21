import pandas as pd
import random

role ={
    0:"Developer",
    1:"Designer",
    2:"Researcher",
    3:"Tester",
    4:"Documenter",
    5:"TeamLeader"
}

data = []
for _ in range(300):
    program= random.randint(1, 10)
    communication= random.randint(1, 10)
    cgpa= round(random.uniform(5.0, 9.5), 2)
    interest= random.randint(1, 4)  # 1: Coding, 2: Design, 3: Research, 4: Management
    experience= random.randint(0, 5)
    problem_solving= random.randint(1, 10)
    creative=random.randint(1, 10)

    if interest==1 and program>=7:
        role =0  # Developer
    elif interest== 2 and creative>= 7:
        role =1  # Designer
    elif interest== 3 and cgpa>= 7.5:
        role= 2  # Researcher
    elif communication>= 7 and interest== 4:
        role =5  # Team Leader
    elif problem_solving<= 5:
        role= 3  # Tester
    else:
        role= 4  # Documenter

    data.append([program, communication, cgpa, interest, experience, problem_solving, creative, role])

df = pd.DataFrame(data, columns=[
    "program", "communication", "cgpa", "interest", "experience", "problem_solving", "creative", "role"
])

df.to_csv("dataset.csv", index=False)
print("dataset.csv generated successfully!")