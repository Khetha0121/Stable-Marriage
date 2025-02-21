# -*- coding: utf-8 -*-
"""
Created on Fri Feb 21 20:09:47 2025

@author: User
"""

def stable_matching(students, universities):
    """
    Implements the Gale-Shapley stable matching algorithm.
    :param students: Dictionary where keys are student names and values are lists of university preferences.
    :param universities: Dictionary where keys are university names and values are lists of student preferences.
    :return: A stable matching dictionary {student: university}
    """
    # Initialize all students as free
    free_students = list(students.keys())
    matches = {}  # Final matching
    university_choices = {uni: None for uni in universities}  # Tracks which student a university has accepted
    
    # Invert the preference lists for fast lookup
    university_rankings = {uni: {student: rank for rank, student in enumerate(pref_list)} for uni, pref_list in universities.items()}
    
    # Propose until all students are matched
    while free_students:
        student = free_students.pop(0)
        student_prefs = students[student]
        
        for uni in student_prefs:
            current_student = university_choices[uni]
            
            if current_student is None:
                # University is free, accept the student
                university_choices[uni] = student
                matches[student] = uni
                break
            else:
                # University already has a student, check preference
                if university_rankings[uni][student] < university_rankings[uni][current_student]:
                    # University prefers the new student over the current one
                    free_students.append(current_student)  # The rejected student becomes free
                    university_choices[uni] = student
                    matches[student] = uni
                    break
    
    return matches

# Example usage
students = {
    "Khetha": ["Wits", "UP", "UKZN"],
    "Zamo": ["UKZN", "Wits", "UP"],
    "Tsepho": ["UKZN", "UP", "wits"],
}

universities = {
    "Wits": ["Zamo", "Khetha", "Tsepho"],
    "UP": ["Khetha", "Zamo", "Tsepho"],
    "UKZN": ["Tsepho", "Zamo", "Khetha"],
}

matches = stable_matching(students, universities)
print("Stable Matches:", matches)
