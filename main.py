from database import get_connection, create_table 

def main():
    conn = get_connection()
    create_table(conn)
    print('Database connected and table ready')
    
if __name__== "__main__":
    main()
