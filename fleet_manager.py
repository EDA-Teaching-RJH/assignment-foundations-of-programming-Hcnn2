def init_database():
    names = ["Jean-Luc Picard", "William T. Riker", "Geordi La Forge", "Data", "Beverly Crusher"]
    ranks = ["Captain", "Commander", "Lieutenant Commander", "Lieutenant Commander", "Commander"]
    divs = ["Command", "Command", "Operations", "Operations", "Sciences"]
    ids = ["PIC1", "RIK2", "LAF3", "DAT4", "CRU5"]
    return names, ranks, divs, ids

def display_menu(current_user):
    print("STARFLEET MANAGER")
    print(f"Logged in as {current_user}")
    print("\n1. Add New Crew Member")
    print("2. Remove Crew Member")
    print("3. Update Rank")
    print("4. Display Full Roster")
    print("5. Count Senior Officers")
    print("6. Exit")
    return input("Enter your choice (1-5):").strip

