# AIPE_group5 – Titanic Data Viewer

A simple full-stack project using **Flask**, **MySQL**, and **Docker Compose** to load and view Titanic passenger data from a CSV file (`my_titanic.csv`). Designed for fast deployment via `docker-compose up`.

---

## 🐳 Features

- 🐍 Python Flask web server  
- 🗄️ MySQL 8.0 database  
- 📊 Auto-import Titanic data from CSV  
- 🌐 Web-based viewer (or JSON API only)  
- 📦 One-command setup with Docker Compose  

---

## 📁 Project Structure

AIPE_group5/
│
├── app/
│ ├── app.py # Flask backend logic
│ ├── my_titanic.csv # Titanic CSV dataset
│ └── templates/index.html # (Optional) HTML table view
│
├── init.sql # SQL to define passengers table
├── Dockerfile # For Flask server build
├── docker-compose.yml # Compose config for web + MySQL
└── README.md # You are here

---

## 🚀 Quick Start

> 📦 Prerequisites: Docker & Docker Compose installed

```bash
git clone https://github.com/<your-username>/AIPE_group5.git
cd AIPE_group5
docker-compose up

Then visit http://localhost:9999
Or replace localhost with your server's IP.



