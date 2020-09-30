"""
监控软件内存、CPU、磁盘占用的情况
需使用管理员权限打开
"""
import os
import time
import logging
from logging import handlers
import psutil
from pywinauto import application


# 获取当前pid的CPU和内存，以及磁盘占用情况
def get_info(pid):
    rss = psutil.Process(pid).memory_full_info().rss / (1024 * 1024)
    cpu_percent = psutil.Process(pid).cpu_percent()
    disk = psutil.disk_usage('/')
    return rss, cpu_percent, '%.3f' % (disk.free/1073741824), disk.percent


def record(pid):
    """记录格式
    时间, other, 内存(MB)，磁盘剩余(GB)，磁盘占用百分比(%)
    """
    info = ','.join(map(str, get_info(pid)))
    logging.info(',' + info)
    time.sleep(4)


def log_handler(save_path):
    log_format = '%(asctime)s %(message)s'  # 定义日志输出格式
    logging.basicConfig(format=log_format, level=logging.INFO, filemode='a')

    # 创建TimedRotatingFileHandler处理对象
    # 间隔1(Day)创建新的名称为myLog%Y%m%d_%H%M%S.log的文件，并一直占用myLog文件。
    if not os.path.isdir(save_path):
        os.makedirs(save_path)
    fileshandle = logging.handlers.TimedRotatingFileHandler(os.path.join(save_path, 'MyLog.csv'), when='D',
                                                            interval=1, backupCount=10)
    fileshandle.suffix = "%Y%m%d_%H%M%S.csv"

    # 设置日志输出级别和格式
    formatter = logging.Formatter(log_format)
    fileshandle.setFormatter(formatter)

    logging.getLogger('').addHandler(fileshandle)  # 添加到日志处理对象集合


def find_pid(process_name):
    for proc in psutil.process_iter():
        if proc.name() == process_name:
            print('pid: ', proc.pid)
            return proc.pid
    return None


# 获取客户端PID
def get_pid(process_name, path):
    pid = find_pid(process_name)
    if pid is not None:
        return pid
    print('start %s' % process_name)

    application.Application().start(path)
    time.sleep(10)
    return find_pid(process_name)


if __name__ == '__main__':
    app = 'SmartVMS.exe'
    ProgramFile = r'C:\Program Files (x86)\SmartVMS\SmartVMS.exe'
    path = './record'  # 日志保存路径

    PID = get_pid(app, ProgramFile)
    log_handler(path)
    while True:
        record(PID)
