# Import necessary libraries
from users import users


#Store submitted tickets in a list
tickets = []

# User login
print("Welcome to the IT Help Desk System!")

employee_id = input("Please enter your employee ID: ")
name = input("Please enter your full name: ")

logged_in_user = None

for user in users: 
    if str(user["id"]) == employee_id and user["name"].lower() == name.lower():
        logged_in_user = user
        break
    
if logged_in_user is None:
    print("Invalid employee ID or name. Access denied.")
    exit()
else:
    print(f"Welcome, {logged_in_user['name']}! You are logged in as a {logged_in_user['role']}.")
    print(f"Role: {logged_in_user['role']}")


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
    
