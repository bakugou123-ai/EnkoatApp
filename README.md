## Project Summary
This project is a full-stack application  that simulates a contractor-facing interface for submitting project quotes and visualizing project performance data. 

The contractor can : 
- Submit new roofing project quotes through a styled form
- View a Bokeh-powered dashboard with charts and trends

Tech Stakc used: 
**Backend:** Django + Django REST Framework  
- **Frontend:** HTML/CSS + JavaScript  
- **Dashboard & Charts:** Bokeh (Python)
- **Faker** To simulate fake data of 700-800 records

## 🧪 How to Run It Locally

### 1. Clone the Repository
git clone https://github.com/bakugou123-ai/EnkoatApp.git

### 2. Setup Environment 
python -m venv venv
venv\Scripts\activate  # Windows
# or
source venv/bin/activate  # Mac/Linux

### 3.Install requirements
pip install -r requirements.txt

### 4. Mock Data generation
python manage.py migrate
python manage.py create_mock_data  # Optional custom command (1000+ entries)

### 5. Start server

Django server
python manage.py runserver

Bokeh dashboard server
python -m bokeh serve bokeh_dashboard.py --allow-websocket-origin=localhost:5006 --allow-websocket-origin=127.0.0.1:8000

Improvements:
With extended time, I would've added the following features:
1. User authentication
2. PDF report generation of data
3. Data filteration
4. Heat map showing the roof type with respect to each state.





