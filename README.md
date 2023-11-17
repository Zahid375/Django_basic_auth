# Django Auth

## Overview

Django Basic Authentication Application

## Setup

### Prerequisites

- Python 3.x

### Installation

1. Clone the repository:

    ```bash
    git clone https://github.com/your-username/your-django-project.git
    ```

2. Navigate to the project directory:

    ```bash
    cd your-django-project
    ```

3. Create a virtual environment (optional but recommended):

    ```bash
    python -m venv venv
    ```

    Activate the virtual environment:

    - On Windows:

        ```bash
        .\venv\Scripts\activate
        ```

    - On macOS/Linux:

        ```bash
        source venv/bin/activate
        ```

4. Install Django and other dependencies:

    ```bash
    pip install -r requirements.txt
    ```

### Configuration

1. Apply migrations:

    ```bash
    python manage.py migrate
    ```

2. Create a superuser for accessing the Django admin:

    ```bash
    python manage.py createsuperuser
    ```

    Follow the prompts to set up the superuser account.

### Usage

1. Run the development server:

    ```bash
    python manage.py runserver
    ```

    The application should now be accessible at [http://localhost:8000/](http://localhost:8000/).

2. Access the Django admin interface at [http://localhost:8000/admin/](http://localhost:8000/admin/) and log in with the superuser credentials.



## License

This project is licensed under the [MIT License](LICENSE).

