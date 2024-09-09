import os

def check_file_lines(directory):
    for filename in os.listdir(directory):
        if filename.endswith(".txt"): 
            filepath = os.path.join(directory, filename)
            with open(filepath, 'r') as file:
                lines = file.readlines()
                if len(lines) != 3:
                    print(f"File {filename} has {len(lines)} lines.")

directory_path = 'data/protext/proxd_train/context_versions/batch_10'  # REPLACE PATH
check_file_lines(directory_path)

