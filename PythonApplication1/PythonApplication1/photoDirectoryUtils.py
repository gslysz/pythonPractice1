import os
import datetime
import calendar
import time
import glob


def create_month_folders(year_folder_path):
    dir_exists = os.path.exists(year_folder_path)
    if dir_exists:
        index_vals = list(range(1, 13, 1))

        for i in index_vals:
            month = calendar.month_abbr[i]
            padded_month_num = str(i).zfill(2)
            month_folder_text = "{}-{}".format(padded_month_num, month)

            month_folder_path = year_folder_path + "/" + month_folder_text
            month_folder_exists = os.path.exists(month_folder_path)
            if not month_folder_exists:
                os.mkdir(month_folder_path)
                print("Created the folder: " + month_folder_path)


def organize_files(source_folder_path, target_year_folder_path):
    source_exists = os.path.exists(source_folder_path)
    if not source_exists:
        msg = "Cannot organize files. Source path does not exist. Source=" + source_folder_path
        print(msg)
        return
    if not os.path.exists(target_year_folder_path):
        msg = "Created target year folder: " + target_year_folder_path
        print(msg)
        os.mkdir(target_year_folder_path)

    all_files = os.listdir(source_folder_path)
    filtered_files = []

    for f in all_files:
        f_lower = f.lower()
        if f_lower.endswith(".jpg") or f_lower.endswith(".mp4") or f_lower.endswith(".mov"):
            filtered_files.append(f_lower)

    for f in filtered_files:
        last_mod = time.ctime(os.path.getmtime(source_folder_path + "//" + f))
        #created_time = os.path.getctime(f)
        print("File to be copied = " + f + "\t\tlast mod= " + last_mod)

        #print("Will copy the following file: " + f + "; last mod= " + last_mod + "; created = " + created_time)












