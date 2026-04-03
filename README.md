# RoleGenie AI

RoleGenie AI is a neural-network-based application that predicts the most suitable project role for individuals based on their skills and interests. The system uses PyTorch for the model and Streamlit for the interface.

## Live App

https://role-genie-ai.streamlit.app

## Features

### Individual Role Prediction

Predict the best role for a single person based on:

- Programming Skill
- Communication Skill
- Problem Solving
- Leadership
- Technical Depth
- Experience
- Area of Interest

Output includes:

- Predicted Role
- Confidence Score
- Advisory Tips

### Team Role Simulation

Simulate role assignment for multiple team members. The system evaluates each member and assigns the most suitable role.

Example output:

- Arun -> Developer (84%)
- Priya -> Designer (78%)
- Rahul -> Researcher (72%)

## Machine Learning Model

The system uses a Multi-Layer Perceptron (MLP) neural network.

Model architecture:

- Input Layer -> 10 Features
- Hidden Layer -> 64 Neurons
- Hidden Layer -> 32 Neurons
- Hidden Layer -> 16 Neurons
- Output Layer -> 6 Role Classes

Roles predicted by the model:

- Developer
- Designer
- Researcher
- Tester
- DevOps
- Manager

Model performance:

- Test Accuracy ~= 83%

## Input Features

The neural network evaluates the following attributes:

| Feature | Description |
| --- | --- |
| Programming Skill | Coding proficiency |
| Communication | Team communication ability |
| Problem Solving | Analytical ability |
| Leadership | Team leadership capability |
| Experience | Years of project experience |
| Technical Depth | Technical expertise |
| Interest | Preferred domain |

Skill levels:

- Very Low
- Low
- Medium
- Good
- Excellent

## Technology Stack

- Python
- Streamlit
- PyTorch
- Pandas
- NumPy
- Scikit-learn

## Project Structure

```text
project-role-assistant
|-- app.py
|-- predictor.py
|-- advisor.py
|-- train.py
|-- neural_model.pth
|-- encoder.pkl
|-- scaler.pkl
|-- neural_dataset.csv
|-- neural_dataset.py
|-- requirements.txt
`-- README.md
```

## Running the Project

1. Clone the repository.
2. Install dependencies with `pip install -r requirements.txt`.
3. Run the application with `streamlit run app.py`.

## Deployment

This application is deployed using Streamlit Community Cloud:

https://role-genie-ai.streamlit.app

## Author

Lavanya S  
Artificial Intelligence & Machine Learning Student
