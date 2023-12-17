# used for high level file operation
import shutil

def reset():
    """
    resets the test folder to run and see this scripts commands in operation
    """
    import os
    if os.path.exists("./test/destination/data.txt"):
        os.remove("./test/destination/data.txt")
    if os.path.exists("./test/destination/copy_test"):
        # os.remove("./test/destination/copy_test/")
        shutil.rmtree("./test/destination/copy_test/")
    if os.path.exists("./test/destination/copy_with_filter_test"):
        # os.remove("./test/destination/copy_with_filter_test/")
        shutil.rmtree("./test/destination/copy_with_filter_test/")



reset()

# copying a file
shutil.copy("./test/source/data.txt","./test/destination/data.txt")

# copy a folder
shutil.copytree("./test/copy_folder","./test/destination/copy_test/")

# copy folder ignoring certain file
# for this need a function that acts as a filter
def file_filter(directory,files):
    """
    filter funtion returns a list of files that need to be excluded
    """
    return [f for f in files if f == "ignore_this_file.txt"]
shutil.copytree("./test/copy_folder","./test/destination/copy_with_filter_test/",ignore=file_filter)

# to move file
# shutil.move()

# to remove a folder
# shutil.rmtree()

#  to get disk usage
total,used,free=shutil.disk_usage('C:')
print(total,used,free)

# to copy metadat from one file to another file
# shutil.copystat("onefile","anotherfile")

# change ownership of a file or directory
# shutil.chown("file/dir",user="shrey")

# to see teh location of a program
# shutil.which("python")

# to pack and unpack archive
# shutil.make_archive()
# shutil.unpack_archive()