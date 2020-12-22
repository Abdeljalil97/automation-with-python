import argparse
import os
from bs4 import UnicodeDammit
def search_txt(filename, word):
    '''
    Search the word in a text file
    '''
    # Detect the encoding
    with open(filename, 'rb') as file:
        content = file.read(1024)

    suggestion = UnicodeDammit(content)
    encoding = suggestion.original_encoding

    # Open and read
    with open(filename, encoding=encoding) as file:
        for line in file:
            if word in line.lower():
                return True

    return False
    
EXTENSIONS ={
    'txt': search_txt,
    'csv': search_csv,
    'pdf': search_pdf,
    'docx': search_docs
}
def main(word):
    #crawling and seraching directories
    for root, dirs, files in os.walk('.'):
        for file in files:
            extension = file.split('.')[-1]
            if extension in EXTENSIONS:
                search_file = EXTENSIONS.get(extension)
                full_file_path = os.path.join(root, file)
                if search_file(full_file_path, word):
                    print(f'>>> Word found in {full_file_path}')



    
if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument('-w',type=str, help='word to search ')
    args= parser.parse_args()
    main(args.w.lower())