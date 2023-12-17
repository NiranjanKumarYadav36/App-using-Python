import zipfile


def extract_archive(archive_path, dest_dir):
    with zipfile.ZipFile(archive_path, 'r') as file:
        file.extractall(dest_dir)


if __name__ == "__main__":
    extract_archive("output.zip", r"C:\Users\ANIL KUMAR YADAV\python app\ToDo-List-App\File_Extractor\files")
