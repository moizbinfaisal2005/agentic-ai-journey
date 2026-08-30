"""
All the database work lives here (Lesson 12).

Keeping the database code in its own file makes app.py shorter and easier to
read. app.py just imports these functions and uses them.
"""

import sqlite3

DB_FILE = "feedback.db"

def init_db():
    """Create the feedback table the first time we run."""
    conn = sqlite3.connect(DB_FILE)
    conn.execute("""
        CREATE TABLE IF NOT EXISTS feedback (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            review TEXT,
            label TEXT,
            score INTEGER,
            theme TEXT
        )
    """)
    conn.commit()
    conn.close()

def save_results(results):
    """Write all analyzed reviews into the database."""
    conn = sqlite3.connect(DB_FILE)
    for r in results:
        conn.execute(
            "INSERT INTO feedback (review, label, score, theme) VALUES (?, ?, ?, ?)",
            (r.get("review", ""), r.get("label", ""), r.get("score", 0), r.get("theme", "")),
        )
    conn.commit()
    conn.close()

def load_history(order_by="id DESC"):
    """Read every review we have saved so far, ordered by newest first."""
    conn = sqlite3.connect(DB_FILE)
    rows = conn.execute(
        f"SELECT review, label, score, theme FROM feedback ORDER BY {order_by}"
    ).fetchall()
    conn.close()
    # Return as list of dicts for easier use in Streamlit
    return [
        {"review": r[0], "label": r[1], "score": r[2], "theme": r[3]}
        for r in rows
    ]
