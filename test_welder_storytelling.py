#!/usr/bin/env python3
"""
Test Welder Storytelling Template
=================================

Test that welder roles get proper storytelling treatment when entered in browse mode.
"""

import sys
import os
import tempfile
from unittest.mock import patch

sys.path.append(os.path.dirname(os.path.abspath(__file__)))

from resume_windows import ResumeOptimizer

def test_welder_field_detection():
    print("🔥 TESTING WELDER FIELD DETECTION")
    print("=" * 50)
    
    optimizer = ResumeOptimizer()
    
    # Test various welder terms
    welder_roles = [
        "Welder",
        "Senior Welder", 
        "Certified Welder",
        "TIG Welder",
        "MIG Welder",
        "Arc Welder",
        "Stick Welder",
        "Structural Welder",
        "Pipe Welder",
        "Fabricator",
        "Welding Inspector",
        "welding technician",
        "fabrication specialist"
    ]
    
    print(">>> Testing field detection for welding roles:")
    all_detected = True
    for role in welder_roles:
        detected_field = optimizer.detect_career_field(role.lower())
        status = "✅" if detected_field == 'welder' else "❌"
        print(f"   {status} '{role}' → '{detected_field}'")
        if detected_field != 'welder':
            all_detected = False
    
    return all_detected

def test_welder_story_template():
    print("\n🔥 TESTING WELDER STORY TEMPLATE")
    print("=" * 50)
    
    optimizer = ResumeOptimizer()
    
    # Test story generation
    story = optimizer.generate_career_story('welder', 'Senior Welder', 'Industrial Manufacturing Co.')
    
    print(">>> Checking story template elements:")
    checks = {
        'Opening Hook': 'METAL MASTER' in story['opening_hook'],
        'Professional Narrative': 'art meets engineering' in story['professional_narrative'],
        'Career Progression': 'Chapter 1: THE FOUNDATION' in story['career_progression'],
        'Achievements': len(story['signature_achievements']) >= 4,
        'Projects': len(story['story_projects']) >= 4,
        'Closing Vision': 'Industrial Manufacturing Co.' in story['closing_vision']
    }
    
    all_passed = True
    for check, result in checks.items():
        status = "✅" if result else "❌"
        print(f"   {status} {check}")
        if not result:
            all_passed = False
    
    if all_passed:
        print("\n📖 WELDER STORY PREVIEW:")
        print(f"   Opening: {story['opening_hook']}")
        print(f"   First Achievement: {story['signature_achievements'][0]}")
        print(f"   First Project: {story['story_projects'][0]}")
    
    return all_passed

def test_welder_complete_workflow():
    print("\n🔥 TESTING COMPLETE WELDER WORKFLOW")
    print("=" * 50)
    
    # Create realistic welder resume
    welder_resume = """Mike Rodriguez
Certified Welder

Contact Information:
Email: m.rodriguez@email.com
Phone: (555) 234-5678
Address: Houston, TX

Professional Experience:
- Performed structural welding on high-rise construction projects
- Completed AWS D1.1 certified welding for critical steel connections
- Operated MIG, TIG, and stick welding equipment with 99% pass rate
- Maintained strict safety protocols preventing workplace accidents
- Trained apprentice welders in proper welding techniques

Certifications:
AWS D1.1 Structural Welding Certification
OSHA 10-Hour Construction Safety
6G Pipe Welding Certification
TIG Welding Aluminum Specialist

Technical Skills:
MIG Welding, TIG Welding, Stick Welding (SMAW), Flux-Core Welding,
Structural Steel Welding, Pipe Welding, Aluminum Welding,
Blueprint Reading, Welding Inspection, Safety Protocols,
Plasma Cutting, Oxy-Acetylene Cutting

Education:
Welding Technology Certificate, Houston Community College, 2018
OSHA Safety Training Certification

Key Projects:
- Downtown Skyscraper: Structural steel welding for 40-story building
- Petrochemical Pipeline: High-pressure pipe welding meeting ASME B31.3
- Offshore Platform Repair: Emergency welding repairs in marine environment
- Custom Fabrication: Precision welding for specialized industrial equipment"""

    # Create realistic welding job posting
    welding_job = """Senior Structural Welder - Construction
BuildRight Construction - Dallas, TX

About BuildRight Construction:
We're a leading construction company specializing in commercial and industrial 
projects. Our reputation is built on quality craftsmanship and safety excellence.

Position Overview:
We seek an experienced Senior Structural Welder to join our steel construction 
team. You'll perform critical welding operations on high-profile building projects.

Key Responsibilities:
- Perform structural welding on steel frame construction
- Execute welding operations meeting AWS D1.1 specifications
- Read and interpret structural blueprints and welding symbols
- Maintain welding equipment and ensure proper safety protocols
- Mentor junior welders and apprentices
- Participate in quality control inspections

Required Qualifications:
- 5+ years experience in structural steel welding
- AWS D1.1 Structural Welding Certification required
- Proficiency in MIG, TIG, and stick welding processes
- Ability to weld in all positions (1G, 2G, 3G, 4G)
- Strong knowledge of welding safety protocols
- Valid OSHA 10-Hour certification

Preferred Qualifications:
- Experience with high-rise construction projects
- 6G pipe welding certification
- Welding inspection experience
- Leadership or training experience
- Blueprint reading proficiency

What We Offer:
- Competitive hourly wages ($28-35/hour based on experience)
- Comprehensive health benefits and retirement plan
- Opportunities for overtime and project bonuses
- Ongoing training and certification support
- Safe, professional work environment

Join our team and help build the structures that shape our city's skyline!"""

    try:
        optimizer = ResumeOptimizer()
        
        print(">>> Testing field detection with job content...")
        detected_field = optimizer.detect_career_field(welding_job.lower())
        print(f"   Job content detection: '{detected_field}'")
        
        print("\n>>> Testing complete storytelling workflow...")
        # Simulate user choosing option 1 (Story Resume)
        with patch('builtins.input', return_value='1'):
            results = optimizer.process_complete_optimization(
                welding_job, welder_resume, "Senior Structural Welder", "BuildRight Construction"
            )
        
        # Find the narrative resume
        narrative_key = None
        for key in results.keys():
            if 'narrative' in key.lower():
                narrative_key = key
                break
        
        if not narrative_key:
            print("   ❌ No narrative resume found")
            return False
        
        narrative_content = results[narrative_key]
        print(f"   ✅ Narrative resume created: {len(narrative_content)} characters")
        
        # Verify welder story elements
        story_checks = {
            'Metal Master Hook': 'METAL MASTER' in narrative_content,
            'Welding Narrative': 'art meets engineering' in narrative_content,
            'Structural Focus': 'structural' in narrative_content.lower(),
            'AWS Certification': 'AWS' in narrative_content,
            'Safety Emphasis': 'safety' in narrative_content.lower(),
            'Target Company': 'BuildRight Construction' in narrative_content,
            'Personal Info': 'MIKE RODRIGUEZ' in narrative_content,
            'Contact Info': 'm.rodriguez@email.com' in narrative_content,
            'Technical Skills': any(term in narrative_content for term in ['MIG', 'TIG', 'welding']),
            'Experience': 'structural welding' in narrative_content.lower()
        }
        
        print("\n>>> Verifying welder story elements:")
        all_passed = True
        for check, result in story_checks.items():
            status = "✅" if result else "❌"
            print(f"   {status} {check}")
            if not result:
                all_passed = False
        
        if all_passed:
            print(f"\n📖 WELDER STORY PREVIEW:")
            print("=" * 60)
            lines = narrative_content.split('\n')
            for i, line in enumerate(lines[:15]):  # Show first 15 lines
                print(f"   {line}")
            print("   ...")
            print("=" * 60)
        
        return all_passed
        
    except Exception as e:
        print(f"❌ ERROR: {e}")
        import traceback
        traceback.print_exc()
        return False

def main():
    print("🔥 WELDER STORYTELLING TEMPLATE TEST")
    print("=" * 80)
    print("Testing welder storytelling for browse_mode_fixed.py")
    print()
    
    # Run all tests
    detection_passed = test_welder_field_detection()
    template_passed = test_welder_story_template()
    workflow_passed = test_welder_complete_workflow()
    
    overall_passed = detection_passed and template_passed and workflow_passed
    
    print("\n" + "=" * 80)
    print("📊 TEST RESULTS:")
    print(f"   Field Detection: {'✅ PASSED' if detection_passed else '❌ FAILED'}")
    print(f"   Story Template: {'✅ PASSED' if template_passed else '❌ FAILED'}")
    print(f"   Complete Workflow: {'✅ PASSED' if workflow_passed else '❌ FAILED'}")
    
    print(f"\n🎯 OVERALL RESULT: {'✅ SUCCESS' if overall_passed else '❌ ISSUES'}")
    
    if overall_passed:
        print("\n🎉 WELDER STORYTELLING IS READY!")
        print("\n✅ How to use for welding roles:")
        print("   1. Run: python browse_mode_fixed.py")
        print("   2. Select welding job description file")
        print("   3. Select welder resume file")
        print("   4. Enter role: 'Welder', 'Senior Welder', 'TIG Welder', etc.")
        print("   5. Choose option 1 for Story Resume")
        print("   6. Get '🔥 THE METAL MASTER' narrative!")
        
        print("\n🔥 What makes welder stories special:")
        print("   • 'METAL MASTER' opening hook")
        print("   • Art meets engineering narrative")
        print("   • AWS certification and safety focus")
        print("   • Structural and precision welding expertise")
        print("   • Career progression from foundation to mastery")
    else:
        print("\n⚠️ Some issues need to be resolved")
    
    return overall_passed

if __name__ == "__main__":
    success = main()
    sys.exit(0 if success else 1)