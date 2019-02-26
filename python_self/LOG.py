import logging  # 引入logging模块
logging.basicConfig(level=logging.DEBUG,
                    format='%(asctime)s - %(filename)s[line:%(lineno)d] - %(levelname)s: %(message)s')  # logging.basicConfig函数对日志的输出格式及方式做相关配置
# 由于日志基本配置中级别设置为DEBUG，所以一下打印信息将会全部显示在控制台上
logging.info('this is a loggging info message')
logging.debug('this is a loggging debug message')
logging.warning('this is loggging a warning message')
logging.error('this is an loggging error message')
logging.critical('this is a loggging critical message')

#output is:
# 2019-02-26 08:53:15,234 - test.py[line:5] - INFO: this is a loggging info message
# 2019-02-26 08:53:15,234 - test.py[line:6] - DEBUG: this is a loggging debug message
# 2019-02-26 08:53:15,234 - test.py[line:7] - WARNING: this is loggging a warning message
# 2019-02-26 08:53:15,234 - test.py[line:8] - ERROR: this is an loggging error message
# 2019-02-26 08:53:15,234 - test.py[line:9] - CRITICAL: this is a loggging critical message
