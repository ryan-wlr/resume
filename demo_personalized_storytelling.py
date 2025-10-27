#!/usr/bin/env python3
"""
Demo: Before vs After Storytelling Fix
=====================================

This demonstrates the difference between the old default templates and 
the new personalized storytelling that uses actual resume content.
"""

import sys
import os

# Add current directory to path
sys.path.append(os.path.dirname(os.path.abspath(__file__)))

try:
    from resume_windows import ResumeOptimizer
except ImportError as e:
    print(f"ERROR: Could not import ResumeOptimizer: {e}")
    sys.exit(1)

def demo_personalized_vs_generic():
    print("🎭 STORYTELLING DEMO: PERSONALIZED vs GENERIC")
    print("=" * 80)
    
    # Your actual resume content
    your_resume = """Ryan Thomas Weiler
Software Engineer

Contact: ryan_wlr@yahoo.com | (561) 906-2118
LinkedIn: https://www.linkedin.com/in/ryan-weiler-7a3119190/
GitHub: https://github.com/ryan-wlr

Experience:
- Developed Python applications for financial analysis and algorithmic trading
- Created automated trading systems achieving 15% annual returns
- Built web applications using Django and Flask frameworks
- Implemented data analysis pipelines using pandas and NumPy
- Worked with financial APIs and real-time market data

Skills:
Python, Django, Flask, pandas, NumPy, JavaScript, SQL, Git, Financial Analysis, Algorithmic Trading

Education:
Computer Science coursework at Florida Atlantic University

Projects:
- Algorithmic Trading Bot: Python-based system for automated stock trading
- Financial Dashboard: Real-time market data visualization using Django
- Portfolio Optimizer: Risk management tool using modern portfolio theory"""

    job_posting = """Senior Software Engineer - FinTech
    
We're looking for a talented engineer to join our financial technology team.
You'll work on trading algorithms and build systems for financial analysis.

Required: Python, financial markets knowledge, algorithmic trading experience
Preferred: Django, pandas, real-time systems"""

    # Initialize optimizer
    optimizer = ResumeOptimizer()
    
    print(">>> Creating personalized story resume using YOUR actual content...")
    job_analysis = optimizer.analyze_job_posting(job_posting, "Senior Software Engineer", "FinTech Company")
    
    # Extract your actual information
    resume_info = optimizer.extract_resume_information(your_resume)
    
    print("\n📊 YOUR ACTUAL RESUME DATA EXTRACTED:")
    print(f"   Name: {resume_info['name']}")
    print(f"   Skills: {', '.join(resume_info['skills'][:6])}")
    print(f"   Experience: {len(resume_info['experience'])} entries")
    print(f"   Projects: {len(resume_info['projects'])} projects")
    
    # Create personalized story
    narrative_resume = optimizer.create_narrative_resume(
        your_resume, job_analysis, "Senior Software Engineer", "FinTech Company"
    )
    
    print("\n✨ YOUR PERSONALIZED STORY RESUME PREVIEW:")
    print("-" * 60)
    
    # Show key personalized sections
    lines = narrative_resume.split('\n')
    in_key_section = False
    
    for line in lines:
        # Show opening, name, contact, and key achievements
        if any(marker in line for marker in [
            'CAREER STORY RESUME', 'THE CODE CRAFTSMAN', 'RYAN THOMAS WEILER', 
            'ryan_wlr@yahoo.com', 'KEY ACHIEVEMENTS', 'algorithmic trading', 
            'Django', 'pandas', 'Trading Bot', 'Financial Dashboard'
        ]):
            print(f"   {line}")
            in_key_section = True
        elif in_key_section and line.strip() == "":
            print()
            in_key_section = False
        elif in_key_section:
            print(f"   {line}")
    
    print("\n🎯 KEY PERSONALIZATIONS:")
    print("   ✅ Uses YOUR name: Ryan Thomas Weiler")
    print("   ✅ Uses YOUR contact info: ryan_wlr@yahoo.com")
    print("   ✅ Features YOUR skills: Python, Django, pandas, algorithmic trading")
    print("   ✅ Includes YOUR projects: Trading Bot, Financial Dashboard")
    print("   ✅ References YOUR experience: financial analysis, trading systems")
    print("   ✅ Tailored to target role: Senior Software Engineer at FinTech")
    
    print("\n🆚 DIFFERENCE FROM BEFORE:")
    print("   ❌ OLD: Used generic finance resume template")
    print("   ❌ OLD: Same content for everyone") 
    print("   ❌ OLD: Didn't read your actual resume")
    print("   ✅ NEW: Extracts YOUR specific information")
    print("   ✅ NEW: Creates story based on YOUR experience")
    print("   ✅ NEW: Personalizes every section to YOU")
    
    print("\n🚀 TO USE YOUR PERSONALIZED STORY RESUME:")
    print("   1. Run: python resume_windows.py --browse")
    print("   2. Select your job description file")
    print("   3. Select your resume file") 
    print("   4. Choose option 1 for 'Story Resume'")
    print("   5. Get a narrative that tells YOUR unique story!")
    
    print("\n💡 The system now:")
    print("   • Reads your actual resume content")
    print("   • Extracts your real skills, experience, and projects")
    print("   • Creates a personalized career narrative")
    print("   • Adapts the story to your target role")
    print("   • Makes YOU the hero of your professional story!")

if __name__ == "__main__":
    demo_personalized_vs_generic()