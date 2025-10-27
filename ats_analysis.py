#!/usr/bin/env python3
"""
ATS Analysis Tool - Evaluate resume formats for ATS compatibility
Checks both storytelling and standard formats
"""

import sys
import os
import re
from collections import Counter

def analyze_ats_compatibility(content, format_name):
    """Analyze resume content for ATS compatibility"""
    
    print(f"\n🤖 ATS ANALYSIS: {format_name.upper()}")
    print("=" * 60)
    
    lines = content.split('\n')
    issues = []
    strengths = []
    score = 100
    
    # 1. Check for standard sections
    print("📋 SECTION ANALYSIS:")
    required_sections = {
        'contact': ['contact', 'phone', 'email', '@'],
        'experience': ['experience', 'work', 'employment', 'professional'],
        'education': ['education', 'degree', 'university', 'college'],
        'skills': ['skills', 'technical', 'competencies', 'technologies']
    }
    
    sections_found = {}
    for section, keywords in required_sections.items():
        found = any(any(keyword in line.lower() for keyword in keywords) for line in lines)
        sections_found[section] = found
        status = "✅" if found else "❌"
        print(f"   {status} {section.title()}: {'Found' if found else 'Missing'}")
        if not found:
            issues.append(f"Missing {section} section")
            score -= 15
        else:
            strengths.append(f"Has {section} section")
    
    # 2. Check formatting issues
    print(f"\n🎨 FORMATTING ANALYSIS:")
    
    # Check for problematic characters/formatting
    problematic_chars = ['🔥', '🔬', '💻', '🌟', '📞', '✉️', '🔗', '💻']
    emoji_count = sum(line.count(char) for line in lines for char in problematic_chars)
    if emoji_count > 0:
        print(f"   ❌ Emojis/Special characters: {emoji_count} found")
        issues.append(f"Contains {emoji_count} emojis (ATS may not parse)")
        score -= min(emoji_count * 2, 20)
    else:
        print(f"   ✅ No problematic emojis")
        strengths.append("Clean text formatting")
    
    # Check for graphics/images (text-based check)
    graphics_indicators = ['image', 'graphic', 'chart', 'logo']
    graphics_found = any(any(indicator in line.lower() for indicator in graphics_indicators) for line in lines)
    if graphics_found:
        print(f"   ❌ May contain graphics/images")
        issues.append("Contains graphics/images")
        score -= 10
    else:
        print(f"   ✅ Text-only format")
        strengths.append("Text-only format")
    
    # 3. Check keyword density
    print(f"\n🔤 KEYWORD ANALYSIS:")
    
    # Extract common technical/professional keywords
    text = content.lower()
    common_keywords = [
        'experience', 'skills', 'project', 'develop', 'manage', 'lead',
        'engineer', 'technical', 'analysis', 'design', 'system'
    ]
    
    keyword_count = sum(text.count(keyword) for keyword in common_keywords)
    keyword_density = keyword_count / len(text.split()) * 100 if text.split() else 0
    
    print(f"   📊 Keyword density: {keyword_density:.2f}%")
    if keyword_density >= 3:
        print(f"   ✅ Good keyword density")
        strengths.append(f"Good keyword density ({keyword_density:.1f}%)")
    elif keyword_density >= 1.5:
        print(f"   ⚠️  Moderate keyword density")
        score -= 5
    else:
        print(f"   ❌ Low keyword density")
        issues.append("Low keyword density")
        score -= 15
    
    # 4. Check structure and readability
    print(f"\n📖 STRUCTURE ANALYSIS:")
    
    # Check for bullet points
    bullet_lines = [line for line in lines if line.strip().startswith('•') or line.strip().startswith('-')]
    if bullet_lines:
        print(f"   ✅ Uses bullet points: {len(bullet_lines)} found")
        strengths.append(f"Uses {len(bullet_lines)} bullet points")
    else:
        print(f"   ❌ No bullet points found")
        issues.append("No bullet points for readability")
        score -= 10
    
    # Check for quantified achievements
    numbers = re.findall(r'\d+(?:%|\+|years?|months?)', content.lower())
    if numbers:
        print(f"   ✅ Quantified achievements: {len(numbers)} metrics found")
        strengths.append(f"Contains {len(numbers)} quantified metrics")
    else:
        print(f"   ⚠️  Limited quantified achievements")
        score -= 5
    
    # 5. Check for problematic narrative elements
    print(f"\n📝 NARRATIVE ANALYSIS:")
    
    narrative_phrases = [
        'my journey', 'my story', 'career story', 'chapter', 'narrative',
        'always been', 'passion for', 'fascination with'
    ]
    
    narrative_count = sum(text.count(phrase) for phrase in narrative_phrases)
    if narrative_count > 5:
        print(f"   ⚠️  Heavy narrative style: {narrative_count} narrative phrases")
        print(f"   💡 May be less ATS-friendly but more human-engaging")
        score -= 10
    elif narrative_count > 0:
        print(f"   ⚠️  Moderate narrative elements: {narrative_count} phrases")
        score -= 5
    else:
        print(f"   ✅ Professional, fact-based style")
        strengths.append("Fact-based professional style")
    
    # Calculate final score
    score = max(0, min(100, score))
    
    # Determine ATS compatibility level
    if score >= 85:
        compatibility = "EXCELLENT"
        color = "🟢"
    elif score >= 70:
        compatibility = "GOOD"
        color = "🟡"
    elif score >= 55:
        compatibility = "FAIR"
        color = "🟠"
    else:
        compatibility = "POOR"
        color = "🔴"
    
    print(f"\n{color} ATS COMPATIBILITY SCORE: {score}/100 ({compatibility})")
    
    print(f"\n✅ STRENGTHS ({len(strengths)}):")
    for strength in strengths[:5]:  # Show top 5
        print(f"   • {strength}")
    
    print(f"\n⚠️  POTENTIAL ISSUES ({len(issues)}):")
    for issue in issues[:5]:  # Show top 5
        print(f"   • {issue}")
    
    return score, compatibility, strengths, issues

def main():
    print("🤖 ATS COMPATIBILITY ANALYZER")
    print("Analyzing storytelling vs standard resume formats...")
    
    # Find latest output folder
    folders = [f for f in os.listdir('.') if f.startswith('browse_mode_output_')]
    if not folders:
        print("❌ No browse_mode_output folders found")
        return
    
    latest_folder = sorted(folders)[-1]
    print(f"📂 Analyzing: {latest_folder}")
    
    # Analyze storytelling resume
    narrative_path = os.path.join(latest_folder, 'narrative_story_resume.txt')
    if os.path.exists(narrative_path):
        with open(narrative_path, 'r', encoding='utf-8') as f:
            narrative_content = f.read()
        narrative_score, narrative_compat, narrative_strengths, narrative_issues = analyze_ats_compatibility(narrative_content, "Storytelling Resume")
    else:
        print("❌ Storytelling resume not found")
        narrative_score = 0
        narrative_compat = "NOT FOUND"
    
    # Analyze ATS-optimized resume
    ats_path = os.path.join(latest_folder, 'resume_ats_optimized.txt')
    if os.path.exists(ats_path):
        with open(ats_path, 'r', encoding='utf-8') as f:
            ats_content = f.read()
        ats_score, ats_compat, ats_strengths, ats_issues = analyze_ats_compatibility(ats_content, "ATS-Optimized Resume")
    else:
        print("❌ ATS-optimized resume not found")
        ats_score = 0
        ats_compat = "NOT FOUND"
    
    # Comparison summary
    print(f"\n📊 FINAL COMPARISON:")
    print(f"=" * 60)
    print(f"📖 Storytelling Resume:  {narrative_score}/100 ({narrative_compat})")
    print(f"🤖 ATS-Optimized Resume: {ats_score}/100 ({ats_compat})")
    
    print(f"\n💡 RECOMMENDATIONS:")
    if narrative_score >= 70:
        print("✅ Storytelling resume is ATS-compatible")
        print("   • Good balance of narrative engagement and ATS parsing")
        print("   • Should pass most ATS systems successfully")
    else:
        print("⚠️  Storytelling resume may have ATS challenges")
        print("   • Consider using ATS-optimized version for initial screening")
        print("   • Save storytelling version for human recruiters")
    
    if ats_score > narrative_score:
        print(f"🎯 For maximum ATS compatibility, use the ATS-optimized version")
    else:
        print(f"🎯 Storytelling version performs well for ATS systems")
    
    print(f"\n📋 USAGE STRATEGY:")
    print(f"   1. Use ATS-optimized version for online applications")
    print(f"   2. Use storytelling version for networking and direct submissions")
    print(f"   3. Both versions contain the same core information")

if __name__ == "__main__":
    main()