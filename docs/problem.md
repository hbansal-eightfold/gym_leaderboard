## My Gym Leaderboard

Context  
You are given a Python application for "My Gym". The system manages gym members, allows workout logging, and displays a leaderboard.  
Some functionality is partially implemented. Your task is to understand the existing codebase and extend it with additional features.

### Tasks  

#### Level 1 (Partially Implemented – Complete the Basics)  
- Members can log workouts with calories burned and workout counts.  
- Some parts of the leaderboard logic are missing. You need to:  
  - Complete the sorting logic so that members are ranked by:  
    1. Calories burned (higher first)  
    2. If tied → Workouts completed (higher first)  
    3. If tied → Alphabetical order of names  
  - Ensure the leaderboard is passed correctly to the HTML template.  
  - Fix any missing/wrong pieces in the Flask route or template rendering.  

Expected outcome: A working **basic leaderboard** shown in the browser.  

#### Level 2 (Intermediate)  
- Modify workout logging to include dates.  
- Implement a **weekly leaderboard** (only workouts from the current week count).  
- Extend the HTML UI to allow switching between all-time and weekly leaderboard views.  
- Add unit tests for the new leaderboard logic.  

#### Level 3 (Advanced)  
- Implement a challenge system model (e.g., “Burn 5000 calories in a week”). Sample: Challenge(id, description, target_calories, start_date, end_date)
- Add challenge leaderboard showing each member's progress. Should cover Rank, Member, Progress (%), Calories Burned.
- Award badges to members upon completing a challenge. Extend leaderboard UI to display badges (e.g., as text or small icons).
- Ensure the design scales for hundreds of members and frequent workout updates.  

### Setup  
Run `app.py` to start the Flask application.
