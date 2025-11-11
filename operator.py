class Time:
    def __init__(self, hour=0, minute=0, second=0):
        self.hour = hour
        self.minute = minute
        self.second = second

    def __str__(self):
        return f"{self.hour:02d}:{self.minute:02d}:{self.second:02d}"

    def __add__(self, other):
        total_seconds = self.second + other.second
        total_minutes = self.minute + other.minute + total_seconds // 60
        total_hours = self.hour + other.hour + total_minutes // 60

        # Normalize time
        result = Time(
            total_hours % 24,  # wrap around 24-hour format
            total_minutes % 60,
            total_seconds % 60
        )
        return result

# Example usage
t1 = Time(2, 45, 50)
t2 = Time(3, 20, 30)

t3 = t1 + t2
print("Sum of times:", t3)
