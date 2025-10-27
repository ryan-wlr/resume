#!/usr/bin/env python3
"""
Debug Storytelling Issue
========================
"""

import sys
import os
sys.path.append(os.path.dirname(os.path.abspath(__file__)))

from resume_windows import ResumeOptimizer

def debug_storytelling():
    print("🔍 DEBUGGING STORYTELLING ISSUE")
    print("=" * 50)
    
    optimizer = ResumeOptimizer()
    
    # Test story generation directly
    resume_info = {
        'name': 'RYAN THOMAS WEILER',
        'contact_info': 'ryan_wlr@yahoo.com',
        'skills': ['Python', 'Django'],
        'experience': ['Built trading systems'],
        'projects': ['Trading Bot'],
        'education': 'Computer Science'
    }
    
    print(">>> Testing story generation...")
    story = optimizer.generate_personalized_story(
        resume_info, 'software_engineer', 'Senior Developer', 'Test Company'
    )
    
    print(f"Opening hook: {story['opening_hook']}")
    print(f"Has CRAFTSMAN: {'CRAFTSMAN' in story['opening_hook']}")
    
    # Test full narrative creation
    sample_resume = "Ryan Weiler\nSoftware Engineer\nPython, Django"
    job_analysis = optimizer.analyze_job_posting("Python Developer", "Senior Developer", "Test Co")
    
    print("\n>>> Testing narrative creation...")
    narrative = optimizer.create_narrative_resume(
        sample_resume, job_analysis, "Senior Developer", "Test Company"
    )
    
    print("First 200 characters of narrative:")
    print(narrative[:200])
    print(f"\nHas opening hook in narrative: {'CRAFTSMAN' in narrative}")
    
    # Check where the issue might be
    lines = narrative.split('\n')
    for i, line in enumerate(lines[:10]):
        print(f"Line {i}: {line}")

if __name__ == "__main__":
    debug_storytelling()