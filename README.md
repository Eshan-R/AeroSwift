# ✈️ AeroSwift: Real-Time Flight Booking System

AeroSwift is a high-performance, full-stack web application built with **Flask** that leverages the **Amadeus API** to provide real-time flight data. It features a custom-engineered interactive seat selection tool and a professional user dashboard.

## 🌟 Key Features
* **Live Flight Data:** Integrated with the **Amadeus API** to fetch real-time flight schedules, pricing, and availability.
* **Interactive Seat Map:** A grid-based selection system using the "Checkbox Hack" for a responsive, JS-light user experience.
* **Smart Search:** Search for flights across global destinations with dynamic data fetching.
* **Booking Management:** Integrated "My Trips" dashboard to track flight details and seat assignments.
* **Modern UI:** Styled with CSS Grid and Flexbox for a premium, sleek aesthetic.

## 🧠 Technical Concept Brush-up
This project served as a deep dive into several core full-stack concepts:

### 1. External API Integration (Amadeus)
* **Logic:** Implemented secure OAuth2 authentication to communicate with Amadeus servers.
* **Data Parsing:** Processed complex JSON responses from the API to display flight options to the user in a clean, readable format.

### 2. The Checkbox Hack (UI Logic)
Instead of relying heavily on JavaScript to track seat selection, I used hidden `<input type="checkbox">` elements.
* **Logic:** When a user clicks a seat, the checkbox is toggled.
* **Styling:** CSS sibling selectors (`input:checked + .seat-label`) handle the visual change (color/border).

### 3. Backend Architecture (Flask)
* **Environment Security:** Used `.env` to store the Amadeus API Key and Secret, ensuring they never leak to GitHub.
* **Models:** Used SQLAlchemy to link API-provided flight data with local user booking records.

## 🛠️ Tech Stack
- **API:** Amadeus for Developers
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
