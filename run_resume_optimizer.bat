@echo off
echo ================================================
echo    RESUME OPTIMIZER - WINDOWS LAUNCHER
echo ================================================
echo.
echo Choose your preferred method:
echo.
echo 1. Demo Mode (recommended for testing)
echo 2. No File Dialogs (if dialogs cause issues) 
echo 3. Command Line Mode
echo 4. Sample Files Mode
echo.

set /p choice="Enter choice (1-4): "

if "%choice%"=="1" (
    echo.
    echo Running demo mode...
    echo 3 | python resume_windows.py
    goto end
)

if "%choice%"=="2" (
    echo.
    echo Running without file dialogs...
    python resume_no_dialogs.py
    goto end
)

if "%choice%"=="3" (
    echo.
    echo Command Line Mode:
    echo Usage: python resume_windows.py "job description" --resume "resume text"
    echo.
    pause
    goto end
)

if "%choice%"=="4" (
    echo.
    echo Creating sample files and running...
    python create_sample_files.py
    python resume_windows.py sample_job_description.txt --resume sample_resume.txt
    goto end
)

echo Invalid choice. Please run the script again.

:end
echo.
echo Press any key to exit...
pause > nul