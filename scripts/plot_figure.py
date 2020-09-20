import matplotlib.pyplot as plt
import matplotlib.dates as mdate
from openpyxl import load_workbook


def return_excel(path):
    """读取EXCEL中的数据"""
    wb = load_workbook(path, read_only=True)
    ws = wb['MyLog']
    ws_iter = ws.rows
    r_time, memory, cpu, disk_free, disk_percent = [], [], [], [], []
    for line in ws_iter:
        # 读取时间，内存等...
        r_time.append(line[0].value)
        memory.append(line[2].value)
        cpu.append(line[3].value)
        disk_free.append(line[4].value)
        disk_percent.append(line[5].value)
    return r_time, memory, cpu, disk_free, disk_percent


def plot_memory(x, y, title='Memory'):
    """内存曲线"""
    plt.figure(num=1, figsize=(8, 4))  # 指定图表大小800*400
    plt.rcParams['font.sans-serif'] = ['SimHei']  # 支持中文标题
    plt.title(title)

    plt.xlabel("时间")
    plt.gca().xaxis.set_major_formatter(mdate.DateFormatter('%Y-%m-%d %H:%M:%S'))

    plt.ylabel("内存（MB）")

    plt.plot(x, y)
    plt.gcf().autofmt_xdate()
    plt.show()


def plot_disk(x, y1, y2, title='Disk Capacity'):
    """磁盘容量曲线"""
    plt.figure(num=1, figsize=(8, 4))  # 指定图表大小800*400
    plt.rcParams['font.sans-serif'] = ['SimHei']  # 支持中文标题
    plt.title(title)

    plt.xlabel("时间")
    plt.gca().xaxis.set_major_formatter(mdate.DateFormatter('%Y-%m-%d %H:%M:%S'))
    plt.ylabel("硬盘剩余容量（GB）")

    # ax2 = plt.twinx()
    # ax2.plot(x, y2, label='disk percent')
    # ax2.legend()
    # ax2.set_ylabel("硬盘占用百分比（%）")

    plt.plot(x, y1, label='disk free')
    plt.gcf().autofmt_xdate()
    # plt.legend()

    plt.show()


if __name__ == '__main__':
    file_path = r'C:\Users\dengshangping\Desktop\MyLog.xlsx'
    print('reading...')
    rows = return_excel(file_path)
    print('plotting...')
    # plot_memory(rows[0], rows[1])
    plot_disk(rows[0], rows[3], rows[4])
