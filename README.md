# my-crud-app
A simple Flask CRUD task tracker (To-Do list) using Flask-SQLAlchemy.

## Live Demo
- https://t5h3p4n9.pythonanywhere.com/

## Features
- Create tasks
- Read/list tasks
- Update/edit tasks
- Delete tasks
- SQLite persistence with SQLAlchemy models

## Tech Stack
- Python 3
- Flask
- Flask-SQLAlchemy
- SQLite

## Project Structure
- `app.py` - Flask application routes and database model
- `templates/` - HTML templates (`base.html`, `index.html`, `edit.html`)
- `static/styles.css` - UI styling
- `requirements.txt` - dependencies

## Getting Started
1. Clone repository
   ```bash
   git clone https://github.com/yourusername/my-crud-app.git
   cd my-crud-app
   ```
2. Create and activate virtual environment
   ```bash
   python -m venv venv
   venv\Scripts\activate   # Windows
   source venv/bin/activate  # macOS/Linux
   ```
3. Install dependencies
   ```bash
   pip install -r requirements.txt
   ```
4. Run the app
   ```bash
   python app.py
   ```
5. Open in browser
   - http://127.0.0.1:5000/

## Deployment
- Deployed at https://t5h3p4n9.pythonanywhere.com/

## License
MIT (or adapt to your preference)

