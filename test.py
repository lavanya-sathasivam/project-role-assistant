from predictor import predict_role

# sample input
programming = 8
communication = 7
problem_solving = 9
leadership = 6
experience = 2
technical_depth = 8
interest = "Coding"

role, confidence = predict_role(
    programming,
    communication,
    problem_solving,
    leadership,
    experience,
    technical_depth,
    interest
)

print("Predicted Role:", role)
print("Confidence:", confidence, "%")