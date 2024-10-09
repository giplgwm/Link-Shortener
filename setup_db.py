import sqlite3

conn = sqlite3.connect("shortener.db")
conn.execute("""
CREATE TABLE urls (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    original_url TEXT NOT NULL,
    short_code TEXT NOT NULL UNIQUE,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);    
""")
conn.close()
print("Database setup completed.")