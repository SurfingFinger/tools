"""Changes files without extensions to .txt files in directory entered by user.
   Works recursively to treat all subdirectories.
   Prints a list of subdirectories in the dirctory entered at prompt.
   Written 21.Feb.2022"""

import os

def handle_folder_contents(folder_to_work):
    files = os.listdir(folder_to_work)
    
    for file in files:
        if "." not in file:
            this_file = os.path.join(folder_to_work, file)
            if os.path.isfile(this_file):
                os.rename(this_file, this_file + '.txt')

            elif os.path.isdir(this_file):
                handle_folder_contents(this_file)

            else:
                print("this_file: ")
                print(this_file)
                print(f"{file} isn't a file or directory.")



if __name__ == "__main__":
    print("Please enter the directory you'd like to work with:")
    handle_folder_contents(input())

