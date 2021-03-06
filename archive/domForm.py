import cv2, time
import numpy as np
import threading
import listening
import connect

channel = connect.join()

def transform( image ):
    img = cv2.imread(image, 0)

    # resize img for transform
    img = cv2.resize(img, (16,24), interpolation = cv2.INTER_NEAREST)

    # add img together x3 for total transform
    img = np.concatenate((img, img, img), axis=1)

    # flatten array
    img = img.flatten()

    # stringify for server
    transformSend = ""
    for ele in img:
        transformSend+=(" "+str(ele))

    # if you want to look at the numbers :)
    print (transformSend)

    # uncomment this to send to server
    channel.push("input",{"body": transformSend})

def everything():
    print ('everything')
    transform('./img/everything.png')

def links():
    print ('links')
    transform('./img/links.png')

def headings():
    print ('headings')
    transform('./headings.jpg')

def images():
    print ('images')
    transform('./images.jpg')


def listen(function, keyword):
    print ('listening for' + keyword)
    listening.recognition(function, keyword, True)

if __name__ == "__main__":
    t0 = threading.Thread(target = listen, args=(everything,'everything'))
    t1 = threading.Thread(target = listen, args=(links,'links'))
    t2 = threading.Thread(target = listen, args=(headings,'headings'))
    t3 = threading.Thread(target = listen, args=(images, 'images'))
    t0.start()
    time.sleep(5)
    t1.start()
    time.sleep(5)
    t2.start()
    time.sleep(5)
    t3.start()