from django.db.migrations import serializer
from rest_framework import fields, serializers
from rest_framework.serializers import ModelSerializer

# 学生信息的序列化  与反序列化
from api.models import Student


class StudentModelSerializer(ModelSerializer):
    class Meta:
        model = Student

        fields = ('id', 'name', 'age', 'date', 'pic', 'salary')

    extra_kwargs = {
        'pic': {
            'read_only': True
        },
        'name': {
            'min_length': 4,
            'max_length': 8,
        },
        "salary": {
            "max_digits": 8,
            "decimal_places": 2,
        }
    }

    def validate(self, attrs):
        return attrs

    def validate_name(self, value):
        stu_name = Student.objects.filter(name=value)
        if stu_name:
            raise serializers.ValidationError('学生已经存在')
        return value
