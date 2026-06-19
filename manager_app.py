#This is a School managing program for students, to keep track of their assignments and expenses

#This is where default variables are defined

print("Welcome to BLS School Manager APP.")
assignment =  [ ["math", "incomplete"],
                ["science", "incomplete"], 
                ["english", "incomplete"], 
                ["history", "incomplete"], 
                ["economics", "incomplete"] 
                ]

expenses = []

start = True
#This block is where the program starts with a menu asking the student for the action they want to perform
while start:
    print("\nMENU")
    print("1. Assignment To-Do List.")
    print("2. Expense Tracker.")
    print("3. Exit")
    start1 = input("\nPlease select what you want to do: ")

  #This block takes the student to the to-do list section while viewing default subjects and their status
    if start1 == "1":
        for subject in assignment:
            print(subject[0], subject[1], sep=":")

        action = True
 #This block allows the student to edit the default assignment list by adding or removing a subject form the list
        while action:
            action1 = input("Do you want to add or remove a subject from your assignment to-do list(Yes/No): ").lower()
            if action1 == "yes":
                action2 = input("What do you want to do (Add/Remove): ").lower()
                if action2 == "add":
                        new_subject = input("Enter new subject: ").lower()
                        assignment.append([new_subject, "incomplete"])
                        print("Subject has been added")
                elif action2 == "remove":
                    delete = input("What subject do you want to remove: ").lower()
                    for item in assignment:
                        if item[0] == delete:
                            assignment.remove(item)
                            print("Subject has been removed")
                            break
                    else:
                            print("Subject mentioned isn't part of subjects available.")
                else:
                    print("Invalid action, please enter 'add'or 'remove' to proceed.")
            elif action1 == "no":
                action = False
            else:
                print("Invalid input, Please enter a valid input to proceed")

        print("\nUpdated Assignment")
        for subject in assignment:
            print(subject[0], subject[1], sep=":")
                        
        #This block allows the user to change the status of the subjects in the updated list    
        print("\nAssignment Status\n")

        action3 = input("\nDo you want to update your Assignment (Yes/No)? ").lower()
        if action3 == "yes":
            update = input("What assignment status do you want to update: ").lower()

            found = False

            for item in assignment:
                if item[0] == update:
                    new_status = input("Please update the Status: ").lower()
                    found = True

                    if new_status in ["complete" ,"incomplete"]:
                        item[1] = new_status
                        print("Status updated")
                        break
                    else:
                        print("Invalid Status, Please pick a valid status")
            if not found:
                print("This subject does not exist")
        elif action3 == "no":
            print("Thanks for using our to-do list")
        else:
            print("Invalid input")

#This block displays the finished/final updated to-do list
        print("\nUpdated Assignment status\n")  
        for subject in assignment:
            print(subject[0], subject[1], sep=":")
          
#This block takes the student to the expense tracker system
    elif start1 == "2":
        track = True
      #This block allows the user to add expenses or view the expenses added or to exit this block
        while track:
            decision = input("Do you want to add or view or exit expenses: ").lower()

            if decision == "add":
                category = input("Please enter the category of expense: ").lower()
                amount = input("Please enter the amount: ")
                if amount.isdigit(): 
                    amount = int(amount)
                    expenses.append((category, amount))
                else:
                    print("Enter amount in numeric format")
#This block allows the user to view the expense list by category or an amount range
            elif decision == "view":
                if not expenses:
                    print("There are no expenses to view")
                else:
                    decision1 = input("View by:\n1. Category\n2.Amount\n3.Full Expense list\nEnter view type: ")
                    if decision1 == "1":
                        category_search =  input("Enter the category you want: ").lower()
                        category_searchresult = [expense for expense in expenses if expense[0] == category_search]
                        if category_searchresult:
                            for expense in category_searchresult:
                                print(expense[0], expense[1], sep=":")
                        else: 
                            print("No expenses found in this category")
                    elif decision1 == "2":
                        amount_search = input("Enter minimum you want to view: ")
                        if amount_search.isdigit():
                            amount_search = int(amount_search)
                            amount_searchresult = [expense for expense in expenses if expense[1]>= amount_search]
                            if amount_searchresult:
                                for expense in amount_searchresult:
                                    print(expense[0], expense[1], sep=":") 
                            else:
                                print("No expenses with this amount range can be found")
                        else:
                            print("Amount should be in numeric form")
                    elif decision1 == "3":  
                            print("Full Expense List")        
                            for expense in expenses:
                                print(expense[0], expense[1], sep=":")
                    else:
                        print("Invalid view option")
       #This block is used to exit the expense section     
            elif decision == "exit":
                    track = False
                    print("Thank you for using BLS expense Tracker")
            
            else:
                print("Please enter a valid option")
  #This block is used to exit the program            
    elif start1 == "3":
        start = False
        print("Thank you for using BLS School Manager App")
    else:
        print("Please enter a valid option")



    

