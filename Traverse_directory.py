import os


def directory(path):
    for folderName, subfolders, filenames in os.walk(path):
        print('The current folder is', folderName)
        for subfolder in subfolders:
            print('SUBFOLDER OF', folderName, ':', subfolder)
        for filename in filenames:
            print('FILE INSIDE', folderName, ':', filename)
        print('')


if __name__ == '__main__':
    directory(os.getcwd())
