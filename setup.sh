#!/bin/bash

# Create a virtual environment
echo "Creating virtual environment..."
python3 -m venv venv

# Activate the virtual environment
echo "Activating virtual environment..."
source venv/bin/activate

# Install Django
echo "Installing Django..."
pip install django

# Start a new Django project called 'cacheville'
echo "Starting Django project 'cacheville'..."
django-admin startproject cacheville

# Navigate into the project directory
cd cacheville

# Create the core part called 'engine'
echo "Creating core part 'engine'..."
django-admin startapp engine

# Start apps called 'users', 'news', 'weather'
echo "Creating app 'users'..."
django-admin startapp users

echo "Creating app 'news'..."
django-admin startapp news

echo "Creating app 'weather'..."
django-admin startapp weather

echo "Django project setup complete!"
