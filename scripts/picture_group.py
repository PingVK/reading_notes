"""
用于批量复制文件夹中的部分图片
文件数量较大时，注意关闭Windows Defender的实时防护，可提升速度
"""

import os
import shutil
from tqdm import tqdm


def get_group(folder_path, group_num):
    """将文件中的文件等分为group_num组"""
    all_files = os.listdir(folder_path)
    for i in range(len(all_files)):
        all_files[i] = os.path.join(folder_path, all_files[i])
    assert group_num >= 2
    group = []
    num = len(all_files) // group_num
    for i in range(group_num-1):
        group.append(all_files[i*num:(i+1)*num])
    group.append(all_files[(i+1)*num:])
    return group


def get_part(folder_path, proportion, tail=False):
    """获取文件夹中一定比例的文件 """
    all_files = os.listdir(folder_path)
    length = int(proportion*len(all_files))
    print(length)
    if tail:
        part = all_files[-length:]
    else:
        part = all_files[:length]
    for i in range(len(part)):
        part[i] = os.path.join(folder_path, part[i])
    return part


def get_exac_num(folder_path, num):
    """获取文件夹中固定数量的文件 """
    all_files = os.listdir(folder_path)
    files = all_files[:num]
    for i in range(len(files)):
        files[i] = os.path.join(folder_path, files[i])
    return files


def copy_file(file_list, to_path):
    """获取列表中的文件路径，并复制到指定文件夹中"""
    if not os.path.isdir(to_path):
        os.mkdir(to_path)
    for file in tqdm(file_list):
        try:
            shutil.copy(file, to_path)
        except Exception as err:
            print('Error in %s' % file)
            print('%r' % err)


def folder_split_copy(from_path, to_path, split_num):
    """将全部文件等分为split_num组分别保存"""
    groups = get_group(from_path, split_num)
    if not os.path.isdir(to_path):
        os.mkdir(to_path)
    for i in range(len(groups)):
        target_folder = os.path.join(to_path, 'part' + str(i))
        os.mkdir(target_folder)
        copy_file(groups[i], target_folder)


if __name__ == '__main__':
    # picture_5w = get_part(r'D:\python_file\labelA_jpeg', 0.5, tail=True)
    # copy_file(picture_5w, r'D:\picture\新建文件夹')
    # folder_split_copy(r'D:\python_file\png_file', r'D:\yanzheng', 4)
    lst = get_exac_num(r'D:\qa-picture\10万-1', 10002)  # 从目标文件夹获取固定数量文件列表
    copy_file(lst, r'D:\qa-picture\1W')  # 拷贝文件至目标文件夹
