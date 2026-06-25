# Sentiment Dashboard API

A REST API built with FastAPI, async SQLAlchemy, JWT authentication,
and automatic sentiment analysis using HuggingFace DistilBERT.

**Live URL:** https://fastapi-intern-projects.onrender.com

---

## Setup

\`\`\`bash
git clone https://github.com/Safana14/fastapi-intern-projects.git
cd fastapi-intern-projects/Day_19
python -m venv venv
venv\Scripts\activate
pip install -r requirements.txt
cp .env.example .env
uvicorn app.main:app --reload
\`\`\`

## Environment Variables

| Variable | Description | Default |
|---|---|---|
| DATABASE_URL | PostgreSQL connection string | - |
| SECRET_KEY | JWT signing secret (min 32 chars) | - |
| ALGORITHM | JWT algorithm | HS256 |
| ACCESS_TOKEN_EXPIRE_MINUTES | Token lifetime in minutes | 30 |

## API Endpoints

| Method | Endpoint | Auth | Description |
|---|---|---|---|
| POST | /auth/register | No | Register new user |
| POST | /auth/login | No | Login, get JWT token |
| POST | /entries/ | Yes | Create entry with auto sentiment |
| GET | /entries/ | No | List all entries |
| GET | /entries/{id} | No | Get entry by ID |
| PUT | /entries/{id} | No | Update entry |
| DELETE | /entries/{id} | No | Delete entry |
| GET | /reports/summary | Yes | Sentiment summary report |
| GET | /reports/trend | Yes | Sentiment trend report |

## Running Tests

\`\`\`bash
pytest -v
\`\`\`