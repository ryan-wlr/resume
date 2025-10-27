#!/usr/bin/env python3
"""
Demo Script: Resume Storytelling Feature
========================================

This script demonstrates the new narrative storytelling feature for resumes.
It creates story-driven resumes that show career progression and tell a compelling narrative.
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
    print("Make sure resume_windows.py is in the same directory")
    sys.exit(1)

def main():
    print("🎭 RESUME STORYTELLING DEMO")
    print("=" * 50)
    print("This demo shows how to create narrative-driven resumes that tell your career story.")
    print()
    
    # Sample resume content
    sample_resume = """Ryan Thomas Weiler
Software Engineer

Contact: ryan_wlr@yahoo.com | (561) 906-2118
LinkedIn: https://www.linkedin.com/in/ryan-weiler-7a3119190/
GitHub: https://github.com/ryan-wlr

Experience:
- Developed Python applications for financial analysis
- Created automated trading algorithms 
- Built web applications using Django and Flask
- Worked with data analysis using pandas and NumPy

Skills:
Python, Django, Flask, pandas, NumPy, JavaScript, SQL, Git

Education:
Computer Science coursework at Florida Atlantic University"""

    # Sample job descriptions for different storytelling examples
    job_descriptions = {
        "Software Engineer": """Software Engineer - FinTech Company
        
We're looking for a passionate Software Engineer to join our financial technology team.
You'll work on cutting-edge algorithms and build systems that process millions of transactions.

Required: Python, machine learning, financial markets knowledge, algorithmic trading
Preferred: AWS, Docker, React, quantitative analysis

Join us in revolutionizing how people interact with financial markets!""",
        
        "Quantum Computing Scientist": """Quantum Computing Research Scientist - Tech Giant
        
We seek a brilliant quantum computing scientist to push the boundaries of computation.
You'll develop quantum algorithms and work on error correction for fault-tolerant systems.

Required: Quantum mechanics, linear algebra, quantum algorithms, error correction
Preferred: VQE, QAOA, surface codes, topological qubits

Help us build the quantum computers of tomorrow!""",
        
        "Mathematics Professor": """Mathematics Professor - Research University
        
Join our mathematics department as a tenured professor in pure mathematics.
You'll conduct research in algebraic geometry and teach graduate students.

Required: Ph.D. in Mathematics, research publications, teaching experience
Preferred: Algebraic geometry, cohomology theory, category theory

Shape the next generation of mathematical minds!"""
    }
    
    # Initialize optimizer
    print(">>> Initializing Resume Optimizer...")
    optimizer = ResumeOptimizer()
    print()
    
    # Demonstrate storytelling for different career fields
    for role, job_desc in job_descriptions.items():
        print(f"🎯 CREATING STORY RESUME FOR: {role}")
        print("-" * 60)
        
        try:
            # Get field-specific story elements
            detected_field = optimizer.detect_career_field(role.lower())
            print(f"Detected field: {detected_field}")
            
            # Generate story elements
            story_elements = optimizer.generate_career_story(detected_field, role, "Demo Company")
            
            print("\n📖 STORY ELEMENTS PREVIEW:")
            print(f"Opening Hook: {story_elements['opening_hook'][:100]}...")
            print(f"Career Chapters: {len(story_elements['career_progression'].split('Chapter'))}")
            print(f"Signature Achievements: {len(story_elements['signature_achievements'])}")
            print(f"Story Projects: {len(story_elements['story_projects'])}")
            print()
            
            # Create mini narrative resume preview
            print("✨ NARRATIVE RESUME PREVIEW:")
            print(f"""
{story_elements['opening_hook']}

RYAN THOMAS WEILER
{detected_field.replace('_', ' ').title()} Professional

{story_elements['professional_narrative'][:300]}...

CAREER JOURNEY HIGHLIGHTS:
{chr(10).join(['• ' + achievement for achievement in story_elements['signature_achievements'][:3]])}

{story_elements['closing_vision'][:200]}...
""")
            
        except Exception as e:
            print(f"ERROR creating story for {role}: {e}")
        
        print("\n" + "="*80 + "\n")
    
    # Summary
    print("🎉 STORYTELLING DEMO COMPLETE!")
    print()
    print("KEY FEATURES DEMONSTRATED:")
    print("• Field-specific career narratives")
    print("• Compelling opening hooks and closing visions")
    print("• Career progression structured as story chapters")
    print("• Signature achievements that define professional journey")
    print("• Story projects showing growth and impact")
    print()
    print("💡 TO USE STORYTELLING IN MAIN SYSTEM:")
    print("1. Run: python resume_windows.py --browse")
    print("2. Choose option 1 for 'Story Resume' when prompted")
    print("3. Or choose option 3 for both story and standard versions")
    print()
    print("📝 The story resume tells a compelling narrative that shows:")
    print("• How you discovered your passion")
    print("• Your journey of growth and learning")
    print("• Major breakthroughs and achievements")
    print("• Your vision for the future")
    print()
    print("This approach helps recruiters and hiring managers see you as a")
    print("complete professional with a clear trajectory, not just a list of skills!")

if __name__ == "__main__":
    main()