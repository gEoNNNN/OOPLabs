from folderMonitor import FolderMonitor

while True:
    print("Options:")
    print("commit")
    print("info <filename>")
    print("status")
    inpt = input("Chose one option:")
    folder_path = "C:\\Users\\Eugen Ostafi\\Desktop\\labs\\Lab3\\filesstorage\\"
    Monitor = FolderMonitor(folder_path)
    saves = Monitor.scan()
    savedSnapshot = Monitor.snapshotTime()
    
    if inpt == "commit":
        Monitor.commit()
        saves = Monitor.scan()
        savedSnapshot = Monitor.snapshotTime()

    elif inpt.startswith("info"):
        name = inpt.replace("info ", "")
        Monitor.info(name)

    elif inpt == "status":
        print("Created Snapshot at: ", savedSnapshot)
        Monitor.status(saves)
    break