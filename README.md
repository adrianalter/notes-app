# Initial Setup
django-admin startproject backend
cd backend
python manage.py startapp api

# Create user
touch api/serializers.py
in views.py


# Create frontend
Go to root folder
npm create vite@latest frontend -- --template react
cd frontend
npm install axios react-react-dom jwt-decode

Go to frontend/src and create folders "components, pages, styles"
Also create api.js and constants.js