"""
COMP2152 - Assignment 1
Student ID: 101352126
Name: Mechel Fernando
"""

# -----------------------------
# Part B: Variables (with types)
# -----------------------------
gym_member = "Alex Alliton"          # str
preferred_weight_kg = 20.5          # float
highest_reps = 25                   # int
membership_active = True            # bool

print("Variables:")
print(gym_member, preferred_weight_kg, highest_reps, membership_active)

# ---------------------------------------------------------
# Part C: Dictionary (dict[str, tuple[int, int, int]])
# Each tuple = (yoga_minutes, running_minutes, weight_minutes)
# ---------------------------------------------------------
workout_stats = {
    "Alex": (30, 45, 20),
    "Jamie": (40, 30, 25),
    "Taylor": (20, 60, 30),
    "Jordan": (35, 25, 15),
}

# ---------------------------------------------------------
# Part D: Add totals back into the dictionary
# (e.g., "Alex_Total": 95)
# ---------------------------------------------------------
for friend, minutes_tuple in list(workout_stats.items()):
    if isinstance(minutes_tuple, tuple):
        workout_stats[f"{friend}_Total"] = sum(minutes_tuple)

print("\nWorkout Stats (with totals added):")
for k, v in workout_stats.items():
    print(k, ":", v)

# ---------------------------------------------------------
# Part E: Create a 2D (nested) list of workout minutes
# workout_list[row][col] -> minutes
# ---------------------------------------------------------
friends = [name for name in workout_stats.keys() if not name.endswith("_Total")]
workout_list = [list(workout_stats[name]) for name in friends]  # list[list[int]]

print("\nWorkout List (2D list):")
print(workout_list)

# ---------------------------------------------------------
# Part F: Slicing
# 1) Yoga and running for all friends (cols 0 and 1)
# 2) Weightlifting for last two friends (col 2, last two rows)
# ---------------------------------------------------------
yoga_and_running_all = [row[0:2] for row in workout_list]
print("\nYoga and Running (all friends):")
print(yoga_and_running_all)

weight_last_two = [row[2] for row in workout_list[-2:]]
print("\nWeightlifting (last two friends):")
print(weight_last_two)

# ---------------------------------------------------------
# Part G: If-statement within loop (>= 120 minutes total)
# ---------------------------------------------------------
print("\nActivity Shoutouts (>=120 total minutes):")
for friend in friends:
    if workout_stats[f"{friend}_Total"] >= 120:
        print(f"Great job staying active, {friend}!")

# ---------------------------------------------------------
# Part H: User lookup
# ---------------------------------------------------------
lookup_name = input("\nEnter a friend's name to look up (e.g., Alex): ").strip()

if lookup_name in workout_stats and isinstance(workout_stats[lookup_name], tuple):
    y, r, w = workout_stats[lookup_name]
    total = workout_stats.get(f"{lookup_name}_Total", y + r + w)
    print(f"\n{lookup_name}'s workout minutes:")
    print(f"  Yoga:         {y}")
    print(f"  Running:      {r}")
    print(f"  Weightlifting:{w}")
    print(f"  Total:        {total}")
else:
    print(f"Friend {lookup_name} not found in the records.")

# ---------------------------------------------------------
# Part I: Highest and lowest totals
# ---------------------------------------------------------
totals = {friend: workout_stats[f"{friend}_Total"] for friend in friends}
highest_friend = max(totals, key=totals.get)
lowest_friend = min(totals, key=totals.get)

print("\nSummary:")
print("Friend with highest total workout minutes:", highest_friend, "-", totals[highest_friend])
print("Friend with lowest total workout minutes:", lowest_friend, "-", totals[lowest_friend])
