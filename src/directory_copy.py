import os
import shutil
def recur_copy(source,dest):
    if not os.path.exists(dest):
        os.mkdir(dest)
    if os.path.exists(source):
        list_dir=os.listdir(source)
        for item in list_dir:
            if os.path.isfile(os.path.join(source,item)):
                shutil.copy(os.path.join(source,item),dest)
            else:
                recur_copy(os.path.join(source,item),os.path.join(dest,item))
        return
    else:
        raise Error("Source Destination invalid")
def static_to_public():
    source_path="/home/borderline_corporate_slave/workspace/github.com/parathabanado/Static-Site-Generator/static"
    destination_path="/home/borderline_corporate_slave/workspace/github.com/parathabanado/Static-Site-Generator/public"
    if os.path.exists(destination_path):
        try:
            shutil.rmtree(destination_path)
        except OSError as e:
            print(f"Error: could not delete {destination_path} : {e}") 
    recur_copy(source_path,destination_path)
        