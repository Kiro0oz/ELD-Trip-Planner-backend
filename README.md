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
- **SQLite** 
- **ReportLab** (For generating PDF reports)

---

## 📦 Installation

### 1️⃣ Clone the repository:
```bash
 git clone https://github.com/Kiro0oz/ELD-Trip-Planner-backend.git
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

### 6️⃣ Run the development server:
```bash
python manage.py runserver
```

---

## 🔑 Authentication

This project uses **JWT authentication** via **Django SimpleJWT**.

---

### ERD:
![ERD](https://github.com/user-attachments/assets/b3723251-7cb1-4275-a90a-35c10d9e4b37)



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

