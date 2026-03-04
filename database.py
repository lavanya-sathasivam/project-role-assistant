import sqlite3
DB="projects.db"
def init_db():
    conn=sqlite3.connect(DB)
    c=conn.cursor()
    c.execute("""CREATE TABLE IF NOT EXISTS users(
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        username TEXT UNIQUE,
        password TEXT
    )""")
    c.execute("""
    CREATE TABLE IF NOT EXISTS history(
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        username TEXT,
        project_name TEXT,
        result TEXT
    )
    """)
    conn.commit()
    conn.close()
def add_user(username,password):
    conn=sqlite3.connect(DB)
    c=conn.cursor()
    c.execute(
        "INSERT INTO users VALUES(NULL,?,?)",
        (username,password)
    )
    conn.commit()
    conn.close()
def login_user(username,password):
    conn=sqlite3.connect(DB)
    c=conn.cursor()
    c.execute(
        "SELECT * FROM users WHERE username=? AND password=?",
        (username,password)
    )
    data=c.fetchone()
    conn.close()
    return data
def save_history(username,project_name,result):
    conn=sqlite3.connect(DB)
    c=conn.cursor()
    c.execute(
        "INSERT INTO history VALUES(NULL,?,?,?)",
        (username,project_name,result)
    )
    conn.commit()
    conn.close()
def get_history(username):
    conn=sqlite3.connect(DB)
    c=conn.cursor()
    c.execute(
        "SELECT project_name,result FROM history WHERE username=?",
        (username,)
    )
    data=c.fetchall()
    conn.close()
    return data
