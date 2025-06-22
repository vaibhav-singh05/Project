# 🌐 Google Auth + CSV to Excel + Hotel Listing Web App

This is a Django-based full-stack web application that features:

- ✅ Google Sign-In authentication (using OAuth 2.0)
- 📁 CSV to Excel file conversion
- 🏨 Hotel listing based on city filter
- 🖥️ Responsive front-end (HTML + Bootstrap)
- ☁️ Live deployed on [Render](https://project-1-5kp0.onrender.com/)

---

## 🚀 Live Demo

🔗 [https://project-1-5kp0.onrender.com/api/google-login-page/](https://project-1-5kp0.onrender.com/api/google-login-page/) <br>
🔗 [https://project-1-5kp0.onrender.com/api/dashboard/](https://project-1-5kp0.onrender.com/api/dashboard/) <br>
🔗 [https://project-1-5kp0.onrender.com/api/hotels-page/](https://project-1-5kp0.onrender.com/api/hotels-page/) <br>

---

## 🔑 Features

- 🔐 **Google Login**: Authenticate users securely using their Google account
- ↻ **CSV to Excel Conversion**: Upload a `.csv` file and get an `.xlsx` file
- 📍 **Hotel API**: Get hotel listings based on city search via API and HTML page
- 🩼 **Whitenoise + Gunicorn**: For static file handling and deployment

---

## 🛠️ Tech Stack

- **Frontend**: HTML, CSS (Bootstrap 5), JavaScript
- **Backend**: Python, Django, Django Rest Framework
- **Database**: SQLite (development)
- **Auth**: Google OAuth 2.0 (GSI)
- **Deployment**: Render
- **Others**: Gunicorn, Whitenoise

---

## 📂 Directory Structure

```
google_csv_project/
├── core/
│   ├── migrations/
│   ├── templates/
│   ├── static/
│   ├── views.py
│   ├── urls.py
│   └── models.py
├── google_csv_project/
│   ├── wsgi.py
│   └── settings.py
├── db.sqlite3
├── manage.py
└── requirements.txt
```

---

## 🔧 Setup Instructions (Local)

1. **Clone the repo**
   ```bash
   git clone https://github.com/your-username/your-repo-name.git
   cd your-repo-name
   ```

2. **Create virtual environment**
   ```bash
   python -m venv venv
   source venv/bin/activate  # Windows: venv\Scripts\activate
   ```

3. **Install dependencies**
   ```bash
   pip install -r requirements.txt
   ```

4. **Run the server**
   ```bash
   python manage.py runserver
   ```

5. **Visit in browser**
   ```
   http://127.0.0.1:8000/api/google-login-page/
   ```

---

## 🔐 Google OAuth Setup

1. Go to [Google Cloud Console](https://console.cloud.google.com/)
2. Create a **Web Application** credential
3. Add the following:
   - **Authorized JavaScript origins**:
     ```
     https://project-1-5kp0.onrender.com
     ```
   - **Authorized redirect URIs**:
     ```
     https://project-1-5kp0.onrender.com/api/google-login-page/callback
     ```

4. Add your client ID in Django settings:
   ```python
   GOOGLE_CLIENT_ID = 'your-client-id.apps.googleusercontent.com'
   ```

---

## 📦 Deployment on Render

1. Push code to GitHub
2. Create new **Web Service** on [Render](https://render.com/)
3. Add Build Command:
   ```bash
   pip install -r requirements.txt
   ```
4. Add Start Command:
   ```bash
   gunicorn google_csv_project.wsgi:application
   ```
5. Add Environment Variables:
   - `GOOGLE_CLIENT_ID` = `your-client-id`
6. Click **Deploy** ✅

---

## 🖼️ Screenshots

> 📌 Add screenshots of login page, CSV upload, and hotel list results here.

---

## 👤 Author

**Vaibhav Singh**  
📧 [vaibhavsingh273010@gmail.com](mailto:vaibhavsingh273010@gmail.com)  
🔗 [LinkedIn](https://www.linkedin.com/in/vaibhav-singh-2a5991229/)  
💻 [GitHub](https://github.com/vaibhav-singh05)

---


**Happy Coding!** 🚀
