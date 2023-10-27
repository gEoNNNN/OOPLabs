from folderMonitor import FolderMonitor

class programRun:
    def __init__(self, folder_path="C:\\Users\\Eugen Ostafi\\Desktop\\labs\\Lab3\\filesstorage\\"):
        self.Monitor = FolderMonitor(folder_path)
        self.saves = self.Monitor.scan()  # Take an initial snapshot
        self.savedSnapshot = self.Monitor.snapshotTime()

    def run(self):
        while True:
            print("\nOptions:")
            print("1. commit")
            print("2. info <filename>")
            print("3. status")
            print("4. exit")

            inpt = input("Choose one option: ")

            if inpt == "commit":
                self.Monitor.commit()
                self.saves = self.Monitor.scan()  # Update the snapshot after committing
                self.savedSnapshot = self.Monitor.snapshotTime()

            elif inpt.startswith("info"):
                name = inpt.replace("info ", "")
                self.Monitor.info(name)

            elif inpt == "status":
                print("Created Snapshot at:", self.savedSnapshot)
                current = self.Monitor.scan()
                self.Monitor.status(self.saves, current)

            elif inpt == "exit":
                print("Exiting the program...")
                break

            else:
                print("Invalid option. Please choose again.")