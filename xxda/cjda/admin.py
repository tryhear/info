from django.contrib import admin
from django.http import HttpResponse
from cjda.models import Tag, Consumer, Xiangmu, Fapiao, Mulu, Ziliao, KehuZiliao


# Register your models here.
admin.site.site_title = '欣兴档案信息管理系统'
admin.site.index_title = '四川欣兴档案管理咨询有限公司'
admin.site.site_header = '欣兴档案信息管理系统'


class TagInline(admin.TabularInline):
    model = Tag


class XiangmuAdmin(admin.ModelAdmin):
    list_display = ('name', 'jaw', 'saw', 'jeri', 'zly', 'phone', 'jsr',)
    search_fields = ('name',)
    list_filter = ('jeri', 'jsr',)
    date_hierarchy = 'jeri'
    inlines = [TagInline]

    fieldsets = (
        ['项目基本信息', {
            'fields': ('name', ('jaw', 'saw'), 'jeri',),
        }],
        ['人员基本信息', {
            #'classes': ('collapse',),  # CSS
            'fields': (('zly', 'phone'), 'jsr',),
        }]
    )


@admin.register(Fapiao)
class FapiaoAdmin(admin.ModelAdmin):
    list_display = ('开票单位', '项目名称', '金额', '开票日期', '发票号码', '备注')
    search_fields = ('开票单位', '项目名称')
    list_filter = ('开票日期',)
    date_hierarchy = '开票日期'
    #list_per_page设置每页显示多少条记录，默认是100条
    list_per_page = 15
    
    #ordering设置默认排序字段，负号表示降序排序
    ordering = ('-开票日期','-发票号码',)
  
    #list_editable 设置默认可编辑字段
    #list_editable = ['开票单位', '项目名称']
  
    #fk_fields 设置显示外键字段
    #fk_fields = ('machine_room_id',)
    #设置哪些字段可以点击进入编辑界面
    list_display_links = ('开票单位', '项目名称')


    fieldsets = (
        ['发票详情', {
            'fields': (('开票单位', '项目名称'), '金额', '开票日期', '发票号码', '备注'),
        }],
    )

@admin.register(Mulu)
class MuluAdmin(admin.ModelAdmin):
    # list_display = ('工程名称', '合同签订', '扫描', '录入', '转双层', '数据入馆', '纸质移交', '刻盘','开证','备注',)
    list_display = ('合同签订','开证','工程名称', '扫描', '录入', '转双层', '数据入馆', '纸质移交', '刻盘', '电子档案移交检验登记表', '备注',)
    search_fields = ('工程名称', )
    list_filter = ('扫描','录入', '转双层', '数据入馆','纸质移交','刻盘','开证','转双层',)
    # date_hierarchy = '已入馆'
    # list_per_page = 20
    ordering = ('-扫描','-录入','-数据入馆')
    list_display_links = ('工程名称','备注', )

    fieldsets = (
        ['工程详情', {
            'fields': ('工程名称',('合同签订', '合同编号'), ('开证','开证日期'),('扫描', '扫描人'),('录入','录入人'),),
        }],
        ['进度详情', {
            'fields': (('转双层','数据入馆','纸质移交','刻盘','电子档案移交检验登记表',),'备注',),
        }],
    )

@admin.register(Ziliao)
class ZiliaoAdmin(admin.ModelAdmin):
    list_display = ('资料名称', '日期','文件编号','份数', '备注')
    search_fields = ('资料名称', )
    list_filter = ('日期',)
    date_hierarchy = '日期'
    ordering = ('-日期','-文件编号',)

@admin.register(KehuZiliao)
class ZiliaoAdmin(admin.ModelAdmin):
    list_display = ('名称', '纳税人识别号','地址','电话', '开户银行','账号')
    search_fields = ('名称', )
    # list_filter = ('日期',)
    # date_hierarchy = '日期'
    # ordering = ('-日期','-文件编号',)
    list_display_links = ('名称',)

# admin.site.register(Xiangmu, XiangmuAdmin)
# admin.site.register(Consumer)
#admin.site.register(Fapiao, FapiaoAdmin)
#admin.site.register(Mulu, MuluAdmin)
#admin.site.register(Ziliao, ZiliaoAdmin)
# admin.site.register(Tag)
