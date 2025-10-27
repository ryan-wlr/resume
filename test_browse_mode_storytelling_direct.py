#!/usr/bin/env python3
"""
Direct Browse Mode Storytelling Test
===================================

This test simulates exactly what happens when a user selects option 1 
for storytelling in the browse_mode_fixed.py workflow.
"""

import sys
import os
import tempfile
from datetime import datetime
from unittest.mock import patch
import io

# Add current directory to path
sys.path.append(os.path.dirname(os.path.abspath(__file__)))

def test_browse_mode_storytelling_flow():
    """Test the exact flow that happens in browse_mode_fixed.py with storytelling"""
    print("🎯 DIRECT BROWSE MODE STORYTELLING TEST")
    print("=" * 70)
    
    # Create test files
    job_content = """Senior Python Developer - FinTech
    
We need a skilled Python developer for our trading platform.
You'll work on algorithmic trading and data analysis systems.

Required: Python, Django, financial markets, algorithmic trading
Preferred: AWS, Docker, React, machine learning"""

    resume_content = """Ryan Thomas Weiler
Python Developer

Email: ryan_wlr@yahoo.com
Phone: (561) 906-2118

Experience:
- Built Python trading algorithms achieving 15% returns
- Developed Django web applications for financial analysis
- Created real-time data processing systems

Skills: Python, Django, Flask, pandas, algorithmic trading, AWS"""

    # Write to temp files
    with tempfile.NamedTemporaryFile(mode='w', suffix='.txt', delete=False) as f:
        f.write(job_content)
        job_file = f.name
    
    with tempfile.NamedTemporaryFile(mode='w', suffix='.txt', delete=False) as f:
        f.write(resume_content)
        resume_file = f.name
    
    try:
        print(">>> Importing browse_mode_fixed...")
        import browse_mode_fixed
        
        print(">>> Reading test files using browse_mode functions...")
        job_text = browse_mode_fixed.read_file_safely(job_file)
        resume_text = browse_mode_fixed.read_file_safely(resume_file)
        
        if "Error:" in job_text or "Error:" in resume_text:
            print(f"❌ File reading failed: {job_text if 'Error:' in job_text else resume_text}")
            return False
        
        print("✅ Files read successfully by browse_mode functions")
        
        # Test the ResumeOptimizer import and process that browse_mode uses
        print(">>> Testing ResumeOptimizer import (as browse_mode does)...")
        from resume_windows import ResumeOptimizer
        
        optimizer = ResumeOptimizer()
        print("✅ ResumeOptimizer initialized successfully")
        
        # Simulate the process_complete_optimization call with user input simulation
        print(">>> Testing process_complete_optimization with storytelling...")
        
        # Mock the input for storytelling choice (option 1)
        with patch('builtins.input', side_effect=['1']):  # User chooses option 1 (Story Resume)
            print("   (Simulating user choosing option 1 for Story Resume)")
            
            results = optimizer.process_complete_optimization(
                job_content, resume_content, "Senior Python Developer", "FinTech Company"
            )
        
        print("✅ process_complete_optimization completed with storytelling choice!")
        
        # Analyze results
        print("\n📊 STORYTELLING RESULTS ANALYSIS:")
        
        story_found = False
        narrative_key = None
        
        for key, content in results.items():
            if 'narrative' in key.lower() or 'story' in key.lower():
                story_found = True
                narrative_key = key
                break
        
        if story_found:
            print(f"   ✅ Story resume created: {narrative_key}")
            narrative_content = results[narrative_key]
            
            # Check personalization
            personalizations = {
                'Name': 'RYAN THOMAS WEILER' in narrative_content,
                'Contact': 'ryan_wlr@yahoo.com' in narrative_content,
                'Skills': 'Python' in narrative_content and 'Django' in narrative_content,
                'Story Elements': any(elem in narrative_content for elem in ['CRAFTSMAN', 'journey', 'story']),
                'Target Company': 'FinTech Company' in narrative_content
            }
            
            print("   📋 Personalization Check:")
            all_personalized = True
            for check, passed in personalizations.items():
                status = "✅" if passed else "❌"
                print(f"      {status} {check}")
                if not passed:
                    all_personalized = False
            
            if all_personalized:
                print("   🎉 ALL PERSONALIZATION CHECKS PASSED!")
            else:
                print("   ⚠️  Some personalization issues found")
            
            # Show preview
            print("\n   📖 Story Resume Preview (first 300 chars):")
            print(f"      {narrative_content[:300]}...")
            
            return all_personalized
        else:
            print("   ❌ No story resume found in results")
            print(f"   Available keys: {list(results.keys())}")
            return False
    
    except Exception as e:
        print(f"❌ ERROR: {e}")
        import traceback
        traceback.print_exc()
        return False
    
    finally:
        # Clean up
        try:
            os.unlink(job_file)
            os.unlink(resume_file)
        except:
            pass

def test_user_workflow_simulation():
    """Simulate the complete user workflow"""
    print("\n🎭 USER WORKFLOW SIMULATION")
    print("=" * 70)
    
    print("This simulates what happens when a user:")
    print("1. Runs: python browse_mode_fixed.py")
    print("2. Selects job description and resume files")
    print("3. Enters target role and company")
    print("4. The system calls process_complete_optimization")
    print("5. User is prompted to choose resume style")
    print("6. User selects option 1 (Story Resume)")
    print("7. System generates personalized story resume")
    
    workflow_test = test_browse_mode_storytelling_flow()
    
    if workflow_test:
        print("\n✅ USER WORKFLOW TEST: PASSED")
        print("   The storytelling feature works correctly in browse mode!")
    else:
        print("\n❌ USER WORKFLOW TEST: FAILED")
        print("   There are issues with the storytelling integration")
    
    return workflow_test

def main():
    print("🧪 BROWSE MODE STORYTELLING VERIFICATION")
    print("=" * 80)
    print("Testing that option 1 (Story Resume) works in browse_mode_fixed.py")
    print()
    
    workflow_passed = test_user_workflow_simulation()
    
    print("\n" + "=" * 80)
    if workflow_passed:
        print("🎉 VERIFICATION COMPLETE: STORYTELLING WORKS IN BROWSE MODE!")
        print()
        print("✅ How to use storytelling:")
        print("   1. Run: python browse_mode_fixed.py")
        print("   2. Select your job description file")
        print("   3. Select your resume file") 
        print("   4. Enter target role and company")
        print("   5. When prompted for resume style, choose 1")
        print("   6. Get your personalized story resume!")
        print()
        print("✅ Or use the main system:")
        print("   1. Run: python resume_windows.py --browse")
        print("   2. Follow the same steps")
    else:
        print("❌ VERIFICATION FAILED: Issues found with storytelling integration")
        print("   The storytelling feature may not work properly in browse mode")
    
    return workflow_passed

if __name__ == "__main__":
    success = main()
    sys.exit(0 if success else 1)