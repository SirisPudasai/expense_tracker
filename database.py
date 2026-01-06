import sqlite3

def get_connection(db_name= "expenses.sqlite3"):
    conn = sqlite3.connect(db_name)
    return conn
    
def create_table(conn):
    cur = conn.cursor()
    create_table = """ 
     CREATE TABLE IF NOT EXISTS expenses (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        amount REAL NOT NULL,
        category TEXT NOT NULL,
        payment_method TEXT NOT NULL,
        description TEXT,
        expense_date DATE NOT NULL,
        created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
    );
    """
    cur.execute(create_table)
    conn.commit()
