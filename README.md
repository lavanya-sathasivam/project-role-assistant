🧠 RoleGenie AI

RoleGenie AI is a Neural Network based application that predicts the most suitable project role for individuals based on their skills and interests.
The system is built using PyTorch for deep learning and Streamlit for the web interface.

🌐 Live App:
https://role-genie-ai.streamlit.app

🚀 Features
    Individual Role Prediction:
    Predict the best role for a single person based on their skills.

Inputs include:
    💠Programming Skill
    💠Communication Skill
    💠Problem Solving
    💠Leadership
    💠Technical Depth
    💠Experience
    💠Area of Interest

Output:
    💠Predicted Role
    💠Confidence Score
    💠Advisory Tips

Team Role Simulation:
    Users can simulate role assignment for multiple team members.
The system evaluates each member and assigns the most suitable role.

Example output:
    Arun → Developer (84%)
    Priya → Designer (78%)
    Rahul → Researcher (72%)

🧠 Machine Learning Model
    The system uses a Multi-Layer Perceptron (MLP) neural network.

Model architecture:
    💠Input Layer → 10 Features
    💠Hidden Layer → 64 Neurons
    💠Hidden Layer → 32 Neurons
    💠Hidden Layer → 16 Neurons
    💠Output Layer → 6 Role Classes

Roles predicted by the model:
    💠Developer
    💠Designer
    💠Researcher
    💠Tester
    💠Documenter
    💠Team Leader

Model performance:
    Test Accuracy ≈ 83%

📊 Input Features
    The neural network evaluates the following attributes:

| Feature           | Description                 |
| ----------------- | --------------------------- |
| Programming Skill | Coding proficiency          |
| Communication     | Team communication ability  |
| Problem Solving   | Analytical ability          |
| Leadership        | Team leadership capability  |
| Experience        | Years of project experience |
| Technical Depth   | Technical expertise         |
| Interest          | Preferred domain            |

Skill levels are captured using:
    Very Low → Low → Medium → Good → Excellent

🖥 Technology Stack
    💠Python
    💠Streamlit
    💠PyTorch
    💠Pandas
    💠NumPy
    💠Scikit-learn

📂 Project Structure
    project-role-assistant
    │
    ├── app.py
    ├── predictor.py
    ├── advisor.py
    ├── train.py
    │
    ├── neural_model.pth
    ├── encoder.pkl
    ├── scaler.pkl
    │
    ├── neural_dataset.csv
    ├── dataset_generation.py
    │
    ├── requirements.txt
    └── README.md

⚙️ Running the Project
    Clone the repository
        git clone https://github.com/yourusername/project-role-assistant.git
        cd project-role-assistant
    Install dependencies:
        pip install -r requirements.txt
    Run the application:
        streamlit run app.py
    
🌐 Deployment
    This application is deployed using Streamlit Community Cloud.
    Live demo:
        https://role-genie-ai.streamlit.app

👩🏻‍💻Author
Lavanya S
Artificial Intelligence & Machine Learning Student