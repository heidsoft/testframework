# -*- coding: utf-8 -*-
import json
from django.db import models

"""
单继承
class <类名>(父类名)
   <语句>

类的多重继承
class 类名(父类1,父类2,....,父类n)
     <语句1>


verbose_name=None
name=None
primary_key=False
max_length=None 表示最大长度
unique=False
blank=False
null=False
db_index=False
rel=None
default=NOT_PROVIDED
editable=True
serialize=True
unique_for_date=None
unique_for_month=None
unique_for_year=None
choices=None
help_text
db_column=None,
db_tablespace=None
auto_created=False
validators=[]
error_messages=None
null=True 表示字段可以为空
"""
class NgUser(models.Model):
    name = models.CharField(max_length=127)
    age =  models.IntegerField(null=True)
    password = models.CharField(max_length=32)

    #对象序列化
    def __unicode__(self):
        return json.dumps({"name":self.name,"age":self.age})

    #自定义表名称
    class Meta:
        db_table = 'ng_user'