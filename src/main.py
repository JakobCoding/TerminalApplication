import random #Import (random) python module - Allows program to select random symbols when called

MAX_LINES = 3 #Python Global Constants 
MAX_BET = 100
MIN_BET = 1

ROWS = 3 #specifies number of rows and colums in the slot machine
COLS = 3

symbol_count = {  #specifies amount of symbols and values / these are provided in a dictionary {} 
    "A": 2, # A = Most valuable with only 2 A's in the column 
    "B": 4,
    "C": 6,
    "D": 8  # D = Least valuable with 8 D's in the column 
}
#Not a very balanced slot machine Just trying to make something that works
symbol_value = {
    "A": 5,   #symbol values self explanitory A = 5 
    "B": 4,
    "C": 3,
    "D": 2    #symbol values D = 2 
}


def check_winnings(columns, lines, bet, values):
    winnings = 0 
    winning_lines = []
    for line in range(lines):
        symbol = columns[0][line]
        for column in columns:
            symbol_to_check = column[line]
            if symbol != symbol_to_check:
                break
        else: 
            winnings += values[symbol] * bet
            winning_lines.append(line + 1)

    return winnings, winning_lines

def get_slot_machine_spin(rows, cols, symbols): #three parameters that are passed to this function 
    all_symbols = [] #create list to contain all the symbols that could possibly randomly choose from 
    for symbol, symbol_count in symbols.items(): #for loop which adds how ever many symbols we have above into the all_symbols list
        for _ in range(symbol_count):            #.items gives the key and the value associated with a dictionary  
            all_symbols.append(symbol) 

    columns = [] #define column list
    for _ in range(cols): #generate a column for every column we have in this case 3 columns 
        column = []
        current_symbols = all_symbols[:] # [:] = copy of a list and all symbols  
        for _ in range(rows): #loop through the number of values that need to be generated that is equal to the number of rows in the slot machine,
            value = random.choice(current_symbols) # random choice from imported random module 
            current_symbols.remove(value) #removing symbols from list as to not get repeated results in slot machine spins per game 
            column.append(value) #add value to column list 

        columns.append(column)

    return columns

def print_slot_machine(columns): #transposing columns so they display correctly upright on the screen instead of left to right like a row 
    for row in range(len(columns[0])): 
        for i, column in enumerate(columns):
            if i != len(columns) - 1: #maximum index we have to access an element in the columns list is 2
                print(column[row], end=" | ") #pipe operater provides some seperation between results 
            else:
                print (column[row], end="")

        print()



def deposit(): #(Deposit Function) Collects User Input - 
    while True: #While loop continually asks the user for a deposit amount until they provide a valid amount
        amount = input("What would you like to deposit? $") #request user input
        if amount.isdigit(): #isdigit string method checks if the input is a valid whole number 
            amount = int(amount) #converts above string input to numeric value
            if amount > 0: #checks if the number is greater than zero
                break #if number is greater than zero break out of while loop 
            else:
                print("Amount must be greater that 0.") #error handling if user input is not greater than zero 
        else: 
            print("Please enter a number.") #error handling is user input is not a number 

    return amount 


def get_number_of_lines(): 
    while True:
        lines = input(
            "Enter the number of lines you would like to bet on (1-" + str(MAX_LINES) + ")? ")
        if lines.isdigit(): 
            lines = int(lines)
            if 1 <= lines <= MAX_LINES: #check if value is inbetween two values 
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
            amount = int(amount)
            if MIN_BET <= amount <= MAX_BET: 
                break
            else:
                print(f"Amount must be between ${MIN_BET} - ${MAX_BET}.") #f string allows variables to be inserted inside of a string
        else: 
            print("Please enter a number.") 

    return amount



def spin(balance):
    lines = get_number_of_lines()
    while True:
        bet = get_bet()
        total_bet = bet * lines

        if total_bet > balance:
            print(
                f"You do not have enough to bet that amount, your current balance is: ${balance}")
        else:
            break    

    print(
        f"You are betting ${bet} on {lines} lines. Total bet is equal to: ${total_bet}")

    slots = get_slot_machine_spin(ROWS, COLS, symbol_count)  
    print_slot_machine(slots)
    winnings, winning_lines = check_winnings(slots, lines, bet, symbol_value)
    print(f"You won ${winnings}.")
    print(f"You won on lines:", *winning_lines)
    return winnings - total_bet

def main():
    balance = deposit()
    while True:
        print(f"Current balance is ${balance}")
        answer = input("Press enter to play (q to quit).")
        if answer == "q":
            break
        balance += spin(balance)

    print(f"You left with ${balance}")
  
main()

