#Imageio 是一个读写照片数据，包括动态图，video,volumetric data,and scientific formats的库，
########example
##https://imageio.readthedocs.io/en/latest/examples.html
import imageio
im = imageio.imread('imageio:chelsea.png')  # read a standard image
im.shape  # im is a numpy array
(300, 451, 3)
imageio.imwrite('~/chelsea-gray.jpg', im[:, :, 0])

###
import imageio
reader = imageio.get_reader('imageio:cockatoo.mp4')
for i, im in enumerate(reader):
    print('Mean of frame %i is %1.1f' % (i, im.mean()))
#使用imageio 制作动图
import imageio
def create_gif(image_list, gif_name):
    frames = []
    for image_name in image_list:
        frames.append(imageio.imread(image_name))
    # Save them as frames into a gif
    imageio.mimsave(gif_name, frames, 'GIF', duration=0.5)
    

    return
def main():
    image_list =glob.glob(r"D:\pythonrun\20180504rnn\*.jpg")
    print(image_list)
    gif_name = 'created_gif.gif'
    create_gif(image_list, gif_name)
if __name__ == "__main__":
    main()
