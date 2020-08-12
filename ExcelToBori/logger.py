import logging
from logging.handlers import TimedRotatingFileHandler
import os
from pathlib import Path

home = str(Path.home())

log_dir = '/home/easypnp/pyLog/'

# log 폴더 없을 경우 생성
if not os.path.exists(log_dir):
    os.mkdir(log_dir)

# format 설정
formatter = logging.Formatter(u'%(asctime)s [%(pathname)s] [%(levelname)8s] %(message)s')

# file handler 설정
file_handler = TimedRotatingFileHandler(
    filename=log_dir + 'pylog_excel.log',
    when='midnight',
    interval=1,
    encoding='utf-8'
)

file_handler.setFormatter(formatter)
file_handler.suffix = '%Y%m%d'
file_handler.setLevel(logging.DEBUG)

# logger 생성
dev_logger = logging.getLogger('develop')
dev_logger.setLevel(logging.DEBUG) #debug level 이상은 출력하도록 설정
dev_logger.addHandler(file_handler)