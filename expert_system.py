def greet_user():
    print("👋 Welcome to TechHelp Desk!")
    name = input("👤 May I have your name, please? ")
    print(f"Hi {name}, I'm your virtual help desk assistant. Let's troubleshoot your problem.")
    return name

def ask_issue_type():
    print("\nPlease select the issue you're facing:")
    print("1. Internet Issue")
    print("2. Software Issue")
    print("3. Hardware Issue")
    choice = input("Enter the number corresponding to your issue: ")
    return choice

def internet_issue():
    print("\nLet me help you with Internet issues.")
    connected = input("Are other devices able to connect to the internet? (yes/no): ").lower()
    if connected == "yes":
        print("🛠 Try restarting your device or reconnecting to the Wi-Fi.")
    else:
        print("🛠 Try restarting your router. If the issue persists, contact your ISP.")

def software_issue():
    print("\nLet’s troubleshoot software problems.")
    software = input("Which software is causing issues? ")
    crash = input(f"Is {software} crashing or freezing? (yes/no): ").lower()
    if crash == "yes":
        print(f"🛠 Try reinstalling {software} or updating it to the latest version.")
    else:
        print(f"🔍 Try restarting {software}. If the issue persists, check logs or contact support.")

def hardware_issue():
    print("\nLet’s deal with hardware problems.")
    device = input("Which device is not working? (e.g., mouse, keyboard, printer): ").lower()
    plugged = input(f"Is your {device} properly connected or plugged in? (yes/no): ").lower()
    if plugged == "no":
        print(f"🔌 Please connect or plug in the {device} properly.")
    else:
        print(f"⚠ The {device} might be faulty. Try using it on another computer or replacing it.")

def main():
    name = greet_user()
    while True:
        issue = ask_issue_type()
        if issue == "1":
            internet_issue()
        elif issue == "2":
            software_issue()
        elif issue == "3":
            hardware_issue()
        else:
            print("❌ Invalid option. Please select 1, 2, or 3.")
            continue

        cont = input("\nDo you need help with anything else? (yes/no): ").lower()
        if cont != "yes":
            print(f"\n👋 Thank you, {name}! Have a great day. If the issue persists, contact IT support.")
            break

# Run the system
main()
