# Golf Score Recording App

holes = [
    {"number": 1, "par": 4},
    {"number": 2, "par": 3},
    {"number": 3, "par": 5},
    {"number": 4, "par": 4},
    {"number": 5, "par": 4},
    {"number": 6, "par": 5},
    {"number": 7, "par": 3},
    {"number": 8, "par": 4},
    {"number": 9, "par": 4},
]

# Mapping from spoken results to strokes relative to par
score_map = {
    "albatross": -3,
    "eagle": -2,
    "birdie": -1,
    "par": 0,
    "bogey": 1,
    "double bogey": 2,
    "triple bogey": 3,
}

scores = []

print("Welcome to the Golf Score Recorder!\n")
print("Instructions: type how you scored on each hole (e.g. birdie, par, bogey).\n"
      "You can also enter a number of strokes directly.")

for hole in holes:
    par = hole["par"]
    while True:
        user_input = input(f"Hole {hole['number']} (par {par}): ").strip().lower()
        if user_input.isdigit():
            strokes = int(user_input)
            break
        if user_input in score_map:
            strokes = par + score_map[user_input]
            break
        print("Please enter a number of strokes or one of: " + ", ".join(score_map.keys()))
    scores.append(strokes)

print("\nScorecard:")
for i, hole in enumerate(holes):
    par = hole["par"]
    strokes = scores[i]
    diff = strokes - par
    sign = "+" if diff > 0 else ""
    print(f"Hole {hole['number']}: {strokes} ({sign}{diff} relative to par)")

total_strokes = sum(scores)
total_par = sum(h["par"] for h in holes)
total_diff = total_strokes - total_par
sign = "+" if total_diff > 0 else ""
print(f"\nTotal: {total_strokes} strokes ({sign}{total_diff} relative to par)")
