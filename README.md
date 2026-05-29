# 🚀 Personal Coding Projects

Welcome to my personal coding repository. This repo is a collection of school tools, coding practice projects, web experiments, Python terminal apps, and a bigger self-hosted school manager web application.

The repository is mainly used for learning, experimenting, and building useful tools for student life, especially grade tracking, deadline management, study tracking, and productivity.

## 📌 What This Repository Contains

- 🐍 Python terminal programs
- 🌐 HTML/CSS/JavaScript browser projects
- ⚛️ React + Vite school management app
- 🧠 Grade calculation and prediction experiments
- 📅 Task and deadline managers
- 📊 Study tracking tools with charts
- 🔐 Password checker and password generator practice
- 🐳 Docker setup for the self-hosted web app
- 🧪 Miscellaneous practice files and experiments

## 🗂️ Repository Structure

```text
Personal-Coding-Project/
|-- HTML/
|   `-- grade_manager.html
|-- JavaScript/
|   |-- something.html
|   `-- something.js
|-- Python/
|   |-- Password checker/
|   |-- School_AVG_Predictions- IN DEV/
|   |-- School_Things_Manager/
|   |-- Task-Deadline manager/
|   |-- grade_manager - IN DEV/
|   |-- number_game/
|   |-- task_manager/
|   `-- Stuffs/
|-- school-manager-selfhost - VIBE CODING/
|   |-- src/
|   |-- server/
|   |-- public/
|   |-- package.json
|   |-- Dockerfile
|   `-- docker-compose.yml
|-- sessions
|-- sessions.txt
|-- tasks.json
`-- README.md
```

## 🛠️ Main Technologies

| Technology | Used For |
| --- | --- |
| 🐍 Python | Terminal apps, grade tools, study tools, experiments |
| 🌐 HTML/CSS | Standalone web pages and UI practice |
| 🟨 JavaScript | Browser interactivity and Node.js practice |
| ⚛️ React | Main school manager frontend |
| ⚡ Vite | React development/build tool |
| 🟢 Node.js | Backend server and JavaScript CLI practice |
| 🚂 Express.js | Local REST API for the school manager |
| 🎨 Tailwind CSS | Styling the React app |
| 📦 JSON | Local file-based data storage |
| 🐳 Docker | Container deployment for the school manager |

## ⭐ Featured Project: School Manager Self-Host

Folder:

```text
school-manager-selfhost - VIBE CODING/
```

This is the biggest and most complete project in the repository. It is a self-hosted school management app built with React, Vite, Express.js, and local JSON storage.

It was refactored to run locally without Base44. The frontend talks to a small local backend API, and the backend stores data in:

```text
school-manager-selfhost - VIBE CODING/server/data/db.json
```

### ✨ Features

- 📊 Dashboard for school performance overview
- 📚 Subject management
- 📝 Grade entry and score calculation
- 📅 Exam/test schedule management
- 🎯 Goal tracking for target scores
- 📈 Reports and charts
- ⚖️ Semester comparison between HK1 and HK2
- 💡 Suggested learning path page
- 🔌 Local REST API for subjects, grades, and goals
- 👤 Local mock authentication endpoint
- 📤 Excel export support with `xlsx`
- 📄 PDF generation support with `jspdf`
- 📱 Responsive UI
- 🐳 Docker support

### 🧭 Frontend Routes

| Route | Page | Purpose |
| --- | --- | --- |
| `/` | Dashboard | View overall learning stats |
| `/mon-hoc` | Subjects | Manage school subjects |
| `/diem-so` | Grades | Add and calculate scores |
| `/lich-kiem-tra` | Exam Schedule | Manage tests and calendar data |
| `/muc-tieu` | Goals | Set and track target scores |
| `/bao-cao` | Reports | View reports and charts |
| `/so-sanh` | Semester Compare | Compare HK1 and HK2 results |
| `/lo-trinh` | Learning Path | See suggested focus areas |

### 🔌 Backend API

The local Express server provides:

```text
GET    /api/health
GET    /api/auth/me

GET    /api/subjects
POST   /api/subjects
PUT    /api/subjects/:id
DELETE /api/subjects/:id

GET    /api/grades
POST   /api/grades
PUT    /api/grades/:id
DELETE /api/grades/:id

GET    /api/goals
POST   /api/goals
PUT    /api/goals/:id
DELETE /api/goals/:id

POST   /api/llm/invoke
```

> ⚠️ Note: `/api/llm/invoke` currently returns `501 not_implemented`. It is a placeholder for a future AI feature.

### ▶️ Run School Manager in Development

Start the backend API:

```bash
cd "school-manager-selfhost - VIBE CODING"
npm install
npm run dev:server
```

In another terminal, start the frontend:

```bash
cd "school-manager-selfhost - VIBE CODING"
npm run dev
```

The backend runs at:

```text
http://localhost:8787
```

The Vite frontend usually runs at:

```text
http://localhost:5173
```

Vite proxies `/api` requests to `http://localhost:8787`.

### 🏗️ Run Production-Like Build

```bash
cd "school-manager-selfhost - VIBE CODING"
npm install
npm run build
npm start
```

Then open:

```text
http://localhost:8787
```

### 🐳 Run with Docker

```bash
cd "school-manager-selfhost - VIBE CODING"
docker compose up --build
```

Open:

```text
http://localhost:8787
```

Docker Compose mounts this folder so data can persist:

```text
server/data/
```

## 🌐 HTML Projects

Folder:

```text
HTML/
```

### 📊 `grade_manager.html`

A standalone browser-based grade manager written with HTML, CSS, and JavaScript.

Features include:

- 📊 Grade dashboard
- 📚 Subject tracking
- 🧮 Score calculation
- 📈 Charts using Chart.js
- 📤 Excel import/export using SheetJS
- 📄 PDF export using jsPDF
- 🖼️ Screenshot/PDF support with html2canvas
- 📱 Responsive layout
- 💾 Browser-side data handling

Run it by opening:

```text
HTML/grade_manager.html
```

## 🟨 JavaScript Projects

Folder:

```text
JavaScript/
```

### 👋 `something.js`

A small Node.js command-line script that asks for your name and prints a greeting.

Run it with:

```bash
cd JavaScript
node something.js
```

### 🛒 `something.html`

A standalone marketplace-style web page inspired by classified listing sites.

Features include:

- 🔍 Product search
- 🧩 Category filters
- 💰 Price filters
- ↕️ Sorting
- 🧾 Product cards
- ➕ Post listing modal
- 🖼️ Image upload preview
- 🔔 Toast notifications
- 📱 Responsive design

Run it by opening:

```text
JavaScript/something.html
```

## 🐍 Python Projects

Folder:

```text
Python/
```

This folder contains most of the terminal apps and practice programs. Many scripts use local `.txt` or `.json` files for storage.

## 🔐 Password Checker

Folder:

```text
Python/Password checker/
```

Main file:

```text
password_checker.py
```

This is a terminal password utility. It can:

- ✅ Check password strength
- 🔁 Generate random passwords
- 💾 Save username/password pairs to `accounts.txt`
- 👀 View saved accounts

The password checker scores passwords using:

- Lowercase letters
- Uppercase letters
- Digits
- Symbols
- Length of at least 8 characters

Run it with:

```bash
cd "Python/Password checker"
python password_checker.py
```

> ⚠️ Security note: this is a learning project. It stores passwords in plain text, so do not use it for real private passwords.

## 🧮 School Average Predictions

Folder:

```text
Python/School_AVG_Predictions- IN DEV/
```

Important files:

```text
grades.py
storage.py
display.py
main.py
grades.json
test.py
```

This project is for school average calculation and prediction logic.

Current helper functions include:

- `calc_semester_avg(...)` - calculates weighted semester averages
- `calc_needed_score(...)` - calculates the missing score needed to reach a goal
- `calc_year_avg(...)` - calculates yearly average from HK1 and HK2
- `check_goals(...)` - checks whether current grades meet targets

Local data is stored in:

```text
grades.json
```

Status: 🚧 In development

## 🏫 Grade Manager in Development

Folder:

```text
Python/grade_manager - IN DEV/
```

Important files:

```text
main.py
student.py
file_handler.py
test.py
test.json
```

This is a terminal grade manager practice project. It is designed to:

- ➕ Add students
- 📝 Store subject scores
- 🧮 Calculate GPA
- 🏅 Rank students
- 💾 Save/load data with JSON

Status: 🚧 In development. Some placeholders such as `___` are still present in `main.py`.

## 📅 Task Deadline Manager

Folder:

```text
Python/Task-Deadline manager/
```

Main file:

```text
Task-Deadline manager.py
```

Data file:

```text
tasks.json
```

This is a terminal task and deadline tracker.

Features include:

- ➕ Add tasks
- 📅 Set deadlines
- 🔁 Update existing deadlines
- ⏰ Add more time to a task
- 🔍 Search tasks
- ✅ Mark tasks as done
- 🗑️ Delete tasks
- 📤 Export deadlines to a text file
- 🎨 Color terminal output using `colorama`

Run it with:

```bash
cd "Python/Task-Deadline manager"
python "Task-Deadline manager.py"
```

Optional dependency:

```bash
pip install colorama
```

## 📚 School Things Manager / Study Tracker

Folder:

```text
Python/School_Things_Manager/
```

Main file:

```text
study_tracker.py
```

Data file:

```text
sessions.txt
```

This is a study-session tracker for recording study time by subject.

Features include:

- ➕ Add study sessions
- ⏱️ Add extra minutes to an existing subject
- 📋 View sessions in a table
- 🗑️ Delete sessions
- 📊 Show daily study statistics with a bar chart
- 🔄 Reset session data

Run it with:

```bash
cd "Python/School_Things_Manager"
python study_tracker.py
```

Optional dependencies:

```bash
pip install prettytable matplotlib
```

## 🎲 Number Guessing Game

Folder:

```text
Python/number_game/
```

Main file:

```text
numberguessinggame.py
```

A small terminal game where the user guesses a randomly selected number.

Run it with:

```bash
cd "Python/number_game"
python numberguessinggame.py
```

## ✅ Task Manager

Folder:

```text
Python/task_manager/
```

Main file:

```text
task.py
```

A smaller task-management practice script. This appears to be an earlier or simpler task project compared with the larger Task Deadline Manager.

## 🧪 Stuffs

Folder:

```text
Python/Stuffs/
```

This folder contains miscellaneous practice scripts, older versions, and experiments.

Examples:

- 🧮 `calculator.py` - calculator practice
- ⚖️ `bmi.py` - BMI calculator
- 💸 `expensetracker.py` and `expensetracker2.0.py` - expense tracker experiments
- 🎲 `numberguessinggame.py` - number guessing game copy
- 🔐 `password_checker.py` - password checker copy
- 🪟 `winver.py` - Windows verification experiment
- 🧱 `chrome_lock.cpp`, `chrome_lock.exe`, `build_chrome_lock.bat` - C++/Windows experiment
- 🧪 `enetviet.py`, `test.py`, `mda.py`, `nhap.py`, `Questions.py` - extra experiments and practice files

> ⚠️ Some scripts in `Python/Stuffs/` interact with Windows processes, keyboard input, browser behavior, or system UI. Read the source code before running them.

## 💾 Data Files

| File | Purpose |
| --- | --- |
| `sessions.txt` | Root-level session/practice data |
| `sessions` | Small root-level session file |
| `tasks.json` | Root-level task data |
| `Python/tasks.json` | Python task data |
| `Python/accounts.txt` | Account/password practice data |
| `Python/Password checker/accounts.txt` | Password checker saved account data |
| `Python/School_Things_Manager/sessions.txt` | Study tracker data |
| `Python/Task-Deadline manager/tasks.json` | Deadline manager storage |
| `Python/School_AVG_Predictions- IN DEV/grades.json` | Grade prediction data |
| `school-manager-selfhost - VIBE CODING/server/data/db.json` | School manager local database |

## ⚙️ Suggested Setup

### Requirements

- Git
- Python 3.10 or newer
- Node.js 20 or newer
- npm
- Docker Desktop, optional

### Clone the Repository

```bash
git clone https://github.com/Hello-ItsTuaan/Personal-Coding-Projects.git
cd Personal-Coding-Projects
```

### Python Dependencies

Most Python scripts use the standard library, but some projects may need extra packages:

```bash
pip install colorama prettytable matplotlib psutil keyboard pywinrt
```

Install only the packages needed for the script you want to run.

| Package | Used For |
| --- | --- |
| `colorama` | Colored terminal output |
| `prettytable` | Terminal tables |
| `matplotlib` | Study charts |
| `psutil` | Process/system experiments |
| `keyboard` | Keyboard input experiments |
| `pywinrt` / `winrt` | Windows-specific verification |

### Node Dependencies

For the school manager:

```bash
cd "school-manager-selfhost - VIBE CODING"
npm install
```

For the small JavaScript CLI script:

```bash
cd JavaScript
node something.js
```

## 🚦 Development Status

| Area | Status |
| --- | --- |
| `school-manager-selfhost - VIBE CODING/` | ✅ Main polished app |
| `HTML/grade_manager.html` | ✅ Large standalone web app |
| `JavaScript/something.html` | ✅ Standalone UI experiment |
| `JavaScript/something.js` | ✅ Small Node.js practice script |
| `Python/Task-Deadline manager/` | ✅ Functional terminal app |
| `Python/School_Things_Manager/` | ✅ Functional study tracker |
| `Python/Password checker/` | ✅ Learning project |
| `Python/School_AVG_Predictions- IN DEV/` | 🚧 In development |
| `Python/grade_manager - IN DEV/` | 🚧 In development |
| `Python/Stuffs/` | 🧪 Mixed experiments |

## 📝 Notes

- This repository is a personal learning archive.
- Some projects are finished enough to run, while others are experiments.
- Some scripts use Vietnamese labels and comments.
- Some older source files may have text encoding issues.
- Plain-text data files are included only for practice.
- Do not store real passwords or private data in the included `.txt` or `.json` files.

## 🔮 Future Improvements

- Add `requirements.txt` files for Python subprojects
- Add screenshots for the web projects
- Add unit tests for grade calculation logic
- Finish placeholders in `Python/grade_manager - IN DEV/main.py`
- Improve text encoding in older Vietnamese files
- Implement `/api/llm/invoke` in the school manager backend
- Add environment variable examples
- Add a root-level project index with screenshots and quick links

## 👤 Author

**Hello-ItsTuaan** - [GitHub Profile](https://github.com/Hello-ItsTuaan)

Created by Tuan Nguyen as a personal coding and school-tool development repository.

## 🔗 Repository

```text
https://github.com/Hello-ItsTuaan/Personal-Coding-Projects
```
