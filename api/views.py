from django.shortcuts import render

# Create your views here.
from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView
from api.models import Student
from api.serializer import StudentModelSerializer


class StudentAPI(APIView):

    def get(self, request, *args, **kwargs):
        # 增加一个
        get_id = kwargs.get('id')
        print('get_id=', get_id)
        if get_id:
            stu = Student.objects.get(pk=get_id)
            data = StudentModelSerializer(stu).data
            return Response({'msg': '查询单个成功', 'results': data})
        else:
            # 查询所有学生信息
            query_set = Student.objects.all()
            data = StudentModelSerializer(query_set, many=True).data
            print('data=', data)

            return Response({'mag': '查询所有成功', 'results': data})

    def post(self, request, *args, **kwargs):
        request_data = request.data
        print('request_data=', request_data)
        if isinstance(request_data, dict) and request_data != {}:
            many = False
        elif isinstance(request_data, list) and request_data != []:
            many = True
        else:
            return Response({"msg": "参数格式有误"}, status=status.HTTP_400_BAD_REQUEST)

        # 判断单个还是多个增加
        print('many=', many)
        s_data = StudentModelSerializer(data=request_data, many=many)

        # 校验序列化的数据是否正确
        print(s_data.is_valid(), s_data.errors)
        s_data.is_valid(raise_exception=True)
        stu = s_data.save()
        return Response({'msg': '添加成功', 'results': StudentModelSerializer(stu, many=many).data},
                        status=status.HTTP_201_CREATED)

    def delete(self, request, *args, **kwargs):
        id = request.data.get("id")
        is_ = Student.objects.filter(pk=id)
        if is_:
            is_[0].delete()
            return Response({'msg': '删除成功'}, status=status.HTTP_200_OK)
        return Response({'mag': '删除的信息不存在'}, status=status.HTTP_400_BAD_REQUEST)

    def patch(self, request, *args, **kwargs):
        request_data = request.data
        stu_id = request.data.get("id")
        print('patch_request_data=', request_data)
        print('patch_id=', stu_id)
        stu_obj = Student.objects.filter(pk=stu_id)
        print('stu_obj=', stu_obj)
        if stu_obj:
            serializer = StudentModelSerializer(data=request_data, instance=stu_obj[0], partial=True)
            # print('serializer.is_valid=',serializer.is_valid())
            serializer.is_valid(raise_exception=True)
            stu = serializer.save()
            return Response({'msg': '修改成功', 'results': StudentModelSerializer(stu).data}, status=status.HTTP_200_OK)
        else:
            return Response({'mag': '要修改的图书不存在'}, status=status.HTTP_400_BAD_REQUEST)
