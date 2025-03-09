import os
import shutil

# scan directory for files that start with _ and move them to a new directory and rename them
def scan_dir(target_dir):
    
    files = os.listdir(target_dir)
    
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
            print(f'source_dir: {source_dir}')
            
            # target direcory
            dest_dir = os.path.join(target_dir, parts[0], parts[1])
            print(f'dest_dir: {dest_dir}')
            
            # move new file to create
            print(f'new file: {os.path.join(dest_dir, parts[-1])}')
            # create new folders if it doesnt exist
            os.makedirs(dest_dir, exist_ok=True)
            # move and rename file
            shutil.move(source_dir, os.path.join(dest_dir, parts[-1]))
            
            
    
if __name__ == '__main__':
    target_dir = r"C:\Users\PC\Desktop\test"
    scan_dir(target_dir)
    