import requests
from pprint import pprint

class YaUploader:
    def __init__(self, token: str):
        self.token = token

    def upload(self, file_path: str):
        API_BASE_URL = 'https://cloud-api.yandex.net/'
        headers = {
            'content-type': 'application/json',
            'accept': 'application/json',
            'authorization': f'OAuth {uploader.token}'
        }
        files_list = requests.get(API_BASE_URL + 'v1/disk/resources/upload', params={'path': 'new/' + file_path}, headers=headers)
        pprint(files_list.json())
        pprint(files_list)
        files = files_list.json()['href']
        with open(file_path, 'rb') as file:
            upload_files = requests.put(files, data=file)
            print(upload_files)

if __name__ == '__main__':
    path_to_file = ''
    token = ''
    uploader = YaUploader(token)
    result = uploader.upload(path_to_file)


