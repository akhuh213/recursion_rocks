# You will have to figure out what parameters to include
# 🚨 All functions must use recursion 🚨`

# This function returns an array of all possible outcomes from flipping a coin N times.
# Input type: Integer 
# H stands for Heads and T stands for tails
# Represent the two outcomes of each flip as "H" or "T"
coin = ["H","T"]
second_coin = ["H","T"]

def coin_flips(n, result =[]):
    if n <= 0 :       
        return result
    for i in coin:
        for j in second_coin:
            result.append(i+j)

    return(coin_flips(n-1,result))


print(coin_flips(5))
    # Write code here
    

# print(coinFlips(2)) 
# => ["HH", "HT", "TH", "TT"]