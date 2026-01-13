from database import get_connection, create_table
import calendar ,csv,matplotlib.pyplot as plt
from queries import (
    add_expense,
    get_all_expenses,
    update_expenses,
    delete_expenses,
    get_monthly_total,
    get_yearly_total,
    get_category_breakdown
)

def show_menu():
    print("\n=== Expense Tracker ===")
    print("1. Add Expense")
    print("2. View All Expenses")
    print("3. Update Expense")
    print("4. Delete Expense")
    print("5. Yearly Summary Report")
    print("6. Monthly report")
    print("7. Export yearly report to CSV")
    print("8. Plot category-wise expenses")
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
            year=input('Enter Year:')
            tot_amt=get_yearly_total(conn,year)
            rows=get_category_breakdown(conn,year)
            print(f'YEARLY EXPENSE REPORT({year}) ')
            print('-------------------------------')
            print(f'Total Expense:{tot_amt}'  )
            print('\n')
            print('Category Breakdown:')
            for category,amount in rows:
                print(f'{category:<15}: {amount}') # '<' → left-align , 15 -> min width i.e 15 character wide
        elif choice == "6":
            year=input('Enter Year:')
            month=input('Enter month:').zfill(2)
            total=get_monthly_total(conn,year,month)
            rows=get_category_breakdown(conn,year,month)
            month_name = calendar.month_name[int(month)]
            print(f'Monthly Report : {month_name} {year}')
            print(f'Monthly total: {total}')
            print('Category Breakdown:')
            for category,amount in rows:
                print(f'{category:<15}: {amount}')
        elif choice == "7":
            year=input('Enter year:')
            rows=get_category_breakdown(conn,year)
            if not rows:
                print('No data available for this year')
            else:
                filename=f'expense_report_{year}.csv'
                
                with open(filename,'w',newline="",encoding='utf-8') as f:
                     writer=csv.writer(f)
                     writer.writerow(['year','category','Total_amount'])
                     for category,amount in rows:
                         writer.writerow([year,category,amount])
                         
                print(f"Report exported successfully to {filename}")
            
        elif choice == "8":
            import matplotlib.pyplot as plt
            import csv
            year=input('Enter year:')
            filename =f'expense_report_{year}.csv'
            categories=[]
            amounts=[]
            with open(filename,'r',encoding='utf-8') as f:
                reader=csv.reader(f)
                next(reader)
                for _,category,amount in reader:
                    categories.append(category)
                    amounts.append(float(amount))
            
            plt.bar(categories,amounts)
            plt.xlabel('Categories')
            plt.ylabel('Amount')
            plt.title(f'Expense_report {year}')
            plt.show()
            
            
            
        elif choice == "0":
            print("Goodbye 👋")
            break

        else:
            print("Invalid choice ❌")

    conn.close()

if __name__ == "__main__":
    main()
