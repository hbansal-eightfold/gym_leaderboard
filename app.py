from flask import Flask, render_template
from gym_system import GymSystem

app = Flask(__name__)
gym = GymSystem()

# Seed some data
gym.log_workout("Ananya", 800)
gym.log_workout("Rahul", 700)
gym.log_workout("Priya", 600)
gym.log_workout("Ananya", 700)
gym.log_workout("Priya", 900)
gym.log_workout("Rahul", 800)

@app.route("/")
def leaderboard():
    leaderboard = gym.get_leaderboard()
    return render_template("leaderboard.html", leaderboard=leaderboard)

if __name__ == "__main__":
    app.run(debug=True)
