#!/usr/bin/python

import os
import datetime
import time
import subprocess
import glob
import TransferUtils

print "\n########################################"
print "## Starting RECO Data Distribution      ##"
print "##########################################\n"

#You need to change this the kerberos principal being used
user = "sxie"

#Change to the location disk location
LocalDataLocation = "/data2/"

#change to name of the testbeam campaign directory
CampaignDirectoryName = "2019_04_April_CMSTiming"


continueLoop = True
while continueLoop : 

    print "\n########################################"
    print "## Starting a new data transfer cycle   ##"
    print "Time: ", str(datetime.datetime.now())
    print "##########################################\n"


    #Copy VME Raw Data from ftbf-daq-08
    print "\n\n"
    print "\n##########################################"
    print   "Transferring VME Raw Data from ftbf-daq-08"
    print   "##########################################\n"
    command = "rsync -uv --progress otsdaq@ftbf-daq-08.fnal.gov:/data/TestBeam/"+CampaignDirectoryName+"/CMSTiming/* " + LocalDataLocation+CampaignDirectoryName+"/VME/RawData/"
    print command
    os.system(command)
    time.sleep(0.5)

    
    #Copy VME RECO Data to CMSLPC EOS
    print "\n\n"
    print "\n##########################################"
    print   "Transferring VME RECO Data to CMSLPC EOS"
    print   "##########################################\n"
    TransferUtils.XrdCopyLocalToRemote("cmseos.fnal.gov", 
                                       "/store/group/cmstestbeam/" + CampaignDirectoryName + "/VME/RecoData/RecoWithTracks/",
                                       LocalDataLocation+CampaignDirectoryName+"/VME/RecoData/RecoWithTracks/")
    time.sleep(0.5)

    
    #Copy DT5742 RECO Data to CMSLPC EOS
    print "\n\n"
    print "\n##########################################"
    print   "Transferring DT5742 RECO Data to CMSLPC EOS"
    print   "##########################################\n"
    TransferUtils.XrdCopyLocalToRemote("cmseos.fnal.gov", 
                                       "/store/group/cmstestbeam/" + CampaignDirectoryName + "/DT5742/RecoData/RecoWithTracks/",
                                       LocalDataLocation+CampaignDirectoryName+"/DT5742/RecoData/RecoWithTracks/")
    print command
    os.system(command)
    time.sleep(0.5)

 
    #Copy KeysightScope RECO Data to CMSLPC EOS
    print "\n\n"
    print "\n###################################################"
    print   "Transferring KeysightScope RECO Data to CMSLPC EOS"
    print   "##################################################\n"
    TransferUtils.XrdCopyLocalToRemote("cmseos.fnal.gov", 
                                       "/store/group/cmstestbeam/" + CampaignDirectoryName + "/KeySightScope/RecoData/RecoWithTracks/",
                                       LocalDataLocation+CampaignDirectoryName+"/KeySightScope/RecoData/RecoWithTracks/")
    time.sleep(0.5)

 
