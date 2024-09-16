# InvoiceApp - Django Project

## Description
InvoiceApp is a web-based application for managing invoices, clients, products, and product categories. The project is built using Django, and it includes TailwindCSS for styling through the `django-tailwind` package.

## Requirements

To install and run the project, make sure you have the following prerequisites:

- Python 3.8+
- Git
- Node.js and npm (for TailwindCSS)
- Virtualenv (recommended for virtual environments)

## Installation

1. **Clone the repository:**
   ```bash
   https://github.com/zoubinnaba/invoices
   cd invoices

2. **Create and activate a virtual environment:**
   ```bash
   python -m venv env
   source env/bin/activate  # On Windows: env\Scripts\activate

3. **Install the required Python packages:**
    ```bash
   pip install -r requirements.txt
   
4. **Set up the database: Run the migrations to create the database schema.**
   ```bash
   python manage.py migrate

5. **Create a superuser (admin account):**
   ```bash
   python manage.py createsuperuser

6. **Install TailwindCSS with django-tailwind: Run the following commands to install and initialize TailwindCSS for your Django project.**
   1. **Install Tailwind dependencies:**
      ```bash
      python manage.py tailwind install
   2. **Configure Tailwind: Open the settings.py file and make sure that TAILWIND_APP_NAME is set to the correct app name (e.g., 'theme').**
      ```bash
      TAILWIND_APP_NAME = 'theme'
   3. **Install Tailwind dependencies:**
      ```bash
      python manage.py tailwind start

7. **Run the Django development server:**
   ```bash
   python manage.py runserver
