# Blog-Website
Introduction
This Django Blog project provides a simple and customizable platform for creating and managing blog posts. Users can create, edit, and delete blog posts, and the application includes user authentication for a secure experience.

## Features
- View a list of blog posts
- View individual blog posts in detail
- Create new blog posts (staff members only)
- Update existing blog posts (staff members only)
- Delete blog posts (staff members only)
- User authentication and login functionality

## Prerequisites
Before running this project, ensure you have the following installed:

- Python (version 3.x)
- Django (version 3.x)

## Installation
1. Clone the repository:
   ```bash
   git clone https://github.com/asif-7z/Blog-Website/
2. Change into the project directory:
   ```bash
   cd Blog-Website/src/
3. Install the required dependencies:
   ```bash
   pip install django,pillow
4. Apply migrations to set up the database:
   ```
   python manage.py migrate
5. Run the development server:
   ```
   python manage.py runserver

## Usage
1. Run the development server:
   ```
   python manage.py runserver
2. Open your web browser and go to http://localhost:8000/ to access the blog application.

## Views and Functionality
### 1. View Blog Post List
- URL: /blog2/
- Displays a list of all published blog posts.
### 2. View Blog Post Detail
- URL: /blog2/<slug>/
- Displays the details of a specific blog post identified by its slug.
### 3. Create Blog Post (Staff Members Only)
- URL: /blog2/create/
- Allows staff members to create new blog posts.
- Requires user authentication.
### 4. Update Blog Post (Staff Members Only)
- URL: /blog2/<slug>/update/
- Allows staff members to update existing blog posts.
- Requires user authentication.
### 5. Delete Blog Post (Staff Members Only)
- URL: /blog2/<slug>/delete/
- Allows staff members to delete existing blog posts.
- Requires user authentication.
