# 📊 Offline Exam Result Analytics System (Web Based)

A **Flask-based web application** that manages offline exam results and provides advanced analytics to evaluate student performance, subject difficulty, and overall class statistics.

---

## 🚀 Features

### 🔐 Role-Based Login System
- Admin and Teacher login
- Secure session-based authentication
- Role-based page access

| Role  | Access                                   |
|-------|-----------------------------------------|
| Admin | Full access including analytics & reports |
| Teacher | Marks entry & results only             |

---

### 🧑‍🎓 Student & Marks Management
- Add students
- Define subjects
- Enter offline exam marks
- Automatic calculation of:
  - Total marks
  - Percentage
  - Pass / Fail status

---

### 📄 Result Management
- View subject-wise student results
- Color-coded Pass/Fail status
- Dynamic result table

---

### 📊 Analytics Dashboard (Admin Only)
#### Subject Difficulty Index
- Calculates average marks per subject
- Lowest average = most difficult subject
- Bar chart difficulty ranking

#### Student Performance Categories
| Percentage | Category |
|------------|---------|
| ≥ 75%      | Excellent |
| 40–74%     | Average |
| < 40%      | Needs Improvement |

- Pie chart distribution

#### Analytics Summary Report
- Total students
- Pass percentage
- Class average
- Top performer
- Most difficult subject

---

### 📥 PDF Analytics Report
- Download complete class performance report
- Auto-generated using **FPDF**

---

## 🛠 Technology Stack

| Layer      | Technology                   |
|------------|------------------------------|
| Frontend   | HTML, CSS, Bootstrap, Chart.js |
| Backend    | Python Flask                 |
| Database   | MySQL                        |
| PDF Reports| FPDF                         |

---

## 🔑 Demo Login Credentials

| Role    | Username  | Password   |
|---------|----------|-----------|
| Admin   | admin     | admin@123 |
| Teacher | teacher1  | teach@123 |
| Teacher | teacher2  | teach@456 |

---

## ⚙ Installation & Setup

1. Clone the repository:
2. ```bash
git clone <your-repo-url>

Navigate to the project folder:

cd offline-exam-result-analytics


Install dependencies:
pip install -r requirements.txt

Run the Flask app:
python app.py


git clone <your-repo-url>
