"""
Prompt:Write a function (run_timing) that asks how long it took for you to run 
10 km. The function continues to ask how long (in minutes) it took for 
additional runs, until the user presses Enter. At that point, the function 
exits--but only after calculating and displaying the average time that the 10 
km runs took.
"""

def run_timing():
    times = []
    while(time_input := int(input('Enter 10 km run time: ') or 0)):
        times.append(time_input)
    print(f'Average of {sum(times) / len(times):.2f} over {len(times)} runs')
    
    
# Input error handling version:

def run_timing2():
    times = []
    while True:
        try:
            time_input = int(input('Enter 10 km run time: ') or 0)
        except ValueError:
            print('Please input a valid number')
            continue
        if time_input:
            times.append(time_input)
        else:
            break
    print(f'Average of {sum(times) / len(times):.2f} over {len(times)} runs')
    