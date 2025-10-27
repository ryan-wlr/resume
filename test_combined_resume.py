#!/usr/bin/env python3
"""Test the new combined resume functionality for Option 3"""

import sys
import os
import tempfile
import shutil

# Add the current directory to path
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))

from resume_windows import ResumeOptimizer

def test_combined_resume():
    """Test that option 3 creates a truly combined resume with both storytelling and professional elements"""
    print("🔍 Testing Combined Resume functionality (Option 3)...")
    
    # Create temp output directory
    temp_dir = tempfile.mkdtemp()
    print(f"Using temp directory: {temp_dir}")
    
    try:
        # Initialize optimizer
        optimizer = ResumeOptimizer()
        
        # Mock the style choice input to simulate option 3
        import builtins
        original_input = builtins.input
        inputs = iter(['3'])  # Option 3: Both versions (now combined)
        builtins.input = lambda prompt: next(inputs)
        
        try:
            # Mock job description and resume content
            job_description = """
            Job Title: Data Scientist
            Company: NASA
            
            We are seeking an experienced Data Scientist to join our team.
            
            Requirements:
            - Advanced machine learning experience
            - Python and R programming
            - Statistical analysis expertise
            - Big data technologies
            
            Experience:
            - 5+ years data science experience
            - PhD in Data Science or related field
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
                job_description, resume_content, "data scientist", "nasa"
            )
            
            # Save results
            optimizer.save_results_to_files(results, temp_dir)
            
            # Check what files were created
            files_created = os.listdir(temp_dir)
            print(f"\n📁 Files created ({len(files_created)} total):")
            for file in sorted(files_created):
                print(f"   • {file}")
            
            # Check for the new combined resume
            combined_file = 'combined_comprehensive_resume.txt'
            combined_exists = combined_file in files_created
            print(f"\n📋 Combined Resume Check:")
            print(f"   {'✅' if combined_exists else '❌'} {combined_file}: {'Found' if combined_exists else 'Missing'}")
            
            # Check results dictionary
            print(f"\n📊 Results Dictionary Check:")
            combined_result = '7_combined_resume' in results
            narrative_ref = '8_narrative_only' in results 
            enhanced_ref = '9_enhanced_only' in results
            
            print(f"   {'✅' if combined_result else '❌'} 7_combined_resume: {'Present' if combined_result else 'Missing'}")
            print(f"   {'✅' if narrative_ref else '❌'} 8_narrative_only: {'Present' if narrative_ref else 'Missing'}")
            print(f"   {'✅' if enhanced_ref else '❌'} 9_enhanced_only: {'Present' if enhanced_ref else 'Missing'}")
            
            # Check combined content
            if combined_result:
                combined_content = results['7_combined_resume']
                print(f"\n📖 Combined Resume Analysis:")
                
                # Check for storytelling elements
                has_hook = ('🔥 THE' in combined_content or '🔬 THE' in combined_content or 
                           '💻 THE' in combined_content or '🌟 THE' in combined_content)
                has_narrative = 'CAREER NARRATIVE' in combined_content
                has_achievements = 'SIGNATURE ACHIEVEMENTS' in combined_content
                
                # Check for professional elements  
                has_summary = 'PROFESSIONAL SUMMARY' in combined_content
                has_competencies = 'CORE TECHNICAL COMPETENCIES' in combined_content
                has_experience = 'PROFESSIONAL EXPERIENCE' in combined_content
                
                print(f"   Storytelling Elements:")
                print(f"     {'✅' if has_hook else '❌'} Opening Hook")
                print(f"     {'✅' if has_narrative else '❌'} Career Narrative")
                print(f"     {'✅' if has_achievements else '❌'} Signature Achievements")
                
                print(f"   Professional Elements:")
                print(f"     {'✅' if has_summary else '❌'} Professional Summary")
                print(f"     {'✅' if has_competencies else '❌'} Technical Competencies")
                print(f"     {'✅' if has_experience else '❌'} Professional Experience")
                
                total_elements = sum([has_hook, has_narrative, has_achievements, 
                                    has_summary, has_competencies, has_experience])
                
                if total_elements >= 5:
                    print(f"\n🎉 SUCCESS: Combined resume has both storytelling and professional elements!")
                    print(f"   • {total_elements}/6 key sections present")
                    print(f"   • True combination of narrative and professional content")
                else:
                    print(f"\n⚠️  Partial success: {total_elements}/6 elements found")
                
                # Show preview
                preview = combined_content[:300] + "..."
                print(f"\n📄 Combined Resume Preview:\n{preview}")
            
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
    test_combined_resume()