def init_database():
    names = ["Jean-Luc Picard", "William T. Riker", "Geordi La Forge", "Data", "Beverly Crusher"]
    ranks = ["Captain", "Commander", "Lieutenant Commander", "Lieutenant Commander", "Commander"]
    divs  = ["Command", "Command", "Operations", "Operations", "Sciences"]
    ids   = ["PIC1", "RIK2", "LAF3", "DAT4", "CRU5"]
    return names, ranks, divs, ids

def display_menu(current_user):
    print("STARFLEET MANAGER")
    print(f"Logged in as: {current_user}")
    print("\n1. Add New Crew Member")
    print("2. Remove Crew Member")
    print("3. Update Rank")
    print("4. Display Full Roster")
    print("5. Count Senior Officers")
    print("6. Exit")
    return input("Enter your choice (1-5): ")

def add_member(names, ranks, divs, ids):
    print("\n--- ADD NEW CREW MEMBER ---")
    name = input("Full Name: ").strip()
    
    valid_ranks = ["Ensign", "Lieutenant", "Lieutenant Commander", "Commander", "Captain"]
    while True:
        rank = input("Rank (Ensign / Lieutenant / Lieutenant Commander / Commander / Captain): ").strip().title()
        if rank in valid_ranks: break
        print("Invalid rank.")
    
    while True:
        div = input("Division (Command / Operations / Sciences): ").strip().title()
        if div in ["Command", "Operations", "Sciences"]: break
        print("Invalid division.")
    
    while True:
        crew_id = input("Unique ID: ").strip().upper()
        if crew_id not in ids: break
        print("Invalid id.")
    
    names.append(name)
    ranks.append(rank)
    divs.append(div)
    ids.append(crew_id)
    print(f"{name} added.")

def remove_member(names, ranks, divs, ids):
    print("\n--- REMOVE CREW MEMBER ---")
    crew_id = input("Enter ID: ").strip().upper()
    if crew_id in ids:
        idx = ids.index(crew_id)
        print(f"Removed: {names[idx]}")
        del names[idx], ranks[idx], divs[idx], ids[idx]
    else:
        print("ID not found.")

def display_roster(names, ranks, divs, ids):
    print("CREW ROSTER")
    print(f"{'ID'} {'Name'} {'Rank'} {'Division'}")
    for i in range(len(names)):
        print(f"{ids[i]} {names[i]} {ranks[i]} {divs[i]}")