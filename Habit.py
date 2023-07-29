import json
import datetime
import os


class Habit:
    def __init__(self, name, description, periodicity):
        self.name = name
        self.description = description
        self.periodicity = periodicity
        self.created_date = datetime.date.today()
        self.completions = []

    def complete_task(self):
        today = datetime.date.today()
        if self.completions and self.completions[-1].date() == today:
            return False  # Task already completed for today
        else:
            self.completions.append(datetime.datetime.now())
            # Save the updated data to the file
            with open('habit_data.json', 'r') as f:
                data = json.load(f)
                for habit_data in data:
                    if habit_data["name"] == self.name:
                        habit_data["completions"] = [c.strftime('%Y-%m-%d %H:%M:%S') for c in self.completions]
                        break
            with open('habit_data.json', 'w') as f:
                json.dump(data, f, indent=2)
            return True  # Task successfully completed for today

    def streak(self):
        streak_count = 0
        today = datetime.date.today()
        for date in self.completions[::-1]:
            if (today - date.date()).days <= 1 if self.periodicity == "daily" else (today - date.date()).days <= 7:
                streak_count += 1
                today = date.date()
            else:
                break
        return streak_count

    def __str__(self):
        return f"{self.name}: {self.streak()} days streak"