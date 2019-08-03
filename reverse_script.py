import os, sys
import re
import json

# DESCRIPTION
# We are launching script from the command line 
# Taking the name of the file with the dictionary (json) from the command
# Reversing dictionary
# Writing the result to the file (the name of the file present in system variable)

# reverting dictionary (changing keys with values)
def reversing_dict(dictionary):
    result_dict = {}
    buffer = []
    for key, value in dictionary.items():
        if value not in result_dict.keys(): #adding new entry if it is a new key
            result_dict[value] = key
        else:   #adding new value to the existed one to the same key
            buffer = list(result_dict[value])
            buffer.append(key)
            result_dict[value] = buffer
    return result_dict

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

try:
    # reading command
    source_file_path = sys.argv[1]
    # reading file and reverd dictionary
    if os.path.exists(source_file_path):
        source_file = open(source_file_path, 'r')
        # substitute (') for  (") to allow json.loads not to provoke exeptions
        soursed_dictionary_str = re.sub("\'", "\"", source_file.read()) 
        reversed_dictionary = reversing_dict(json.loads(soursed_dictionary_str))    #reverting dictionary
        # writing reverted dictionary to the file
        try:
            resulted_file = open(os.environ['REVDICTPATH'], 'w')
            resulted_file.write(json.dumps(reversed_dictionary))
            print("File with results is here: " + os.environ['REVDICTPATH'])
        except:
            print('File not found, we have wrote nothing')
        finally:
            resulted_file.close()  
        source_file.close() 
    else:
        print('File does not exist')
except:
    print("PLease enter name of the data file")
# deleting env variable (don't want to have it in system)
del os.environ['REVDICTPATH']




