#!/usr/bin/env python3
"""
Automated test of browse mode with storytelling
"""

import os
from resume_windows import ResumeOptimizer

def test_browse_mode_storytelling():
    """Test browse mode storytelling functionality"""
    
    print("🧪 TESTING BROWSE MODE STORYTELLING")
    print("=" * 50)
    
    # Read test files
    with open('test_welder_job.txt', 'r') as f:
        job_content = f.read()
    
    with open('test_welder_resume.txt', 'r') as f:
        resume_content = f.read()
    
    print(f"📄 Job content: {len(job_content)} characters")
    print(f"📄 Resume content: {len(resume_content)} characters")
    print()
    
    # Initialize optimizer
    optimizer = ResumeOptimizer()
    
    # Mock the user input for storytelling choice by patching input
    import builtins
    original_input = builtins.input
    
    def mock_input(prompt):
        if "Choose resume style" in prompt:
            print("Mock choosing option 1 (Story Resume)")
            return "1"
        return ""
    
    builtins.input = mock_input
    
    try:
        # Call the complete optimization process
        print("🚀 RUNNING COMPLETE OPTIMIZATION WITH STORYTELLING")
        print("-" * 50)
        
        results = optimizer.process_complete_optimization(
            job_content, 
            resume_content, 
            "Senior Welder", 
            "MetalWorks Construction"
        )
        
        print()
        print("📊 RESULTS ANALYSIS:")
        print("-" * 30)
        
        for key, value in results.items():
            print(f"✅ {key}: {len(value)} characters")
            if 'narrative' in key.lower():
                print(f"   📖 Preview: {value[:100]}...")
        
        # Check if storytelling elements are present
        if '7_narrative_resume' in results:
            narrative = results['7_narrative_resume']
            story_elements = {
                'Metal Master Hook': '🔥 THE METAL MASTER' in narrative,
                'Welding Narrative': 'art meets engineering' in narrative,
                'Company Integration': 'MetalWorks Construction' in narrative,
                'Professional Narrative': 'PROFESSIONAL NARRATIVE:' in narrative,
                'Career Progression': 'Chapter 1:' in narrative
            }
            
            print()
            print("🎭 STORYTELLING VERIFICATION:")
            for element, found in story_elements.items():
                status = "✅" if found else "❌"
                print(f"   {status} {element}")
            
            all_found = all(story_elements.values())
            print()
            if all_found:
                print("🎉 STORYTELLING IN BROWSE MODE: ✅ WORKING PERFECTLY!")
            else:
                print("❌ Some storytelling elements missing")
        else:
            print("❌ No narrative resume found in results")
    
    finally:
        # Restore original input
        builtins.input = original_input

if __name__ == "__main__":
    test_browse_mode_storytelling()