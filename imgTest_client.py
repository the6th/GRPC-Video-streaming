from __future__ import print_function

import grpc
import cv2
import imageTest_pb2
import imageTest_pb2_grpc
import skvideo.io
import skvideo.datasets

URL = "./Resouces/movie.mp4"

def run():
    TestPlayMovie()
    # TestImageShow()
    # channel = grpc.insecure_channel('127.0.0.1:8080')
    # stub = imageTest_pb2_grpc.ImageTestStub(channel)
    # #temp = cv2.imread('/home/nirvan/img_one.png')
    # for response in stub.Analyse( generateRequests() ):
    #     print(str(response.reply))


def generateRequests():
    videogen = skvideo.io.vreader(URL)
    i=0
    cnt = 1
    for frame in videogen:
        
        if(cnt == 5):
            cnt = 1
        else:
            cnt+=1
            continue
        
        frame = cv2.cvtColor( frame, cv2.COLOR_RGB2GRAY )
        frame = bytes(frame)
        yield imageTest_pb2.MsgRequest(img= frame)

def TestImageShow():
    img = cv2.imread("./Resouces/image.png")
    cv2.imshow('image',img)
    cv2.waitKey(0)
    cv2.destroyAllWindows()

def TestPlayMovie():

    videodata = skvideo.io.vread(skvideo.datasets.bigbuckbunny())
    print(videodata.shape)

    for frame in videodata:
        print(frame.shape)
        cv2.imshow('image',frame)
        key = cv2.waitKey(33)#pauses for 3 seconds before fetching next image
        if key == 27:#if ESC is pressed, exit loop
            cv2.destroyAllWindows()
            break

if __name__ == '__main__':
  run()
