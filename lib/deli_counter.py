katz_deli =[]

def line(katz_deli):
    if not katz_deli:
        print("The line is currently empty.") 
    else:
        line_status = "The line is currently:"
        for i in range(len(katz_deli)):
            line_status += f" {i+1}. {katz_deli[i]}"
        print(line_status)

def take_a_number(katz_deli, customer_name):
    katz_deli.append(customer_name)
    print(f"Welcome, {customer_name}. You are number {len(katz_deli)} in line.")

def now_serving(katz_deli):
    if not katz_deli: 
        print("There is nobody waiting to be served!")
    else: 
        print(f"Currently serving {katz_deli[0]}.")
        del katz_deli[0]