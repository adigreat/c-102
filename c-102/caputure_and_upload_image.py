import cv2
import dropbox
import time
import random


start_time=time.time()

def take_snapshot():
    number=random.randint(0,100)
    videoCaptureObject=cv2.VideoCapture(0)
    result=True
    while(result):
        ret,frame=videoCaptureObject.read()
        image_name="img"+str(number)+".png"
        cv2.imwrite(image_name,frame)
        start_time=time.time
        result=False
    return img_name
    print("snapshot taken") 
    videoCaptureObject.release()
    cv2.destroyallwindows()

def upload_file(img_name):
    access_token="-RkLnZlOqgAAAAAAAAAALbnRb4n1kTjH1QIw902dSL7qSL4iUJ_8kFLmAN0As9Zw"       
    file=img_counter 
    file_from=file
    file_to="/newfolder1/"+(img_name)
    dbx=dropbox.Dropbox(access_token)

    with open(file_from,'rb') as f:
        dbx.files_upload(f.read(),file_to,mode=dropbox.files.WriteMode.overwrite)
        print("file space uploaded")

def main():
    while(True):
        if((time.time()-start_time)>=300):
            name=take_snapshot()
            upload_file(name)

main()            

