#!/usr/bin/env python3
"""
Test Updated Storytelling Feature
================================

Test that the storytelling feature now uses actual resume content instead of default templates.
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

def test_personalized_storytelling():
    print("🧪 TESTING PERSONALIZED STORYTELLING FEATURE")
    print("=" * 60)
    
    # Sample resume with actual content
    sample_resume = """John Smith
Senior Software Engineer

Contact Information:
Email: john.smith@email.com
Phone: (555) 123-4567
LinkedIn: linkedin.com/in/johnsmith
GitHub: github.com/johnsmith

Experience:
- Led development of microservices architecture serving 1M+ users
- Improved system performance by 40% through database optimization
- Mentored 5 junior developers on React and Node.js best practices
- Built automated CI/CD pipeline reducing deployment time by 60%

Skills:
Python, JavaScript, React, Node.js, Docker, AWS, PostgreSQL, Redis, Git

Education:
Bachelor of Computer Science, University of Technology, 2018

Projects:
- E-commerce Platform: Full-stack application with payment integration
- Real-time Chat System: WebSocket-based messaging with 10k concurrent users
- Machine Learning Recommender: Collaborative filtering for product suggestions"""

    sample_job = """Senior Full Stack Developer - Tech Startup
    
We need a senior developer to lead our product development team.
You'll work on scalable web applications and mentor junior developers.

Required: JavaScript, React, Node.js, Python, AWS
Preferred: Docker, microservices, team leadership"""

    # Initialize optimizer
    optimizer = ResumeOptimizer()
    
    print(">>> Testing resume information extraction...")
    resume_info = optimizer.extract_resume_information(sample_resume)
    
    print("✅ EXTRACTED RESUME INFORMATION:")
    print(f"   Name: {resume_info['name']}")
    print(f"   Skills: {resume_info['skills'][:5]}...")  # Show first 5 skills
    print(f"   Experience entries: {len(resume_info['experience'])}")
    print(f"   Projects: {len(resume_info['projects'])}")
    print(f"   Education: {resume_info['education'][:50]}...")
    
    print("\n>>> Testing personalized story generation...")
    job_analysis = optimizer.analyze_job_posting(sample_job, "Senior Full Stack Developer", "Tech Startup")
    
    # Test narrative resume with real data
    try:
        narrative_resume = optimizer.create_narrative_resume(
            sample_resume, job_analysis, "Senior Full Stack Developer", "Tech Startup"
        )
        
        print("✅ PERSONALIZED NARRATIVE RESUME CREATED!")
        print(f"   Resume length: {len(narrative_resume)} characters")
        
        # Check if actual content is used
        name_used = "JOHN SMITH" in narrative_resume
        skills_used = any(skill in narrative_resume for skill in ["Python", "JavaScript", "React"])
        experience_used = "microservices" in narrative_resume or "40%" in narrative_resume
        projects_used = "E-commerce" in narrative_resume or "Chat System" in narrative_resume
        
        print(f"   ✅ Name from resume used: {name_used}")
        print(f"   ✅ Skills from resume used: {skills_used}")
        print(f"   ✅ Experience from resume used: {experience_used}")
        print(f"   ✅ Projects from resume used: {projects_used}")
        
        # Show a sample of the personalized content
        print("\n📖 PERSONALIZED NARRATIVE PREVIEW:")
        lines = narrative_resume.split('\n')
        for i, line in enumerate(lines[:15]):  # Show first 15 lines
            print(f"   {line}")
        print("   ...")
        
        if name_used and skills_used:
            print("\n🎉 SUCCESS: Storytelling now uses actual resume content!")
            return True
        else:
            print("\n❌ ISSUE: Still using default content instead of actual resume")
            return False
            
    except Exception as e:
        print(f"❌ Error creating personalized narrative: {e}")
        return False

if __name__ == "__main__":
    success = test_personalized_storytelling()
    
    if success:
        print("\n💡 NOW YOU CAN CREATE PERSONALIZED STORY RESUMES!")
        print("   Run: python resume_windows.py --browse")
        print("   Choose option 1 for personalized story resumes")
    else:
        print("\n⚠️ There may still be issues with personalization")
    
    sys.exit(0 if success else 1)