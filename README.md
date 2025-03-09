# ELD Trip Planner - Backend

This is the backend service for the **ELD Trip Planner Application** built with **Django Rest Framework (DRF)**. It provides user authentication, trip management, and report generation features.

---

## 🚀 Features
- User authentication (Register, Login, JWT-based authentication)
- Trip management (CRUD operations)
- Generate trip reports as PDFs
- Secure API endpoints with permissions

---

## 📌 Technologies Used
- **Python 3**
- **Django 4**
- **Django Rest Framework (DRF)**
- **PostgreSQL / SQLite** (Choose based on your environment)
- **ReportLab** (For generating PDF reports)

---

## 📦 Installation

### 1️⃣ Clone the repository:
```bash
 git clone https://github.com/yourusername/eld-trip-planner-backend.git
 cd eld-trip-planner-backend
```

### 2️⃣ Create and activate a virtual environment:
```bash
python -m venv env
source env/bin/activate  # On MacOS/Linux
env\Scripts\activate    # On Windows
```

### 3️⃣ Install dependencies:
```bash
pip install -r requirements.txt
```

### 4️⃣ Set up the database:
```bash
python manage.py makemigrations
python manage.py migrate
```

### 5️⃣ Create a superuser:
```bash
python manage.py createsuperuser
```

### 6️⃣ Run the development server:
```bash
python manage.py runserver
```

---

## 🔑 Authentication

This project uses **JWT authentication** via **Django SimpleJWT**.

---

### ERD:
![ERD](https://github.com/user-attachments/assets/4a6be24c-8b29-46a1-b0c2-05b6a352d575)


---

## 🏠 API Endpoints Documentation:
https://www.apidog.com/apidoc/shared-31f4333e-52de-4b22-9b63-0eff393ea66a/get-the-trip-details-14642270e0


---

## 📂 Project Structure
```
core/
│── trip/                 # Trip app (models, views, serializers)
│── report/               # Report generation app
│── user/                 # User authentication & management
│── core/                 # Main Django settings
│── env/                  # Virtual environment (not committed)
│── manage.py             # Django management script
│── requirements.txt      # Dependencies
```

---


## 👥 Contributors
- [Kirollos Adel](https://github.com/kiro0oz)

---

## 📄 License
This project is licensed under the **MIT License**.

