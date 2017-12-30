import os

path = os.getcwd()

accepted_extensions = ['.mp3','.wav']

def get_songs_list():
    return [i for i in os.listdir(os.path.join(path,'Music')) if os.path.splitext(i)[1] in accepted_extensions]
