import os
import psycopg
from flask import Flask, jsonify

app = Flask(__name__)

@app.get("/api/health")
def health():
    return jsonify({"status": "ok"})

@app.get("/api/db-test")
def db_test():
    try:
        db_url = os.environ["DATABASE_URL"]
        with psycopg.connect(db_url) as conn:
            with conn.cursor() as cur:
                cur.execute("select 1;")
                x = cur.fetchone()[0]
        return jsonify({"db": "ok", "result": x})
    except Exception as e:
        return jsonify({"db": "failed", "error": str(e)}), 500
