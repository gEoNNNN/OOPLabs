from folderMonitor import FolderMonitor
import time
import threading

class programRun:
    def __init__(self, folder_path="C:\\Users\\Eugen Ostafi\\Desktop\\labs\\Lab3\\filesstorage\\"):
        self.Monitor = FolderMonitor(folder_path)
        self.saves = self.Monitor.scan()
        self.savedSnapshot = self.Monitor.snapshotTime()

    def scheduled_function(self):
        while True:
            self.savesForEvery5sec = self.Monitor.scan()
            time.sleep(5)
            currentForEvery5sec = self.Monitor.scan()
            self.Monitor.Schedule(self.savesForEvery5sec, currentForEvery5sec)

    def run(self):
        thread = threading.Thread(target=self.scheduled_function)
        thread.daemon = True
        thread.start()

        self.display_options()
        self.saves = self.Monitor.scan()
        while True:
            inpt = input("Choose one option: ")

            if inpt == "commit":
                self.Monitor.commit()
                self.saves = self.Monitor.scan()
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

            self.display_options()

    def display_options(self):
        print("\nOptions:")
        print("1. commit")
        print("2. info <filename>")
        print("3. status")
        print("4. exit")

if __name__ == '__main__':
    programRun_object = programRun()
    programRun_object.run()
