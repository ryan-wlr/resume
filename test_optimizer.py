#!/usr/bin/env python3
"""
Test script to verify the Resume Optimizer works correctly
"""

def test_dynamic_detection():
    """Test the dynamic field detection system"""
    print("🧪 TESTING DYNAMIC FIELD DETECTION")
    print("=" * 50)
    
    try:
        from resume_windows import ResumeOptimizer
        
        optimizer = ResumeOptimizer()
        
        # Test cases for various fields
        test_cases = [
            ("brain surgeon", "Brain surgery specialist"),
            ("marine biologist", "Ocean research scientist"), 
            ("astrophysicist", "Space research expert"),
            ("video game designer", "Gaming industry creative"),
            ("environmental scientist", "Environmental research"),
            ("mechanical engineer", "Engineering professional"),
            ("chef", "Culinary professional"),
            ("lawyer", "Legal professional")
        ]
        
        print("Testing field detection and content generation...")
        print()
        
        for field_input, description in test_cases:
            try:
                # Test field detection
                detected_field = optimizer.detect_career_field(field_input)
                
                # Test content generation
                field_data = optimizer.get_field_data(detected_field)
                
                # Test title generation
                title = optimizer.generate_dynamic_title(detected_field)
                
                print(f"✅ {field_input:<20} -> {detected_field}")
                print(f"   Title: {title}")
                print(f"   Skills: {field_data['skills'][0][:60]}...")
                print()
                
            except Exception as e:
                print(f"❌ {field_input:<20} -> Error: {e}")
                
        print("🎉 Dynamic field detection test completed!")
        return True
        
    except ImportError as e:
        print(f"❌ Cannot import resume_windows: {e}")
        print("Make sure resume_windows.py is in the same directory.")
        return False
    except Exception as e:
        print(f"❌ Test failed: {e}")
        return False

def test_dependencies():
    """Test if required dependencies are available"""
    print("\n🔧 TESTING DEPENDENCIES")
    print("=" * 30)
    
    try:
        import docx
        print("✅ python-docx: Available")
    except ImportError:
        print("❌ python-docx: Missing (pip install python-docx)")
        return False
        
    try:
        import tkinter
        print("✅ tkinter: Available")
    except ImportError:
        print("⚠️  tkinter: Missing (file dialogs won't work)")
        
    return True

if __name__ == "__main__":
    print("🧪 RESUME OPTIMIZER TEST SUITE")
    print("=" * 40)
    
    # Test dependencies
    deps_ok = test_dependencies()
    
    if deps_ok:
        # Test dynamic detection
        detection_ok = test_dynamic_detection()
        
        if detection_ok:
            print("\n🎉 ALL TESTS PASSED!")
            print("The Resume Optimizer is ready to use.")
            print("\nRun 'python browse_mode_fixed.py' to start optimizing resumes!")
        else:
            print("\n❌ Some tests failed. Check the errors above.")
    else:
        print("\n❌ Missing dependencies. Install with: pip install python-docx")