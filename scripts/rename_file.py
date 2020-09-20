"""
批量重命名文件
fake_data.py应在同级目录下
"""


import os
from fake_data import *
from tqdm import tqdm


def get_individual_info():
    """获取单个姓名"""
    name = get_name(length=3)  # 姓名
    sex = get_sex()  # 性别
    birthday = get_birthday()  # 出生日期
    id_type = get_id_type()  # 证件类型
    id_number = get_id_number()  # 证件号
    member_characteristic = get_member_characteristic()  # 人员特征
    member_type = get_member_type()  # 人员类型
    ethnicity = get_ethnicity()  # 民族
    serial_number = get_serial_number()  # 编号
    address = get_address()  # 家庭住址
    birth_place = get_address(city_flag=False, street_flag=False, street_num_flag=False)  # 籍贯
    remake = get_remark()  # 备注
    info = '_'.join([name, sex, birthday, id_type, id_number, member_characteristic,
                     member_type, ethnicity, serial_number, address, birth_place,
                     remake])
    return info


def modify_name(PATH):
    """重命名文件夹内的文件"""
    files = os.listdir(PATH)
    # print(files)
    for file in tqdm(files):
        extension = os.path.splitext(file)[1]
        old_file = os.path.join(PATH, file)
        new_file = os.path.join(PATH, get_individual_info() + extension)
        # print(old_file, new_file)
        os.rename(old_file, new_file)


if __name__ == '__main__':
    # print(get_individual_info())
    modify_name(r'D:\qa-picture\1W')
