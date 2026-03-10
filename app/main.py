from fastapi import FastAPI
import psycopg2
import os

app = FastAPI()

@app.get("/api/health")
def health():
    return {"status": "ok"}

@app.get("/api/db-check")
def db_check():
    conn = psycopg2.connect(
        dbname=os.getenv("POSTGRES_DB"),
        user=os.getenv("POSTGRES_USER"),
        password=os.getenv("POSTGRES_PASSWORD"),
        host="db"
    )

    cur = conn.cursor()
    cur.execute("SELECT version();")
    version = cur.fetchone()

    return {"postgres_version": version}
