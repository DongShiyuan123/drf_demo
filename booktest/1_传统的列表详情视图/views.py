import json
from django import http
from django.views import View
from booktest.models import BookInfo
from booktest.serializer import BookInfoSerializer

# 列表视图
class BookInfoView(View):
    """
    查询所有图书
    路由：GET /books/
    """
    def get(self, request):
        """获得所有书籍"""
        # 1.查询所有书籍
        books = BookInfo.objects.all()
        # 2.数据转换
        '''
        book_list = []
        for book in books:
            book_dict = {
                "id": book.id,
                "btitle": book.btitle,
                "bpub_date": book.bpub_date,
                "bread": book.bread,
                "bcomment": book.bcomment,
            }
            book_list.append(book_dict)
        # 3.返回数据
        return http.JsonResponse(book_list, safe=False)
        '''
        serializer = BookInfoSerializer(instance=books,many=True)
        return http.JsonResponse(serializer.data, safe=False)


    def post(self, request):
        # 1.获取数据
        # json_bytes = request.body
        # json_str = json_bytes.decode() # 解码
        # book_dict = json.loads(json_str)
        dict_data = json.loads(request.body.decode())
        btitle = dict_data.get("btitle")
        bpub_date = dict_data.get("bpub_date")
        bread = dict_data.get("bread")
        bcomment = dict_data.get("bcomment")
        #2.此处详细的校验参数省略

        #3.数据入库
        book = BookInfo.objects.create(**dict_data)

        #4.返回相应
        # book_dict={
        #     'id': book.id,
        #     'btitle': book.btitle,
        #     'bpub_date': book.bpub_date,
        #     'bread': book.bread,
        #     'bcomment': book.bcomment,
        # }

        # return http.JsonResponse(book_dict,status=201)
        serializer = BookInfoSerializer(instance=book)
        return http.JsonResponse(serializer.data,status=201)


# 详情视图
class BookInfoDetailView(View):
    def get(self,request,pk):
        # 1.通过pk获取对象
        book=BookInfo.objects.get(pk=pk)

        # 2.转换对象
        # book_dict={
        #     'id': book.id,
        #     'btitle': book.btitle,
        #     'bpub_date': book.bpub_date,
        #     'bread': book.bread,
        #     'bcomment': book.bcomment,
        # }
        # 3.返回数据
        # return http.JsonResponse(book_dict)
        serializer = BookInfoSerializer(instance=book)
        return http.JsonResponse(serializer.data)


    def put(self, request, pk):
        # 1.获取参数，对象
        dict_data=json.loads(request.body.decode())
        # 2.参数校验
        # 3.数据入库
        BookInfo.objects.filter(pk=pk).update(**dict_data)
        book = BookInfo.objects.get(pk=pk)
        # book_dict = {
        #     'id': book.id,
        #     'btitle': book.btitle,
        #     'bpub_date': book.bpub_date,
        #     'bread': book.bread,
        #     'bcomment': book.bcomment,
        # }
        # # 4.返回响应
        # return http.JsonResponse(book_dict)
        serializer = BookInfoSerializer(instance=book)
        return http.JsonResponse(serializer.data)

    def delete(self,request,pk):
        # 1.获取书籍
        book=BookInfo.objects.get(id=pk)
        # 2.删除书籍
        book.delete()
        # 3.返回数据
        return http.HttpResponse(status=204)