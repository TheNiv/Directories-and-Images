# -*- coding: utf-8 -*-
"""
Created on Mon Oct 26 11:39:36 2020

@author: Niv Lifshitz
"""
import os
import cv2
import matplotlib.pyplot as plt
import numpy as np


IMG_PATH = r"C:\Users\Niv Lifshitz\Desktop\ImagesWork"  #The path to the image directory
PATH_TO_SAVE = r"C:\Users\Niv Lifshitz\Desktop"  #The default path to save the directory with the images in

def create_dir(path ,dir_name):
    """
    Parameters:
    path: (string) a path to a directory
    dir_name: (string) the name of the directory to create
    -------------------
    Creates a new directory with the name dir_name and test and train directories inside it
    if a directory with this name does not already exists
    """
    new_path = path + '/' + dir_name
    try:
        os.mkdir(new_path)  #מייצר את התיקיה בעלת השם name
        os.mkdir(new_path+'/test') #creat the directory test inside name
        os.mkdir(new_path+'/train')#creat the directory train inside name
    except OSError:
        print ("Creation of the directories failed, you already have such directory")
    else:
        print ("Successfully created the directories")
               
    
def save_file_in(path,file_name):
    """
    Parameters:
    path: (string) a path to a directory
    file_name: (string) the name of the image to save
    
    Saves the image named file_name to the path if there are no other files with the same name already
    """
    img = cv2.imread(os.path.join(IMG_PATH,file_name))  
    if not os.path.exists(os.path.join(path,file_name)):
        cv2.imwrite(os.path.join(path,file_name),img)
    else:
        print(f"Image with the name: {file_name} already exists in: {path}")


def plot_images(images):
    """
    images: a list of images represented as numpy arrays
    
    The function plots each image in the list images
    """
    #plots the images in the list images
    f ,axs = plt.subplots(len(images))
    for i in range(len(images)):
        axs[i].imshow(images[i])
    plt.tight_layout()
    plt.show()


def path_exists(path):
    """
    path: a string of a path to a file or a directory
    
    Returns true if the path exists,and false otherwise
    """
    return os.path.exists(path)
        

def main():
    path = input("Enter the path you want to save in:")
    path = path  if path_exists(path) else PATH_TO_SAVE  #the path to save the images in
    create_dir(path,'dataset')  #create the dataset directory
    path_to_save = os.path.join(path +'\dataset','train')
    image_paths = os.listdir(IMG_PATH)
    images = [cv2.imread(os.path.join(IMG_PATH,filename)) for filename in image_paths] # a list of numpy arrays that represent the pixels of the images
    for img in image_paths:  #saving each image in the directory
        save_file_in(path_to_save,img)
    plot_images(images)  #shows the images


if __name__ == "__main__":
    main()
