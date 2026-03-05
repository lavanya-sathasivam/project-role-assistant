import streamlit as st
from predictor import predict_role  
from advisor import get_tips
st.set_page_config(page_title="RoleGenie AI", layout="centered")
st.title("RoleGenie AI")
st.subheader("Your AI-Powered Team Role Prediction Assistant")
st.divider()
tab1, tab2= st.tabs(["Role Prediction","Team Simulation"])
with tab1:
    st.header("Individual Role Prediction")
    with st.form("predictionform"):
        prog=st.number_input("Programming Skill (1-10)", min_value=1, max_value=10)
        comm=st.number_input("Communication Skill (1-10)", min_value=1, max_value=10)
        prob=st.number_input("Problem Solving (1-10)", min_value=1, max_value=10)
        lead=st.number_input("Leadership (1-10)", min_value=1, max_value=10)
        exp=st.number_input("Experience (years)", min_value=0, max_value=10)
        tech=st.number_input("Technical Depth (1-10)", min_value=1, max_value=10)
        interest=st.selectbox("Area of Interest", ["Coding","Design","Research","Management"])
        submit=st.form_submit_button("Predict Role")
    if submit:
        role,confidence= predict_role(prog, comm, prob, lead, exp, tech, interest)
        st.success(f"Predicted Role: {role}")
        st.write(f"Confidence: {confidence}%")
        tip= get_tips(role)
        st.info(tip)
with tab2:
    st.header("Team Role Simulation")
    st.write("Enter team member details to predict the most suitable roles.")
    team_size = st.number_input("Number of Team Members", min_value=1, max_value=6, value=3)
    members = []
    for i in range(team_size):
        st.subheader(f"Member {i+1}")
        name= st.text_input(f"Name of Member {i+1}", key=f"name_{i}")
        programming = st.number_input("Programming Skill (1-10)", 1, 10, 5, key=f"prog_{i}")
        communication = st.number_input("Communication Skill (1-10)", 1, 10, 5, key=f"comm_{i}")
        problem_solving = st.number_input("Problem Solving (1-10)", 1, 10, 5, key=f"prob_{i}")
        leadership = st.number_input("Leadership (1-10)", 1, 10, 5, key=f"lead_{i}")
        experience = st.number_input("Experience (years)", 0, 10, 1, key=f"exp_{i}")
        technical_depth = st.number_input("Technical Depth (1-10)", 1, 10, 5, key=f"tech_{i}")
        interest = st.selectbox("Area of Interest", ["Coding", "Design", "Research", "Management"], key=f"interest_{i}")
        members.append({"name": name, "data": (programming, communication, problem_solving, leadership, experience, technical_depth, interest)})   
        if st.button("Predict Team Roles", key=f"predict_{i}"):
            st.subheader("Predicted Team Roles")
            for member in members:
                role, confidence = predict_role(*member["data"])
                display_name = member["name"] if member["name"] else "Unnamed Member"
                st.success(f"{display_name} → {role} ({confidence}%)")