#!/usr/bin/env python3
"""
Quick Demo - Resume Optimizer with Sample Files
This demonstrates the resume optimizer working with the provided sample files.
"""

import os
import sys

# Add current directory to path
sys.path.insert(0, os.getcwd())

def run_demo():
    """Run a demonstration with the sample files"""
    print("🎯 RESUME OPTIMIZER DEMO")
    print("=" * 40)
    print("This demo will optimize a resume for a brain surgeon position")
    print("using our sample files to avoid any DOCX file issues.")
    print()
    
    # Check if sample files exist
    job_file = 'sample_brain_surgeon_job.txt'
    resume_file = 'sample_current_resume.txt'
    
    if not os.path.exists(job_file):
        print(f"❌ Missing sample file: {job_file}")
        return
        
    if not os.path.exists(resume_file):
        print(f"❌ Missing sample file: {resume_file}")
        return
    
    print(f"✅ Found sample job description: {job_file}")
    print(f"✅ Found sample resume: {resume_file}")
    print()
    
    try:
        from resume_windows import ResumeOptimizer
        
        # Read the sample files
        with open(job_file, 'r', encoding='utf-8') as f:
            job_content = f.read()
            
        with open(resume_file, 'r', encoding='utf-8') as f:
            resume_content = f.read()
        
        print("📋 DEMO PARAMETERS:")
        print(f"   Job Description: {len(job_content)} characters")
        print(f"   Current Resume: {len(resume_content)} characters")
        print(f"   Target Role: Brain Surgeon")
        print(f"   Target Company: Medical Center")
        print()
        
        input("Press Enter to start optimization...")
        
        # Run the optimizer
        optimizer = ResumeOptimizer()
        results = optimizer.process_complete_optimization(
            job_content, resume_content, "Brain Surgeon", "Medical Center"
        )
        
        # Save results
        from datetime import datetime
        output_dir = f"demo_output_{datetime.now().strftime('%Y%m%d_%H%M%S')}"
        optimizer.save_results_to_files(results, output_dir)
        
        print(f"\n🎉 DEMO COMPLETE!")
        print(f"📂 Results saved to: {output_dir}")
        print(f"📄 Check the optimized_resume.docx file!")
        print()
        
        # Show a preview of the optimized resume
        if '7_tailored_resume' in results:
            preview = results['7_tailored_resume'][:500]
            print("📝 PREVIEW OF OPTIMIZED RESUME:")
            print("=" * 45)
            print(preview + "...")
            print("=" * 45)
        
        print(f"\n✅ Demo successful! The system can generate professional resumes for ANY field.")
        print("🔧 To fix your DOCX file issue:")
        print("   1. Copy the DOCX from OneDrive to Desktop")
        print("   2. Open in Word and Save As > Plain Text (.txt)")
        print("   3. Use the .txt file instead")
        
    except Exception as e:
        print(f"❌ Demo error: {e}")
        import traceback
        traceback.print_exc()

if __name__ == "__main__":
    run_demo()