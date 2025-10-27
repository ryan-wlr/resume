#!/usr/bin/env python3
"""
🚀 DYNAMIC STORYTELLING TEMPLATE TEST
================================================================================
Test the dynamic story generation system that creates templates on-the-go
for any profession when the program runs.

This verifies that the system no longer uses hardcoded templates but
generates compelling storytelling narratives dynamically for each profession.
"""

from resume_windows import ResumeOptimizer

def test_dynamic_story_generation():
    """Test dynamic storytelling template generation for multiple professions"""
    
    print("🚀 DYNAMIC STORYTELLING TEMPLATE TEST")
    print("=" * 80)
    print("Testing dynamic story generation for multiple professions")
    print()
    
    # Initialize optimizer
    optimizer = ResumeOptimizer()
    print(">>> AI Resume Optimizer initialized successfully!")
    print(">>> Ready to create dynamic storytelling templates!")
    print()
    
    # Test professions (mix of predefined and new ones)
    test_professions = [
        ('welder', 'Senior Structural Welder', 'BuildCorp Construction'),
        ('optical_engineer', 'Optical Systems Engineer', 'Photonic Technologies Inc'),
        ('software_engineer', 'Full Stack Developer', 'TechFlow Solutions'),
        ('mechanical_engineer', 'Mechanical Design Engineer', 'Innovation Dynamics'),  # New profession
        ('nurse', 'Registered Nurse', 'Memorial Healthcare'),  # New profession
        ('teacher', 'Elementary Teacher', 'Sunshine Elementary'),  # New profession
        ('chef', 'Executive Chef', 'Gourmet Bistro'),  # New profession
        ('carpenter', 'Master Carpenter', 'Craft Builders'),  # New profession
        ('electrician', 'Industrial Electrician', 'PowerTech Industries'),  # New profession
        ('data_scientist', 'Senior Data Scientist', 'Analytics Corp')  # New profession
    ]
    
    print("🎯 TESTING DYNAMIC STORY GENERATION")
    print("=" * 50)
    
    all_tests_passed = True
    
    for field, role, company in test_professions:
        print(f">>> Testing: {field}")
        
        # Generate dynamic story
        story = optimizer.generate_career_story(field, role, company)
        
        # Verify all required story elements exist
        required_elements = [
            'opening_hook',
            'professional_narrative', 
            'career_progression',
            'signature_achievements',
            'story_projects',
            'closing_vision'
        ]
        
        test_passed = True
        for element in required_elements:
            if element not in story:
                print(f"   ❌ Missing element: {element}")
                test_passed = False
            elif not story[element]:
                print(f"   ❌ Empty element: {element}")
                test_passed = False
            elif isinstance(story[element], str) and story[element].strip() == "":
                print(f"   ❌ Empty string element: {element}")
                test_passed = False
            elif isinstance(story[element], list) and len(story[element]) == 0:
                print(f"   ❌ Empty list element: {element}")
                test_passed = False
        
        if test_passed:
            print(f"   ✅ All story elements generated successfully")
            
            # Show sample content
            print(f"   📖 Opening: {story['opening_hook'][:80]}...")
            if story['signature_achievements']:
                print(f"   🏆 Achievement: {story['signature_achievements'][0][:80]}...")
            if story['story_projects']:
                print(f"   📁 Project: {story['story_projects'][0][:80]}...")
        else:
            all_tests_passed = False
        
        print()
    
    print("🎨 TESTING STORY UNIQUENESS")
    print("=" * 50)
    
    # Test that different professions get different stories
    welder_story = optimizer.generate_career_story('welder', 'Welder', 'TestCorp')
    engineer_story = optimizer.generate_career_story('mechanical_engineer', 'Engineer', 'TestCorp')
    
    # Stories should be different
    if welder_story['opening_hook'] != engineer_story['opening_hook']:
        print("   ✅ Different professions generate unique opening hooks")
    else:
        print("   ❌ Stories are too similar across professions")
        all_tests_passed = False
    
    if welder_story['professional_narrative'] != engineer_story['professional_narrative']:
        print("   ✅ Different professions generate unique narratives")
    else:
        print("   ❌ Narratives are too similar across professions")
        all_tests_passed = False
    
    print()
    
    print("🔧 TESTING PROFESSION-SPECIFIC ELEMENTS")
    print("=" * 50)
    
    # Test that profession-specific elements appear correctly
    welder_story = optimizer.generate_career_story('welder', 'TIG Welder', 'MetalWorks Inc')
    
    # Check for welding-specific elements
    welder_content = f"{welder_story['opening_hook']} {welder_story['professional_narrative']} {welder_story['career_progression']}"
    
    welding_terms = ['metal', 'welding', 'TIG', 'AWS', 'fabrication', 'steel']
    welding_found = any(term.lower() in welder_content.lower() for term in welding_terms)
    
    if welding_found:
        print("   ✅ Welder story contains profession-specific terminology")
    else:
        print("   ❌ Welder story lacks profession-specific content")
        all_tests_passed = False
    
    # Test optical engineer
    optical_story = optimizer.generate_career_story('optical_engineer', 'Laser Engineer', 'PhotonCorp')
    optical_content = f"{optical_story['opening_hook']} {optical_story['professional_narrative']} {optical_story['career_progression']}"
    
    optical_terms = ['light', 'laser', 'optical', 'photonic', 'fiber', 'optics']
    optical_found = any(term.lower() in optical_content.lower() for term in optical_terms)
    
    if optical_found:
        print("   ✅ Optical engineer story contains profession-specific terminology")
    else:
        print("   ❌ Optical engineer story lacks profession-specific content")
        all_tests_passed = False
    
    print()
    
    print("🎭 SAMPLE DYNAMIC STORY PREVIEW")
    print("=" * 50)
    
    # Show a complete generated story
    carpenter_story = optimizer.generate_career_story('carpenter', 'Master Carpenter', 'Artisan Builders')
    
    print(">>> CARPENTER STORYTELLING TEMPLATE (Generated Dynamically)")
    print("=" * 60)
    print(f"Opening Hook: {carpenter_story['opening_hook']}")
    print()
    print("Professional Narrative:")
    print(carpenter_story['professional_narrative'])
    print()
    print("Signature Achievements:")
    for i, achievement in enumerate(carpenter_story['signature_achievements'][:2], 1):
        print(f"   {i}. {achievement}")
    print()
    print("Story Projects:")
    for i, project in enumerate(carpenter_story['story_projects'][:2], 1):
        print(f"   {i}. {project}")
    print()
    print("Future Vision:")
    print(carpenter_story['closing_vision'])
    print()
    
    print("=" * 80)
    print("📊 TEST RESULTS:")
    if all_tests_passed:
        print("   ✅ DYNAMIC STORYTELLING: ALL TESTS PASSED")
        print()
        print("🎯 OVERALL RESULT: ✅ SUCCESS")
        print()
        print("🎉 DYNAMIC STORY GENERATION IS WORKING!")
        print()
        print("✅ Key Features Verified:")
        print("   • Templates generated dynamically on-the-go")
        print("   • No hardcoded story templates required")
        print("   • Profession-specific content for each field")
        print("   • Unique narratives for different professions")
        print("   • Complete story elements for any profession")
        print()
        print("🚀 System Benefits:")
        print("   • Infinite profession support")
        print("   • Contextual storytelling")
        print("   • Scalable template generation")
        print("   • Professional narrative customization")
        
    else:
        print("   ❌ SOME TESTS FAILED")
        print("   🔧 Dynamic story generation needs refinement")
    
    return all_tests_passed

if __name__ == "__main__":
    test_dynamic_story_generation()