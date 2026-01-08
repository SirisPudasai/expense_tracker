from database import get_connection
conn = get_connection()
def add_expense(conn,amount,category,payment_method,description,expense_date):
    insert_query = """
    INSERT INTO expenses (amount,category,payment_method,description,expense_date)
    VALUES
    (?,?,?,?,?);
    """
    cur=conn.cursor()
    cur.execute(insert_query,(amount,category,payment_method,description,expense_date,))
    conn.commit()
    
def get_all_expenses(conn):
      cur=conn.cursor()
      sql="""
      select * from expenses """
      cur.execute(sql)
      rows=cur.fetchall()
      return rows
  
def update_expenses(conn,expense_id,amount,category,payment_method,description,expense_date):
    sql="""
    UPDATE expenses 
    SET amount = ? ,category = ? ,payment_method = ?,description = ?,expense_date = ?
    WHERE id = ? 
    """
    cur=conn.cursor()
    cur.execute(sql,(amount,category,payment_method,description,expense_date,expense_id,))
    conn.commit()
    
def delete_expenses(conn,expense_id):
    sql="""
    DELETE FROM expenses
    WHERE id = ?
    """
    cur=conn.cursor()
    cur.execute(sql,(expense_id,))
    conn.commit()
    
def get_monthly_total(conn,year,month):
    sql="""
    SELECT SUM(amount) FROM expenses 
    WHERE strftime('%Y',expense_date) = ?
    AND strftime('%m',expense_date) = ?
    """
    cur=conn.cursor()
    cur.execute(sql,(year,month,))
    row=cur.fetchone()
    return row[0]  if row[0] is not None else 0  

def get_yearly_total(conn,year):
    sql="""
    SELECT SUM(amount)
    FROM expenses WHERE strftime('%Y',expense_date) = ?
    """
    cur=conn.cursor()
    cur.execute(sql,(year,))
    row=cur.fetchone()
    return row[0] if row[0] is not None else 0

def get_category_breakdown(conn,year,month=None): #Return total expenses per category, filtered by year, optionally by month
    sql="""
    SELECT category, SUM(amount) FROM expenses
    WHERE strftime('%Y',expense_date) = ?
    
    """
    cur=conn.cursor()
    params = [year]
    if month:   
        sql += " AND strftime('%m', expense_date) = ?"
        params.append(month)
    sql += " GROUP BY category ORDER BY SUM(amount) DESC"
    cur.execute(sql,tuple(params))
    rows=cur.fetchall()
    return rows
     
