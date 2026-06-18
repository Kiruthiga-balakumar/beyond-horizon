from fastapi import FastAPI
from sqlalchemy import text
from app.database.connection import engine

print("LOADED BEYOND-HORIZON MAIN")

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
    
    
    
    
@app.get("/organizations")
def get_organizations():
    with engine.connect() as conn:
        result = conn.execute(
            text("SELECT * FROM organizations")
        )

        organizations = []

        for row in result:
            organizations.append({
                "id": row.id,
                "name": row.name,
                "type": row.type
            })

        return organizations   


@app.get("/health-metrics")
def get_health_metrics():
    with engine.connect() as conn:
        result = conn.execute(
            text("SELECT * FROM health_metrics")
        )

        metrics = []

        for row in result:
            metrics.append({
                "id": row.id,
                "user_id": row.user_id,
                "heart_rate": row.heart_rate,
                "steps": row.steps,
                "sleep_hours": float(row.sleep_hours)
            })

        return metrics
    

@app.get("/recommendations")
def get_recommendations():
    with engine.connect() as conn:
        result = conn.execute(
            text("SELECT * FROM recommendations")
        )

        recommendations = []

        for row in result:
            recommendations.append({
                "id": row.id,
                "user_id": row.user_id,
                "recommendation": row.recommendation_type
            })

        return recommendations    
    
@app.get("/appointments")
def get_appointments():
    with engine.connect() as conn:
        result = conn.execute(
            text("SELECT * FROM appointments")
        )

        appointments = []

        for row in result:
            appointments.append({
                "id": row.id,
                "user_id": row.user_id,
                "doctor_name": row.doctor_name,
                "appointment_date": str(row.appointment_date),
                "status": row.status,
                "notes": row.notes
                
            })

        return appointments 
    
@app.get("/feedback")
def get_feedback():
    with engine.connect() as conn:
        result = conn.execute(
            text("SELECT * FROM feedback")
        )

        feedbacks = []

        for row in result:
            feedbacks.append({
                "id": row.id,
                "user_id": row.user_id,
                "rating": row.rating,
                "comments": row.comments,
                "created_at": str(row.created_at)
            })

        return feedbacks    

@app.get("/notifications")
def get_notifications():
    with engine.connect() as conn:
        result = conn.execute(
            text("SELECT * FROM notifications")
        )

        notifications = []

        for row in result:
            notifications.append({
                "id": row.id,
                "user_id": row.user_id,
                "title": row.title,
                "message": row.message,
                "is_read": row.is_read,
                "created_at": str(row.created_at)
                
            })

        return notifications

@app.get("/chat-history")
def get_chat_history():
    with engine.connect() as conn:
        result = conn.execute(
            text("SELECT * FROM chat_history")
        )

        chats = []

        for row in result:
            chats.append({
                 "id": row.id,
                "user_id": row.user_id,
                "user_message": row.user_message,
                "bot_response": row.bot_response,
                "created_at": str(row.created_at)
                
            })

        return chats  

@app.get("/invite-codes")
def get_invite_codes():
    with engine.connect() as conn:
        result = conn.execute(
            text("SELECT * FROM invite_codes")
        )

        codes = []

        for row in result:
            codes.append({
                "id": row.id,
                "code": row.code,
                "organization_id": row.organization_id,
                "role": row.role,
                "is_active": row.is_active,
                "created_at": str(row.created_at)
                
            })

        return codes             