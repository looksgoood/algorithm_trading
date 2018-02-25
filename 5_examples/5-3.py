import os

def get_text_list(path):
    files = os.listdir(path)
    for file in files:
        if file.endswith('.py'):
            print(file)

get_text_list('.')