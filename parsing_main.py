import os
import shutil


def parse_files(folder_path, destination_folder):
    nc_files = []
    mpf_files = []
    other_files = []

    for file_name in os.listdir(folder_path):
        file_path = os.path.join(folder_path, file_name)

        if os.path.isfile(file_path):
            file_extension = os.path.splitext(file_name)[1]

            if file_extension == '.nc':
                nc_files.append(file_path)
            elif file_extension == '.mpf':
                mpf_files.append(file_path)
            elif file_extension == '':
                other_files.append(file_path)

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


    return nc_files, mpf_files, other_files


# Provide the folder path where the files are located
folder_path = 'C:/Users/User/Desktop/sudo/ParsingFiles'
# Provide the destination folder path. Leave empty to create the new directory
destination_folder = ''  

parse_files(folder_path, destination_folder)
