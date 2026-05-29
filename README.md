# Personal Coding Projects

This repository is a personal learning workspace that collects coding practice, school-related tools, web experiments, and a larger self-hosted school management web app. It includes projects written in Python, HTML, JavaScript, React, Node.js, and Docker.

The folder is organized as a practical archive of experiments: some files are polished enough to run directly, while others are clearly marked as in-development practice projects. Most projects focus on student productivity, grade tracking, deadlines, study sessions, password utilities, and small web interfaces.

## Repository Overview

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

## Main Technologies

- Python 3 for terminal utilities, school tools, file-based storage, and small experiments
- HTML, CSS, and vanilla JavaScript for standalone browser projects
- React 18 and Vite for the self-hosted school manager frontend
- Express.js for the local backend API
- JSON files for lightweight local data storage
- Docker and Docker Compose for containerized deployment of the school manager app
- Tailwind CSS, Radix UI, shadcn-style UI components, Lucide icons, Recharts, XLSX, and jsPDF in the React app

## Featured Project: School Manager Self-Host

Folder:

```text
school-manager-selfhost - VIBE CODING/
```

This is the largest project in the repository. It is a Vite + React school management application that has been refactored to run locally without Base44. The app includes a small Express backend and stores local data in:

```text
school-manager-selfhost - VIBE CODING/server/data/db.json
```

### Features

- Dashboard for viewing overall school performance
- Subject management page
- Grade entry page
- Test and exam calendar
- Goal tracking for target scores
- Reports and charts
- Semester comparison
- Suggested learning path page
- Local REST API for subjects, grades, and goals
- Local mock authentication endpoint
- Excel export support through `xlsx`
- PDF generation support through `jspdf`
- Charts through `recharts`
- Responsive UI built with React components and Tailwind CSS

### Main Frontend Routes

| Route | Page | Purpose |
| --- | --- | --- |
| `/` | Dashboard | Overall score summary and key learning stats |
| `/mon-hoc` | Subjects | Manage school subjects |
| `/diem-so` | Grades | Add and calculate scores |
| `/lich-kiem-tra` | Exam Schedule | Manage tests and export calendar data |
| `/muc-tieu` | Goals | Set and track subject goals |
| `/bao-cao` | Reports | View reports and charts |
| `/so-sanh` | Semester Compare | Compare HK1 and HK2 performance |
| `/lo-trinh` | Learning Path | See suggested focus areas |

### Backend API

The Express server exposes these local endpoints:

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

Note: `/api/llm/invoke` currently returns `501 not_implemented`. It is a placeholder left from the Base44 version and can be connected to a server-side AI provider later.

### Run the School Manager in Development

```bash
cd "school-manager-selfhost - VIBE CODING"
npm install
npm run dev:server
```

In a second terminal:

```bash
cd "school-manager-selfhost - VIBE CODING"
npm run dev
```

<<<<<<< HEAD
The API server runs on:
=======
**Tun140113** - [GitHub Profile](https://github.com/Hello-ItsTuaan)
>>>>>>> 3f658a8f774c8afa3038eca4a8f92b84ff606b9c

```text
http://localhost:8787
```

The Vite frontend usually runs on:

```text
http://localhost:5173
```

Vite proxies `/api` requests to `http://localhost:8787`.

### Run the School Manager in Production-Like Mode

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

### Run with Docker

```bash
cd "school-manager-selfhost - VIBE CODING"
docker compose up --build
```

The container exposes the app on:

```text
http://localhost:8787
```

Docker Compose mounts this folder so data persists outside the container:

```text
server/data/
```

## HTML Projects

Folder:

```text
HTML/
```

### `grade_manager.html`

A standalone browser-based grade manager written with HTML, CSS, and JavaScript. It includes a full UI for managing student grades and uses browser-side JavaScript instead of a backend.

Notable features include:

- Dashboard-style school grade interface
- Subject and grade tracking
- Semester support
- Charts through Chart.js
- Excel import/export through SheetJS
- PDF export through jsPDF
- Screenshot/PDF support through html2canvas
- Browser local data handling
- Responsive layout with sidebar navigation

Run it by opening the file directly in a browser:

```text
HTML/grade_manager.html
```

## JavaScript Projects

Folder:

```text
JavaScript/
```

### `something.js`

A small Node.js command-line practice script that asks for a name using the `readline` module and prints a greeting.

Run it with:

```bash
cd JavaScript
node something.js
```

### `something.html`

A large standalone marketplace-style web page inspired by a classified listing app. It includes:

- Product grid
- Search bar
- Category filters
- Price filters
- Sorting
- Product post modal
- Image upload preview
- Toast notifications
- Responsive layout

Run it by opening:

```text
JavaScript/something.html
```

## Python Projects

Folder:

```text
Python/
```

The Python folder contains most of the small practice programs. Several of them store data in local `.txt` or `.json` files next to the scripts.

### Password Checker

Folder:

```text
Python/Password checker/
```

Main file:

```text
password_checker.py
```

A terminal password utility with a simple menu. It can:

- Check password strength
- Generate random passwords
- Save username/password pairs to `accounts.txt`
- View saved accounts

The password score checks:

- Lowercase letters
- Uppercase letters
- Digits
- Symbols
- Minimum length of 8 characters

Run it with:

```bash
cd "Python/Password checker"
python password_checker.py
```

Important note: this script stores passwords in plain text in `accounts.txt`. It is useful for learning, but it should not be used as a real password manager.

### School Average Predictions

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

This in-development project focuses on grade calculations and prediction logic. The current calculation helpers include:

- `calc_semester_avg(...)` for weighted semester averages
- `calc_needed_score(...)` for calculating the missing score needed to reach a target
- `calc_year_avg(...)` for year-end averages using HK1/HK2 weights
- `check_goals(...)` for comparing current subject averages with goals

The project uses `grades.json` for local data storage.

### Grade Manager in Development

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

This is a practice terminal grade manager. It is designed to:

- Add students
- Store scores for Vietnamese, Math, and English
- Calculate GPA
- Rank students
- Save and load data with JSON

Some placeholders such as `___` are still present in `main.py`, so this project is not fully finished yet.

### Task Deadline Manager

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

A terminal deadline tracker that stores tasks in JSON. It can:

- Add a task with a deadline
- Detect duplicate task names
- Add more time to an existing task
- Replace an existing deadline
- List tasks sorted by deadline
- Search tasks by keyword
- Mark tasks as done
- Delete tasks
- Export deadlines to a text file
- Color output based on urgency using `colorama`

Run it with:

```bash
cd "Python/Task-Deadline manager"
python "Task-Deadline manager.py"
```

Optional dependency:

```bash
pip install colorama
```

### School Things Manager / Study Tracker

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

A study-session tracker for recording how much time is spent on each subject. It can:

- Add study sessions
- Prevent duplicate subject entries
- Add extra minutes to an existing subject
- View sessions in a table
- Delete sessions
- Display daily study statistics with a bar chart
- Reset session data

Run it with:

```bash
cd "Python/School_Things_Manager"
python study_tracker.py
```

Optional dependencies:

```bash
pip install prettytable matplotlib
```

### Number Guessing Game

Folder:

```text
Python/number_game/
```

Main file:

```text
numberguessinggame.py
```

A small terminal number guessing game using Python's `random` module.

Run it with:

```bash
cd "Python/number_game"
python numberguessinggame.py
```

### Task Manager

Folder:

```text
Python/task_manager/
```

Main file:

```text
task.py
```

A small task-management practice script. This appears to be an earlier or simpler version compared with the larger Task Deadline Manager.

### Stuffs

Folder:

```text
Python/Stuffs/
```

This folder contains miscellaneous experiments, older versions, and practice files. Examples include:

- `calculator.py` - calculator practice
- `bmi.py` - BMI calculator
- `expensetracker.py` and `expensetracker2.0.py` - expense tracking experiments
- `numberguessinggame.py` - another number guessing game copy
- `password_checker.py` - another password checker copy
- `chrome_lock.cpp`, `chrome_lock.exe`, `build_chrome_lock.bat` - C++/Windows experiment related to locking Chrome
- `winver.py` - Windows credential/user verification experiment
- `enetviet.py`, `test.py`, `mda.py`, `nhap.py`, `Questions.py` - additional experiments and practice scripts

Some files in this folder are experiments and should be reviewed before running, especially scripts that interact with Windows processes, keyboard input, browser behavior, or system UI.

## Data Files

The repository includes several local data files used by the scripts:

| File | Purpose |
| --- | --- |
| `sessions.txt` | Root-level session data or practice data |
| `sessions` | Small root-level session file |
| `tasks.json` | Root-level task data |
| `Python/tasks.json` | Python task data |
| `Python/accounts.txt` | Account/password practice data |
| `Python/Password checker/accounts.txt` | Password checker saved account data |
| `Python/School_Things_Manager/sessions.txt` | Study tracker data |
| `Python/Task-Deadline manager/tasks.json` | Deadline manager task storage |
| `Python/School_AVG_Predictions- IN DEV/grades.json` | Grade prediction project data |
| `school-manager-selfhost - VIBE CODING/server/data/db.json` | React school manager local database |

## Suggested Setup

### Requirements

- Git
- Python 3.10 or newer
- Node.js 20 or newer
- npm
- Docker Desktop, optional, only for the self-hosted school manager

### Clone the Repository

```bash
git clone https://github.com/Hello-ItsTuaan/Personal-Coding-Projects.git
cd Personal-Coding-Projects
```

### Python Dependencies

Most Python scripts use only the standard library. Some scripts need extra packages:

```bash
pip install colorama prettytable matplotlib psutil keyboard pywinrt
```

You may not need all of these at once. Install only what is required by the script you want to run.

Common optional packages by project:

| Package | Used for |
| --- | --- |
| `colorama` | Colored terminal output in the deadline manager |
| `prettytable` | Table display in the study tracker and expense tracker experiments |
| `matplotlib` | Study statistics chart |
| `psutil` | Windows/process experiments in `Stuffs/` |
| `keyboard` | Keyboard input experiments in `Stuffs/` |
| `pywinrt` / `winrt` | Windows-specific verification experiment |

### Node Dependencies

For the React school manager:

```bash
cd "school-manager-selfhost - VIBE CODING"
npm install
```

For the small JavaScript CLI file:

```bash
cd JavaScript
node something.js
```

No npm install is required for `something.js` because it uses Node's built-in `readline` module.

## Development Status

This repository is a personal coding workspace, so projects are at different stages:

| Area | Status |
| --- | --- |
| `school-manager-selfhost - VIBE CODING/` | Main polished app, runnable with npm or Docker |
| `HTML/grade_manager.html` | Large standalone browser app |
| `JavaScript/something.html` | Standalone web UI experiment |
| `Python/Task-Deadline manager/` | Functional terminal app |
| `Python/School_Things_Manager/` | Functional terminal app with charts |
| `Python/Password checker/` | Functional learning project, not secure for real secrets |
| `Python/School_AVG_Predictions- IN DEV/` | In development |
| `Python/grade_manager - IN DEV/` | In development, contains placeholders |
| `Python/Stuffs/` | Mixed experiments and practice files |

## Notes for GitHub Visitors

- This repository is best understood as a learning archive plus one larger school manager app.
- Some scripts use Vietnamese labels and comments.
- Some terminal output may look different depending on the shell, OS, and text encoding.
- Some files are intentionally experimental and may not be production-ready.
- Plain-text data files are included for practice; avoid storing private real data in them.
- Before running scripts in `Python/Stuffs/`, read the source code first because several files interact with local system behavior.

## Possible Future Improvements

- Add `requirements.txt` files for Python subprojects
- Split polished apps and experiments into separate folders
- Fix text encoding issues in older Vietnamese source files
- Add screenshots for the web projects
- Add unit tests for grade calculation helpers
- Finish placeholders in `Python/grade_manager - IN DEV/main.py`
- Implement `/api/llm/invoke` in the self-hosted school manager backend
- Add environment variable examples for future AI or authentication features
- Add a root-level project index with screenshots and direct run commands

## Author

Created by Tuan Nguyen as a personal coding and school-tool development repository.

GitHub remote:

```text
https://github.com/Hello-ItsTuaan/Personal-Coding-Projects
```
