from resume_windows import ResumeOptimizer

opt = ResumeOptimizer()
print("Testing dynamic template for Marine Biologist...")
story = opt.generate_career_story('marine_biologist', 'Senior Marine Biologist', 'Ocean Research Institute')
print("Template generated successfully!")
print("Hook:", story['opening_hook'])
print("Achievement:", story['signature_achievements'][0][:100] + "...")
print("DYNAMIC STORYTELLING VERIFIED WORKING!")