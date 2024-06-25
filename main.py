no_of_service = int(input("No: of Service Types: "))
services = []
total_cost = 0

while no_of_service != 0:
    ask_service = input("Your Service: ").lower()
    services.append(ask_service)
    no_of_service -= 1

for service in services:
    if service == "bc":
        no_of_bc = int(input("No: of B/C: "))
        cost = no_of_bc * 2
        total_cost += cost
    elif service == "cc":
        no_of_cc = int(input("No: of C/C: "))
        cost = no_of_cc * 3
        total_cost += cost
    elif service == "bp":
        no_of_bp = int(input("No: of B/P: "))
        cost = no_of_bp * 3
        total_cost += cost
    elif service == "cp":
        no_of_cp = int(input("No: of C/P: "))
        cost = no_of_cp * 5
        total_cost += cost
    elif service == "pp":
        type_of_pp = input("46 or 34: ")
        if type_of_pp == '46':
            no_of_pp = int(input("No: of P/P 4-6: "))
            if no_of_pp % 3 == 0:
                cost = (no_of_pp // 3) * 20
                total_cost += cost
            else:
                cost = ((no_of_pp // 3) * 20) + ((no_of_pp % 3) * 10)
                total_cost += cost

        elif type_of_pp == '34':
            no_of_pp = int(input("No: of P/P 3-4: "))
            cost = ((no_of_pp // 4) * 20) + ((no_of_pp % 4) * 5)
            total_cost += cost
            
    elif service == "s":
        no_of_scan = int(input("No: of S: "))
        cost = no_of_scan * 3
        total_cost += cost

print(f"Total Cost is: {total_cost}")
