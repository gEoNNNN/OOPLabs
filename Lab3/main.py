from folderMonitor import FolderMonitor

while True:
    print("Options:")
    print("commit")
    print("info <filename>")
    print("status")
    inpt = input("Chose one option:")
    folder_path = "C:\\Users\\Eugen Ostafi\\Desktop\\lab3\\OOP-Labs\\Lab3\\filesstorage"
    Monitor = FolderMonitor(folder_path)
    saves = Monitor.scan()
    savedSnapshot = Monitor.snapshotTime()
    if inpt == "commit":
        Monitor.commit()
    if inpt[0] == 'i' and inpt[1] == 'n' and inpt[2] == 'f' and inpt[3] == 'o':
        name = inpt.replace("info ","")
        Monitor.info(name)
    if inpt == "status":
        Monitor.status(saves)
        print("Created Snapshot at: ",savedSnapshot)
        saves = Monitor.scan()
        savedSnapshot = Monitor.snapshotTime()
    break