# from PyPDF2 import PdfReader
# import re
# reader = PdfReader("dummy_fixed.pdf")
# number_of_pages = len(reader.pages)
# print((number_of_pages))
# page = reader.pages[0]
# text = page.extract_text()
# print(text)
#

from bs4 import BeautifulSoup
#
# import requests
# import re
# URL = "https://www.geeksforgeeks.org/"
# r = requests.get(URL)
# con=r.content
# remove=re.sub('\s+',' ','\n'+str(con.rstrip()))
#
# print(remove)


# import re
# import docx2txt
# text = docx2txt.process("doc.docx")
# # print((text))
# remove=re.sub('\s+',' ',text.rstrip())
#
# print(remove)

# importing required modules
# import PyPDF2
#
# # creating a pdf file object
# pdfFileObj = open('dummy.pdf', 'rb')
#
# # creating a pdf reader object
# pdfReader = PyPDF2.PdfFileReader(pdfFileObj)
#
# # printing number of pages in pdf file
# print(pdfReader.numPages)
#
# # creating a page object
# pageObj = pdfReader.getPage(0)
#
# # extracting text from page
# print(pageObj.extractText())
#
# # closing the pdf file object
# pdfFileObj.close()

# import requests
# from bs4 import BeautifulSoup
# import re
# URL = "http://www.values.com/inspirational-quotes"
# r = requests.get(URL)
#
# soup = BeautifulSoup(r.content, 'html5lib')  # If this line causes an error, run 'pip install html5lib' or install html5lib
#
# text=soup.prettify()
# # remove=re.sub('<[^<]+?>', '', text)
# print(text)

# from selenium import webdriver
# from selenium.webdriver.chrome.options import Options
# from webdriver_manager.chrome import ChromeDriverManager
#
# options = Options()
# options.headless = True
#
# # 3
# driver = webdriver.Chrome(ChromeDriverManager().install(), options=options)
#
# # 4
# driver.get('https://www.w3schools.com/')
# driver.save_screenshot('screenshot.png')
#
# # 5
# driver.quit()

# importing library
# from googlesearch import search
#
# # enter website name
# website = input('Enter website: ')
# # enter query
# query = input('Enter query: ')
# # initilazing index=0
# index = 0
#
# # search will return an object containing
# # all url from google search results
# # here, tid is top level domain,
# # stop means how many search results you want
# # stop=100 means we will get top 100 results from google
# for i in search(query, tld="com", num=10, stop=100, pause=2):
#   # checking website in results
#   if website in i:
#       # printing index of website and url
#       print(index+1, i)
#   index+=1

# from scipy import misc,ndimage
# from matplotlib import pyplot as plt
#
# face = misc.face()
# blurred_face = ndimage.gaussian_filter(face, sigma=3)
#
# fig, ax = plt.subplots(1, 2, figsize=(16, 8))
#
# ax[0].imshow(face)
# ax[0].set_title("Original Image")
# ax[0].set_xticks([])
# ax[0].set_yticks([])
# ax[1].imshow(blurred_face)
# ax[1].set_title("Blurred Image")
# ax[1].set_xticks([])
# ax[1].set_yticks([])



# import cv2
# import numpy as np
# import matplotlib.pyplot as plt
#
# image = cv2.imread(r"screenshot.png", 1)
# # Loading the image
#
# half = cv2.resize(image, (0, 0), fx = 0.1, fy = 0.1)
# bigger = cv2.resize(image, (1050, 1610))
#
# stretch_near = cv2.resize(image, (780, 540),interpolation = cv2.INTER_LINEAR)
#
#
# Titles =["Original", "Half", "Bigger", "Interpolation Nearest"]
# images =[image, half, bigger, stretch_near]
# count = 4
#
# for i in range(count):
# 	plt.subplot(2, 2, i + 1)
# 	plt.title(Titles[i])
# 	plt.imshow(images[i])
#
# plt.show()



from PIL import Image, ImageFilter

image = Image.open('pc.jpg')
print(f"Original size : {image.size}") # 5464x3640

option=input("Enter name of function")
if option=="Pixel":
    print("Pixel")
elif option=="Inch":
    print("Inch")
elif option=="Centi":
    print("Centimeter")

def Pixel(height,width):
    sunset_resized = image.resize((height, width))
    pixel=sunset_resized.save("sunset-aspect_size500.jpeg")
    return pixel
height = int(input("Enter height"))
width = int(input("Enter width"))
Pixel(height,width)

def Inch(toinch1,toinch2):
    cal1=float(toinch1*96)
    cal2=float(toinch2*96)
    sunset_resized = image.resize((int(cal1),int(cal2)))
    sunset_resized.save("sunset-aspect_inch.jpeg")
    return cal1,cal2
toinch1=float(input("enter Height: "))
toinch2=float(input("enter Width"))
Inch(toinch1,toinch2)

def Centi(centi1,centi2):
    total1=float(centi1/96)*2.54
    total2=float(centi2/96)*2.54
    sunset_resized = image.resize((int(total1), int(total2)))
    sunset_resized.save("sunset-aspect_centi.jpeg")
    return total1,total2
centi1=float(input("Enter Height"))
centi2=float(input("Enter Height"))
Centi(centi1,centi2)


####---------------------image Thumbnill
# image.thumbnail((400, 400))
# image.save("sunset-aspect_dipi300.jpeg", dpi=(300.0, 300.0))
# image.save("sunset-aspect_dpuser.jpeg", dpc=(x, y))

####--------------------image Crop
# Crop the image
# box = (300, 300, 700, 900)
# cropped_image = image.crop(box)
# cropped_image.save('cropped-image.jpg')

# -------------------400x600 size of the image
# print(cropped_image.size)

####-----------------------Jpg to png
# im1 = Image.open(r'sunset_400.jpeg')
# im1.save(r'covert.png')


####------------------Jpg to png
# im1 = Image.open(r'covert.png')
# im1.save(r'covertpng.jpg')


####--------------------webp extension
# im1 = Image.open(r'sunset-aspect.jpeg').convert("RGB")
# im1.save('covertwebp.webp', "webp")

####--------------------------Crop image
# cropped_img = image.crop((300, 150, 700, 1000))
# print(cropped_img.size)
# cropped_img.show()
# low_res_img = cropped_img.resize(
#     (cropped_img.width // 4, cropped_img.height // 4))
# low_res_img.show()

####---------------------------Grayscale image
# filename = "pc.jpg"
# with Image.open(filename) as img:
#     img.load()
#
# cmyk_img = img.convert("CMYK")
# cmyk_img.show()
# gray_img = img.convert("L")  # Grayscale
# gray_img.show()


####--------------------------Convert Blur image
# im1 = image.filter(ImageFilter.BoxBlur(4))
# Shows the image in image viewer
# im1.show()

####------------------transparency
# image = Image.open('pc.jpg')
# image.putalpha(128)
# image.save('pillow_putalpha_solid.png')





#####----------------------------Tikenter
# import required modules
from tkinter import *
from tkinter import filedialog as fd
import os
from PIL import Image
from tkinter import messagebox

# create TK object
# root = Tk()

# naming the GUI interface to image_conversion_APP
# root.title("Image_Conversion_App")

####------------------------Merging
# importing Image class from PIL package
from PIL import Image

# creating a object
# image = Image.open(r"pc.jpg")
# image.load()

# Splitting the image into individual
# bands
# r, g, b, = image.split()

# merge function used
# im1 = Image.merge('RGB', (g, b, r))
# im1.show()
#

####-------------------------Merging 2 or more images
# from PIL import Image
#
# img_01 = Image.open("screenshot.png")
# img_02 = Image.open("sunset_400.jpeg")
# img_03 = Image.open("covertpng.png")
# img_04 = Image.open("sunset-aspect_size.jpeg")
#
# img_01_size = img_01.size
# img_02_size = img_02.size
# img_03_size = img_02.size
# img_02_size = img_02.size
#
# print('img 1 size: ', img_01_size)
# print('img 2 size: ', img_02_size)
# print('img 3 size: ', img_03_size)
# print('img 4 size: ', img_03_size)
#
# new_im = Image.new('RGB', (2*img_01_size[0],2*img_01_size[1]), (250,250,250))
#
# new_im.paste(img_01, (0,0))
# new_im.paste(img_02, (img_01_size[0],0))
# new_im.paste(img_03, (0,img_01_size[1]))
# new_im.paste(img_04, (img_01_size[0],img_01_size[1]))
#
# new_im.save("merged_images.png", "PNG")
# new_im.show()



# ###-------------------------------Tikenter
# # function to convert jpg to gif
# def jpg_to_gif():
#     global im1
#
#     # import the image from the folder
#     import_filename = fd.askopenfilename()
#     if import_filename.endswith(".jpg"):
#
#         im1 = Image.open(import_filename)
#
#         # after converting the image save to desired
#         # location with the Extersion .png
#         export_filename = fd.asksaveasfilename(defaultextension=".gif")
#         im1.save(export_filename)
#
#         # displaying the Messaging box with the Success
#         messagebox.showinfo("success ", "your Image converted to GIF Format")
#     else:
#
#         # if Image select is not with the Format of .jpg
#         # then display the Error
#         Label_2 = Label(root, text="Error!", width=20,
#                         fg="red", font=("bold", 15))
#         Label_2.place(x=80, y=280)
#         messagebox.showerror("Fail!!", "Something Went Wrong...")
#
#
# # function to convert gif to jpg
# def gif_to_jpg():
#     global im1
#     import_filename = fd.askopenfilename()
#
#     if import_filename.endswith(".gif"):
#         im1 = Image.open(import_filename).convert('RGB')
#         export_filename = fd.asksaveasfilename(defaultextension=".jpg")
#         im1.save(export_filename)
#         messagebox.showinfo("Success", "File converted to .jpg")
#
#     else:
#         messagebox.showerror("Fail!!", "Error Interrupted!!!! Check Again")
#
#
# # Driver Code
#
# # add buttons
# button1 = Button(root, text="JPG_to_GIF", width=20,
#                  height=2, bg="green", fg="white",
#                  font=("helvetica", 12, "bold"),
#                  command=jpg_to_gif)
#
# button1.place(x=120, y=120)
#
# button2 = Button(root, text="GIF_to_JPG", width=20,
#                  height=2, bg="green", fg="white",
#                  font=("helvetica", 12, "bold"),
#                  command=gif_to_jpg)
#
# button2.place(x=120, y=220)
#
# # adjust window size
# root.geometry("500x500+400+200")
# root.mainloop()

###----------------------------------Gif to image
# Image.open('giphy.gif').convert('RGB').save('image.jpg')


