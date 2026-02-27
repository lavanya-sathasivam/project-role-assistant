import streamlit as st
import joblib
import numpy as np
import pandas as pd

model =joblib.load("model.pkl")

st.title("Project Role Assignment Assistant")
st.write("Enter your project and team details to get role assignments and smart tips.")

project_type =st.selectbox(
    "Select Project Type",
    ["Web Development","Machine Learning","Mobile App","Research","General Software"]
)

team_size =st.number_input("Number of Team Members",min_value=1, max_value=10, value=3, step=1)

st.divider()

interest_map = {
    "Coding": 1,
    "Design": 2,
    "Research": 3,
    "Management": 4
}

role_map = {
    0: "Developer",
    1: "Designer",
    2: "Researcher",
    3: "Tester",
    4: "Documenter",
    5: "Team Leader"
}

team_data =[]

st.subheader("Enter Details for Each Team Member")

for i in range(int(team_size)):
    st.markdown(f"Member {i+1}")

    name = st.text_input(f"Name of Member {i+1}", key=f"name_{i}")

    prog = st.slider("Programming Skill (1-10)", 1, 10, 5, key=f"prog_{i}")
    comm = st.slider("Communication Skill (1-10)", 1, 10, 5, key=f"comm_{i}")
    cgpa = st.slider("CGPA", 0.0, 10.0, 7.0, key=f"cgpa_{i}")
    interest = st.selectbox("Interest Area", ["Coding", "Design", "Research", "Management"], key=f"interest_{i}")
    exp = st.slider("Project Experience (years)", 0, 5, 1, key=f"exp_{i}")
    prob = st.slider("Problem Solving Skill (1-10)", 1, 10, 5, key=f"prob_{i}")
    creative = st.slider("Creativity (1-10)", 1, 10, 5, key=f"creative_{i}")

    team_data.append({
        "name": name if name else f"Member {i+1}",
        "features": [prog, comm, cgpa, interest_map[interest], exp, prob, creative]
    })

st.divider()

if st.button("Generate Team Roles"):
    results = []
    role_counts = {}

    for member in team_data:
        features = np.array([member["features"]])
        pred = model.predict(features)[0]
        role = role_map[pred]

        results.append({
            "Name": member["name"],
            "Assigned Role": role
        })

        role_counts[role] = role_counts.get(role, 0) + 1

    df_results = pd.DataFrame(results)

    st.subheader("Team Role Assignment")
    st.table(df_results)