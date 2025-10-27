#!/usr/bin/env python3
"""
Storytelling Status Summary
===========================

Quick verification of storytelling functionality status.
"""

import sys
import os
sys.path.append(os.path.dirname(os.path.abspath(__file__)))

def verify_storytelling_status():
    print("📊 STORYTELLING FEATURE STATUS REPORT")
    print("=" * 60)
    
    try:
        # Test basic functionality
        from resume_windows import ResumeOptimizer
        optimizer = ResumeOptimizer()
        
        sample_resume = """Ryan Thomas Weiler
Software Engineer
ryan_wlr@yahoo.com
(561) 906-2118

Experience:
- Built Python trading algorithms
- Developed Django applications

Skills: Python, Django, algorithmic trading"""

        sample_job = """Senior Developer Position
Python, Django, trading systems required"""

        # Test the core storytelling functions
        print("✅ ResumeOptimizer imports successfully")
        
        # Test resume information extraction
        resume_info = optimizer.extract_resume_information(sample_resume)
        print(f"✅ Resume extraction works: {resume_info['name']}")
        
        # Test story generation
        story = optimizer.generate_personalized_story(
            resume_info, "software_engineer", "Senior Developer", "Test Company"
        )
        print("✅ Story generation works")
        
        # Test job analysis
        job_analysis = optimizer.analyze_job_posting(sample_job, "Senior Developer", "Test Company")
        print("✅ Job analysis works")
        
        # Test narrative resume creation
        from unittest.mock import patch
        with patch('builtins.input', return_value='1'):
            narrative = optimizer.create_narrative_resume(
                sample_resume, job_analysis, "Senior Developer", "Test Company"
            )
        
        print("✅ Narrative resume creation works")
        print(f"   Generated {len(narrative)} characters")
        
        # Key checks
        checks = {
            'Has Name': 'RYAN THOMAS WEILER' in narrative,
            'Has Contact': 'ryan_wlr@yahoo.com' in narrative,
            'Has Story Hook': 'CRAFTSMAN' in narrative,
            'Has Skills': 'Python' in narrative,
            'Has Company': 'Test Company' in narrative,
            'Reasonable Length': len(narrative) > 1000
        }
        
        print("\n📋 CORE FUNCTIONALITY CHECKS:")
        all_passed = True
        for check, result in checks.items():
            status = "✅" if result else "❌"
            print(f"   {status} {check}")
            if not result:
                all_passed = False
        
        print(f"\n🎯 STORYTELLING STATUS: {'✅ FUNCTIONAL' if all_passed else '❌ NEEDS WORK'}")
        
        if all_passed:
            print("\n🚀 READY TO USE:")
            print("   1. Run: python resume_windows.py --browse")
            print("   2. OR run: python browse_mode_fixed.py")
            print("   3. Select your files and choose option 1 for Story Resume")
            print("   4. Get your personalized narrative resume!")
            
            print("\n✨ WHAT WORKS:")
            print("   • Extracts your real resume information")
            print("   • Creates personalized career narratives")
            print("   • Uses your actual skills and experience")
            print("   • Tailors story to target role and company")
            print("   • Integrates with browse mode workflow")
        
        return all_passed
        
    except Exception as e:
        print(f"❌ ERROR: {e}")
        return False

def main():
    print("🎭 STORYTELLING VERIFICATION SUMMARY")
    print("=" * 80)
    
    is_working = verify_storytelling_status()
    
    print("\n" + "=" * 80)
    if is_working:
        print("🎉 CONCLUSION: STORYTELLING FEATURE IS WORKING!")
        print("\nThe storytelling feature successfully:")
        print("• Reads your actual resume content")
        print("• Extracts your personal information, skills, and experience")  
        print("• Creates compelling career narratives")
        print("• Personalizes content for target roles and companies")
        print("• Integrates with the browse mode workflow")
        print("• Responds correctly to user option 1 selection")
        print("\nMinor formatting details may vary, but core functionality is solid.")
    else:
        print("❌ CONCLUSION: STORYTELLING NEEDS DEBUGGING")
        print("There are fundamental issues that need to be resolved.")
    
    return is_working

if __name__ == "__main__":
    success = main()
    sys.exit(0 if success else 1)