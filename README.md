# Student Resource Hub API

A RESTful API backend for a platform where Nigerian university students and lecturers can upload, discover, and download study materials — past questions, lecture notes, textbooks, and summaries — organized by department, course, and level.

## Problem

Nigerian university students have no structured, searchable place to find course materials. Everything lives in scattered WhatsApp groups and Telegram channels. Materials get lost, repeated every year, never organized.

This app solves that.

## Features

- **Authentication** — JWT-based register, login, and token refresh
- **Role-based users** — Student, Lecturer, and Admin roles
- **Resource upload** — Upload study materials with file, title, description, and category
- **Categories** — Hierarchical organization by faculty, department, and level
- **Tagging** — Freeform tags on resources for flexible discovery
- **Search** — Search resources by title, description, tag, or category
- **Ratings** — 1–5 star ratings per resource, one per user
- **Threaded comments** — Nested comment threads on any resource
- **Notifications** — Auto-notify uploaders when their resource is rated or commented on
- **Download tracking** — Track download count per resource
- **Ownership permissions** — Only the uploader can edit or delete their resource

## Design Patterns Used

| Pattern | Where |
|---|---|
| Observer | Signals auto-create notifications on rating/comment |
| Strategy | Pluggable search filter via DRF `filter_backends` |
| Factory | `Resource.create_resource()` controls creation by type |
| Repository | `ResourceDownloadView` isolates download logic |
| Decorator | `IsOwnerOrReadOnly` wraps views with ownership check |
| Template Method | `get_object` override in `ProfileView` |

## Tech Stack

- **Language** — Python
- **Framework** — Django + Django REST Framework
- **Database** — db.sqlite3(psql later)
- **Auth** — JWT via `djangorestframework-simplejwt`
- **Deployment** — Render
- **File Storage** — Local (Render disk / upgradeable to S3)

- **live project url** -- https://student-resource-hub-qx57..onrender.com/api/accounts/register/

## Project Structure

student-resource-hub/
├── core/               # Project settings and root URLs
├── accounts/           # Custom user model, auth endpoints
├── resources/          # Categories, resources, tags, search
├── interactions/       # Ratings, comments, notifications
├── manage.py
├── requirements.txt
├── build.sh
└── Procfile

## API Endpoints

### Accounts
| Method | Endpoint | Description |
|---|---|---|
| POST | `/api/accounts/register/` | Register a new user |
| POST | `/api/accounts/login/` | Login and get JWT tokens |
| POST | `/api/accounts/token/refresh/` | Refresh access token |
| GET/PATCH | `/api/accounts/profile/` | View or update your profile |

- **live accounts project url** -- https://student-resource-hub-qx57..onrender.com/api/accounts/register/

### Resources
| Method | Endpoint | Description |
|---|---|---|
| GET/POST | `/api/resources/categories/` | List or create categories |
| GET/POST | `/api/resources/resources/` | List or upload a resource |
| GET/PATCH/DELETE | `/api/resources/resources/<id>/` | Retrieve, update, or delete a resource |
| GET | `/api/resources/resources/<id>/download/` | Download a resource |
| GET/POST | `/api/resources/tags/` | List or create tags |
| GET | `/api/resources/search/?search=<query>` | Search resources |

- **live  resources project url** -- https://student-resource-hub-qx57..onrender.com/api/resources/resources/pk/download/

### Interactions
| Method | Endpoint | Description |
|---|---|---|
| POST | `/api/interactions/ratings/` | Rate a resource |
| GET/POST | `/api/interactions/comments/` | List or post a comment |
| GET | `/api/interactions/notifications/` | View your notifications |

## Setup & Installation

```bash
# Clone the repo
git clone https://github.com/Houzsaad/student-resource-hub.git
cd student-resource-hub

# Create and activate virtual environment
python -m venv venv
venv\Scripts\activate  # Windows
source venv/bin/activate  # Mac/Linux

# Install dependencies
pip install -r requirements.txt

# Create .env file
SECRET_KEY=your-secret-key
DEBUG=True
DATABASE_URL=your-database-url

# Run migrations
python manage.py migrate

# Create superuser
python manage.py createsuperuser

# Start server
python manage.py runserver
```

## Environment Variables

| Variable | Description |
|---|---|
| `SECRET_KEY` | Django secret key |
| `DEBUG` | `True` for development, `False` for production |
| `DATABASE_URL` | PostgreSQL connection string |

## Author

**Huzaifa** — Self-taught backend developer  
GitHub: [Houzsaad](https://github.com/Houzsaad)  
Fiverr: [fiverr.com/s/Q78QpXP](https://fiverr.com/s/Q78QpXP)