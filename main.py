from fastapi import FastAPI,Request
from fastapi.templating import Jinja2Templates

app = FastAPI()

templates = Jinja2Templates(directory="templates")

posts: list[dict] = [
    {
        "id": 1,
        "author": "Pruthvik Shetty",
        "title": "Getting Started with FastAPI",
        "content": "FastAPI is a modern, fast web framework for building APIs with Python.",
        "date_posted": "February 27, 2026"
    },
    {
        "id": 2,
        "author": "John Doe",
        "title": "Why Backend Development Matters",
        "content": "Backend development handles business logic, database interactions, and authentication.",
        "date_posted": "February 26, 2026"
    }
]

@app.get("/",include_in_schema=False)
@app.get("/posts",include_in_schema=False)
def home(request: Request):
    return templates.TemplateResponse(request,"home.html", {"posts":posts, "title":"Home"})

@app.get("/api/posts")
def get_posts():
    return posts