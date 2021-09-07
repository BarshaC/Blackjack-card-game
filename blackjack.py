import random
import time

def get_card_value(cards):
    t = 0
    aces = 0
    for c in cards:
        if (c == "2" or c == "3" or c == "4" or c == "5" or c == "6" or c == "7" or c == "8" or c == "9" or c == "10"):
            t = int(c)
        elif c == "A":
            aces += 10
            t = 1
        else:
            t = 10
    if aces != 0 or t < 12:
        t += 10
        aces -= 10
    return t-10

def get_dealer_hand():
    d = list()
    d.append(get_card())
    d.append(get_card())
    a = get_card()
    if get_card_value(d) < 17:
        d.append(a)
    return d

def is_bust(cards_sum):
    s = 0
    for k in cards_sum:
        print(get_card_value(k))
        s += get_card_value(k)
    #print("Sum", s)
    if s > 21:
        return True
    else:
        return False

#card = random.randint(1, 13)
def get_card():
    card = random.randint(1, 13)
    face_cards = {1: "A", 11: "J", 12: "Q", 13: "K"}
    if card in face_cards:
        return face_cards[card]
    return str(card)

def get_user_decision():
    user_input = input("Would you like to hit (H) or stay (S)? ")
    user_input = user_input.upper()
    while user_input != "H" and user_input != "S":
        print("Please insert H or S")
        user_input = (input("Would you like to hit (H) or stay (S)? "))
    return user_input

def cards_print_out(p, c):
    result = p + " cards are "
    for card in c:
        result += str(card) + " "
    card_value = get_card_value(c)
    return result

def play_a_turn():
    cards = list()
    cards.append(get_card())
    cards.append(get_card())
    print(cards_print_out("Your", cards))
    user_decision = get_user_decision()
    user_decision.upper()
    if user_decision == "S":
        print(cards_print_out("Your", cards))
        if is_bust(cards):
                print(cards_print_out("Your", cards))
                print("You busted! You lose!")
                return False
    while user_decision == "H":
        if user_decision == "H":
            cards.append(get_card())
            if is_bust(cards):
                print(cards_print_out("Your", cards))
                print("You busted! You lose!")
                return False
            else:
                print(cards_print_out("Your", cards))
                user_decision = get_user_decision()
    print(cards_print_out("Your", cards))
    dealer_cards = get_dealer_hand()
    print(cards_print_out("Dealer's", dealer_cards))
    your_value = get_card_value(cards)
    dealer_value = get_card_value(dealer_cards)
    total_value = your_value + dealer_value
    if your_value > dealer_value and is_bust(cards) == False:
        print("You win!")
        return True
    else:
        print("You lose!")
        return False
        
def get_time(start_time):
    time_elapsed = start_time - time.time()
    time_in_sec = time_elapsed
    n = int(time_in_sec // 60)
    l = int(time_in_sec / 60)
    return str(n) + "." + str(l).zfill(2)

def get_time(end_time):
    end_time = time.time()
    time_in_sec = end_time
    n= int(time_in_sec // 60)
    l = int(time_in_sec // 60)
    return str(n) + '.' + str(l).zfill(2)

def play_game(initial_bet):
    print("Welcome to Blackjack")
    q = initial_bet
    start_time = time.time()
    play_more = True
    while q > 0 and play_more:
        print("Welcome to another round")
        u = input("How much would you like to bet? ")
        win = play_a_turn()
        if win:
            q += int(u)
        else:
            q -= int(u)
        print("You currently have $" + str(q))
        play_more = input("Would you like to play more? (Y or N) ")
        if play_more.upper() == "N":
          play_more = False
    end_time = time.time()
    time_elapsed = round((end_time - start_time)/60, 4)
    print("You have been playing for " + str(time_elapsed) + " minutes.")
    


# This makes sure that we only run the play game when the blackjack
# program is the "main" program.
# You don't have to change anything underneath this.
if __name__ == "__main__":
    INITIAL_BET = int(input("Please insert how much $$$ you want to start with: "))
    play_game(INITIAL_BET)
