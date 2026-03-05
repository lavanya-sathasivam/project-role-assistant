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
    skillmap={"Very Low":2,"Low":4,"Medium":6,"Good":8,"Excellent":10}
    with st.form("predictionform"):
        col1,col2=st.columns(2)
        with col1:
            prog_label=st.select_slider("Programming Skill",
                                        ["Very Low","Low","Medium","Good","Excellent"])
            prob_label=st.select_slider("Problem Solving",
                                        ["Very Low","Low","Medium","Good","Excellent"])
            tech_label=st.select_slider("Technical Depth",
                                        ["Very Low","Low","Medium","Good","Excellent"])
        with col2:
            comm_label=st.select_slider("Communication Skill",
                                        ["Very Low","Low","Medium","Good","Excellent"])
            lead_label=st.select_slider("Leadership",
                                        ["Very Low","Low","Medium","Good","Excellent"])
            exp=st.selectbox("Experience (Years)",
                             [0,1,2,3,4,5])
        interest=st.selectbox("Area of Interest",
                              ["Coding","Design","Research","Management"])
        submit=st.form_submit_button("Predict Role")
    if submit:
        prog=skillmap[prog_label]
        comm=skillmap[comm_label]
        prob=skillmap[prob_label]
        lead=skillmap[lead_label]
        tech=skillmap[tech_label]
        role,confidence=predict_role(prog,comm,prob,lead,exp,tech,interest)
        st.success(f"Predicted Role: {role}")
        st.write(f"Confidence: {confidence}%")
        tip=get_tips(role)
        st.info(tip)
with tab2:
    st.header("Team Role Simulation")
    st.write("Enter team member details to predict the most suitable roles.")
    team_size=st.number_input("Number of Team Members",min_value=1,max_value=6,value=3)
    members=[]
    skill_map={"Very Low":2,"Low":4,"Medium":6,"Good":8,"Excellent":10}
    for i in range(team_size):
        st.divider()
        st.subheader(f"Member {i+1}")
        name=st.text_input(f"Member {i+1} Name",key=f"name_{i}")
        col1,col2=st.columns(2)
        with col1:
            programming_label=st.select_slider("Programming Skill",
                                               ["Very Low","Low","Medium","Good","Excellent"],
                                               key=f"prog_{i}")
            programming=skill_map[programming_label]
        with col2:
            communication_label=st.select_slider("Communication Skill",
                                                 ["Very Low","Low","Medium","Good","Excellent"],
                                                 key=f"comm_{i}")
            communication=skill_map[communication_label]
        col3,col4=st.columns(2)
        with col3:
            problem_label=st.select_slider("Problem Solving",
                                           ["Very Low","Low","Medium","Good","Excellent"],
                                           key=f"prob_{i}")
            problem_solving=skill_map[problem_label]
        with col4:
            leadership_label=st.select_slider("Leadership",
                                              ["Very Low","Low","Medium","Good","Excellent"],
                                              key=f"lead_{i}")
            leadership=skill_map[leadership_label]
        col5,col6=st.columns(2)
        with col5:
            experience=st.selectbox("Experience (Years)",
                                    [0,1,2,3,4,5],key=f"exp_{i}")
        with col6:
            tech_label=st.select_slider("Technical Depth",
                                        ["Very Low","Low","Medium","Good","Excellent"],
                                        key=f"tech_{i}")
            technical_depth=skill_map[tech_label]
        interest=st.selectbox("Area of Interest",
                              ["Coding","Design","Research","Management"],
                              key=f"interest_{i}")
        members.append({"name":name,
                        "data":(programming,communication,problem_solving,leadership,experience,technical_depth,interest)})
    if st.button("Predict Team Roles"):
        st.subheader("Predicted Team Roles")
        for member in members:
            role,confidence=predict_role(*member["data"])
            display_name=member["name"] if member["name"] else "Unnamed Member"
            st.success(f"{display_name} → {role} ({confidence}%)")