# image是PIL库中最重要的类
# image类的图像读取和创建方法
'''
    Image.open(filename) # 根据参数加载图像文件
    Image.new(mode,size,color) # 根据给定参数创建一个新的图像
    Image.open(StringIO.StringIO(buffer)) #从字符串中获取图像
    Image.frombytes(mode,size,color) # 根据像素点data创建图像
    Image.verify() # 对图像文件完整性进行检查，返回异常

    # 处理图片的常用属性
    Image.format # 标识图像格式或来源，如果图像不是从文件读取，值为None
    Image.mode # 图像的色彩模式，L：灰度图像 RGB：真彩色图像 CMYK：出版图像
    Image.size # 图像的宽度和高度，单位是px，返回值是二元元组（tuple）
    Image.palette # 调色板属性，返回一个ImagePalette

    Image.seek(frame) # 跳转并返回图像中的指定帧
    Image.tell() # 返回当前帧的序号
    Image.save(filename,format) # 将图像保存为filename文件名，format是图片格式
    Image.convert(mode) # 使用不同的参数，转换图像为新的模式
    Image.thumbnail(size) #  创建图像的略缩图，size是略缩图尺寸的二元元组
    Image.resize(size) # 按size大小调整图片
    Image.rotate(angle) # 按angle角度旋转图像，生成副本
    Image.split() # 提取RGB图像的每个颜色通道，返回图像副本
    Image.merge(mode,bands) # 合并通道，mode：表示色彩，bands：表示新的色彩通道
    Image.blend（im1，im2，alpha）# 将两张图按照im1*（1.0-alpha）+im2*alpha公式生成新的图像
'''
from PIL import  Image
from PIL import ImageFilter

def I_a():
    im = Image.open("D:\Desktop\python小练习\python——revive\教材案例\\5.jpg")
    print(im.format,im.size,im.mode)

def J_P():#格式转化，jpg__png
    im = Image.open("D:\Desktop\python小练习\python——revive\教材案例\\5.jpg")
    #print(im.format,im.size,im.mode)
    im.save("D:\Desktop\python小练习\python——revive\教材案例\\5.jpg","png")
def gif():#gif文件图像提取
    im=Image.open("D:\Desktop\python小练习\python——revive\教材案例\\cat.gif")
    try:
        im.save('picframe{:02d}.png'.format(im.tell()))
        while True:
            im.seek(im.tell()+1)
            im.save('picframe{:02d}.png'.format(im.tell()))
    except:
        print("处理结束")

def color_Change():#图片的颜色交换
    im=Image.open("D:\Desktop\python小练习\python——revive\教材案例\\5.jpg")
    r,g,b=im.split()
    om=Image.merge("RGB",(b,g,r))
    om.save("D:\Desktop\python小练习\python——revive\教材案例\\5_cpp.jpg")

def I_1():#图片的轮廓获取
    im=Image.open("D:\Desktop\python小练习\python——revive\教材案例\\5.jpg")
    om=im.filter(ImageFilter.CONTOUR)#图片的轮廓效果
    om.save("D:\Desktop\python小练习\python——revive\教材案例\\5_Contour.jpg")

if __name__=='__main__':
    I_a()
    gif()
    J_P()
    color_Change()
    I_1()
