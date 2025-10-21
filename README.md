
# ✈️ Airline Ticket Booking System

## 📘 Overview
The **Airline Ticket Booking System** is a hybrid **Flask + JavaScript-based web application** that enables users to **search flights, book tickets, view/cancel bookings**, and simulate a queue-based boarding mechanism using core **Data Structures and Algorithms (DSA)**.

Built collaboratively by a **4-member team in one week**, this project integrates **free flight data APIs** (like AviationStack) to fetch real-time flight information.

---

## 🧩 Features

- 🔍 **Flight Search** — Live data via free flight APIs  
- 🎟️ **Ticket Booking** — Uses Queue/Linked List DSA concepts  
- 🚫 **Ticket Cancellation** — Automatic seat release logic  
- ⚡ **Flask REST API** — Lightweight and modular  
- 🎨 **Frontend Interface** — Minimal HTML/CSS/JS (or React optional)  
- 💾 **Cache Mechanism** — Reduces redundant API calls  
- 📦 **SQLite/JSON DB** — Stores user and booking information  

---

## ⚙️ Tech Stack

| Layer | Tools/Frameworks |
|-------|------------------|
| **Backend** | Python, Flask, Requests, DSA |
| **Frontend** | HTML, CSS, JavaScript (or React) |
| **Database** | SQLite / JSON File |
| **APIs** | AviationStack (Free Tier) |
| **Version Control** | Git & GitHub |

---

## 👥 Team Roles

| Member | Role | Responsibilities |
|---------|------|------------------|
| **Eshan** | Backend Lead | Flask setup, API integration, route handling |
| **Backend Partner** | Backend Support | DSA logic (queue, cancellation, cache system) |
| **Frontend Lead** | Frontend Development | UI design, API integration |
| **Frontend Partner** | Frontend Support | Styling, interactivity, testing |

---

## 🚀 Setup Instructions

### Backend (Flask)
```bash
cd backend
pip install -r requirements.txt
python app.py
```

### Frontend
```bash
cd frontend
npm install
npm start
```

Then open:
- Backend: http://localhost:5000  
- Frontend: http://localhost:3000
