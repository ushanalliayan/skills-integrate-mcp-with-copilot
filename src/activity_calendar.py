# activity_calendar.py

activities = []  # list to store all activities

def add_activity(title, date, description=""):
    """
    Add a new activity to the calendar.
    """
    activity = {"title": title, "date": date, "description": description}
    activities.append(activity)
    print(f"Activity '{title}' added successfully.")

def view_activities():
    """
    Display all upcoming activities sorted by date.
    """
    if not activities:
        print("No activities scheduled.")
        return

    sorted_activities = sorted(activities, key=lambda x: x["date"])
    print("Upcoming Activities:")
    for act in sorted_activities:
        print(f"{act['date']} - {act['title']}: {act['description']}")
