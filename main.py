from database import get_connection, create_table
from queries import (
    add_expense,
    get_all_expenses,
    update_expenses,
    delete_expenses,
    get_monthly_total,
    get_category_breakdown
)

def show_menu():
    print("\n=== Expense Tracker ===")
    print("1. Add Expense")
    print("2. View All Expenses")
    print("3. Update Expense")
    print("4. Delete Expense")
    print("5. Category-wise Breakdown")
    print("0. Exit")

def main():
    conn = get_connection()
    create_table(conn)

    while True:
        show_menu()
        choice = input("Choose an option: ")

        if choice == "1":
            try:
                amount = float(input('Amount:'))
                category = input('Category:')
                payment_method = input('Payment_method:')
                description = input('Description:')
                expense_date = input('Expense date (YYYY-MM-DD):')
                
                add_expense(conn,amount,category,payment_method,description,expense_date)
                
                print('Expense added successfully')
                
            except ValueError:
                print('Invalid amount. Please enter a number.')

        elif choice == "2":
            rows = get_all_expenses(conn)
            if not rows:
                print('No expense found')
            else:
                for row in rows:
                    print(f'ID:{row[0]} \t AMOUNT:{row[1]} \t CATEGORY:{row[2]} \t PAY_METHOD:{row[3]} \t DESCRIPTION:{row[4]} \t DATE: {row[5]} ')
                
    

        elif choice == "3":
            try:
                id=int(input('Enter ID for update:'))
                amount=float(input('Enter Amount:'))
                category = input('Enter Category:')
                payment_method= input('Enter Pay_method:')
                description = input('Enter Description:')
                expense_date = input('Enter Date(YYYY-MM-DD):')
                update_expenses(conn,id,amount,category,payment_method,description,expense_date)
                print('Expense Updated successfully')
            except ValueError:
                print('Invalid Input')
            

        elif choice == "4":
            id=int(input('Enter ID for deletion :'))
            delete_expenses(conn,id)
            print('Expense Deleted successfully')
            

        elif choice == "5":
            print("Category breakdown selected")

        elif choice == "0":
            print("Goodbye 👋")
            break

        else:
            print("Invalid choice ❌")

    conn.close()

if __name__ == "__main__":
    main()
