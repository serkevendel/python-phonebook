#!usr/bin/bash
import json
import os

class PhoneBook:

    def __init__(self):
        self.phoneDict : dict = {}
        if os.path.exists("contacts.json"):
            with open("contacts.json") as file:
                self.phoneDict = json.load(file)

    def showMenu(self):
        entry = 0
        while entry == 0:
            print("Press 1 to add a new entry")
            print("Press 2 to list current entries")
            print("Press 3 to delete an entry")
            print("Press 4 to exit!")
            entry = input()

            if entry.isdigit():
                entry = int(entry)
                if entry == 1 :
                    self.addNewEntry()
                    self.showMenu()
                if entry == 2 :
                    self.listCurrentEntries()
                    self.showMenu()
                if entry == 3 :
                    self.deleteEntry()
                    self.showMenu()
                if entry == 4 :
                    return

    def saveDict(self):
        with open('contacts.json', 'w') as file:
            dictAsJson = json.dumps(self.phoneDict)
            file.write(dictAsJson)

    def addNewEntry(self):
        name = input("Enter name: (To cancel process, write 'cancel') ")
        while name.isdigit() :
            name = input("Sorry, name cannot be a number. Please try again: ")

        if name == 'cancel':
            return

        self.phoneDict : dict

        if name in self.phoneDict:
            choice = input("An entry is already found with this name. Do you want to overwrite? (y or n (cancels operation)): ")
            if choice == "n":
                return

        phoneNumber = input("Enter phone number (To cancel process, write 'cancel') ")
        if not phoneNumber.isdigit():
            phoneNumber = input("Enter phone number (To cancel process, write 'cancel') ")

        self.phoneDict[name] = phoneNumber

        self.saveDict()

        input("Save successful! Press any key to go back to menu.\n")

    def listCurrentEntries(self):
        self.phoneDict : dict
        print()
        for key, value in self.phoneDict.items():
            print(key, "\t", value)
        input("End of entries reached!\nPress any key to go back to menu.\n")

    def deleteEntry(self):
        name = input("Enter name to be deleted: ")
        del self.phoneDict[name]
        print("Deleted entry with name: {}".format(name))

def main():
    print("Welcome to PhoneBook!")
    print("\n")
    phonebook = PhoneBook()
    phonebook.showMenu()

if __name__ == "__main__":
    main()
