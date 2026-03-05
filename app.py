import streamlit as st
from predictor import predict_role  
from advisor import get_tips
st.set_page_config(page_title="RoleGenie AI", layout="centered")
st.title("RoleGenie AI")
st.subheader("Your AI-Powered Team Role Prediction Assistant")
tab1, tab2= st.tabs(["Role Prediction","Team Simulation"])
with tab1:
    st.header("Individual Role Prediction")
    with st.form("predictionform"):
        prog=st.number_input("Programming Skill (1-10)", min_value=1, max_value=10, value=1)
        comm=st.number_input("Communication Skill (1-10)", min_value=1, max_value=10, value=1)
        prob=st.number_input("Problem Solving (1-10)", min_value=1, max_value=10, value=1)
        lead=st.number_input("Leadership (1-10)", min_value=1, max_value=10, value=1)
        exp=st.number_input("Experience (years)", min_value=0, max_value=10, value=1)
        tech=st.number_input("Technical Depth (1-10)", min_value=1, max_value=10, value=5)
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
    st.warning("This feature is under development. Stay tuned for updates!")
    team_size = st.number_input("Number of Team Members", min_value=1, max_value=6, value=3)
    members = []
    for i in range(team_size):
        st.subheader(f"Member {i+1}")
        prog =st.number_input(f"Programming Skill {i+1}", 1, 10, 5)
        comm =st.number_input(f"Communication Skill {i+1}", 1, 10, 5)
        prob =st.number_input(f"Problem Solving {i+1}", 1, 10, 5)
        lead =st.number_input(f"Leadership {i+1}", 1, 10, 5)
        exp =st.number_input(f"Experience (years) {i+1}", 0, 10, 1)
        tech =st.number_input(f"Technical Depth {i+1}", 1, 10, 5)
        interest =st.selectbox(f"Area of Interest {i+1}", ["Coding", "Design", "Research", "Management"])
        members.append((prog, comm, prob, lead, exp, tech, interest))
    if st.button("Predict Team Roles"):
        for i,m in enumerate(members):
            role,conf =predict_role(*m)
            st.write(f"Member {i+1} → **{role}** ({conf}%)")