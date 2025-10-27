#!/usr/bin/env python3
"""
Quick Test: Resume Storytelling Integration
==========================================

Test the storytelling feature integration with the main resume optimizer system.
"""

import sys
import os
from datetime import datetime

# Add current directory to path
sys.path.append(os.path.dirname(os.path.abspath(__file__)))

try:
    from resume_windows import ResumeOptimizer
except ImportError as e:
    print(f"ERROR: Could not import ResumeOptimizer: {e}")
    sys.exit(1)

def test_storytelling_integration():
    print("🧪 TESTING STORYTELLING INTEGRATION")
    print("=" * 50)
    
    # Sample data
    sample_job = """Senior Software Engineer - FinTech Startup

We're building the future of financial technology and need a passionate engineer
to join our team. You'll work on algorithmic trading systems and data analytics.

Required: Python, machine learning, financial markets
Preferred: AWS, Docker, React"""

    sample_resume = """Ryan Thomas Weiler
Software Engineer
ryan_wlr@yahoo.com | (561) 906-2118

Experience with Python, Django, financial analysis"""

    # Initialize optimizer
    optimizer = ResumeOptimizer()
    
    # Test story generation directly
    print(">>> Testing story generation...")
    try:
        story_elements = optimizer.generate_career_story("software_engineer", "Senior Software Engineer", "FinTech Startup")
        print("✅ Story generation successful")
        print(f"   - Opening hook: {len(story_elements['opening_hook'])} characters")
        print(f"   - Career progression: {len(story_elements['career_progression'])} characters")
        print(f"   - Achievements: {len(story_elements['signature_achievements'])} items")
        print(f"   - Projects: {len(story_elements['story_projects'])} items")
    except Exception as e:
        print(f"❌ Story generation failed: {e}")
        return False
    
    # Test narrative resume creation
    print("\n>>> Testing narrative resume creation...")
    try:
        job_analysis = optimizer.analyze_job_posting(sample_job, "Senior Software Engineer", "FinTech Startup")
        narrative_resume = optimizer.create_narrative_resume(sample_resume, job_analysis, "Senior Software Engineer", "FinTech Startup")
        print("✅ Narrative resume creation successful")
        print(f"   - Resume length: {len(narrative_resume)} characters")
        print(f"   - Contains story elements: {'🌟' in narrative_resume}")
    except Exception as e:
        print(f"❌ Narrative resume creation failed: {e}")
        return False
        
    # Test enhanced resume creation
    print("\n>>> Testing enhanced resume creation...")
    try:
        enhanced_resume = optimizer.create_enhanced_resume(sample_resume, job_analysis, "Senior Software Engineer", "FinTech Startup")
        print("✅ Enhanced resume creation successful")
        print(f"   - Resume length: {len(enhanced_resume)} characters")
        print(f"   - Professional format: {'PROFESSIONAL SUMMARY' in enhanced_resume}")
    except Exception as e:
        print(f"❌ Enhanced resume creation failed: {e}")
        return False
    
    print("\n🎉 ALL TESTS PASSED!")
    print("\n📝 SYSTEM READY FOR STORYTELLING!")
    print("\nTo use the storytelling feature:")
    print("1. Run: python resume_windows.py --browse")
    print("2. Select your job description and resume files")
    print("3. Choose option 1 for Story Resume when prompted")
    print("4. Or choose option 3 for both Story and Standard versions")
    
    return True

if __name__ == "__main__":
    success = test_storytelling_integration()
    sys.exit(0 if success else 1)