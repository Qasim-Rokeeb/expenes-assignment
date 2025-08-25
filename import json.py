import json
import os
from datetime import datetime

class SimpleFinanceTracker:
    def __init__(self):
        self.data_file = 'transactions.json'
        self.transactions = self.load_data()
    
    def load_data(self):
        """Load transactions from file"""
        if os.path.exists(self.data_file):
            try:
                with open(self.data_file, 'r') as f:
                    return json.load(f)
            except:
                return []
        return []
    
    def save_data(self):
        """Save transactions to file"""
        with open(self.data_file, 'w') as f:
            json.dump(self.transactions, f, indent=2)
    
    def add_income(self, amount, description):
        """Add an income entry"""
        transaction = {
            'type': 'Income',
            'amount': amount,
            'description': description,
            'date': datetime.now().strftime('%Y-%m-%d'),
            'time': datetime.now().strftime('%H:%M:%S')
        }
        self.transactions.append(transaction)
        self.save_data()
        print(f"✓ Income of ${amount:.2f} added successfully!")
    
    def add_expense(self, amount, description):
        """Add an expense entry"""
        transaction = {
            'type': 'Expense',
            'amount': amount,
            'description': description,
            'date': datetime.now().strftime('%Y-%m-%d'),
            'time': datetime.now().strftime('%H:%M:%S')
        }
        self.transactions.append(transaction)
        self.save_data()
        print(f"✓ Expense of ${amount:.2f} added successfully!")
    
    def view_transactions(self):
        """Display all transactions"""
        if not self.transactions:
            print("\nNo transactions found.")
            return
        
        print("\n" + "="*60)
        print("                    ALL TRANSACTIONS")
        print("="*60)
        print(f"{'Date':<12} {'Type':<8} {'Amount':<10} {'Description'}")
        print("-"*60)
        
        for transaction in self.transactions:
            print(f"{transaction['date']:<12} {transaction['type']:<8} "
                  f"${transaction['amount']:<9.2f} {transaction['description']}")
    
    def view_balance(self):
        """Show current balance and summary"""
        total_income = sum(t['amount'] for t in self.transactions if t['type'] == 'Income')
        total_expenses = sum(t['amount'] for t in self.transactions if t['type'] == 'Expense')
        balance = total_income - total_expenses
        
        print("\n" + "="*40)
        print("            FINANCIAL SUMMARY")
        print("="*40)
        print(f"Total Income:   ${total_income:.2f}")
        print(f"Total Expenses: ${total_expenses:.2f}")
        print("-"*40)
        print(f"Current Balance: ${balance:.2f}")
        
        if balance > 0:
            print("Status: You're saving money! 😊")
        elif balance < 0:
            print("Status: You're spending more than earning! ⚠️")
        else:
            print("Status: Breaking even.")
    
    def clear_all_data(self):
        """Clear all transactions"""
        confirm = input("Are you sure you want to delete all data? (yes/no): ")
        if confirm.lower() == 'yes':
            self.transactions = []
            self.save_data()
            print("✓ All data cleared!")
        else:
            print("Operation cancelled.")

def show_menu():
    """Display the main menu"""
    print("\n" + "="*40)
    print("    SIMPLE FINANCE TRACKER")
    print("="*40)
    print("1. Add Income")
    print("2. Add Expense")
    print("3. View All Transactions")
    print("4. View Balance Summary")
    print("5. Clear All Data")
    print("6. Exit")
    print("="*40)

def get_amount():
    """Get amount input from user"""
    while True:
        try:
            amount = float(input("Enter amount: $"))
            if amount <= 0:
                print("Please enter a positive amount.")
                continue
            return amount
        except ValueError:
            print("Please enter a valid number.")

def main():
    """Main program loop"""
    tracker = SimpleFinanceTracker()
    
    print("Welcome to Simple Finance Tracker!")
    
    while True:
        show_menu()
        choice = input("Choose an option (1-6): ")
        
        if choice == '1':
            print("\n--- ADD INCOME ---")
            amount = get_amount()
            description = input("Enter description: ")
            tracker.add_income(amount, description)
        
        elif choice == '2':
            print("\n--- ADD EXPENSE ---")
            amount = get_amount()
            description = input("Enter description: ")
            tracker.add_expense(amount, description)
        
        elif choice == '3':
            tracker.view_transactions()
        
        elif choice == '4':
            tracker.view_balance()
        
        elif choice == '5':
            tracker.clear_all_data()
        
        elif choice == '6':
            print("\nThank you for using Simple Finance Tracker!")
            print("Your data has been saved automatically.")
            break
        
        else:
            print("Invalid choice. Please select 1-6.")

if __name__ == "__main__":
    main()