import file_manager as fM

def say_hi():
    print("We need more clients like you !")

def new_client():
    new_client = input("...New client name: ")
    if not new_client in fM.get_clients():
        fM.add_client(new_client)
        print("Client added !")
    else:
        print("Client already exist !")
    
def new_transaction():
    client_list = fM.get_clients()
    print(client_list)
    debtor = input("Debtor name: ")
    creditor = input("Creditor name: ")
    if debtor not in client_list or creditor not in client_list:
        print("Unknown debtor or creditor")
        return
    amount = float(input("How much ?: "))
    fM.add_transaction(debtor,creditor,amount)
    
def look_credit():
    client_list = fM.get_clients()
    print(client_list)
    client_name = input("Who do you want to spy on?: ")
    if client_name not in client_list:
        print("Unknown client")
        return
    transactions = fM.get_transactions()
    solde = 0
    for transaction in transactions:
        if transaction[0] == client_name:
            solde -= float(transaction[2])
        elif transaction[1] == client_name:
            solde += float(transaction[2])
    print(client_name+" have "+str(solde)+" potatoes")