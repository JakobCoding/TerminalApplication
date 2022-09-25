MAX_LINES = 3 #Global Constant - Slot Machine Terminal APP 
MAX_BET = 100
MIN_BET = 1

#Functions
def deposit(): #Deposit Function - Input - Loop(Bool) - Break  
    while True:
        amount = input("What would you like to deposit? $")
        if amount.isdigit(): 
            amount = int(amount)
            if amount > 0:
                break
            else:
                print("Amount must be greater that 0.")
        else: 
            print("Please enter a number.") 

    return amount


def get_number_of_lines(): 
    while True:
        lines = input("Enter the number of lines to bet on (1-" + str(MAX_LINES) + ")? ")
        if lines.isdigit(): 
            lines = int(lines)
            if 1 <= lines <= MAX_LINES:
                break
            else:
                print("Enter a valid number of lines.")
        else: 
            print("Please enter a number.") 

    return lines
    
def get_bet(): 
    while True:
        amount = input("What would you like to bet on each line? $")
        if amount.isdigit(): 
            amount = int(lines)
            if MIN_BET <= amount <= MAX_BET: 
                break
            else:
                print(f"Amount must be between ${MIN_BET} - ${MAX_BET}.")
        else: 
            print("Please enter a number.") 

    return amount

def main():
    balance = deposit()
    lines = get_number_of_lines()
    bet = get_bet
    print(balance, lines) 
    
main()
