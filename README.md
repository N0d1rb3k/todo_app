# 📝 Django To-Do App

A simple and minimal To-Do List web application built with Django, HTML, CSS, JavaScript, and SQLite. It allows users to create, update, complete, and delete tasks. 🔧 No login system yet.

---

## 🚀 Features

- ✅ Add new tasks  
- ✏️ Edit and delete tasks  
- ☑️ Mark tasks as complete/incomplete  
- 🧼 Clean UI using HTML, CSS, and JavaScript  
- 🐳 Docker support  
- 🗃️ Uses SQLite (no setup required)

---

## 🛠️ Tech Stack

- ⚙️ **Backend**: Django (Python)  
- 🎨 **Frontend**: HTML, CSS, JavaScript  
- 💾 **Database**: SQLite  
- 🐳 **Containerization**: Docker  

---

## 💻 Local Setup

### 1. 📥 Clone the repository:

```bash
git clone git@github.com:N0d1rb3k/todo_app.git
cd todo_app
```

### 2. 🧪 Create and activate a virtual environment:

```bash
python -m venv venv
source venv/bin/activate  # Windows: venv\Scripts\activate
```

### 3. 📦 Install dependencies:

```bash
pip install -r requirements.txt
```

### 4. 🔄 Apply migrations:

```bash
python manage.py migrate
```

### 5. ▶️ Start the development server:

```bash
python manage.py runserver
```

📍 Then open: [http://127.0.0.1:8000](http://127.0.0.1:8000)

---

## 🐳 Docker Setup

### 1. 🔨 Build the Docker image:

```bash
docker build -t todo-app .
```

### 2. 🏃‍♂️ Run the container:

```bash
docker run -d -p 8000:8000 todo-app
```

🌐 Visit: [http://localhost:8000](http://localhost:8000)

---

## 🗂 Project Structure

```
Todo/
├── main/
│   ├── migrations/
│   ├── static/
│   ├── templates/
│   ├── admin.py
│   ├── models.py
│   ├── urls.py
│   └── views.py
├── Todo/
│   ├── settings.py
│   ├── urls.py
│   └── wsgi.py
├── Dockerfile
├── manage.py
├── requirements.txt
├── Procfile
└── db.sqlite3
```

---

## 🌟 Future Improvements

- 🔐 Add login/logout functionality  
- ⏰ Add due dates and reminders  
- 🏷️ Add categories/tags  
- ⚙️ REST API support with Django REST Framework  

---

## 📄 License

This project is licensed under the **MIT License**.

👤 Author: [Nodirbek Xonimqulov](https://github.com/N0d1rb3k)
