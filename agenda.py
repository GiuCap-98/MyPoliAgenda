import datetime

class Event:
    def __init__(self, title, date, description):
        self.title = title
        self.date = date
        self.description = description

class Agenda:
    def __init__(self):
        self.temporary_db = {}

    def add_event(self, title, date, description):
        new_event = Event(title=title, date=date, description=description)
        self.temporary_db[new_event.title] = [date, description]
        
    def remove_event(self, title):
        if title in self.temporary_db.keys():
            self.temporary_db.pop(title, None)

    def list_events(self):
        for title, details in self.temporary_db.items():
            date, description = details
            print(f"Title: {title}, Date: {date}, Description: {description}")


if __name__ == "__main__":
    agenda = Agenda()
    print(
        """
     _____      _ _           _                                _       
    |  __ \    | (_)         (_)     /\                       | |      
    | |__) |__ | |_ _ __ ___  _     /  \   __ _  ___ _ __   __| | __ _ 
    |  ___/ _ \| | | '_ ` _ \| |   / /\ \ / _` |/ _ \ '_ \ / _` |/ _` |
    | |  | (_) | | | | | | | | |  / ____ \ (_| |  __/ | | | (_| | (_| |
    |_|   \___/|_|_|_| |_| |_|_| /_/    \_\__, |\___|_| |_|\__,_|\__,_|
                                          __/ |                       
                                         |___/                        
    
    Welcome to the Polimi Agenda Application!
    """
    )
    while True:
        print("\nMenu:")
        print("1. Add Event")
        print("2. Remove Event")
        print("3. List Events")
        print("4. Exit")
        choice = input("Enter your choice: ")

        if choice == "1":
            title = input("Enter your Event Title: ")

            year  = input("Enter Event Year: ")
            month = input("Enter Event Month: ")
            day   = input("Enter Event Day: ")
            date  = datetime.datetime(int(year), int(month), int(day))

            desc  = input("Enter Event Description: ")
            

            agenda.add_event(title=title, date=date, description=desc)

        elif choice == "2":
            title = input("Enter your Event Title: ")
            agenda.remove_event(title=title)

        elif choice == "3":
            agenda.list_events()

        elif choice == "4":
            break
        else:
            print("Invalid choice, please try again.")
