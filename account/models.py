from django.db import models
from django.contrib.auth.models import User


class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='profile')
    telephone = models.CharField('电话', max_length=50, blank=True)
    org = models.CharField('组织', max_length=128, blank=True)
    create_time = models.DateTimeField('创建时间', auto_now_add=True)
    mod_date = models.DateTimeField('最后修改时间', auto_now=True)
    # address = models.CharField('联系地址', max_length=30, null=True, blank=True)

    class Meta:
        verbose_name_plural = '用户信息'

    def __str__(self):
        return self.user.__str__()

# 最近浏览功能
# 通过对每个实例对象的点击，然后将此实例对象的id（唯一标示）或者实例对象加入到用户最近浏览信息中
# 需要定义一个最近浏览类，以一对多的形式关联上当前用户，然后再以一对一的形式关联商品
