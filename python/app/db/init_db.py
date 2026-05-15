import sqlite3
import pugsql
from pathlib import Path

queries = pugsql.module(str(Path(__file__).parent / "queries"))

def init_db(db_path: str = "links.db"):
    conn = sqlite3.connect(db_path)
    conn.execute("""
        CREATE TABLE IF NOT EXISTS links (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            url TEXT NOT NULL,
            slug TEXT NOT NULL UNIQUE,
            created_at INTEGER NOT NULL DEFAULT (strftime('%s', 'now')),
            created_by TEXT NOT NULL,
            clicks INTEGER NOT NULL DEFAULT 0
        )
    """)
    conn.commit()
    conn.close()

    queries.connect(f"sqlite:///{db_path}")