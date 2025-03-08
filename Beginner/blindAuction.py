# DAY 9 FINAL PROJECT - BLIND AUCTION

# Print the logo
import art
art.tprint("BLIND AUCTION")

# Blind auction logic
end_auction = 'yes'
blind_auction = {}
winner = ""
while end_auction != 'no':

    name = input("What is your name?: ")
    bid = int(input("What is your bid?: €"))

    blind_auction[name]=bid
    
    for key in blind_auction:
        if winner in blind_auction:
            if blind_auction[key]<blind_auction[winner]:
                winner = key
        else:
            winner = name  # Save the winner in the first bid 

    end_auction = input("Are there any other bidders? Type 'yes' or 'no': ")
    if end_auction != 'yes' and end_auction!='no':
        end_auction='no'  # Exit the loop in case of invalid input
    
print(f"The winner is {winner} with a bid of €{blind_auction[winner]}")