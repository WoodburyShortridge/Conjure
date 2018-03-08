import cv2
import numpy as np
from occamy import Socket

# uncomment this below to connect to server room
socket = Socket("ws://dlevs.me:4000/socket")
socket.connect()

channel = socket.channel("room:lobby", {})
channel.on("connect", print ('Im in'))
channel.on("new_msg", lambda msg, x: print("> {}".format(msg["body"])))

channel.join()

while(1):
    moreGoods = input('Do you want to purchase more of my goods?: ').lower()
    if moreGoods == 'yes':
        print ("Too bad! You have to say yes for this demo to work :)")

    elif moreGoods == 'no':

        # load image
        img = cv2.imread('img/jesperswind.jpg', 0)

        # resize img for transform
        img = cv2.resize(img, (16,24), interpolation = cv2.INTER_NEAREST)

        # add img together x3 for total transform
        img = np.concatenate((img, img, img), axis=1)

        # uncomment this to see image
        '''
        cv2.imshow('image', img)
        cv2.waitKey()
        '''

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


        print ("Well then, you're ready to start. Good luck! You have a long and difficult journey ahead of you.")

    else:
        print ("I'll take a yes or a no please")

cv2.destroyAllWindows()