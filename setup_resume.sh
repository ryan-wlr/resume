#!/bin/bash
# Resume Optimizer Setup Script

echo "🚀 Setting up AI Resume Optimizer..."

# Create virtual environment (optional but recommended)
python -m venv resume_env
source resume_env/bin/activate 2>/dev/null || resume_env\Scripts\activate

# Install requirements
echo "📦 Installing required packages..."
pip install python-docx>=0.8.11
pip install openai>=0.28.0
pip install requests>=2.28.0

echo "✅ Setup complete!"
echo ""
echo "🎯 Usage Examples:"
echo "1. Basic usage with job description:"
echo "   python resume.py job_description.docx"
echo ""
echo "2. With existing resume and target role:"
echo "   python resume.py job_description.docx --resume my_resume.txt --role 'Senior Developer'"
echo ""
echo "3. Full customization:"
echo "   python resume.py job_description.docx --resume current_resume.txt --role 'Data Scientist' --company 'Google' --output my_output"
echo ""
echo "💡 Set your OpenAI API key:"
echo "   export OPENAI_API_KEY='your-api-key-here'"
echo "   OR use --api-key flag"
echo ""
echo "🔗 Get OpenAI API key at: https://platform.openai.com/api-keys"