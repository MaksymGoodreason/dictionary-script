import os
import sys
import re
import json
import argparse


def reversing_dict(dictionary):
    """this function turns the dictionary inside out"""
    result_dict = {}
    buffer = []
    for key, value in dictionary.items():
        if value not in result_dict: # adding new entry if it is a new key
            result_dict[value] = key
        else:   # adding new value to the existed one to the same key
            buffer = list(result_dict[value])
            buffer.append(key)
            result_dict[value] = buffer
    return result_dict

if __name__ == "__main__":
    # set up a path to the reseult file as constanta 
    # (to allow launch it on any Win PC)
    RESULT_FILE_PATH = os.environ["TEMP"] + '\\resulted_dictionary.json'

    # checking if such environmental variable is present is the system
    # writing needed path to it if yes
    # adding a new entry to the mapping if not
    if 'REVDICTPATH' in os.environ:
        file_path_env = os.environ['REVDICTPATH']
    else:
        os.environ['REVDICTPATH'] = RESULT_FILE_PATH

    # parsing  command 
    my_parser = argparse.ArgumentParser(description='Path to the json file with dictionary that should be reverted')
    my_parser.add_argument('Path',
                           type=str,
                           help='input path to the json file')
    args = my_parser.parse_args()

    # reading the file and reverting json
    try:        
        source_file_path = args.Path
        if os.path.exists(source_file_path):
            source_file = open(source_file_path, 'r')
            # substitute (') for  (") to allow json.loads not to provoke exeptions
            sourced_dictionary_str = re.sub("\'", "\"", source_file.read()) 
            reversed_dictionary = reversing_dict(json.loads(sourced_dictionary_str))    # reverting dictionary
            # writing reverted dictionary to the file
            with open(os.environ['REVDICTPATH'], 'w') as resulted_file:
                resulted_file.write(json.dumps(reversed_dictionary))
                print("File with results is here: " + os.environ['REVDICTPATH'])
            source_file.close() 
        else:
            print('File does not exist')
    except:
        print("Please enter name of the data file")
 
    # deleting env variable (don't want to have it in system)
    del os.environ['REVDICTPATH']