import os


def list_contents(base_path):
    #always points to folder you are currently in
    current_path = base_path
    print "Please pick the folder that contains ",
    print "current months data."
    print
    # loop runs until you find a folder that contains your files
    #add quit function?
    while True:
        #items in current folder
        contents = os.listdir(current_path)
        #used to create previous path string to move up one folder
        pieces_of_path = current_path.split("\\")
        previous_path = "\\".join(pieces_of_path[:len(pieces_of_path)-1])
        print "Current Folder %s" % current_path
        print
        files = []
        directories = []
        #for items in folder categorized them as file or folder to display
        for item in contents:
            if os.path.isdir(current_path + "\\" + item):
                directories.append(item)
            if os.path.isfile(current_path + "\\" + item):
                files.append(item)
        directories.sort()
        #insert location that is one folder up so you can move back as needed
        directories.insert(0,previous_path)
        files.sort()
        #check to see if you have an empty folder
        if len(files) == 0 and len(directories) == 0:
            print "There are no files or folders in this location"
            back_step = raw_input(
                "Would you like to move up one folder(Y/N)? ")
            if back_step.lower() in ['yes','n']:
                current_path = previous_path
                continue
        #if there are files in the folder list them for user
        #if files needed are found, while loop breaks and returns the
        #location of the folder
        if len(files) > 0:
            print "This Folder contains the following files"
            print "Files"
            print "_____________"            
            for num,file_name in enumerate(files):
                print "%d: %s" % (num+1, file_name)
            found_files = raw_input(
                "Does this folder contain your files (Y/N)? ")
            if found_files.lower() in ['yes','y']:
                break                                  
        else:
            print "This folder contains no files"
            print
        #if files were not in that folder, ask user to pick directory where
        # they may be
        if len(directories) > 0:    
            print "Directorties in this Folder"
            print "_____________"
            for num,folder in enumerate(directories):
                #display output for previous folder location
                if num == 0:
                    print "%d: %s (previous folder)" % (num +1, folder)
                else:
                    print "%d: %s" %(num+1, folder)
            print
            next_folder = int(raw_input(
                "which folder would you like to move to "))
            if next_folder == 1:
                current_path = previous_path
                continue
            else:
                print current_path
                current_path = current_path + \
                               "\\" + directories[int(next_folder)-1]
                continue
        #if folder contains no other folder ask user to move up one
        else:
            print "This folder contains no other folders"
            back_step = raw_input("Would you like to move one folder up(Y/N)? ")
            if back_step.lower() in ['yes','y']:
                current_path = previous_path
                continue
    return current_path



def main():
    
    base_path = 'I:\Research Coordinators\Data Cleaning\JHH\Coordinator Cleaning Files'
    list_contents(base_path)

if __name__ =="__main__":
    main()
