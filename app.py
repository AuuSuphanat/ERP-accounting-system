import os
import psycopg2
from flask import Flask, jsonify

app = Flask(__name__)

@app.get("/api/health")
def health():
    return jsonify({"status": "ok"})

@app.get("/api/db-test")
def db_test():
    try:
        db_url = os.environ["DATABASE_URL"]
        conn = psycopg2.connect(db_url)
        cur = conn.cursor()
        cur.execute("SELECT now();")
        t = cur.fetchone()[0]
        cur.close()
        conn.close()
        return jsonify({"db": "connected", "time": str(t)})
    except Exception as e:
        return jsonify({"db": "failed", "error": str(e)}), 500

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=int(os.environ.get("PORT", 5000)))
