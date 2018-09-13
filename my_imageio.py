#Imageio 是一个读写照片数据，包括动态图，video,volumetric data,and scientific formats的库，
########example
##https://imageio.readthedocs.io/en/latest/examples.html
import imageio
im = imageio.imread('imageio:chelsea.png')  # read a standard image
im.shape  # im is a numpy array
(300, 451, 3)
imageio.imwrite('~/chelsea-gray.jpg', im[:, :, 0])

#
import imageio

reader = imageio.get_reader('imageio:cockatoo.mp4')
for i, im in enumerate(reader):
    print('Mean of frame %i is %1.1f' % (i, im.mean()))
