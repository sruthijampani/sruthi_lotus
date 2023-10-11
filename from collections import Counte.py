from collections import Counter
import math

class Statistics:
    def __init__(self, data):
        self.data = data

    def calculate_mean(self):
        if not self.data:
            return None  # Return None for invalid data
        return sum(self.data) / len(self.data)

    def calculate_median(self):
        if not self.data:
            return None
        sorted_data = sorted(self.data)
        n = len(sorted_data)
        middle = n // 2
        if n % 2 == 1:
            return sorted_data[middle]
        else:
            middle1, middle2 = sorted_data[middle - 1], sorted_data[middle]
            return (middle1 + middle2) / 2

    def calculate_mode(self):
        if not self.data:
            return None
        value_count = Counter(self.data)
        max_frequency = max(value_count.values())
        mode = [key for key, value in value_count.items() if value == max_frequency]
        return mode

    def calculate_standard_deviation(self):
        if not self.data:
            return None
        mean = self.calculate_mean()
        squared_diff = [(x - mean) ** 2 for x in self.data]
        variance = sum(squared_diff) / len(self.data)
        std_deviation = math.sqrt(variance)
        return std_deviation

# This is a sample dataset for testing
test_data = [6, 4, 3, 8, 2, 5, 5, 9, 9, 1, 3, 6, 7, 1, 7]

# Create a Statistics object with the test data
stats = Statistics(test_data)

# Calculate statistics
mean = stats.calculate_mean()
median = stats.calculate_median()
mode = stats.calculate_mode()
sd = stats.calculate_standard_deviation()

# Print the results
if mean is not None:
    print("The mean is:", mean)
if median is not None:
    print("The median is:", median)
if mode is not None:
    print("The mode is:", mode)
if sd is not None: