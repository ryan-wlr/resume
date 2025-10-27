#!/usr/bin/env python3
"""
Test that storytelling files are actually saved correctly
"""

from resume_windows import ResumeOptimizer
import os
import shutil
from datetime import datetime

def test_storytelling_file_output():
    """Test that storytelling creates proper output files"""
    
    print("🧪 TESTING STORYTELLING FILE OUTPUT")
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
    
    # Mock the user input for storytelling choice
    import builtins
    original_input = builtins.input
    
    def mock_input(prompt):
        if "Choose resume style" in prompt:
            print(">>> Selecting option 1 (Story Resume)")
            return "1"
        return ""
    
    builtins.input = mock_input
    
    try:
        print("🚀 RUNNING COMPLETE OPTIMIZATION WITH FILE SAVING")
        print("-" * 50)
        
        # Run optimization
        results = optimizer.process_complete_optimization(
            job_content, 
            resume_content, 
            "Senior Welder", 
            "MetalWorks Construction"
        )
        
        # Save results to test directory
        test_output_dir = f"test_storytelling_output_{datetime.now().strftime('%H%M%S')}"
        optimizer.save_results_to_files(results, test_output_dir)
        
        print()
        print("📂 CHECKING OUTPUT FILES:")
        print("-" * 30)
        
        if os.path.exists(test_output_dir):
            files = os.listdir(test_output_dir)
            print(f"✅ Output directory created: {test_output_dir}")
            print(f"📁 Files created: {len(files)}")
            
            # Check for narrative file specifically
            narrative_file = None
            for file in files:
                print(f"   📄 {file}")
                if 'narrative' in file.lower() or 'story' in file.lower():
                    narrative_file = file
            
            if narrative_file:
                print(f"\n📖 STORYTELLING FILE FOUND: {narrative_file}")
                narrative_path = os.path.join(test_output_dir, narrative_file)
                
                with open(narrative_path, 'r', encoding='utf-8') as f:
                    content = f.read()
                
                print(f"📊 File size: {len(content)} characters")
                
                # Check for key storytelling elements
                story_checks = {
                    'Metal Master Hook': '🔥 THE METAL MASTER' in content,
                    'Welding Narrative': 'art meets engineering' in content,
                    'Company Name': 'MetalWorks Construction' in content,
                    'Professional Narrative': 'PROFESSIONAL NARRATIVE:' in content,
                    'Career Progression': 'Chapter 1:' in content or 'THE FOUNDATION' in content,
                    'Achievements': 'Achieved' in content or 'Completed' in content,
                    'Projects': 'Structural Steel' in content or 'Pipeline' in content
                }
                
                print("\n🎭 STORYTELLING CONTENT VERIFICATION:")
                all_found = True
                for element, found in story_checks.items():
                    status = "✅" if found else "❌"
                    print(f"   {status} {element}")
                    if not found:
                        all_found = False
                
                print(f"\n📖 CONTENT PREVIEW:")
                print("=" * 40)
                print(content[:400] + "...")
                print("=" * 40)
                
                if all_found:
                    print("\n🎉 STORYTELLING FILE OUTPUT: ✅ SUCCESS!")
                    print("✅ All storytelling elements properly saved to file")
                    print(f"✅ Users can find their storytelling resume in: {narrative_file}")
                else:
                    print("\n❌ Some storytelling elements missing from saved file")
                
                # Clean up test directory
                try:
                    shutil.rmtree(test_output_dir)
                    print(f"🧹 Cleaned up test directory: {test_output_dir}")
                except:
                    pass
                    
            else:
                print("\n❌ No storytelling/narrative file found in output")
                
        else:
            print("❌ Output directory not created")
    
    finally:
        # Restore original input
        builtins.input = original_input

if __name__ == "__main__":
    test_storytelling_file_output()