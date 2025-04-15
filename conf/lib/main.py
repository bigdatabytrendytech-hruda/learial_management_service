from collections import Counter

def get_frequency_count(input_string):
    return Counter(input_string)

# Example usage
input_string = "loreal management service"
frequency_count = get_frequency_count(input_string)
print(frequency_count)
