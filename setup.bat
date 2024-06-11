@echo off

REM Create a virtual environment
echo Creating virtual environment...
python -m venv virenv

REM Activate the virtual environment
echo Activating virtual environment...
call virenv\Scripts\activate

REM Install Django
echo Installing Django...
pip install django

REM Start a new Django project called 'cacheville'
echo Starting Django project 'cacheville'...
django-admin startproject cacheville

REM Navigate into the project directory
cd cacheville

REM Create the core part called 'engine'
echo Creating core part 'engine'...
django-admin startapp engine

REM Start apps called 'users', 'news', 'weather'
echo Creating app 'users'...
django-admin startapp users

echo Creating app 'news'...
django-admin startapp news

echo Creating app 'weather'...
django-admin startapp weather

echo Django project setup complete!
