#!/usr/bin/env python3
"""
Debug Field Detection
====================
"""

import sys
import os
sys.path.append(os.path.dirname(os.path.abspath(__file__)))

from resume_windows import ResumeOptimizer

def debug_field_detection():
    print("🔍 DEBUGGING FIELD DETECTION")
    print("=" * 50)
    
    optimizer = ResumeOptimizer()
    
    test_cases = [
        "Senior Developer",
        "Software Engineer", 
        "Senior Software Engineer",
        "Python Developer",
        "Senior Python Developer"
    ]
    
    for role in test_cases:
        print(f"\n>>> Testing: '{role}'")
        detected = optimizer.detect_career_field(role.lower())
        print(f"   Detected field: '{detected}'")
        
        # Test personalized story generation
        resume_info = {
            'name': 'RYAN THOMAS WEILER',
            'contact_info': 'ryan_wlr@yahoo.com',
            'skills': ['Python', 'Django'],
            'experience': ['Built systems'],
            'projects': ['Web App'],
            'education': 'Computer Science'
        }
        
        story = optimizer.generate_personalized_story(
            resume_info, detected, role, "Test Company"
        )
        
        print(f"   Opening hook: {story['opening_hook'][:80]}...")
        print(f"   Has CRAFTSMAN: {'CRAFTSMAN' in story['opening_hook']}")

if __name__ == "__main__":
    debug_field_detection()