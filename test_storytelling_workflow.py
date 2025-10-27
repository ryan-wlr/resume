#!/usr/bin/env python3
"""
Test the storytelling functionality with browse mode workflow
"""

from resume_windows import ResumeOptimizer

def test_storytelling_workflow():
    """Test the complete storytelling workflow"""
    
    print("🧪 TESTING STORYTELLING WORKFLOW")
    print("=" * 50)
    
    # Read test files
    with open('test_welder_job.txt', 'r') as f:
        job_content = f.read()
    
    with open('test_welder_resume.txt', 'r') as f:
        resume_content = f.read()
    
    print(f"📄 Loaded job description: {len(job_content)} characters")
    print(f"📄 Loaded resume: {len(resume_content)} characters")
    print()
    
    # Initialize optimizer
    optimizer = ResumeOptimizer()
    
    # Test the storytelling functionality
    print("🎭 TESTING STORYTELLING CREATION")
    print("-" * 30)
    
    # Test 1: Check field detection
    detected_field = optimizer.detect_career_field("welder")
    print(f"Field detection: '{detected_field}'")
    
    # Test 2: Generate story template
    story = optimizer.generate_career_story(detected_field, "Senior Welder", "MetalWorks Construction")
    print(f"Story template generated: {bool(story)}")
    print(f"Opening hook: {story['opening_hook']}")
    print()
    
    # Test 3: Create narrative resume
    print("🎯 CREATING NARRATIVE RESUME")
    print("-" * 30)
    
    # Create job analysis
    job_analysis = optimizer.analyze_job_posting(job_content, "Senior Welder", "MetalWorks Construction")
    
    # Create narrative resume
    narrative = optimizer.create_narrative_resume(resume_content, job_analysis, "Senior Welder", "MetalWorks Construction")
    
    print(f"Narrative resume created: {len(narrative)} characters")
    print()
    print("📖 NARRATIVE PREVIEW:")
    print("=" * 50)
    print(narrative[:500] + "...")
    print("=" * 50)
    
    # Test 4: Check if story elements are included
    story_checks = {
        'Metal Master': 'METAL MASTER' in narrative,
        'Welding narrative': 'welding' in narrative.lower(),
        'Company name': 'MetalWorks Construction' in narrative,
        'AWS certification': 'AWS' in narrative,
        'Opening hook': story['opening_hook'] in narrative
    }
    
    print("✅ STORY ELEMENT VERIFICATION:")
    for element, found in story_checks.items():
        status = "✅" if found else "❌"
        print(f"   {status} {element}: {found}")
    
    print()
    all_passed = all(story_checks.values())
    if all_passed:
        print("🎉 STORYTELLING TEST: ✅ SUCCESS!")
    else:
        print("❌ STORYTELLING TEST: SOME ELEMENTS MISSING")
    
    return all_passed

if __name__ == "__main__":
    test_storytelling_workflow()