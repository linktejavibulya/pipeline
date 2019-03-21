#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Mar 21 12:26:07 2019
A script to create dictionary of scan sessions for feeding into fmriprep
Then convert DICOM to NIFTI.GZ, and organize files according to BIDS

@author: Or Duek, Ruonan Jia
"""

#%% import library
import os
import glob

#%% function. 
# It calls other functions. Should first load them in creatBIDS.py by Or
def fullBids(subNumber, sessionDict, output_dir):
    subName = 'sub-' + subNumber
  #  folder_name = ['anat','func','dwi','other']
    
    for i in sessionDict:
        session = i
        source_dir = sessionDict[i]
        print (session, source_dir)
        fullPath = os.path.join(output_dir, subName, session)
        print(fullPath)
        convert(source_dir,  output_dir, subName, session)
        organizeFiles(output_dir, subName, session)        
        
#%% grab all subject folders
folder = glob.glob('/media/Drobo/Levy_Lab/Projects/R_A_PTSD_Imaging/Data/Scans/Multiband/subj*/*_levy')

#%% create a list of dictionary

# list of subject ID
sub_id = [] # each element is a subject id, the order is matched with session_dict
for sub_idx in range(len(folder)):
    sub_folder = folder[sub_idx].split('subj')
    subject = sub_folder[1].split('/')
    sub_id.append(subject[0])
# get unique elemets    
sub_id = list(set(sub_id))

# session dictionary
session_dict = [] # each element is a dictionary, for a single subject
for sub_idx in range(len(sub_id)): 
    session_count = 0
    subject_id = sub_id[sub_idx]
    session_dict_sub = {}
    for i in folder:        
        if i.find(subject_id)!=-1:
            session_count = session_count + 1
            print(i)
            session_dict_sub.update({'ses-%s' % session_count: i})
    session_dict.append(session_dict_sub)

# check number of subject, and number of dictionary list
len(sub_id)
len(session_dict)
# check if sub_id and session_dict matched by subject id
idx = 49
print(sub_id[idx])
print(session_dict[idx])
    
#%% for converting individual subject
sessionDict = {
        'ses-1': '/media/Drobo/Levy_Lab/Projects/R_A_PTSD_Imaging/Data/Scans/Multiband/subj3/ta8967_levy',
        'ses-2': '/media/Drobo/Levy_Lab/Projects/R_A_PTSD_Imaging/Data/Scans/Multiband/subj3/ta8996_levy'
        }
subNumber = '3'

output_dir = '/media/Data/R_A_PTSD/data_bids_converted/' 

fullBids(subNumber, sessionDict, output_dir)

#%% convert
output_dir = '/media/Data/R_A_PTSD/data_bids_converted/' 

for sub_idx in range(len(sub_id)):
    subject_id = sub_id[sub_idx]
    
    if subject_id != '3': # subjec 3 already converted
        fullBids(subject_id, session_dict[sub_idx], output_dir)
        










