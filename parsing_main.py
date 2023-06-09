import os
import shutil


def parse_files(folder_path, destination_root):
    nc_files = []
    mpf_files = []
    other_files = []

    for file_name in os.listdir(folder_path):
        file_path = os.path.join(folder_path, file_name)

        if os.path.isfile(file_path):
            file_extension = os.path.splitext(file_name)[1]
            file_start_letter = os.path.splitext(file_name)[0][0]

            if file_extension.lower() == '.nc':
                nc_files.append(file_path)
            elif file_extension.lower() == '.mpf':
                mpf_files.append(file_path)
            elif file_extension == '' and (file_start_letter == 'O' or file_start_letter == 'О'):
                other_files.append(file_path)

    destination_folder = os.path.join(destination_root, 'PARSED')
    if not os.path.exists(destination_folder):
        os.makedirs(destination_folder)

    # Move .nc files to the destination folder
    for nc_file in nc_files:
        shutil.move(nc_file, destination_folder)

    # Move .mpf files to the destination folder
    for mpf_file in mpf_files:
        shutil.move(mpf_file, destination_folder)

    # Move other files to the destination folder
    for other_file in other_files:
        shutil.move(other_file, destination_folder)

    print("Files moved successfully.")

    if nc_files:
        print("NC Files:")
        for file in nc_files:
            print(file)

    if mpf_files:
        print("\nMPF Files:")
        for file in mpf_files:
            print(file)

    if other_files:
        print("\nOther Files:")
        for file in other_files:
            print(file)

    return nc_files, mpf_files, other_files


# Provide the folder path where the files are located
folder_path = 'C:/Users/User/Desktop/sudo/VOSST'

# Provide the destination root directory
destination_root = 'C:/Users/User/Desktop/sudo/'

parse_files(folder_path, destination_root)
