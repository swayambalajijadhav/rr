
from asyncore import write
import os
from threading import local
import dropbox
from dropbox.files import WriteMode
 
class TransferData:
    def __init__(self, access_token):
        self.access_token = access_token

    def upload_file(self, file_from, file_to):
       
        dbx = dropbox.Dropbox(self.access_token)

        for root, dirs, flies in os.walk(file_from):

            for filename in files:

                local_path = os.path.join(root,filename)

                relative_path = os.path.relpath(local_path, file_from)
                dropbox_path = os.path.join(file_to,relative_path)

                with open(local_path , 'rb') as f:
                    dbx.files_upload(f.read(), dropbox_path, mode=WriteMode('overwrite'))


def main():
    access_token = 'sl.BKX_FlmyEWUxEJoCyYuvW7aCVcsk90YvtTH93VXObvB6nacGevQTsDDA8Ny6-MhS_Rd2Ka6FQJuF3Ex6QMcry3oAu9O9KYSzVahLB6iPIB1PMrhSNG0M_xuRF3m0iN2FWNlQX53qJ0EP'
    transferData = TransferData(access_token)

    file_from = str(input("Enter the folder path to transfer: "))
    file_to = input("Enter the path to upload to Dropbox: ")


    transferData.upload_file(file_from,file_to)
    print("file has moved")

main()



