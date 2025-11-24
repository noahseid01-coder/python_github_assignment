# app.py
# ----------------------------------------------
# Study Time Tracker Program
# This program asks the user for the number of
# hours studied today and predicts weekly study
# hours. Includes error handling.
# ----------------------------------------------

print("Welcome to the Study Time Tracker!")

# Task 2 — Ask for user input
hours = input("How many hours did you study today? ")

# Task 5 — Error handling
try:
    hours = float(hours)
except ValueError:
    print("❌ Invalid entry. Please enter a numeric value next time.")
    exit()

# Task 3 — Perform calculation
weekly_hours = hours * 7

# Task 4 — Output result
print(f"\n📘 At this pace, you will study about {weekly_hours:.1f} hours this week!")

# Task 6 — Code cleaned and commented