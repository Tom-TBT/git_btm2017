import functionalities as func

options = ["Say hi","Add client","Add transaction","Look at money"]

def show_options():
    index = 0
    for option in options:
        print(index,option)
        index += 1

def reception():
    print("Welcome to the BTM bank, what can we do for you today ?")
    show_options()
    
def wait_demand():
    still_waiting = True
    while still_waiting:
        demand = int(input("...Choose an option: "))
        still_waiting = demand > 0 and demand >= len(options)
    return demand
    
def action_dispatcher(demand):
    if demand == 0:
        func.say_hi()
    elif demand == 1:
        func.new_client()
    elif demand == 2:
        func.new_transaction()
    elif demand == 3:
        func.look_credit()
    
    
        
if __name__=="__main__":
   reception()
   demand = wait_demand()
   action_dispatcher(demand)
    
