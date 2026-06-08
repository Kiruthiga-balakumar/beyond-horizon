from fastapi import FastAPI
from sqlalchemy import text
from app.database.connection import engine

app = FastAPI()

@app.get("/")
def home():
    return {"message": "GenTrack Backend Running"}

@app.get("/db-test")
def db_test():
    with engine.connect() as conn:
        conn.execute(text("SELECT 1"))
    return {"message": "Database Connected Successfully"}

@app.get("/users")
def get_users():
    with engine.connect() as conn:
        result = conn.execute(
            text("SELECT * FROM users")
        )

        users = []

        for row in result:
            users.append({
                "id": row.id,
                "name": row.full_name,
                "email": row.email,
                "role": row.role
            })

        return users