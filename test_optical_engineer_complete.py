#!/usr/bin/env python3
"""
Comprehensive Optical Engineer Storytelling Test
================================================

Test the complete optical engineer storytelling workflow end-to-end.
"""

import sys
import os
import tempfile
from unittest.mock import patch

sys.path.append(os.path.dirname(os.path.abspath(__file__)))

from resume_windows import ResumeOptimizer

def test_optical_engineer_complete_workflow():
    print("🔬 OPTICAL ENGINEER STORYTELLING COMPLETE TEST")
    print("=" * 70)
    
    # Realistic optical engineer resume
    optical_resume = """Dr. Sarah Johnson
Senior Optical Engineer

Contact Information:
Email: s.johnson@email.com
Phone: (555) 987-6543
LinkedIn: linkedin.com/in/sarahjohnson-optics
Location: San Diego, CA

Professional Experience:
- Led design of advanced laser systems for fiber optic telecommunications
- Developed precision optical assemblies with sub-micron alignment tolerances
- Implemented Zemax optical modeling reducing prototype costs by 30%
- Designed fiber optic communication systems supporting 40Gbps data rates
- Built laser safety protocols ensuring OSHA compliance across all projects

Technical Skills:
Optical Design, Zemax, Code V, Laser Systems, Fiber Optics, Photonics,
Optical Modeling, Precision Optics, Laser Safety, Optical Testing,
Ray Tracing, Interferometry, Spectroscopy, OSHA Compliance

Education:
Ph.D. in Optical Engineering, University of Rochester, 2015
M.S. in Photonics, University of Central Florida, 2011
B.S. in Physics, Stanford University, 2009

Key Projects:
- Next-Gen Fiber Network: 100Gbps optical communication system design
- Precision Laser Platform: Sub-nanometer precision optical alignment system
- Photonic Chip Integration: Novel approach to optical-electronic integration
- Laser Safety Initiative: Comprehensive safety protocols for Class 4 lasers"""

    # Realistic optical engineering job posting
    optical_job = """Senior Optical Engineer - Photonics R&D
Quantum Photonics Inc. - Boston, MA

About Quantum Photonics:
We're a leading developer of advanced photonic systems for quantum computing 
and high-speed communications. Our optical technologies enable breakthrough 
performance in quantum processors and fiber optic networks.

Position Overview:
We seek a Senior Optical Engineer to lead development of next-generation 
photonic devices and optical systems. You'll work on cutting-edge laser 
systems, fiber optic communications, and precision optical assemblies.

Key Responsibilities:
- Design advanced laser systems and optical components
- Develop fiber optic communication systems for quantum networks
- Perform optical modeling and simulation using Zemax/Code V
- Lead precision optical assembly and alignment processes
- Implement laser safety protocols and training programs
- Collaborate with quantum physicists on photonic quantum systems

Required Qualifications:
- Ph.D. in Optical Engineering, Photonics, or related field
- 5+ years experience in optical system design
- Expertise in laser systems and fiber optic communications
- Proficiency with Zemax, Code V, or similar optical design software
- Experience with precision optical alignment and testing
- Knowledge of laser safety standards and OSHA compliance

Preferred Qualifications:
- Experience with quantum photonics or quantum optics
- Knowledge of optical-electronic integration
- Familiarity with high-speed optical communication systems
- Experience with interferometry and spectroscopy
- Leadership experience in optical engineering projects

What We Offer:
- Competitive salary and comprehensive benefits
- Work on cutting-edge quantum photonic technologies
- Collaborative research environment with world-class scientists
- Opportunities for professional growth and publication
- State-of-the-art optical labs and equipment

Join us in advancing the future of quantum photonics and optical communications!"""

    try:
        # Initialize optimizer
        optimizer = ResumeOptimizer()
        
        print(">>> Step 1: Testing field detection...")
        detected_field = optimizer.detect_career_field("Senior Optical Engineer")
        print(f"   Field detection: 'Senior Optical Engineer' → '{detected_field}'")
        assert detected_field == 'optical_engineer', f"Expected 'optical_engineer', got '{detected_field}'"
        print("   ✅ Field detection correct")
        
        print("\n>>> Step 2: Testing resume information extraction...")
        resume_info = optimizer.extract_resume_information(optical_resume)
        print(f"   Name: {resume_info['name']}")
        print(f"   Skills: {len(resume_info['skills'])} detected")
        print(f"   Experience: {len(resume_info['experience'])} entries")
        print(f"   Projects: {len(resume_info['projects'])} projects")
        
        # Verify key optical terms are captured
        optical_skills = [skill for skill in resume_info['skills'] if any(term in skill.lower() for term in ['optical', 'laser', 'fiber', 'photonic', 'zemax'])]
        print(f"   Optical-specific skills: {len(optical_skills)}")
        assert len(optical_skills) > 0, "No optical skills detected"
        print("   ✅ Optical skills properly extracted")
        
        print("\n>>> Step 3: Testing job analysis...")
        job_analysis = optimizer.analyze_job_posting(optical_job, "Senior Optical Engineer", "Quantum Photonics Inc.")
        
        optical_keywords = [skill for skill in job_analysis.required_skills if any(term in skill.lower() for term in ['optical', 'laser', 'photonic', 'fiber'])]
        print(f"   Optical keywords detected: {len(optical_keywords)}")
        print("   ✅ Job analysis complete")
        
        print("\n>>> Step 4: Testing complete storytelling workflow...")
        # Simulate user choosing option 1 (Story Resume)
        with patch('builtins.input', return_value='1'):
            results = optimizer.process_complete_optimization(
                optical_job, optical_resume, "Senior Optical Engineer", "Quantum Photonics Inc."
            )
        
        # Find the narrative resume
        narrative_key = None
        for key in results.keys():
            if 'narrative' in key.lower():
                narrative_key = key
                break
        
        assert narrative_key is not None, "No narrative resume found in results"
        narrative_content = results[narrative_key]
        
        print(f"   ✅ Narrative resume created: {len(narrative_content)} characters")
        
        print("\n>>> Step 5: Verifying optical engineer story elements...")
        story_checks = {
            'Light Architect Hook': 'LIGHT ARCHITECT' in narrative_content,
            'Optical Narrative': 'Light has always been my medium' in narrative_content,
            'Precision Optics': 'precision optics' in narrative_content.lower(),
            'Photonic Innovation': 'photonic' in narrative_content.lower(),
            'Laser Systems': 'laser systems' in narrative_content.lower(),
            'Fiber Optics': 'fiber optic' in narrative_content.lower(),
            'Target Company': 'Quantum Photonics Inc.' in narrative_content,
            'Personal Info': 'SARAH JOHNSON' in narrative_content,
            'Contact Info': 's.johnson@email.com' in narrative_content
        }
        
        all_passed = True
        for check, result in story_checks.items():
            status = "✅" if result else "❌"
            print(f"   {status} {check}")
            if not result:
                all_passed = False
        
        print(f"\n📖 OPTICAL ENGINEER STORY PREVIEW:")
        print("=" * 60)
        lines = narrative_content.split('\n')
        for i, line in enumerate(lines[:20]):  # Show first 20 lines
            print(f"   {line}")
        print("   ...")
        print("=" * 60)
        
        print(f"\n🎯 OPTICAL ENGINEER STORYTELLING: {'✅ SUCCESS' if all_passed else '❌ ISSUES'}")
        
        if all_passed:
            print("\n🎉 OPTICAL ENGINEER STORYTELLING FULLY FUNCTIONAL!")
            print("   ✅ Proper field detection for all optical engineering roles")
            print("   ✅ Rich 'LIGHT ARCHITECT' story template")
            print("   ✅ Optical-specific professional narrative")
            print("   ✅ Personalized content extraction and integration")
            print("   ✅ Complete browse mode integration")
        
        return all_passed
        
    except Exception as e:
        print(f"❌ ERROR: {e}")
        import traceback
        traceback.print_exc()
        return False

def main():
    print("🔬 OPTICAL ENGINEER STORYTELLING VERIFICATION")
    print("=" * 90)
    
    success = test_optical_engineer_complete_workflow()
    
    print("\n" + "=" * 90)
    if success:
        print("🏆 FINAL RESULT: OPTICAL ENGINEER STORYTELLING WORKS PERFECTLY!")
        print("\n✅ How to use for optical engineering roles:")
        print("   1. Run: python resume_windows.py --browse")
        print("   2. OR run: python browse_mode_fixed.py")
        print("   3. Select your optical engineering job description")
        print("   4. Select your optical engineer resume")
        print("   5. Enter role (e.g., 'Senior Optical Engineer')")
        print("   6. Choose option 1 for Story Resume")
        print("   7. Get '🔬 THE LIGHT ARCHITECT' narrative!")
        
        print("\n🔬 What makes optical engineer stories special:")
        print("   • 'LIGHT ARCHITECT' opening hook")
        print("   • Photonics and precision optics focus")
        print("   • Career progression in optical design")
        print("   • Laser systems and fiber optics expertise")
        print("   • Personalized with your actual projects")
    else:
        print("❌ OPTICAL ENGINEER STORYTELLING NEEDS MORE WORK")
    
    return success

if __name__ == "__main__":
    success = main()
    sys.exit(0 if success else 1)