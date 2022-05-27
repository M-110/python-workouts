"""
Your function should print the highest, lowest, and average test scores for 
each subject in each class. Given two files (9a.json and 9b.json) in the 
scores directory,
"""
import os
import json


def grades(folder):
    path = os.path.join(os.getcwd(), folder)
    for file in os.listdir(path):
        with open(os.path.join(folder, file), 'r', encoding='utf-8') as f:
            scores = json.load(f)
            print(os.path.join(folder, file))
            for subject in scores[0]:
                x = [student[subject] for student in scores]
                print(f'\t{subject}: min {min(x)}, max {max(x)}, '
                      f'average {sum(x)/len(x)}')

grades('scores')
        