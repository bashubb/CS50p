

def main():

    grocery_list =[]

    while True:
        try:
            item = input()
            grocery_list.append(item)
        except EOFError:
            print("\n")
            break

    grocery_list.sort()
    grocery_dict = {}

    for item in grocery_list:
        if item in grocery_dict.keys():
            grocery_dict[item] += 1
        else:
            grocery_dict[item] = 1


    for key, value in grocery_dict.items():
        print(value, key.upper())



main()

