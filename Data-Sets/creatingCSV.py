from scipy import misc
import csv

fonts = ['AcmeFont', 'AgencyFB', 'Algerian', 'ArialBlack', 'Broadway', 'Calibri', 'Itaianate']
alpha = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H',
         'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P',
         'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X',
         'Y', 'Z']

img = misc.imread('Data-Sets\\'+fonts[0]+'\\'+alpha[0]+'.jpg')
img = misc.imresize(img, (8, 8))
img = img.astype(float)
img = misc.bytescale(img, low=0, high=16)

x = []
for each_row in img:
    for each_column in each_row:
        x.append(sum(each_column)/3.0)
