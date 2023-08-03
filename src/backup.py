from data import log_to_db

import shutil
import os
import datetime

# Get the backup folder path from environment variable
backup_folder_path = os.environ.get('BACKUPFOLDER')
if backup_folder_path is None or not backup_folder_path:
    backup_folder_path = './FCA-Flask/backups'

# Create a backup folder if it doesn't exist
if not os.path.exists(backup_folder_path):
    os.makedirs(backup_folder_path)


def folder(source_folder_path):
    if not os.path.exists(source_folder_path):
        log_to_db("BACKUP", "Folder=" + source_folder_path, "ERROR")
        raise ValueError("Source Folder does not exist")

    # Create a timestamp for the backup folder name
    timestamp = datetime.datetime.now().strftime("%Y%m%d%H%M%S")

    # Copy the contents of the source folder to the backup folder
    if os.path.isfile(source_folder_path):
        backup_folder_name = f"{timestamp}_{os.path.basename(source_folder_path)}"
        backup_path = os.path.join(backup_folder_path, backup_folder_name)
        shutil.copyfile(source_folder_path, backup_path)
    else:
        backup_file_name = f"{os.path.basename(source_folder_path)}_{timestamp}"
        backup_path = os.path.join(backup_folder_path, backup_file_name)
        shutil.copytree(source_folder_path, backup_path)

    log_to_db("BACKUP", "Folder=" + source_folder_path, "SUCCESS")