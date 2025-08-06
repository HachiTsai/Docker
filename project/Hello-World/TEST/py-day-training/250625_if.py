def evaluate_temp(temp):
    message = "Normal temperature"
    if temp > 38:
        message = "Fever"
    elif temp >= 32:
        message = "Conforming to normal range"
    else:
        message = "Hypothermia"
    return message

print(evaluate_temp(33.8))  # Output: Normal temperature
print(evaluate_temp(37))  # Output: Fever