# Python-Django-7

Project Title: Car Inventory Management System

Project Overview:

This project is a web-based Car Inventory Management System developed using Django and Python. The application allows users to manage car data, including the car's name, color, and fuel type. The data is displayed in a tabular format on the screen, and users can add new entries using a web form without directly interacting with the database.

Features:

Data Display: The car inventory data, including the car name, color, and fuel type, is dynamically fetched from the database and displayed in a table.
Data Entry Form: Users can add new car records through an intuitive web form, ensuring ease of use and eliminating the need to manually input data into the database.
User Authentication: The application includes a user authentication system, ensuring that only authorized users can add or view car data.
Custom URL: After running the server, users can access the application via a custom URL that ends with "/c", where they can view the car inventory table and interact with the system.

Technical Details:

Backend: Django (Python)

Database: Integrated with Django's ORM, using SQLite (or another database as configured).
URL: The main interface for the car inventory is accessible at the "/c" URL endpoint after starting the server.

How It Works:

Authentication: Users must log in to access the car inventory.
Viewing Data: Once authenticated, users are redirected to the "/c" page, where they can see a table listing all the cars in the database.
Adding Data: Users can add new car entries via the web form, which updates the database and reflects the changes immediately in the table view the specifed URL:"a/"
