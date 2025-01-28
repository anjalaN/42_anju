#!/usr/bin/env python3
import sys
import time
import random
import math

SEASON_TEMP_RANGES = {
    "spring": (5, 15),
    "summer": (15, 30),
    "autumn": (10, 20),
    "winter": (-5, 5),
}

def simulate_temperature(season):
    min_temp, max_temp = SEASON_TEMP_RANGES.get(season, (0, 0))
    base_temp = (min_temp + max_temp) / 2
    amplitude = (max_temp - min_temp) / 2
    slices_per_day = 48

    for i in range(slices_per_day):
        time_of_day = i / slices_per_day * 2 * math.pi
        temp_variation = amplitude * math.sin(time_of_day)
        temp_variation += random.uniform(-1, 1)

        current_temp = base_temp + temp_variation
        try:
            print(f"{current_temp:.2f}")
            sys.stdout.flush()
        except BrokenPipeError:
            # Handle the broken pipe by breaking the loop early
            break
        time.sleep(1)


if __name__ == "__main__":
    try:
        if len(sys.argv) != 2:
            print("Usage: python environment.py <season>")
        else:
            season = sys.argv[1].lower()
            if season not in SEASON_TEMP_RANGES:
                print(f"Error: '{season}' is not a valid season name. Valid options are: {', '.join(SEASON_TEMP_RANGES.keys())}")
            else:
                simulate_temperature(season)
    except Exception as e:
        print(f"Error: {e}")

# if __name__ == "__main__":
#     try:
#         if len(sys.argv) != 2:
#             print("Usage: python environment.py <season>")
#         elif sys.argv[1].lower() not in SEASON_TEMP_RANGES
#             raise "season is not correct"
#         else:
#             season = sys.argv[1].lower()
#             simulate_temperature(season)
#     except Exception as e:
#         print(f"e")

#for testibg python environment.py spring 
       
