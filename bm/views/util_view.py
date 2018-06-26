import json
import traceback

from django.db import connections
from django.http import JsonResponse
from django.utils.decorators import method_decorator
from rest_framework.views import APIView
from bm.services.admin_service import AdminService
from bm.services.product_service import ProductService
from bm.services.sku_service import SkuService
from django.core.paginator import Paginator
# from public.token.token_utils import auth


class GetSupplierId(APIView):
    def post(self, request, *args, **kwargs):

        resp = {
            'success': True,
            'error_code': 0,
            'error_message': 'success',
            'result': []
        }

        try:
            parm = json.loads(request.body.decode('utf-8'))
            distributor_id = parm['distributor_id']
            item_code = parm['item_code']
            print('util获取供应商ID传入的参数: ', parm)

            resp['result'], msg = SkuService.get_distributor_id(distributor_id=distributor_id, item_code=item_code)

            if msg:
                resp['success'] = False
                resp['error_message'] = msg

        except Exception as e:
            print(str(e))
            traceback.print_exc()

        print('util获取供应商ID响应结果resp: ', resp)

        return JsonResponse(resp)


class GetSkuListView(APIView):
    def get(self, request, *args, **kwargs):

        resp = {
            'success': True,
            'error_code': 0,
            'error_message': 'success',
            'result': {}
        }

        try:
            user_id = int(request.GET.get('user_id'))
            print('util获取sku列表传入的参数: ', user_id)
            resp['result']['rows'], resp['result']['total'] = SkuService.get_sku_list(user_id)

        except Exception as e:
            print(str(e))
            traceback.print_exc()

        print('util获取sku列表响应结果resp: ', resp)

        return JsonResponse(resp)


class GetProdMainImg(APIView):
    def get(self, request, *args, **kwargs):

        resp = {
            'success': True,
            'error_code': 0,
            'error_message': 'success',
            'result': ''
        }

        try:
            sku_id = request.GET.get('sku_id')
            print('util获取商品主图传入的参数: ', sku_id)
            img, err = ProductService.get_main_img_by_sku(sku_id=sku_id)
            resp['result'] = img
            if err:
                resp['error_message'] = err
        except Exception as e:
            print(str(e))
            traceback.print_exc()

        print('util获取商品主图响应结果resp: ', resp)

        return JsonResponse(resp)


