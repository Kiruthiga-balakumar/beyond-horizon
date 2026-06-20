from fastapi import FastAPI,Body,HTTPException
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
    
@app.post("/appointments")
def create_appointment(data: dict = Body(...)):
    with engine.connect() as conn:
        conn.execute(
            text("""
                INSERT INTO appointments
                (user_id, doctor_name, appointment_date, status, notes)
                VALUES
                (:user_id, :doctor_name, :appointment_date, :status, :notes)
            """),
            {
                "user_id": data["user_id"],
                "doctor_name": data["doctor_name"],
                "appointment_date": data["appointment_date"],
                "status": data["status"],
                "notes": data["notes"]
            }
        )
        conn.commit()

    return {"message": "Appointment created successfully"}    

@app.post("/users")
def create_user(data: dict = Body(...)):
    try:
        with engine.connect() as conn:
            conn.execute(
                text("""
                    INSERT INTO users
                    (full_name, email, password, role, phone)
                    VALUES
                    (:full_name, :email, :password, :role, :phone)
                """),
                data
            )
            conn.commit()

        return {"message": "User created successfully"}

    except Exception:
        raise HTTPException(
            status_code=400,
            detail="Email already exists"
        )

@app.post("/organizations")
def create_organization(data: dict = Body(...)):
    with engine.connect() as conn:
        conn.execute(
            text("""
                INSERT INTO organizations
                (name, type)
                VALUES
                (:name, :type)
            """),
            {
                "name": data["name"],
                "type": data["type"]
            }
        )
        conn.commit()

    return {"message": "Organization created successfully"}

@app.post("/feedback")
def create_feedback(data: dict = Body(...)):
    with engine.connect() as conn:
        conn.execute(
            text("""
                INSERT INTO feedback
                (user_id, rating, comments)
                VALUES
                (:user_id, :rating, :comments)
            """),
            {
                "user_id": data["user_id"],
                "rating": data["rating"],
                "comments": data["comments"]
            }
        )
        conn.commit()

    return {"message": "Feedback added successfully"}

@app.post("/notifications")
def create_notification(data: dict = Body(...)):
    with engine.connect() as conn:
        conn.execute(
            text("""
                INSERT INTO notifications
                (user_id, title, message, is_read)
                VALUES
                (:user_id, :title, :message, :is_read)
            """),
            {
                "user_id": data["user_id"],
                "title": data["title"],
                "message": data["message"],
                "is_read": data["is_read"]
            }
        )
        conn.commit()

    return {"message": "Notification created successfully"}

@app.post("/register")
def register(data: dict = Body(...)):
    try:
        with engine.connect() as conn:
            conn.execute(
                text("""
                    INSERT INTO users
                    (full_name, email, password, role, phone)
                    VALUES
                    (:full_name, :email, :password, :role, :phone)
                """),
                {
                    "full_name": data["full_name"],
                    "email": data["email"],
                    "password": data["password"],
                    "role": data["role"],
                    "phone": data["phone"]
                }
            )
            conn.commit()

        return {"message": "Registration successful"}

    except Exception:
        raise HTTPException(
            status_code=400,
            detail="Email already exists"
        )
    
@app.post("/login")
def login(data: dict = Body(...)):
    with engine.connect() as conn:
        result = conn.execute(
            text("""
                SELECT * FROM users
                WHERE email = :email
                AND password = :password
            """),
            {
                "email": data["email"],
                "password": data["password"]
            }
        )

        user = result.fetchone()

        if user:
            return {
                "message": "Login successful",
                "user": {
                    "id": user.id,
                    "name": user.full_name,
                    "email": user.email,
                    "role": user.role
                }
            }

        raise HTTPException(
            status_code=401,
            detail="Invalid email or password"
        )    
    
@app.put("/appointments/{appointment_id}")
def update_appointment(appointment_id: int, data: dict = Body(...)):
    with engine.connect() as conn:
        conn.execute(
            text("""
                UPDATE appointments
                SET status = :status,
                    notes = :notes
                WHERE id = :id
            """),
            {
                "status": data["status"],
                "notes": data["notes"],
                "id": appointment_id
            }
        )
        conn.commit()

    return {"message": "Appointment updated successfully"}    

@app.put("/notifications/{notification_id}")
def update_notification(notification_id: int, data: dict = Body(...)):
    with engine.connect() as conn:
        conn.execute(
            text("""
                UPDATE notifications
                SET is_read = :is_read
                WHERE id = :id
            """),
            {
                "is_read": data["is_read"],
                "id": notification_id
            }
        )
        conn.commit()

    return {"message": "Notification updated successfully"}  

@app.delete("/appointments/{appointment_id}")
def delete_appointment(appointment_id: int):
    with engine.connect() as conn:
        conn.execute(
            text("""
                DELETE FROM appointments
                WHERE id = :id
            """),
            {"id": appointment_id}
        )
        conn.commit()

    return {"message": "Appointment deleted successfully"}   

@app.delete("/notifications/{notification_id}")
def delete_notification(notification_id: int):
    with engine.connect() as conn:
        conn.execute(
            text("""
                DELETE FROM notifications
                WHERE id = :id
            """),
            {"id": notification_id}
        )
        conn.commit()

    return {"message": "Notification deleted successfully"} 

@app.post("/chat")
def chat(data: dict = Body(...)):
    user_id = data["user_id"]
    user_message = data["message"]

    message = user_message.lower()

    if "sleep" in message:
        bot_response = "Try to sleep at least 7-8 hours daily for better recovery."
    elif "stress" in message:
        bot_response = "Take short breaks, hydrate, and practice deep breathing."
    elif "steps" in message:
        bot_response = "Aim for 8000-10000 steps daily."
    else:
        bot_response = "I am GenTrack AI. Please tell me about your health."

    with engine.connect() as conn:
        conn.execute(
            text("""
                INSERT INTO chat_history
                (user_id, user_message, bot_response)
                VALUES
                (:user_id, :user_message, :bot_response)
            """),
            {
                "user_id": user_id,
                "user_message": user_message,
                "bot_response": bot_response
            }
        )
        conn.commit()

    return {
        "user_message": user_message,
        "bot_response": bot_response
    }       
