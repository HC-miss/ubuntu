from django.db import models


class TypeGoods(models.Model):
    title = models.CharField('种类', max_length=30)
    isDelete = models.BooleanField('是否删除', default=False)

    class Meta:
        verbose_name_plural = '商品分类'

    def __str__(self):
        return self.title


class GoodsInfo(models.Model):
    gtitle = models.CharField('商品名称', max_length=20)
    gtype = models.ForeignKey(TypeGoods, on_delete=models.CASCADE)
    gprice = models.DecimalField('价格', max_digits=6, decimal_places=2)
    gdesc = models.CharField('商品介绍', max_length=100, blank=True, null=True)
    isDelete = models.BooleanField('是否删除', default=False)
    img = models.ImageField(upload_to='goodsimg')

    class Meta:
        verbose_name_plural = '商品信息'

    def __str__(self):
        return self.gtitle


