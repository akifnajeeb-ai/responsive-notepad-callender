# Simple Notepad Web Application

This repository contains a minimal **Notepad** web app built with:
- **Flask** (Python) as the backend API and server
- **SQLite** for data storage (no external DB required)
- **HTML/CSS/JavaScript** for the frontend UI

## Project Structure
```
notepad/
├─ app.py                # Flask application
├─ requirements.txt      # Python dependencies
├─ Dockerfile            # Container image definition
├─ README.md             # This file
├─ .gitignore            # Ignored files
└─ static/
   ├─ index.html         # Front‑end UI
   ├─ style.css          # Styles
   └─ script.js          # Front‑end logic
```

## Prerequisites
- **Python 3.9+** (recommended: use a virtual environment)
- **Docker** (optional, for containerised deployment)

## Local Development
1. Open a terminal in the project root.
2. Create and activate a virtual environment (optional but recommended):
   ```powershell
   python -m venv venv
   .\venv\Scripts\Activate.ps1   # PowerShell
   # or
   .\venv\Scripts\activate.bat  # CMD
   ```
3. Install dependencies:
   ```powershell
   pip install -r requirements.txt
   ```
4. Run the Flask development server:
   ```powershell
   python app.py
   ```
5. Open your browser and navigate to **http://localhost:5000**.
   - You can create, edit, and delete notes.
   - All notes are stored in the `notes.db` SQLite file automatically created next to `app.py`.

## Containerised Deployment (Docker)
1. Build the Docker image:
   ```powershell
   docker build -t simple-notepad .
   ```
2. Run the container, mapping port 5000 to your host:
   ```powershell
   docker run -d -p 5000:5000 --name notepad simple-notepad
   ```
3. Access the app at **http://localhost:5000**.

   The container uses the built‑in Flask server for simplicity. For production you may replace the `CMD` with a WSGI server such as **gunicorn**.

## Database
- The SQLite database file (`notes.db`) is created automatically on first launch.
- To inspect or reset the database, simply delete `notes.db` while the app is stopped; a fresh file will be generated on the next start.

## Customisation
- **Backend**: Extend `app.py` with additional REST endpoints or switch to a different database (PostgreSQL, MySQL) by updating the SQLAlchemy URI.
- **Frontend**: Modify `static/style.css` and `static/script.js` to change the look & feel or add new features.

## License
This example is provided under the MIT License – feel free to adapt it for your own projects.

