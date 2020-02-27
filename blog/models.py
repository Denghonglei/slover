from django.conf import settings
from django.core.exceptions import ValidationError
from django.db import models

# Create your models here.
from django.utils.timezone import now


class OAuthUser(models.Model):
    author = models.ForeignKey(settings.AUTH_USER_MODEL, verbose_name='用户', blank=True, null=True,
                               on_delete=models.CASCADE)
    openid = models.CharField(max_length=50)
    nikename = models.CharField(max_length=50, verbose_name='昵称')
    token = models.CharField(max_length=150, null=True, blank=True)
    picture = models.CharField(max_length=350, blank=True, null=True)
    type = models.CharField(blank=False, null=False, max_length=50)
    email = models.CharField(max_length=50, null=True, blank=True)
    matedata = models.TextField(null=True, blank=True)
    created_time = models.DateTimeField('创建时间', default=now)
    last_mod_time = models.DateTimeField('修改时间', default=now)

    def __str__(self):
        return self.nikename

    class Meta:
        verbose_name = 'oauth用户'
        verbose_name_plural = verbose_name
        ordering = ['-created_time']


class OAuthConfig(models.Model):
    TYPE = (
        ('weibo', '微博'),
        ('google', '谷歌'),
        ('github', 'GitHub'),
        ('facebook', 'FaceBook'),
        ('qq', 'QQ'),
    )
    type = models.CharField('类型', max_length=10, choices=TYPE, default='a')
    appkey = models.CharField(max_length=200, verbose_name='AppKey')
    appsecret = models.CharField(max_length=200, verbose_name='AppSecret')
    callback_url = models.CharField(max_length=200, verbose_name='回调地址', blank=False, default='http://www.baidu.com')
    is_enable = models.BooleanField('是否显示', default=True, blank=False, null=False)
    created_time = models.DateTimeField('创建时间', default=now)
    last_mod_time = models.DateTimeField('修改时间', default=now)


    def clean(self):
        if OAuthConfig.objects.filter(type=self.type).exclude(id=self.id).count():
            raise ValidationError(_(self.type + '已经存在'))

    def __str__(self):
        return self.type

    class Meta:
        verbose_name = 'oauth配置'
        verbose_name_plural = verbose_name
        ordering = ['-created_time']


class UrlList(models.Model):
    # goods = models.ForeignKey(Goods, default='', on_delete=models.CASCADE,
    #                              verbose_name='班级')  # 这里可以是一个外键，关联班级id
    pic1 = models.TextField(null=True, blank=True)
    pic2 = models.TextField(null=True, blank=True)
    pic3 = models.TextField(null=True, blank=True)
    pic4 = models.TextField(null=True, blank=True)
    pic5 = models.TextField(null=True, blank=True)
    pic6 = models.TextField(null=True, blank=True)
    pic7 = models.TextField(null=True, blank=True)
    pic8 = models.TextField(null=True, blank=True)
    pic9 = models.TextField(null=True, blank=True)
    pic10 = models.TextField(null=True, blank=True)
    pic11 = models.TextField(null=True, blank=True)
    pic12 = models.TextField(null=True, blank=True)
    pic13 = models.TextField(null=True, blank=True)
    pic14 = models.TextField(null=True, blank=True)
    pic15 = models.TextField(null=True, blank=True)
    pic16 = models.TextField(null=True, blank=True)
    pic17 = models.TextField(null=True, blank=True)
    pic18 = models.TextField(null=True, blank=True)
    pic19 = models.TextField(null=True, blank=True)
    pic20 = models.TextField(null=True, blank=True)
    pic21 = models.TextField(null=True, blank=True)
    pic22 = models.TextField(null=True, blank=True)
    pic23 = models.TextField(null=True, blank=True)
    pic24 = models.TextField(null=True, blank=True)
    pic25 = models.TextField(null=True, blank=True)
    pic26 = models.TextField(null=True, blank=True)
    pic27 = models.TextField(null=True, blank=True)
    pic28 = models.TextField(null=True, blank=True)
    pic29 = models.TextField(null=True, blank=True)
    pic30 = models.TextField(null=True, blank=True)
    pic31 = models.TextField(null=True, blank=True)
    pic32 = models.TextField(null=True, blank=True)
    pic33 = models.TextField(null=True, blank=True)
    pic34 = models.TextField(null=True, blank=True)
    pic35 = models.TextField(null=True, blank=True)
    pic36 = models.TextField(null=True, blank=True)
    pic37 = models.TextField(null=True, blank=True)
    pic38 = models.TextField(null=True, blank=True)
    pic39 = models.TextField(null=True, blank=True)
    pic40 = models.TextField(null=True, blank=True)
    pic41 = models.TextField(null=True, blank=True)
    pic42 = models.TextField(null=True, blank=True)
    pic43 = models.TextField(null=True, blank=True)
    pic44 = models.TextField(null=True, blank=True)
    pic45 = models.TextField(null=True, blank=True)
    pic46 = models.TextField(null=True, blank=True)
    pic47 = models.TextField(null=True, blank=True)
    pic48 = models.TextField(null=True, blank=True)
    pic49 = models.TextField(null=True, blank=True)
    pic50 = models.TextField(null=True, blank=True)
    pic51 = models.TextField(null=True, blank=True)
    pic52 = models.TextField(null=True, blank=True)
    pic53 = models.TextField(null=True, blank=True)
    pic54 = models.TextField(null=True, blank=True)
    pic55 = models.TextField(null=True, blank=True)
    pic56 = models.TextField(null=True, blank=True)
    pic57 = models.TextField(null=True, blank=True)
    pic58 = models.TextField(null=True, blank=True)
    pic59 = models.TextField(null=True, blank=True)
    pic60 = models.TextField(null=True, blank=True)
    pic61 = models.TextField(null=True, blank=True)
    pic62 = models.TextField(null=True, blank=True)
    pic63 = models.TextField(null=True, blank=True)
    pic64 = models.TextField(null=True, blank=True)
    pic65 = models.TextField(null=True, blank=True)
    pic66 = models.TextField(null=True, blank=True)
    pic67 = models.TextField(null=True, blank=True)
    pic68 = models.TextField(null=True, blank=True)
    pic69 = models.TextField(null=True, blank=True)
    pic70 = models.TextField(null=True, blank=True)
    pic71 = models.TextField(null=True, blank=True)
    pic72 = models.TextField(null=True, blank=True)
    pic73 = models.TextField(null=True, blank=True)
    pic74 = models.TextField(null=True, blank=True)
    pic75 = models.TextField(null=True, blank=True)
    pic76 = models.TextField(null=True, blank=True)
    pic77 = models.TextField(null=True, blank=True)
    pic78 = models.TextField(null=True, blank=True)
    pic79 = models.TextField(null=True, blank=True)
    pic80 = models.TextField(null=True, blank=True)
    pic81 = models.TextField(null=True, blank=True)
    pic82 = models.TextField(null=True, blank=True)
    pic83 = models.TextField(null=True, blank=True)
    pic84 = models.TextField(null=True, blank=True)
    pic85 = models.TextField(null=True, blank=True)
    pic86 = models.TextField(null=True, blank=True)
    pic87 = models.TextField(null=True, blank=True)
    pic88 = models.TextField(null=True, blank=True)
    pic89 = models.TextField(null=True, blank=True)
    pic90 = models.TextField(null=True, blank=True)
    pic91 = models.TextField(null=True, blank=True)
    pic92 = models.TextField(null=True, blank=True)
    pic93 = models.TextField(null=True, blank=True)
    pic94 = models.TextField(null=True, blank=True)
    pic95 = models.TextField(null=True, blank=True)
    pic96 = models.TextField(null=True, blank=True)
    pic97 = models.TextField(null=True, blank=True)
    pic98 = models.TextField(null=True, blank=True)
    pic99 = models.TextField(null=True, blank=True)
    pic100 = models.TextField(null=True, blank=True)
    pic101 = models.TextField(null=True, blank=True)
    pic102 = models.TextField(null=True, blank=True)
    pic103 = models.TextField(null=True, blank=True)
    pic104 = models.TextField(null=True, blank=True)
    pic105 = models.TextField(null=True, blank=True)
    pic106 = models.TextField(null=True, blank=True)
    pic107 = models.TextField(null=True, blank=True)
    pic108 = models.TextField(null=True, blank=True)
    pic109 = models.TextField(null=True, blank=True)
    pic110 = models.TextField(null=True, blank=True)
    pic111 = models.TextField(null=True, blank=True)
    pic112 = models.TextField(null=True, blank=True)
    pic113 = models.TextField(null=True, blank=True)
    pic114 = models.TextField(null=True, blank=True)
    pic115 = models.TextField(null=True, blank=True)
    pic116 = models.TextField(null=True, blank=True)
    pic117 = models.TextField(null=True, blank=True)
    pic118 = models.TextField(null=True, blank=True)
    pic119 = models.TextField(null=True, blank=True)
    pic120 = models.TextField(null=True, blank=True)
    pic121 = models.TextField(null=True, blank=True)
    pic122 = models.TextField(null=True, blank=True)
    pic123 = models.TextField(null=True, blank=True)
    pic124 = models.TextField(null=True, blank=True)
    pic125 = models.TextField(null=True, blank=True)
    pic126 = models.TextField(null=True, blank=True)
    pic127 = models.TextField(null=True, blank=True)
    pic128 = models.TextField(null=True, blank=True)
    pic129 = models.TextField(null=True, blank=True)
    pic130 = models.TextField(null=True, blank=True)
    pic131 = models.TextField(null=True, blank=True)
    pic132 = models.TextField(null=True, blank=True)
    pic133 = models.TextField(null=True, blank=True)
    pic134 = models.TextField(null=True, blank=True)
    pic135 = models.TextField(null=True, blank=True)
    pic136 = models.TextField(null=True, blank=True)
    pic137 = models.TextField(null=True, blank=True)
    pic138 = models.TextField(null=True, blank=True)
    pic139 = models.TextField(null=True, blank=True)
    pic140 = models.TextField(null=True, blank=True)
    pic141 = models.TextField(null=True, blank=True)
    pic142 = models.TextField(null=True, blank=True)
    pic143 = models.TextField(null=True, blank=True)
    pic144 = models.TextField(null=True, blank=True)
    pic145 = models.TextField(null=True, blank=True)
    pic146 = models.TextField(null=True, blank=True)
    pic147 = models.TextField(null=True, blank=True)
    pic148 = models.TextField(null=True, blank=True)
    pic149 = models.TextField(null=True, blank=True)
    pic150 = models.TextField(null=True, blank=True)

    def __unicode__(self):
        return self.id


    class Meta:
        db_table  = 'pics'


class Goods(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL,on_delete=models.CASCADE, verbose_name='用户')
    name = models.CharField(max_length=255,blank=True,null=True,verbose_name='标题')
    detail =  models.CharField(max_length=255,blank=True,null=True,verbose_name='详情介绍')
    pic_index  = models.TextField(null=True, blank=True,verbose_name='标题图')
    urls = models.ForeignKey(UrlList, default='', on_delete=models.CASCADE, verbose_name='urls')
    category = models.CharField(verbose_name='类别',
        choices=(("0", "正常"), ("3", "迟到"), ("1", "请假"), ("2", "审核中"), ("4", "早退"), ("5", "旷课"), ("6", "假期")),
        default='0',
        max_length=1)
    is_delete = models.BooleanField(default=False)
    is_sale = models.BooleanField(default=False)
    praise_count = models.IntegerField(default=1)
    browse_count = models.IntegerField(default=1)
    create_time = models.DateTimeField(auto_now_add=True)

    # def __str__(self):
    #     return self.name

    class Meta:
        db_table = "Goods"

class Category(models.Model):

    nickname = models.CharField(max_length=50)

    def __str__(self):
        return self.nickname


