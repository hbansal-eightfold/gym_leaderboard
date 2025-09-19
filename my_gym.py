from models import MemberStats

class MyGym:
    def __init__(self):
        self.members = {}

    def log_workout(self, member_name, calories):
        if member_name not in self.members:
            self.members[member_name] = MemberStats(member_name)
        self.members[member_name].log_workout(calories)

    def get_leaderboard(self):
        leaderboard = sorted(
            self.members.values(),
            key=lambda m: (-m.calories, -m.workouts, m.name)
        )
        return leaderboard
