# BlackJack
import random
cards = [11,1,2,3,4,5,6,7,8,9,10,10,10,10]
bet = [5,10,100,200,500,1000]
print("Welcome to BlackJack Game!")
print("Available options to bet: $5,$10,$100,$200,$500,$1000")
initial_bet = int(input("Enter the bet you want to place: $"))
if initial_bet in bet:
    print(f"Initial bet placed by the Player: ${initial_bet}")
else:
    print("Enter a valid amount from the available options")
    exit()
print("Game begins!")
player_draw1 = random.choice(cards)
player_draw2 = random.choice(cards)
print(f"Player draw: {player_draw1},{player_draw2}")
total_player_draw = player_draw1 + player_draw2
end_of_game = False
if total_player_draw == 21:
    print("BlackJack! You won.")
    exit()
else:
    dealer_draw1 = random.choice(cards)
    dealer_draw2 = random.choice(cards)
    total_dealer_draw = dealer_draw1 + dealer_draw2
    print(f"Dealer draw: {dealer_draw1},X (The second draw is masked)")
    while not end_of_game:
        options = ["Hit", "Stand"]
        option = input("Select your options. Type 'Hit' or 'Stand'.").title()
        if option == options[0]:
            player_draw3 = random.choice(cards)
            total_player_draw += player_draw3
            if total_player_draw > 21:
                print(f"New Player draw: {player_draw1},{player_draw2},{player_draw3}")
                print("You lose. Dealer won")
                end_of_game = True
            else:
                print(f"Player draw: {player_draw1},{player_draw2},{player_draw3}")
            player_draw4 = random.choice(cards)
            total_player_draw += player_draw4
            if total_player_draw > 21:
                print(f"New Player draw: {player_draw1},{player_draw2},{player_draw3},{player_draw4}")
                print("You lose. Dealer won")
                end_of_game = True
            else:
                print(f"New Player draw: {player_draw1},{player_draw2},{player_draw3},{player_draw4}")
        elif option == options[1]:
            print(f"Dealer draw: {dealer_draw1},{dealer_draw2}")
            if total_dealer_draw == 21:
                print("BlackJack! Dealer won.")
                end_of_game = True
            else:
                dealer_draw3 = random.choice(cards)
                total_dealer_draw += dealer_draw3
                if total_dealer_draw > 21:
                    print(f"New Dealer draw: {dealer_draw1},{dealer_draw2},{dealer_draw3}")
                    print("You won.")
                    end_of_game = True
                else:
                    print(f"New Dealer draw: {dealer_draw1},{dealer_draw2},{dealer_draw3}")
                    dealer_option = random.choice(options)
                    if dealer_option == options[0]:
                        dealer_draw4 = random.choice(cards)
                        total_dealer_draw += dealer_draw4
                        if total_dealer_draw > 21:
                            print(f"New Dealer draw: {dealer_draw1},{dealer_draw2},{dealer_draw3},{dealer_draw4}")
                            print("You won")
                            end_of_game = True
                        else:
                            print(f"New Dealer draw: {dealer_draw1},{dealer_draw2},{dealer_draw3},{dealer_draw4}")


        else:
            print("Enter a valid option.")
            exit()
