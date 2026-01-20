# ✈️ AeroSwift: Modern Flight Booking System

AeroSwift is a full-stack web application built with **Flask** that streamlines the flight booking experience. It features a custom-engineered interactive seat selection tool and a clean, user-centric dashboard.

## 🌟 Key Features
* **Interactive Seat Map:** A grid-based selection system using the "Checkbox Hack" for a responsive, JS-light user experience.
* **Smart Search:** Filter flights by origin, destination, and date.
* **Booking Management:** Integrated "My Trips" dashboard to track flight details and seat assignments.
* **Modern UI:** Styled with CSS Grid and Flexbox for a premium, sleek aesthetic.

## 🧠 Technical Concept Brush-up
This project served as a deep dive into several core full-stack concepts:

### 1. The Checkbox Hack (UI Logic)
Instead of relying heavily on JavaScript to track seat selection, I used hidden `<input type="checkbox">` elements.
* **Logic:** When a user clicks a seat, the checkbox is toggled.
* **Styling:** CSS sibling selectors (`input:checked + .seat-label`) handle the visual change (color/border), making the UI incredibly fast.

### 2. CSS Grid Layering
The airplane cabin layout uses `display: grid`.
* **Challenge:** Overlapping elements and spacing.
* **Solution:** Mastered `z-index` and `grid-template-areas` to ensure the "aisle" and "seats" aligned perfectly across all screen sizes.

### 3. Backend Architecture (Flask)
* **Models:** Used SQLAlchemy to create relationships between Flights, Seats, and Bookings.
* **Security:** Implemented environment variables via `.env` to protect sensitive database credentials and secret keys.

## 🛠️ Tech Stack
- **Backend:** Python / Flask
- **Database:** SQLite / SQLAlchemy
- **Frontend:** HTML5, CSS3, FontAwesome
- **Version Control:** Git & GitHub

## 🚀 Installation & Setup
1. **Clone the repository:**
   ```bash
   git clone [https://github.com/Eshan-R/AeroSwift.git](https://github.com/Eshan-R/AeroSwift.git)
   ```
2. **Setup Virtual Environment:**
  ```bash
  python -m venv venv
  source venv/bin/activate  # On Windows: venv\Scripts\activate
  ```
3. **Install Dependencies:**
  ```bash
pip install -r requirements.txt
```

4. **Run the Application:**
  ```bash
python run.py
```
