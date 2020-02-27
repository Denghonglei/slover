from rest_framework import serializers

from blog.models import Goods, UrlList, Category


class UrlListSerializer(serializers.ModelSerializer):

    class Meta:
        model = UrlList
        fields = '__all__'
        allow_null = False
        # exclude = ('null',)


class GoodsSerializer(serializers.ModelSerializer):
    # urls = UrlListSerializer(many=True)
    # groups = serializers.PrimaryKeyRelatedField(many=True)

    class Meta:
        model = Goods
        # fields = ['id', 'title', 'code', 'linenos', 'language', 'style']
        fields = '__all__'
        # exclude = ("is_delete",)
        allow_null = False
        depth = 2

class CategorySerializer(serializers.ModelSerializer):

    class Meta:
        model = Category
        fields = '__all__'



class GoodsForIndexSerializer(serializers.ModelSerializer):

    # 序列化一个外键的字段
    urls = serializers.CharField(source='urls.pic1', read_only=True)

    class Meta:
        model = Goods
        fields = ['id','name','detail','praise_count','pic_index','urls','create_time']