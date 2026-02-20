from database import engine
from sqlalchemy import text

try:
    with engine.connect() as conn:
        print("Connected to PostgreSQL successfully!")
        db = conn.execute(text("SELECT current_database();")).fetchone()[0]
        print("Current database:", db)

except Exception as e:
    print("Failed to connect:", e)
