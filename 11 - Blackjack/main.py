import random, art

print(art.logo)

cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]

user = []
dealer = []
check = False


def distributeCards(card, c):

    for i in range(0, c):
        card.append(random.choice(cards))
        if sum(card) > 21:
            if 11 in card:
                index = card.index(11)
                card[index] = 1
    return card


def dealerCards(dealer, check=False):
    if check:
        print(f"\nDealer cards {dealer}\n\n")
    else:
        print(f"\nDealer cards {dealer[0]}\n\n")


def userCards(user):
    print(f"\n\nUser cards {user}\n\n")


def findWinner(user, dealer):

    if sum(user) > 21:
        print(f"\n\nDealer win! {dealer}\nUser {user}")
        return True
    elif sum(user) == 21:
        print(f"\n\nUser win! {user}\nDealer {dealer}")
        return True
    elif sum(dealer) == 21:
        print(f"\n\nDealer win! {dealer}\nUser {user}")
        return True

    while sum(dealer) < 17:
        dealer = distributeCards(dealer, 1)

    if sum(dealer) > 21:
        print(f"\n\nUser win! {user}\nDealer {dealer}")
    elif sum(user) == sum(dealer):
        print("\n\nDraw!!!\n\n")
    elif sum(user) > sum(dealer):
        print(f"\n\nUser win! {user}\nDealer {dealer}")
    else:
        print(f"\n\nDealer win! {dealer}\nUser {user}")

    return True


def moreCards(user, dealer):
    more = input("Hit or Stand? H or S?").upper()
    if more == "S" or sum(user) >= 21:
        return findWinner(user, dealer)
    else:
        user = distributeCards(user, 1)

    if sum(user) >= 21:
        return findWinner(user, dealer)


user = distributeCards(user, 2)
dealer = distributeCards(dealer, 2)
while not check:

    userCards(user)
    dealerCards(dealer, True)

    check = moreCards(user, dealer)