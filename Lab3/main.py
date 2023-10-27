from folderMonitor import FolderMonitor

folder_path = "C:\\Users\\Eugen Ostafi\\Desktop\\labs\\Lab3\\filesstorage\\"
Monitor = FolderMonitor(folder_path)

saves = Monitor.scan()  # Take an initial snapshot
savedSnapshot = Monitor.snapshotTime()

while True:
    print("\nOptions:")
    print("1. commit")
    print("2. info <filename>")
    print("3. status")
    print("4. exit")
    
    inpt = input("Choose one option: ")

    if inpt == "commit":
        Monitor.commit()
        saves = Monitor.scan()  # Update the snapshot after committing
        savedSnapshot = Monitor.snapshotTime()

    elif inpt.startswith("info"):
        name = inpt.replace("info ", "")
        Monitor.info(name)

    elif inpt == "status":
        print("Created Snapshot at:", savedSnapshot)
        current = Monitor.scan()
        Monitor.status(saves,current)

    elif inpt == "exit":
        print("Exiting the program...")
        break

    else:
        print("Invalid option. Please choose again.")
