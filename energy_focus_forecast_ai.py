print("🧠 AI Energy & Focus Forecast System \n")

energy = int(input("Energy level today (1–5): "))
focus = int(input("Focus level today (1–5): "))
stress = int(input("Stress level today (1–5): "))
work_hours = float(input("Work hours today: "))

score = (
    (energy * 0.3) +
    (focus * 0.3) +
    ((6 - stress) * 0.2) +
    ((8 - min(work_hours, 8)) * 0.2)
)

print("\n📊 FORECAST RESULT")

if score >= 4:
    print("🔮 Tomorrow Forecast: High Productivity")
elif score >= 3:
    print("🔮 Tomorrow Forecast: Moderate Productivity")
else:
    print("🔮 Tomorrow Forecast: Low Productivity")

print("\n🧭 AI Recommendations")

if stress >= 4:
    print("• Reduce stress before sleeping")
if energy <= 2:
    print("• Prioritize rest and sleep")
if work_hours > 8:
    print("• Avoid overworking tomorrow")
if focus >= 4 and energy >= 4:
    print("• Plan important tasks tomorrow")
