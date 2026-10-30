# OnlineCourse Django project

This is a starter implementation for the OnlineCourse assignment. It includes the requested models, admin configuration, Bootstrap course details page, mock exam submission, and result page.

## Run on Windows

1. Install Python 3.10 or newer from https://www.python.org/downloads/ . During installation, tick **Add Python to PATH**.
2. Extract this ZIP file.
3. Open the extracted `OnlineCourse` folder in VS Code.
4. In VS Code choose **Terminal → New Terminal**, then run:

```powershell
py -m venv .venv
.venv\Scripts\activate
py -m pip install -r requirements.txt
py manage.py makemigrations course
py manage.py migrate
py manage.py createsuperuser
py manage.py runserver
```

5. Open http://127.0.0.1:8000/admin/ and sign in using the superuser you created.
6. Add a Course, then a Lesson, then Questions and their Choices. Mark exactly one choice per question as correct.
7. Open the course page at `http://127.0.0.1:8000/course/1/` (replace 1 with the course ID). Take the mock exam.

## Quick demo data

You can also create example content from the terminal after migrations:

```powershell
py manage.py shell
```

Paste:

```python
from course.models import Course, Lesson, Question, Choice
course, _ = Course.objects.get_or_create(name="Introduction to Python", defaults={"description": "A sample course for the OnlineCourse assignment."})
lesson, _ = Lesson.objects.get_or_create(course=course, title="Python Basics", defaults={"content": "Learn variables, data types, and basic Python syntax.", "order": 1})
q1, _ = Question.objects.get_or_create(lesson=lesson, text="Which keyword defines a function in Python?")
if not q1.choices.exists():
    Choice.objects.create(question=q1, text="func", is_correct=False)
    Choice.objects.create(question=q1, text="def", is_correct=True)
    Choice.objects.create(question=q1, text="function", is_correct=False)
q2, _ = Question.objects.get_or_create(lesson=lesson, text="Which data type stores a sequence of characters?")
if not q2.choices.exists():
    Choice.objects.create(question=q2, text="int", is_correct=False)
    Choice.objects.create(question=q2, text="str", is_correct=True)
    Choice.objects.create(question=q2, text="bool", is_correct=False)
print("Demo course created. Exit with exit()")
```

Then open `http://127.0.0.1:8000/course/1/` (or use the course ID printed by `Course.objects.get(name="Introduction to Python").id`).

## Assignment screenshots

- `03-admin-site.png`: sign in to `/admin/`. Capture the Django Admin index showing both **Authentication and Authorization** and **OnlineCourse**. The OnlineCourse section appears after migrations and registration.
- `07-final.png`: take the demo exam and select `def` and `str`. The result page should show the Congratulations message, score `2 / 2`, and `100%`.

Do not submit placeholder or fabricated screenshots: capture them from your running application.

## GitHub upload

Create a new public repository on GitHub, then upload the extracted project files. The requested file links will look like:

- `https://github.com/YOUR-USERNAME/YOUR-REPOSITORY/blob/main/course/models.py`
- `https://github.com/YOUR-USERNAME/YOUR-REPOSITORY/blob/main/course/admin.py`
- `https://github.com/YOUR-USERNAME/YOUR-REPOSITORY/blob/main/course/templates/course/course_details_bootstrap.html`
- `https://github.com/YOUR-USERNAME/YOUR-REPOSITORY/blob/main/course/views.py`
- `https://github.com/YOUR-USERNAME/YOUR-REPOSITORY/blob/main/course/urls.py`

Replace the username and repository name with your own. Do not upload `.venv/`, `db.sqlite3`, or passwords.
