#!/usr/bin/env python3
"""
Debug Optical Engineer Storytelling
===================================

Test why optical engineer resumes aren't getting proper storytelling.
"""

import sys
import os
sys.path.append(os.path.dirname(os.path.abspath(__file__)))

from resume_windows import ResumeOptimizer

def test_optical_engineer_detection():
    print("🔍 DEBUGGING OPTICAL ENGINEER STORYTELLING")
    print("=" * 60)
    
    optimizer = ResumeOptimizer()
    
    # Test various optical engineering terms
    test_cases = [
        "Optical Engineer",
        "Senior Optical Engineer", 
        "Optics Engineer",
        "Photonics Engineer",
        "Laser Engineer",
        "optical systems engineer",
        "optical design engineer"
    ]
    
    print(">>> Testing field detection for optical engineering roles:")
    for role in test_cases:
        detected_field = optimizer.detect_career_field(role.lower())
        print(f"   '{role}' → '{detected_field}'")
    
    # Test with job content that includes optical terms
    optical_job_content = """Senior Optical Engineer Position
    
We need an experienced optical engineer to design laser systems and optical components.
Work with photonics, fiber optics, laser design, optical modeling, and precision optics.

Required: optical design, laser systems, photonics, optics modeling
Preferred: Zemax, Code V, optical simulation, laser safety"""

    print(f"\n>>> Testing with optical job description:")
    detected_field = optimizer.detect_career_field(optical_job_content.lower())
    print(f"   Detected field: '{detected_field}'")
    
    # Test story generation
    print(f"\n>>> Testing story generation for optical engineer:")
    resume_info = {
        'name': 'TEST ENGINEER',
        'contact_info': 'test@email.com',
        'skills': ['optical design', 'laser systems', 'photonics'],
        'experience': ['Designed optical systems', 'Built laser prototypes'],
        'projects': ['Fiber optic project'],
        'education': 'Optical Engineering degree'
    }
    
    story = optimizer.generate_personalized_story(
        resume_info, detected_field, "Optical Engineer", "Tech Company"
    )
    
    print(f"   Opening hook: {story['opening_hook'][:100]}...")
    print(f"   Has specific optical story: {'optical' in story['opening_hook'].lower()}")
    
    # Test full narrative creation
    sample_resume = """John Smith
Optical Engineer
john@email.com
(555) 123-4567

Experience:
- Designed laser systems for telecommunications
- Developed fiber optic communication systems
- Built optical prototypes and testing systems

Skills: Optical design, Zemax, laser systems, photonics, fiber optics"""

    job_analysis = optimizer.analyze_job_posting(optical_job_content, "Optical Engineer", "Tech Company")
    
    print(f"\n>>> Creating full narrative resume:")
    narrative = optimizer.create_narrative_resume(
        sample_resume, job_analysis, "Optical Engineer", "Tech Company"
    )
    
    print(f"   Narrative length: {len(narrative)} characters")
    print(f"   Contains 'CRAFTSMAN': {'CRAFTSMAN' in narrative}")
    print(f"   Contains 'optical': {'optical' in narrative.lower()}")
    print(f"   Contains 'laser': {'laser' in narrative.lower()}")
    
    # Show preview
    print(f"\n📖 NARRATIVE PREVIEW (first 300 chars):")
    print(f"   {narrative[:300]}...")
    
    return detected_field

if __name__ == "__main__":
    test_optical_engineer_detection()