from scipy import misc
import numpy as np

fonts = ['AcmeFont', 'AgencyFB', 'Algerian', 'ArialBlack', 'Broadway', 'Calibri', 'Itaianate']
alpha = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H',
         'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P',
         'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X',
         'Y', 'Z']
data = []
i = 0
for char in alpha:
    # data.append([])
    img = misc.imread(fonts[0]+'\\'+char+'.jpg')
    img = misc.imresize(img, (8, 8))
    img = img.astype(float)
    img = misc.bytescale(img, low=0, high=16)
    x = []
    for each_row in img:
        for each_column in each_row:
            x.append(sum(each_column)/3.0)
    data.append(x)

data2D = np.asarray(data)
np.savetxt("foo.csv", data2D, delimiter=",")