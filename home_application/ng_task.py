# -*- coding: utf-8 -*-
from celery import Celery, task
from common.log import logger

@task()
def ngTask(x, y):
    """
    定义一个 celery 异步任务
    """
    logger.debug(u"celery 定时任务执行成功，执行结果：{:0>2}:{:0>2}".format(x, y))
    return x + y