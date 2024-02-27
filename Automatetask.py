import os
import shutil

def organize_files(directory):
    extensions = {
        'documents': ['.pdf', '.doc', '.docx', '.txt'],
        'images': ['.jpg', '.jpeg', '.png', '.gif'],
        'videos': ['.mp4', '.avi', '.mkv'],
        'music': ['.mp3', '.wav', '.flac'],
        'archives': ['.zip', '.rar', '.tar', '.gz'],
        'other': [] 
    }

    for folder in extensions.keys():
        folder_path = os.path.join(directory, folder)
        if not os.path.exists(folder_path):
            os.makedirs(folder_path)
    for filename in os.listdir(directory):
        if os.path.isfile(os.path.join(directory, filename)):
            file_extension = os.path.splitext(filename)[1].lower()
            moved = False
            for folder, ext_list in extensions.items():
                if file_extension in ext_list:
                    src_path = os.path.join(directory, filename)
                    dest_path = os.path.join(directory, folder, filename)
                    shutil.move(src_path, dest_path)
                    moved = True
                    break
            if not moved:
                src_path = os.path.join(directory, filename)
                dest_path = os.path.join(directory, 'other', filename)
                shutil.move(src_path, dest_path)

    print("Files organized successfully!")
directory_to_organize = "/path/to/directory"
organize_files(directory_to_organize)
