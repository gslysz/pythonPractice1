import os
import datetime
import calendar
import shutil
import sys


def organize_files(source_folder, target_base_folder, split_by_month=True, backup=True, delete_source=True):
    source_exists = os.path.exists(source_folder)
    if not source_exists:
        msg = "Cannot organize files. Source path does not exist. Source=" + source_folder
        print(msg)
        return
    if not os.path.exists(target_base_folder):
        msg = "Created folder: " + target_base_folder
        print(msg)
        os.mkdir(target_base_folder)

    all_files = os.listdir(source_folder)
    filtered_files = []

    for f in all_files:
        f_lower = f.lower()
        if (f_lower.endswith(".jpg")
                or f_lower.endswith(".mp4")
                or f_lower.endswith(".mov")
                or f_lower.endswith(".png")):
            filtered_files.append(f_lower)

    for f in filtered_files:
        path_f = source_folder + "/" + f
        timestamp = os.path.getmtime(path_f)
        last_mod = datetime.datetime.fromtimestamp(timestamp)
        year_num = last_mod.year
        month_num = last_mod.month
        copy_file_to_target_folder(path_f, target_base_folder, year_num, month_num, split_by_month,
                                   backup, delete_source)


if __name__ == "__main__":
    source_path = str(sys.argv[1])
    target_path = str(sys.argv[2])
    organize_files(source_path, target_path)


def create_month_folders(year_folder_path):
    dir_exists = os.path.exists(year_folder_path)
    if dir_exists:
        # noinspection SpellCheckingInspection
        index_vals = list(range(1, 13, 1))

        for i in index_vals:
            create_month_folder(i, year_folder_path)


def create_month_folder(i, year_folder_path):
    month = calendar.month_abbr[i]
    padded_month_num = str(i).zfill(2)
    month_folder_text = "{}-{}".format(padded_month_num, month)
    month_folder_path = year_folder_path + "/" + month_folder_text
    month_folder_exists = os.path.exists(month_folder_path)
    if not month_folder_exists:
        os.mkdir(month_folder_path)
        print("Created the folder: " + month_folder_path)
    return month_folder_path


def copy_file_to_target_folder(source_file, target_base_folder_path, year_num, month_num, split_by_month=True,
                               backup_files=False, delete_source=True):
    file_name = os.path.basename(source_file)
    year_folder_path = target_base_folder_path + "/" + str(year_num)
    if not os.path.exists(year_folder_path):
        os.mkdir(year_folder_path)

    if split_by_month:
        month_folder_path = create_month_folder(month_num, year_folder_path)
        target_file_path = month_folder_path + "/" + file_name
    else:
        target_file_path = year_folder_path + "/" + file_name

    if not os.path.exists(target_file_path):
        shutil.copy2(source_file, target_file_path)
        print("{} copied to {}".format(file_name, target_file_path))

    if backup_files:
        backup_folder_path = target_base_folder_path + "/backup"
        if not os.path.exists(backup_folder_path):
            os.mkdir(backup_folder_path)
            msg = "\t\tCreated backup folder: {}".format(backup_folder_path)
            print(msg)

        backup_file_path = backup_folder_path + "/" + file_name

        shutil.copy2(source_file, backup_file_path)
        msg2 = "\t\tbackup copied to {}".format(backup_folder_path)
        print(msg2)

    if delete_source:
        if os.path.exists(target_file_path):
            os.remove(source_file)
            msg = "\t\tRemoved source file: {}".format(target_file_path)
            print(msg)
