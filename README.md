# HNG 12 Stage Zero
Description: This project is to return user data i.e Email, current date and time, github repo url.

# Back Link for Python
https://hng.tech/hire/python-developers

## Setup

1. Clone the repo.
 ```sh
 git clone "<repo_url>"
```

2. Create a virtual environment.
 ```bash
    python3 -m venv .venv
 ```

3. Activate virtual environment.
```bash
    source /path/to/venv/bin/activate`
```

4. Install project dependencies `pip install -r requirements.txt`

5. Create your own branch.
 ```sh
 git branch <branch-name>
```

6. Pull from origin/main branch.
 ```sh
 git fetch origin main
 git merge origin/main

```

7. Make makemigrations.
 ```sh
 python manage.py makemigrations
```

8. Migrate.
 ```sh
 python manage.py migrate
```

9. Runserver.
 ```sh
 python manage.py runserver
```


# API Documentation

## Overview
The `UserData` API provides user details, including email, the current datetime, and a GitHub repo URL.

## Base URL
http://127.0.0.1:8000

## Endpoints

### 1. Get User Data
**Endpoint: GET /api/v1/data**  

**Description:**  
Retrieves user data including:
- Email
- Current datetime (ISO 8601 format)
- GitHub repo URL

**Response Format:**
- **Status Code:** `200 OK`
- **Content-Type:** `application/json`

#### Example Request
```bash
curl -X GET http://127.0.0.1:8000/api/v1/data
```

### Example Response
```bash
{
    "email": "offsideint@gmail.com",
    "current_datetime": "2025-01-29T12:34:56.789123Z",
    "github_url": "https://github.com/0FFSIDE1/stage0"
}
```











