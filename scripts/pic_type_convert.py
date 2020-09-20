"""
批量转换图片格式
格式转化功能依赖于Pillow
支持常见图片格式，详见 https://pillow.readthedocs.io/en/stable/handbook/image-file-formats.html
"""


import os
from concurrent import futures
from PIL import Image
from tqdm import tqdm


def convert_one(pic_path, to_path, to_type):
    """单张转换"""
    pic_name = os.path.split(pic_path)[1]
    save_name = os.path.splitext(pic_name)[0] + to_type
    try:
        im = Image.open(pic_path)
        im.save(os.path.join(to_path, save_name))
    except Exception as err:
        print('cannot convert %s' % pic_path)
        print(err)


def find_pictures(folder_path, pic_type):
    """寻找文件夹中指定格式的图片"""
    pic_list = []
    for pic in os.listdir(folder_path):
        if os.path.splitext(pic)[1] == pic_type:
            pic_list.append(os.path.join(folder_path, pic))
    return pic_list


def convert_many(pic_list, to_path, to_type):
    """多进程处理"""
    with futures.ProcessPoolExecutor() as executor:
        todo = []
        for pic in pic_list:
            future = executor.submit(convert_one, pic, to_path, to_type)
            todo.append(future)
        for _ in tqdm(futures.as_completed(todo), total=len(pic_list)):
            pass


def convert(pic_folder, pic_type, convert_type):
    """
    主函数，会在目标文件夹同级目录下创建文件夹储存转换文件
    pic_type: 要转换的图片格式，例如'.jpg'
    convert_type: 转换后的格式, 例如'.png'
    note: 不要遗漏格式名前的'.'
    """
    save_folder = pic_folder + '_to_' + convert_type[1:]
    if not os.path.isdir(save_folder):
        os.mkdir(save_folder)
    pictures = find_pictures(pic_folder, pic_type=pic_type)
    convert_many(pictures, save_folder, convert_type)


if __name__ == '__main__':
    convert(r'C:\Users\dengshangping\Desktop\10万-1www\10万-1www', '.jpg', '.png')
