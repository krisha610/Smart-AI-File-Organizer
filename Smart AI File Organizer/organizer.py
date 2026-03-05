import os
import shutil
from ai_classifier import ai_categorize

def organize_files(folder):

    for file in os.listdir(folder):

        file_path = os.path.join(folder, file)

        if os.path.isfile(file_path):

            category = ai_categorize(file)

            category_folder = os.path.join(folder, category)

            os.makedirs(category_folder, exist_ok=True)

            destination = os.path.join(category_folder, file)

            shutil.move(file_path, destination)

    print("Files Organized Successfully 🚀")