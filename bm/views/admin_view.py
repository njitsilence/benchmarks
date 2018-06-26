import json
import traceback

from django.http import JsonResponse
from django.utils.decorators import method_decorator
from rest_framework.views import APIView
from bm.services.admin_service import AdminService
from bm.services.product_service import ProductService
from django.core.paginator import Paginator
from public.token.token_utils import auth


@method_decorator(auth(), name='post')
class CheckProduct(APIView):
    def post(self, request, *args, **kwargs):

        resp = {
            'success': True,
            'error_code': 0,
            'error_message': 'success',
            'result': {}
        }

        try:
            parm = json.loads(request.body.decode('utf-8'))
            user_id = request.user['id']
            print('管理员审核商品传入的参数: ', user_id, parm)

            msg = AdminService.check_product(param=parm)

            if msg:
                resp['error_message'] = msg

        except Exception as e:
            print(str(e))
            traceback.print_exc()

        print('管理员审核商品响应结果resp: ', resp)

        return JsonResponse(resp)


@method_decorator(auth(), name='get')
class AdminGetProductListView(APIView):
    def get(self, request, *args, **kwargs):

        resp = {
            'success': True,
            'error_code': 0,
            'error_message': 'success',
            'result': {}
        }

        try:
            user_id = request.user['id']
            page_index = request.GET.get('page_index', 1)
            page_size = request.GET.get('page_size',10)
            if page_index == '':
                page_index= 1
            if page_size == '':
                page_size= 10
            query_type = request.GET.get('query_type', None)
            product_name = request.GET.get('product_name', None)
            outer_item_code = request.GET.get('outer_item_code', None)
            print('管理员获取商品列表传入的参数: ', user_id, page_index, page_size, query_type, product_name, outer_item_code)
            rows, total = ProductService.query_admin_product_list(query_type=query_type,
                                                       product_name=product_name,
                                                       outer_item_code=outer_item_code)

            paginator = Paginator(rows, page_size)
            paginator.current_page = page_index
            resp['result']['rows'] = paginator.page(page_index).object_list
            resp['result']['total'] = total

        except Exception as e:
            print(str(e))
            traceback.print_exc()

        print('管理员获取商品列表响应结果resp: ', resp)

        return JsonResponse(resp)

