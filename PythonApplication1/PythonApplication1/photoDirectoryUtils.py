import os
import datetime
import calendar


def create_month_folders(yearFolderPath):
    dir_exists = os.path.exists(yearFolderPath)
    if dir_exists:
        indexVals = list(range(1, 13, 1))

        for i in indexVals:
            month = calendar.month_abbr[i]
            padded_month_num = str(i).zfill(2)
            month_folder_text = "{}-{}".format(padded_month_num, month)

            month_folder_path = yearFolderPath + "/" + month_folder_text
            month_folder_exists = os.path.exists(month_folder_path)
            if not month_folder_exists:
                os.mkdir(month_folder_path)
                print("Created the folder: " + month_folder_path)








