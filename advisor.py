def get_tips(role):
    tips={"Developer": "Focus on writing modular and efficient code.",
          "Designer": "Work on UI/UX consistency and user interaction.",
          "Researcher": "Explore algorithms, datasets, and experiment design.",
          "Tester": "Ensure system reliability through unit and integration testing.",
          "DevOps": "Strengthen deployment, automation, and system monitoring skills.",
          "Manager": "Coordinate tasks, remove blockers, and keep the team aligned."
          }
    return tips.get(role, "Keep improving your technical skills.")
