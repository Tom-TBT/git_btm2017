import os

client_filename = "clients.txt"
transaction_filename = "transactions.txt"

def add_client(client_name):
    with open(client_filename,'a') as file:
        file.write(client_name+"\n")
            
def add_transaction(debtor, creditor, amount):
    with open(transaction_filename,'a') as file:
        file.write(debtor+" "+creditor+" "+str(amount)+"\n")
        
def get_clients():
    list_clients = []
    with open(client_filename,'r') as file:
        for line in file:
            list_clients.append(line[0:-1])
    return list_clients

def get_transactions():
    transactions_list = []
    with open(transaction_filename,'r') as file:
        for line in file:
            transactions_list.append(line.split(" "))
        
    return transactions_list