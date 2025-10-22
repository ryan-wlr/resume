@echo off
echo =====================================
echo    AI RESUME OPTIMIZER - EASY MODE
echo =====================================
echo.
echo Available job types:
echo 1. Plumber
echo 2. Electrician  
echo 3. Custom (you'll enter file names)
echo.
set /p choice="Choose option (1, 2, or 3): "

if "%choice%"=="1" (
    echo.
    echo Running plumber resume optimizer...
    python resume_windows.py plumber_job_description.txt --resume ryan_plumber_resume.txt --role "Plumber" --company "Local Plumbing Services"
    goto end
)

if "%choice%"=="2" (
    echo.
    echo Running electrician resume optimizer...
    python resume_windows.py electrician_job_description.txt --resume ryan_electrician_resume.txt --role "Industrial Electrician" --company "M.E.P. Services"
    goto end
)

if "%choice%"=="3" (
    echo.
    echo Opening browse mode...
    python resume_windows.py --browse
    goto end
)

echo Invalid choice. Please run again and choose 1, 2, or 3.

:end
echo.
echo Press any key to exit...
pause >nul