# Roomie

![python 3.9](https://img.shields.io/badge/python-3.9-blue) ![MIT](https://img.shields.io/github/license/MrSquigy/roomie)

This site manages schedules for different rooms.

## How to Run
0. Make sure you have [Python 3.9+](https://python.org/getit/)
1. Clone the repo
```
git clone https://github.com/MrSquigy/roomie
cd roomie
```
2. Setup the virtual environment
```
python -m venv .venv/roomie
.venv/roomie/Scripts/activate
python -m pip install -r requirements.txt
```
3. Perform database migrations
```
python manage.py migrate
```
4. Launch the Django dev server
```
python manage.py runserver
```
5. Visit roomie at http://localhost:8000