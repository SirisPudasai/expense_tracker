from database import get_connection
conn = get_connection()
def add_expense(conn,amount,category,payment_method,description,expense_date):
    insert_query = """
    INSERT INTO expenses (amount,category,payment_method,description,expense_date)
    VALUES
    (?,?,?,?,?);
    """
    cur=conn.cursor()
    cur.execute(insert_query,(amount,category,payment_method,description,expense_date))
    conn.commit()
def get_all_expenses(conn):
      cur=conn.cursor()
      sql="""
      select * from expenses """
      cur.execute(sql)
      rows=cur.fetchall()
      return rows