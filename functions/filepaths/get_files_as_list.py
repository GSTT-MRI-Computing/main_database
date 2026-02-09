import os

def get_files_as_list(path, file_type):
    outputs = []
    files = os.listdir(path)
    for file in files:
        if file.lower().endswith(file_type.lower()) and '.ds_store' not in file.lower():
            outputs.append(os.path.join(path, file))
    return outputs

