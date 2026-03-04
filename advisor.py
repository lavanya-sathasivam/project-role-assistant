def get_tips(role):
    tips={"Developer": "Focus on writing modular and efficient code.",
          "Designer": "Work on UI/UX consistency and user interaction.",
          "Researcher": "Explore algorithms, datasets, and experiment design.",
          "Tester": "Ensure system reliability through unit and integration testing.",
          "Documenter": "Maintain clear documentation for system architecture and workflow.",
          "Team Leader": "Coordinate tasks and ensure smooth collaboration."
          }
    return tips.get(role, "Keep improving your technical skills.")