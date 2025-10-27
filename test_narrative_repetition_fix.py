#!/usr/bin/env python3
"""Test narrative repetition fix for data scientist"""

import sys
import os
import tempfile

# Add the current directory to path
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))

from resume_windows import ResumeOptimizer

def test_narrative_fix():
    """Test that narrative doesn't repeat 'journey' text"""
    print("🔍 Testing Narrative Repetition Fix...")
    
    # Initialize optimizer
    optimizer = ResumeOptimizer()
    
    # Test data scientist narrative generation
    story_elements = optimizer.generate_dynamic_story_template('data_scientist', 'Data Scientist', 'Tech Company')
    
    # Check the professional narrative
    narrative = story_elements['professional_narrative']
    print(f"\n📖 Professional Narrative:")
    print(narrative)
    
    # Count occurrences of "journey"
    journey_count = narrative.lower().count('journey')
    print(f"\n📊 Analysis:")
    print(f"   'Journey' mentions: {journey_count}")
    
    if journey_count <= 1:
        print("   ✅ No repetition detected!")
    else:
        print("   ❌ Still has repetition")
        
    # Check for "my journey" specifically
    my_journey_count = narrative.lower().count('my journey')
    print(f"   'My journey' mentions: {my_journey_count}")
    
    if my_journey_count <= 1:
        print("   ✅ 'My journey' not repeated!")
    else:
        print("   ❌ 'My journey' still repeated")

if __name__ == "__main__":
    test_narrative_fix()