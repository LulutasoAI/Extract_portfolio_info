import pickle 
import datetime 
import os 

def get_currenttime_numeral():
        d = datetime.datetime.now().strftime('%Y%m%d')
        return d

def create_folder_if_None_exists(name):
    if not os.path.exists(name):
        os.makedirs(name)
        print("The folder named '{}' had not existed so I created it.".format(name))
    else:
        print("The folder named '{}' already exists so nothing was executed.".format(name))

def pickle_object(object):
    save_folder = "data_archive"
    create_folder_if_None_exists(save_folder)
    filename = (os.path.join(save_folder,"history.sav"))
    pickle.dump(object,open(filename,"wb"))

def load_object():
    save_folder = "data_archive"
    filename = (os.path.join(save_folder,"history.sav"))
    with open(filename, mode="rb") as f:
        data_loaded = pickle.load(f)
    return data_loaded

def add_data(info_):
    try:
        data = load_object()
    except:
        data = {}
    d = get_currenttime_numeral()
    data[d] = info_
    pickle_object(data)
