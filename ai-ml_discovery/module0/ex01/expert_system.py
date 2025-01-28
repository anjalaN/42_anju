#!/usr/bin/env python3
import sys

def control_air_conditioner(external_temp, in_house_temp, lower_threshold, upper_threshold):
    if in_house_temp < lower_threshold:
        return "heating", in_house_temp + 0.5
    elif in_house_temp > upper_threshold:
        return "cooling", in_house_temp - 0.5
    else:
        if in_house_temp < external_temp:
            return "nothing", in_house_temp + 0.25
        elif in_house_temp > external_temp:
            return "nothing", in_house_temp - 0.25
        else:
            return "nothing", in_house_temp

if __name__ == "__main__":
    try:
        if len(sys.argv) != 4:
            print("Usage: python expert_system.py <season> <lower_threshold> <upper_threshold>")
        else:
            season = sys.argv[1].lower()
            lower_threshold = float(sys.argv[2])
            upper_threshold = float(sys.argv[3])

            in_house_temp = None

            # Read input from environment.py (simulated external temperatures)
            for external_temp_str in sys.stdin:
                try:
                    external_temp = float(external_temp_str.strip())

                    if in_house_temp is None:
                        in_house_temp = external_temp

                    action, in_house_temp = control_air_conditioner(external_temp, in_house_temp, lower_threshold, upper_threshold)
                    print(f"{external_temp:.2f} - {action} - {in_house_temp:.2f} ")

                except ValueError:
                    print("Invalid temperature input. Please enter a valid numeric value.")
                    break  # Optionally, you can decide to skip this iteration and continue with the next input
    except Exception as e:
        print(f"An unexpected error occurred: {e}")

# if __name__ == "__main__":
#     if len(sys.argv) != 4:
#         print("Usage: python expert_system.py <season> <lower_threshold> <upper_threshold>")
#     else:
#         season = sys.argv[1].lower()
#         lower_threshold = float(sys.argv[2])
#         upper_threshold = float(sys.argv[3])

#         in_house_temp = None

#         # Read input from environment.py (simulated external temperatures)
#         for external_temp_str in sys.stdin:
#             try:
#                 external_temp = float(external_temp_str.strip())

#                 if in_house_temp is None:
#                     in_house_temp = external_temp

#                 action, in_house_temp = control_air_conditioner(external_temp, in_house_temp, lower_threshold, upper_threshold)
#                 print(f"{external_temp:.2f} - {action} - {in_house_temp:.2f} ")

#             except ValueError:
#                 print("Invalid temperature input.")
#                 break
#pout tester code 
#python environment.py winter | python expert_system.py winter 1.0 5.0
