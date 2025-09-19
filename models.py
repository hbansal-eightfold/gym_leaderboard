class MemberStats:
    def __init__(self, name):
        self.name = name
        self.workouts = 0
        self.calories = 0

    def log_workout(self, calories):
        self.workouts += 1
        self.calories += calories
