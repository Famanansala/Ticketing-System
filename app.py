# Import necessary libraries
from users import users


#Store submitted tickets in a list
tickets = []

#MENU
while True:
    print("\nWelcome to the IT Help Desk System!")
    print("-----------------------------------")
    print("1. Submit a new ticket")
    print("2. View existing tickets")
    print("3. Update ticket status")
    print("4. View ticket statistics")
    print("5. Exit")

#Select an option
    choice = input("Please select an option (1-5): ")

    if choice == "1":
        print("You have selected to submit a new ticket.")
        name = input("Enter your name: ")
        issue = input("Describe your issue: ")
        priority = input("Enter the priority level (Low, Medium, High): ")
        print("Thank you for submitting your ticket. Our team will get back to you shortly.")
        
        ticket = {
            "id": len(tickets) + 1,
            "name": name,
            "issue": issue,
            "priority": priority,
            "status": "Open"
        }
        tickets.append(ticket)
        print(f"Ticket ID {ticket['id']} has been created successfully.")
    elif choice == "2":
        print("You have selected to view existing tickets.")
    elif choice == "3":
        print("You have selected to update ticket status.")
    elif choice == "4":
        print("You have selected to view ticket statistics.")
    elif choice == "5":
        print("Exiting the system. Goodbye!")
        break
    else:
        print("Invalid option selected. Please try again.")
    
