def main():

    amount = 50
    while amount > 0:
        print(f"Amount Due: {amount}")
        insert_coin = int(input("Insert Coin: "))
        if insert_coin in [25, 10, 5]:
            amount -= insert_coin

    print(f"Change Owed: {amount * -1}")


main()
