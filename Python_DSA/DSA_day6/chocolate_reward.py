child_id = (10,20,30,40,50)
chocolates_received=[12,5,3,4,6]

def calculate_total_chocolates():
    return sum(chocolates_received)

def reward_child(child_id_rewarded,extra_chocolates):
    if(extra_chocolates < 1):
        print("Extra chocolates is less than 1")

    elif(child_id_rewarded not in child_id):
        print("Invalid child id")
    else:
        ind = child_id.index(child_id_rewarded)
        chocolates_received[ind] += extra_chocolates


print(calculate_total_chocolates())
reward_child(20,3)
print(calculate_total_chocolates())