import os
import shutil

# scan directory for files that start with _ and move them to a new directory and rename them
def scan_dir(target_dir):
    
    files = os.listdir(target_dir)
    print(f'files: {files}')
    
    # do this for every file
    for f in files:
        
        if(f.startswith('_')):
            
            # remove underscore
            new_f = f.split('_')[1]
            print(f'file is: {new_f}')
            
            # get the different directories specified in the file seperated by '-'
            parts = new_f.split('-')
            print(f'parts: {parts}')
            
            # path to current file
            source_dir = os.path.join(target_dir, f)
            print(f'source_dir: {type(source_dir)}')
            
            # target directory
            dir_to_use = target_dir
            for subdir in parts[:-1]:
                # create a variable that that adds a subdir each loop and use the var after the final loop
                dir_to_use = os.path.join(dir_to_use,subdir)
                
            print(f'dest_dir: {dir_to_use}')
            
            # move new file to create
            print(f'new file: {os.path.join(dir_to_use, parts[-1])}')
            
            # create new folders if it doesnt exist
            os.makedirs(dir_to_use, exist_ok=True)
            
            # move and rename file
            shutil.move(source_dir, os.path.join(dir_to_use, parts[-1]))
        
    
    
if __name__ == '__main__':
    
    # analyze current directory
    cwd = os.getcwd()
    
    scan_dir(cwd)
    