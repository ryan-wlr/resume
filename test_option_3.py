#!/usr/bin/env python3
"""Test Option 3 (Both Versions) functionality"""

import sys
import os
import tempfile
import shutil

# Add the current directory to path
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))

from resume_windows import ResumeOptimizer

def test_option_3():
    """Test that option 3 creates both narrative and standard resume versions"""
    print("🔍 Testing Option 3 (Both Versions) functionality...")
    
    # Create temp output directory
    temp_dir = tempfile.mkdtemp()
    print(f"Using temp directory: {temp_dir}")
    
    try:
        # Initialize optimizer
        optimizer = ResumeOptimizer()
        
        # Mock the style choice input to simulate option 3
        import builtins
        original_input = builtins.input
        inputs = iter(['3'])  # Option 3: Both versions
        builtins.input = lambda prompt: next(inputs)
        
        try:
            # Mock job description and resume content
            job_description = """
            Job Title: Optical Engineer
            Company: NASA
            
            We are seeking an experienced Optical Engineer to join our team.
            
            Requirements:
            - Advanced optical design experience
            - Laser systems knowledge
            - Fiber optic communications
            - Zemax and Code V proficiency
            
            Experience:
            - 5+ years optical engineering
            - Aerospace applications preferred
            - PhD in Optics or related field
            """
            
            resume_content = """
            Ryan Thomas Weiler
            (561) 906-2118 | ryan_wlr@yahoo.com
            
            Experience:
            Software Developer - Built neural networks and ML systems
            
            Education: 
            University of Central Florida — B.S. Computer Science, 2013
            Valencia College — A.A., 2011
            
            Skills:
            Python, Machine Learning, Data Analysis
            """
            
            # Run the complete optimization with option 3
            results = optimizer.process_complete_optimization(
                job_description, resume_content, "optical engineer", "nasa"
            )
            
            # Save results
            optimizer.save_results_to_files(results, temp_dir)
            
            # Check what files were created
            files_created = os.listdir(temp_dir)
            print(f"\n📁 Files created ({len(files_created)} total):")
            for file in sorted(files_created):
                print(f"   • {file}")
            
            # Check for expected files
            expected_files = [
                'narrative_story_resume.txt',
                'enhanced_standard_resume.txt',
                'narrative_story_resume.docx',
                'enhanced_standard_resume.docx'
            ]
            
            print(f"\n📊 Expected files check:")
            all_found = True
            for expected in expected_files:
                found = expected in files_created
                status = "✅" if found else "❌"
                print(f"   {status} {expected}: {'Found' if found else 'Missing'}")
                if not found:
                    all_found = False
            
            # Check if both resume versions exist in results
            print(f"\n📋 Results dictionary check:")
            narrative_exists = '7_narrative_resume' in results
            standard_exists = '8_enhanced_resume' in results
            
            print(f"   {'✅' if narrative_exists else '❌'} 7_narrative_resume: {'Present' if narrative_exists else 'Missing'}")
            print(f"   {'✅' if standard_exists else '❌'} 8_enhanced_resume: {'Present' if standard_exists else 'Missing'}")
            
            if all_found and narrative_exists and standard_exists:
                print(f"\n🎉 SUCCESS: Option 3 working correctly!")
                print(f"   • Both text files created")
                print(f"   • Both DOCX files created") 
                print(f"   • Both resume versions in results")
            else:
                print(f"\n❌ ISSUES FOUND with Option 3")
                print(f"   • Check missing files or missing result keys")
            
            # Show brief content check
            if narrative_exists:
                narrative_preview = results['7_narrative_resume'][:100] + "..."
                print(f"\n📖 Narrative preview: {narrative_preview}")
            
            if standard_exists:
                standard_preview = results['8_enhanced_resume'][:100] + "..."
                print(f"\n📄 Standard preview: {standard_preview}")
                
        finally:
            # Restore original input function
            builtins.input = original_input
            
    except Exception as e:
        print(f"❌ Error during testing: {e}")
        import traceback
        traceback.print_exc()
        
    finally:
        # Clean up
        try:
            shutil.rmtree(temp_dir)
            print(f"\n🗑️  Cleaned up temp directory: {temp_dir}")
        except:
            pass

if __name__ == "__main__":
    test_option_3()