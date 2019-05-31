import os
import time
import random
from os import listdir
from os.path import isfile, join
from random import randint
from InstagramAPI import InstagramAPI

PhotoPath = os.path.join(os.getcwd(), 'Images') # Change Directory to Folder with Pics that you want to upload
IGUSER = "UserName"  # Change to your Instagram USERNAME
PASSWD = "UserPassword"  # Change to your Instagram Password
# Change to your Photo Hashtag
IGCaption = ["follow friends English, हिंदी, रोचक तथ्य तथा और भी मज़ेदार पोस्टों के लिए हमें फॉलो करे! | रोजाना 50 पोस्टों Follow Admin @panditjiwebsite #diplyfacts #_diplyfacts #paheli #rochaktathya #facts #amazingfacts #rochaktathya #gyanopedia #gyankibaat #gyaanpandit #gk #generalknowledgeindia #currentaffairs #paheli",
			 "follow friends English, हिंदी, रोचक तथ्य तथा और भी मज़ेदार पोस्टों के लिए हमें फॉलो करे! | रोजाना 50 पोस्टों Follow Admin @panditjiwebsite #diplyfacts #_diplyfacts #hindifact #interestingfacts #facts #tejujangid #amazingfacts #rochaktathya #interestingfacts #facts #amazingfacts #rochaktathya #gyanopedia",
			 "follow friends English, हिंदी, रोचक तथ्य तथा और भी मज़ेदार पोस्टों के लिए हमें फॉलो करे! | रोजाना 50 पोस्टों Follow Admin @panditjiwebsite #_diplyfacts #diplyfacts #gyankibaat #gyaanpandit #gk #tejujangid #generalknowledgeindia #currentaffairs #paheli #hindi #ias #ips #ssc #cgl #upsc #girls #wikipedia #facebook",
			 "follow friends English, हिंदी, रोचक तथ्य तथा और भी मज़ेदार पोस्टों के लिए हमें फॉलो करे! | रोजाना 50 पोस्टों Follow Admin @panditjiwebsite #_diplyfacts #diplyfacts #gyaanpandit #hindi #facts #factsfacts #currentaffairs #amazingfacts #gyanopedia #gyankibaat #gk #tejujangid #generalknowledgeindia #interestingfacts",
			 "follow friends English, हिंदी, रोचक तथ्य तथा और भी मज़ेदार पोस्टों के लिए हमें फॉलो करे! | रोजाना 50 पोस्टों Follow Admin @panditjiwebsite #diplyfacts #_diplyfacts #currentaffairs #genera ! #knowledge #mppsc #ibps #bankpo #rochaktathya #indianadministrativeservices #ssccal #hindifactopedia #navy #defence #gk #indian #sarkarinaukri #facts #chsl",
			 "follow friends English, हिंदी, रोचक तथ्य तथा और भी मज़ेदार पोस्टों के लिए हमें फॉलो करे! | रोजाना 50 पोस्टों Follow Admin @panditjiwebsite #diplyfacts #_diplyfacts #prelims #indianarmy #hindifacts #tathyopedia #hindiquotes #hindigk #govtjobs #hindiquotes #loveh indi #hindifacts #hindilover #fishing #fisheriesstudent",
			 "follow friends English, हिंदी, रोचक तथ्य तथा और भी मज़ेदार पोस्टों के लिए हमें फॉलो करे! | रोजाना 50 पोस्टों Follow Admin @panditjiwebsite #diplyfacts #_diplyfacts #hindifacts #hindifact #randomfacts #instafacts #rochaktathya #amazingfacthindi #rochakhindifact #hindifactstation #hindifactopedia #hindiknowledge",
			 "follow friends English, हिंदी, रोचक तथ्य तथा और भी मज़ेदार पोस्टों के लिए हमें फॉलो करे! | रोजाना 50 पोस्टों Follow Admin @panditjiwebsite #diplyfacts #_diplyfacts #hindifact #india #indiafacts #factaboutindia #hindigk #hindigyan #gajabhindi #hindifacts #hindifact #randomfacts #instafacts #rochaktathya #amazingfacthindi #rochakhindifact",
			 "follow friends English, हिंदी, रोचक तथ्य तथा और भी मज़ेदार पोस्टों के लिए हमें फॉलो करे! | रोजाना 50 पोस्टों Follow Admin @panditjiwebsite #diplyfacts #_diplyfacts #hindifactstation #hindifactopedia #hindiknowledge #hindifact #india #indiafacts #factaboutindia #hindigk #hindigyan",
			 "follow friends English, हिंदी, रोचक तथ्य तथा और भी मज़ेदार पोस्टों के लिए हमें फॉलो करे! | रोजाना 50 पोस्टों Follow Admin @panditjiwebsite #diplyfacts #_diplyfacts #hindifacts #hindifact #randomfacts #instafacts #rochaktathya #amazingfacthindi #rochakhindifact #hindifactstation #hindifactopedia #hindiknowledge",
			 "follow friends English, हिंदी, रोचक तथ्य तथा और भी मज़ेदार पोस्टों के लिए हमें फॉलो करे! | रोजाना 50 पोस्टों Follow Admin @panditjiwebsite #diplyfacts #_diplyfacts #hindifact #india #indiafacts #factaboutindia #hindigk #hindigyan #fun_fact #hinditathya"]
os.chdir(PhotoPath)
ListFiles = sorted([f for f in listdir(PhotoPath) if isfile(join(PhotoPath, f))])
print(ListFiles)
print("Total Photo in this folder:" + str(len(ListFiles)))

# #Start Login and Uploading Photo
igapi = InstagramAPI(IGUSER, PASSWD)
igapi.login()  # login

for i, _ in enumerate(ListFiles):
    try:
        captions = IGCaption[randint(0, len(IGCaption)-1)]
        photo = ListFiles[i]
        print("Progress :" + str([i + 1]) + " of " + str(len(ListFiles)))
        print("Now Uploading this photo to instagram: " + photo)
        igapi.uploadPhoto(photo, caption=captions, upload_id=None)
        os.remove(photo)
        # sleep for random between 60 - 120s
        n = randint(69, 72)
        print("Sleep upload for seconds: " + str(n))
        time.sleep(n)
    except Exception as e:
        try:
            photo = ListFiles[i]
            os.remove(photo)
            print(e)
        except Exception as e:
            print(e)
