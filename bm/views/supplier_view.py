import json
import traceback

from django.http import JsonResponse
from django.utils.decorators import method_decorator
from rest_framework.views import APIView
from ..services.product_service import ProductService
from django.core.paginator import Paginator
from public.token.token_utils import auth


@method_decorator(auth(), name='post')
class CreatedProductView(APIView):
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
            print('供应商创建商品传入的参数: ', user_id, parm)

            msg = ProductService.create(user_id, param=parm)

            if msg:
                resp['error_message'] = msg
                resp['success'] = False

        except Exception as e:
            print(str(e))
            traceback.print_exc()

        print('供应商创建商品响应结果resp: ', resp)

        return JsonResponse(resp)


@method_decorator(auth(), name='get')
class GetProductListView(APIView):
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
            print('供应商获取商品列表传入的参数: ', user_id, page_index, page_size, query_type, product_name, outer_item_code)
            rows, total = ProductService.get_prod_list(user_id,
                                                       query_type=query_type,
                                                       product_name=product_name,
                                                       outer_item_code=outer_item_code)

            paginator = Paginator(rows, page_size)
            paginator.current_page = page_index
            resp['result']['rows'] = paginator.page(page_index).object_list
            resp['result']['total'] = total

        except Exception as e:
            print(str(e))
            traceback.print_exc()

        print('供应商获取商品列表响应结果resp: ', resp)

        return JsonResponse(resp)


@method_decorator(auth(), name='get')
class GetProductDetail(APIView):
    def get(self, request, *args, **kwargs):

        resp = {
            'success': True,
            'error_code': 0,
            'error_message': 'success',
            'result': {}
        }

        try:
            prod_id = request.GET.get('prod_id')
            user_id = request.user['id']
            print('供应商获取商品详情传入的参数: ', user_id, prod_id)
            products, err = ProductService.get_prod_detail(prod_id=prod_id)
            resp['result'] = products
            if err:
                resp['error_message'] = err
        except Exception as e:
            print(str(e))
            traceback.print_exc()

        print('供应商获取商品详情响应结果resp: ', resp)

        return JsonResponse(resp)


@method_decorator(auth(), name='post')
class EditProduct(APIView):
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
            print('供应商编辑商品传入的参数: ', user_id, parm)

            msg = ProductService.edit_prod(param=parm)

            if msg:
                resp['error_message'] = msg
                resp['success'] = False

        except Exception as e:
            print(str(e))
            traceback.print_exc()

        print('供应商编辑商品响应结果resp: ', resp)

        return JsonResponse(resp)


@method_decorator(auth(), name='post')
class EditSku(APIView):
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
            print('供应商编辑Sku传入的参数: ', user_id, parm)

            msg = ProductService.edit_sku(param=parm)

            if msg:
                resp['error_message'] = msg
                resp['success'] = False

        except Exception as e:
            print(str(e))
            traceback.print_exc()

        print('供应商编辑Sku响应结果resp: ', resp)

        return JsonResponse(resp)


@method_decorator(auth(), name='post')
class DeleteSku(APIView):
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
            print('供应商删除Sku传入的参数: ', user_id, parm)

            msg = ProductService.delete_sku(param=parm)

            if msg:
                resp['error_message'] = msg
                resp['success'] = False

        except Exception as e:
            print(str(e))
            traceback.print_exc()

        print('供应商删除Sku响应结果resp: ', resp)

        return JsonResponse(resp)


@method_decorator(auth(), name='post')
class DeleteProduct(APIView):
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
            print('供应商删除商品传入的参数: ', user_id, parm)

            msg = ProductService.delete_prod_sku(param=parm)

            if msg:
                resp['error_message'] = msg
                resp['success'] = False

        except Exception as e:
            print(str(e))
            traceback.print_exc()

        print('供应商删除商品响应结果resp: ', resp)

        return JsonResponse(resp)


@method_decorator(auth(), name='post')
class ProcessProduct(APIView):
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
            print('供应商处理商品传入的参数: ', user_id, parm)

            msg = ProductService.process_prod(param=parm)

            if msg:
                resp['error_message'] = msg
                resp['success'] = False

        except Exception as e:
            print(str(e))
            traceback.print_exc()

        print('供应商处理商品响应结果resp: ', resp)

        return JsonResponse(resp)


@method_decorator(auth(), name='post')
class EditProdSku(APIView):
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
            print('供应商编辑商品及Sku传入的参数: ', user_id, parm)

            msg = ProductService.edit_prod_sku(user_id=user_id, param=parm)

            if msg:
                resp['error_message'] = msg
                resp['success'] = False

        except Exception as e:
            print(str(e))
            traceback.print_exc()

        print('供应商编辑商品及Sku响应结果resp: ', resp)

        return JsonResponse(resp)
