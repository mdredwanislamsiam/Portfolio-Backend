

#  Portfolio API – Django REST Framework

A fully functional **Portfolio Backend API** built with **Django REST Framework (DRF)**.
This project allows users to manage their academic, professional, and research portfolio with JWT authentication and interactive API documentation.

---

##  Project Overview

**Portfolio API** is a RESTful backend service where users can:

* Manage Profile Information
* Add Education History
* Add Skills with Images
* Add Work Experiences with Images
* Add Research & Publications
* Add Conferences with Images
* Add Social Media Links

The project uses **JWT authentication (Djoser)** and includes **Swagger documentation (drf-yasg)** for easy API testing.

---

##  Tech Stack

* **Backend Framework:** Django
* **API Framework:** Django REST Framework
* **Authentication:** Djoser + JWT
* **Documentation:** drf-yasg
* **Image Storage:** Cloudinary
* **Database:** SQLite (default) / PostgreSQL (production ready)

---

##  Authentication

JWT Authentication is implemented using **Djoser**.

### Available Auth Endpoints:

* `POST /auth/users/` → Register
* `POST /auth/jwt/create/` → Login (Get Access & Refresh Token)
* `POST /auth/jwt/refresh/` → Refresh Token
* `POST /auth/jwt/verify/` → Verify Token

Authenticated routes require:

```
Authorization: Bearer <access_token>
```

---

##  API Modules

### 👤 Users

* Custom User Model
* Profile image & cover image
* Social media links

### 🎓 Education

* Degree
* Institution
* CGPA
* Duration
* Related images

### 💼 Experience

* Job title
* Description
* Duration
* Related images

### 🛠 Skills

* Skill title
* Description
* Related images

### 🔬 Research

* Title
* Journal
* Volume/Page
* Researchers
* Publication date
* Research images
* Filtering, Searching, Ordering enabled

### 🏛 Conferences

* Title
* Short title
* Organizers
* Date
* Conference images

---

## 🔎 Filtering & Search

For Research & Conference:

* Search by title or journal
* Order by date
* Pagination enabled

Example:

```
/api/research/?search=AI
/api/research/?ordering=-date
```

---

## 📄 Swagger Documentation

Swagger UI is available for interactive API testing.

```
/swagger/
/redoc/
```

Powered by **drf-yasg**.

---

## 🗂 Project Structure

```
portfolio/
│
├── users/
├── resume/
├── research/
├── portfolio/
│
├── manage.py
└── requirements.txt
```

---

## ⚙️ Installation & Setup

### 1️⃣ Clone the Repository

```bash
git clone https://github.com/mdredwanislamsiam/Portfolio-Backend.git
cd Portfolio-Backend
```

### 2️⃣ Create Virtual Environment

```bash
python -m venv venv
source venv/bin/activate
```

### 3️⃣ Install Dependencies

```bash
pip install -r requirements.txt
```

### 4️⃣ Configure Environment Variables

Create a `.env` file and configure:

```
SECRET_KEY=your_secret_key
DEBUG=True

CLOUDINARY_CLOUD_NAME=your_cloud_name
CLOUDINARY_API_KEY=your_api_key
CLOUDINARY_API_SECRET=your_api_secret
```

### 5️⃣ Run Migrations

```bash
python manage.py makemigrations
python manage.py migrate
```

### 6️⃣ Create Superuser

```bash
python manage.py createsuperuser
```

### 7️⃣ Run Server

```bash
python manage.py runserver
```

---

## 🔒 Permissions Logic

* **GET requests** → Public access
* **POST, PUT, PATCH, DELETE** → Authenticated users only
* Staff users can view all data
* Regular users can only manage their own content

---

## 📦 Key Features

✔ Custom User Model
✔ JWT Authentication
✔ Nested Image Upload APIs
✔ Search & Ordering
✔ Pagination
✔ Cloudinary Integration
✔ Swagger Documentation
✔ Modular App Structure

---

## 📈 Future Improvements

* Role-based permissions
* Public portfolio share link
* Caching
* Rate limiting
* Docker support
* CI/CD integration

---

## 👨‍💻 Author

Md. Redwan Islam Siam

If you like this project, feel free to ⭐ the repository!

---

