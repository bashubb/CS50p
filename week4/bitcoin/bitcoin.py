import requests
import sys

def main():

    if len(sys.argv) != 2:
        sys.exit("Missing command-line argument")
    if sys.argv[1].isalpha():
        sys.exit("Command-line argument is not a number")
    try:
        request =  requests.get("https://api.coindesk.com/v1/bpi/currentprice.json")
    except requests.RequestException:
        pass

    in_usd = request.json()["bpi"]["USD"]["rate_float"]
    result = float(sys.argv[1]) * in_usd
    print(f"${result:,.4f}")



if __name__ == "__main__":
    main()

