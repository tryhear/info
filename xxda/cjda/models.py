from django.db import models
import django.utils.timezone as timezone

# Create your models here.


class Consumer(models.Model):
    class Meta:
        verbose_name = '员工'
        verbose_name_plural = '员工'
    name = models.CharField('员工', max_length=10)
    phone = models.CharField('电话', max_length=200, blank=True)
    # email = models.EmailField('电子邮件', null=True)

    def __str__(self):
        return self.name


class Xiangmu(models.Model):
    class Meta:
        verbose_name = '待审项目列表'
        verbose_name_plural = '待审项目列表'
    name = models.CharField('项目名称', max_length=200)
    nb = models.CharField('项目类别', max_length=200, blank=True)
    jaw = models.CharField('建设单位', max_length=200, blank=True)
    saw = models.CharField('施工单位', max_length=200, blank=True)
    jeri = models.DateField('接收日期', null=True, default=timezone.now)
    zly = models.CharField('资料员', max_length=10)
    phone = models.CharField('电话', max_length=200)
    jsr = models.ForeignKey(
        Consumer,
        verbose_name='接收人',
        on_delete=models.SET_NULL,
        null=True,
        default='陈宏')
    #isak = models.BooleanField('资料齐全',default=False)

    def __str__(self):
        return self.name


class Tag(models.Model):
    class Meta:
        verbose_name = '待补齐的资料'
        verbose_name_plural = '待补齐的资料'
    contact = models.ForeignKey(Xiangmu, on_delete=models.CASCADE, null=True)
    name = models.CharField('待补齐的资料列表', max_length=100, blank=True)

    def __str__(self):
        return self.name


class Fapiao(models.Model):
    class Meta:
        verbose_name = '发票明细'
        verbose_name_plural = '发票明细'
    开票单位 = models.CharField(null=True, blank=True, max_length=50)
    项目名称 = models.CharField(max_length=50)
    金额 = models.FloatField(null=True, blank=True)
    开票日期 = models.DateField(null=True, blank=True,default=timezone.now)
    发票号码 = models.IntegerField(null=True, blank=True)
    备注 = models.CharField(null=True, blank=True, max_length=100, default=None)

    def __str__(self):
        return self.项目名称
        
class Mulu(models.Model):
    class Meta:
        verbose_name = '工作进度'
        verbose_name_plural = '工作进度'
    工程名称 = models.CharField(null=True, blank=False, max_length=50)
    合同签订 = models.BooleanField('合同')
    合同编号 = models.CharField(null=True, blank=True, max_length=20)
    扫描 = models.BooleanField()
    扫描人 = models.CharField(null=True, blank=True, max_length=6)
    录入 = models.BooleanField()
    录入人 = models.CharField(null=True, blank=True, max_length=6)
    转双层 = models.BooleanField('双层')
    数据入馆 = models.BooleanField('电子')
    纸质移交 = models.BooleanField('纸质')
    刻盘 = models.BooleanField()
    电子档案移交检验登记表 = models.BooleanField('检验表')
    开证 = models.BooleanField()
    开证日期 = models.DateField(null=True, blank=True)
    备注 = models.CharField(null=True, blank=True, max_length=100)

    def __str__(self):
        return self.工程名称
        
class Ziliao(models.Model):
    class Meta:
        verbose_name = '公司资料'
        verbose_name_plural = '公司资料'
    资料名称 = models.CharField(null=True, blank=False, max_length=50)
    日期 = models.DateField(null=True, blank=True,default=timezone.now)
    文件编号 = models.CharField(null=True,blank=True,max_length=20)
    份数 = models.IntegerField(null=True, blank=True)
    备注 =models.CharField(null=True, blank=True,max_length=100)

    def __str__(self):
        return self.资料名称

class KehuZiliao(models.Model):
    class Meta:
        verbose_name = '客户资料'
        verbose_name_plural = '客户资料'
    名称 = models.CharField(null=True, blank=False,max_length=50)
    纳税人识别号 = models.CharField(null=True, blank=False, max_length=50)
    地址 = models.CharField(null=True, blank=False, max_length=50)
    电话 = models.CharField(null=True, blank=False, max_length=50)
    开户银行 = models.CharField(null=True, blank=False, max_length=50)
    账号 = models.CharField(null=True, blank=False, max_length=50)

    def __str__(self):
        return self.客户资料