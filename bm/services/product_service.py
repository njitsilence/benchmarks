from ..models.product.product import Product
from ..models.product.prod_supplier_distributor import ProdSupplierDistributor
from ..models.product.sku import Sku
from .gen_id import GenID
import traceback
from django.core.exceptions import ObjectDoesNotExist
from django.db.models import Avg
from .user_service import batch_get_user_info_list


class ProductService(object):
    @staticmethod
    def create(user_id, param=None):
        err_msg = ''
        try:
            product_id = GenID(user_id).generate_prod_id()
            img_list = param['product_img']
            if len(img_list) < 5:
                for _ in range(5 - len(img_list) ):
                    img_list.append(None)

            product_name = ''
            product_detail = ''
            product_category = ''
            product_sub_category = ''
            if 'product_name' in param:
                product_name = param['product_name']
            if 'product_detail' in param:
                product_detail = param['product_detail']
            if 'product_category' in param:
                product_category = param['product_category']
            if 'product_sub_category' in param:
                product_sub_category = param['product_sub_category']

            product = Product(
                product_name=product_name,
                product_detail=product_detail,
                product_category=product_category,
                product_sub_category=product_sub_category,
                supplier_id=user_id,
                product_id=product_id,
                img_url_1=img_list[0],
                img_url_2=img_list[1],
                img_url_3=img_list[2],
                img_url_4=img_list[3],
                img_url_5=img_list[4],
            )
            product.save()

            # img = param['product_img']
            # for item in img:
            #     ProductImg.objects.create(
            #         product=product,
            #         img_url=item,
            #         seq=i + 1
            #     )
            #     i += 1
            if 'sku' in param:
                s = param['sku']
                for item in s:
                    sku_name = ''
                    supply_price = 0
                    outer_item_code = ''
                    available_quantity = 0
                    distribution_limit_pct = 0

                    if 'sku_name' in item:
                        sku_name = item['sku_name']
                    if 'supply_price' in item:
                        supply_price = item['supply_price']
                    if 'outer_item_code' in item:
                        outer_item_code = item['outer_item_code']
                    if 'distribution_limit_pct' in item:
                        distribution_limit_pct = item['distribution_limit_pct']
                    if 'available_quantity' in item:
                        available_quantity = item['available_quantity']

                    Sku.objects.create(
                        sku_id=GenID(user_id).generate_sku_id(),
                        sku_name=sku_name,
                        supply_price=supply_price,
                        outer_item_code=outer_item_code,
                        available_quantity=available_quantity,
                        distribution_limit_pct=distribution_limit_pct,
                        product=product,
                    )

        except Exception as e:
            err_msg = '创建商品失败'
            print(str(e))
            traceback.print_exc()

        return err_msg

    @staticmethod
    def get_prod_list(user_id, query_type=None, product_name=None, outer_item_code=None):
        rows = []
        # 处理如果只用商家编码查询
        product_id = []
        if (product_name is None or product_name == '') and outer_item_code is not None:
            # 获取该商家编码的product_id
            sku = Sku.objects.all().filter(is_deleted=False, outer_item_code=outer_item_code).order_by('-created_at')
            for item in sku:
                product_id.append(item.product_id)

        query = Product.objects.all().filter(supplier_id=user_id, is_deleted=False).order_by('-created_at')
        if product_id:
            query = query.filter(product_id__in=product_id)
        if query_type:
            if query_type == '0':
                query_type = 10
            elif query_type == '1':
                query_type = 20
            query = query.filter(product_sale_status=query_type)
        if product_name:
            query = query.filter(product_name__contains=product_name)
        total = len(query)
        for item in query:
            products = {}
            products['product_id'] = item.product_id
            products['product_name'] = item.product_name
            products['product_category'] = item.product_category
            products['product_sub_category'] = item.product_sub_category
            products['product_sale_status'] = item.product_sale_status
            products['product_check_status'] = item.product_check_status
            products['product_main_img_url'] = item.img_url_1
            sku = Sku.objects.all().filter(product=item.product_id, is_deleted=False).order_by('-created_at')
            if outer_item_code:
                sku = sku.filter(outer_item_code=outer_item_code)
            sku_list = []
            for item in sku:
                sku_details = {}
                sku_details['sku_id'] = item.sku_id
                sku_details['sku_name'] = item.sku_name
                sku_details['supply_price'] = str(item.supply_price)
                sku_details['outer_item_code'] = item.outer_item_code
                sku_details['available_quantity'] = str(item.available_quantity)
                sku_details['inventory_quantity'] = str(0)
                sku_details['distribution_limit_pct'] = str(item.distribution_limit_pct)
                sku_details['safety_stock_percent'] = str(item.safety_stock_percent)
                sku_list.append(sku_details)
            products['sku'] = sku_list
            rows.append(products)

        return rows, total

    @staticmethod
    def get_prod_detail(prod_id=None):
        error_message = ''
        products = {}
        product_img = []
        try:
            query = Product.objects.get(product_id=prod_id, is_deleted=False)
            products['product_id'] = query.product_id
            products['product_name'] = query.product_name
            products['product_detail'] = query.product_detail
            products['product_category'] = query.product_category
            products['product_sub_category'] = query.product_sub_category
            products['product_sale_status'] = query.product_sale_status
            products['product_check_status'] = query.product_check_status
            product_img.append(query.img_url_1)
            product_img.append(query.img_url_2)
            product_img.append(query.img_url_3)
            product_img.append(query.img_url_4)
            product_img.append(query.img_url_5)
            products['product_img'] = product_img
            sku = Sku.objects.all().filter(product=query.product_id, is_deleted=False).order_by('-created_at')
            sku_list = []
            for item in sku:
                sku_details = {}
                sku_details['sku_id'] = item.sku_id
                sku_details['sku_name'] = item.sku_name
                sku_details['supply_price'] = str(item.supply_price)
                sku_details['outer_item_code'] = item.outer_item_code
                sku_details['available_quantity'] = str(item.available_quantity)
                sku_details['inventory_quantity'] = str(0)
                sku_details['distribution_limit_pct'] = str(item.distribution_limit_pct)
                sku_details['safety_stock_percent'] = str(item.safety_stock_percent)
                sku_list.append(sku_details)
            products['sku'] = sku_list
        except ObjectDoesNotExist:
            error_message = '未找到商品'

        return products, error_message

    @staticmethod
    def edit_prod(param=None):
        err_msg = ''
        product_id = param['product_id']
        if not product_id:
            err_msg = '请传入product_id'
            return err_msg
        try:
            query = Product.objects.get(product_id=product_id)
            product_id = query.product_id
            product_name = query.product_name
            product_detail = query.product_detail
            product_category = query.product_category
            product_sub_category = query.product_sub_category
            product_img_url_1 = query.img_url_1
            product_img_url_2 = query.img_url_2
            product_img_url_3 = query.img_url_3
            product_img_url_4 = query.img_url_4
            product_img_url_5 = query.img_url_5
            product_sale_status = query.product_sale_status

        except ObjectDoesNotExist:
            err_msg = '未找到商品'
            return err_msg

        try:

            if 'product_name' in param:
                if param['product_name']:
                    product_name = param['product_name']
            if 'product_detail' in param:
                if param['product_detail']:
                    product_detail = param['product_detail']
            if 'product_category' in param:
                if param['product_category']:
                    product_category = param['product_category']
            if 'product_sub_category' in param:
                if param['product_sub_category']:
                    product_sub_category = param['product_sub_category']

            if 'product_img' in param:
                try:
                    product_img_url_1 = param['product_img'][0]
                    product_img_url_2 = param['product_img'][1]
                    product_img_url_3 = param['product_img'][2]
                    product_img_url_4 = param['product_img'][3]
                    product_img_url_5 = param['product_img'][4]
                except Exception as e:
                    print(str(e))


            # if 'product_img_url_1' in param:
            #     if param['product_img_url_1']:
            #         product_img_url_1 = param['product_img_url_1']
            # if 'product_img_url_2' in param:
            #     if param['product_img_url_2']:
            #         product_img_url_2 = param['product_img_url_2']
            # if 'product_img_url_3' in param:
            #     if param['product_img_url_3']:
            #         product_img_url_3 = param['product_img_url_3']
            # if 'product_img_url_4' in param:
            #     if param['product_img_url_4']:
            #         product_img_url_4 = param['product_img_url_4']
            # if 'product_img_url_5' in param:
            #     if param['product_img_url_5']:
            #         product_img_url_5 = param['product_img_url_5']
            if 'product_sale_status' in param:
                if param['product_sale_status']:
                    product_sale_status = param['product_sale_status']
            Product.objects.filter(product_id=product_id).update(
                product_name=product_name,
                product_detail=product_detail,
                product_category=product_category,
                product_sub_category=product_sub_category,
                img_url_1=product_img_url_1,
                img_url_2=product_img_url_2,
                img_url_3=product_img_url_3,
                img_url_4=product_img_url_4,
                img_url_5=product_img_url_5,
                product_sale_status=product_sale_status,
            )
        except Exception as e:
            err_msg = '更新prod失败'
            print(str(e))
            traceback.print_exc()

        return err_msg

    @staticmethod
    def edit_sku(param=None):
        err_msg = ''
        if 'sku_id' not in param:
            err_msg = '请传入sku_id'
            return err_msg
        sku_id = param['sku_id']
        if not sku_id:
            err_msg = '请传入sku_id'
            return err_msg
        try:
            query = Sku.objects.get(sku_id=sku_id)
            sku_name = query.sku_name
            supply_price = query.supply_price
            outer_item_code = query.outer_item_code
            available_quantity = query.available_quantity
            distribution_limit_pct = query.distribution_limit_pct
        except ObjectDoesNotExist:
            err_msg = '未找到Sku'
            return err_msg

        try:

            if 'sku_name' in param:
                if param['sku_name']:
                    sku_name = param['sku_name']
            if 'supply_price' in param:
                if param['supply_price']:
                    supply_price = param['supply_price']
            if 'outer_item_code' in param:
                if param['outer_item_code']:
                    outer_item_code = param['outer_item_code']
            if 'available_quantity' in param:
                if param['available_quantity']:
                    available_quantity = param['available_quantity']
            if 'distribution_limit_pct' in param:
                if param['distribution_limit_pct']:
                    distribution_limit_pct = param['distribution_limit_pct']
            if 'safety_stock_percent' in param:
                if param['safety_stock_percent']:
                    safety_stock_percent = param['safety_stock_percent']
            Sku.objects.filter(sku_id=sku_id).update(
                sku_name=sku_name,
                supply_price=supply_price,
                outer_item_code=outer_item_code,
                available_quantity=available_quantity,
                distribution_limit_pct=distribution_limit_pct,
                safety_stock_percent=safety_stock_percent,
            )
        except Exception as e:
            err_msg = '更新Sku失败'
            print(str(e))
            traceback.print_exc()

        return err_msg

    @staticmethod
    def edit_prod_sku(user_id=None, param=None):
        err_msg = ProductService.edit_prod(param=param)
        product_id = param['product_id']
        if err_msg:
            return err_msg
        if 'sku' in param:
            for item in param['sku']:
                if 'sku_id' in item:
                    if item['sku_id'] is None or item['sku_id'] == '':
                        err_msg = ProductService.create_sku(user_id=user_id, product_id=product_id, param=item)
                    else:
                        # 如果sku_id为空则创建新的sku到该商品下
                        err_msg = ProductService.edit_sku(param=item)
                else:
                    # 如果sku_id未传则创建新的sku到该商品下
                    err_msg = ProductService.create_sku(user_id=user_id, product_id=product_id, param=item)
                if err_msg:
                    return err_msg
        return err_msg

    @staticmethod
    def delete_prod(param=None):
        err_msg = ''
        if 'product_id' not in param:
            err_msg = '请传入product_id'
            return err_msg
        product_id = param['product_id']
        if not product_id:
            err_msg = '请传入product_id'
            return err_msg
        try:
            query = Product.objects.get(product_id=product_id)
        except ObjectDoesNotExist:
            err_msg = '未找到商品'
            return err_msg

        try:
            Product.objects.filter(product_id=product_id).update(is_deleted=True)
        except Exception as e:
            err_msg = '删除失败'
            print(str(e))
            traceback.print_exc()

        return err_msg

    @staticmethod
    def delete_sku(param=None):
        err_msg = ''
        if 'sku_id' not in param:
            err_msg = '请传入sku_id'
            return err_msg
            sku_id = param['sku_id']
        if not product_id:
            err_msg = '请传入sku_id'
            return err_msg
        try:
            query = Sku.objects.get(sku_id=sku_id)
        except ObjectDoesNotExist:
            err_msg = '未找到Sku'
            return err_msg

        try:
            Sku.objects.filter(sku_id=sku_id).update(is_deleted=True)
        except Exception as e:
            err_msg = '删除失败'
            print(str(e))
            traceback.print_exc()

        return err_msg

    @staticmethod
    def delete_prod_sku(param=None):
        err_msg = ''
        if 'product_id' not in param:
            err_msg = '请传入product_id'
            return err_msg
        product_id = param['product_id']
        if not product_id:
            err_msg = '请传入product_id'
            return err_msg
        try:
            query = Product.objects.get(product_id=product_id)
        except ObjectDoesNotExist:
            err_msg = '未找到商品'
            return err_msg

        try:
            Product.objects.filter(product_id=product_id).update(is_deleted=True)
            Sku.objects.filter(product=product_id).update(is_deleted=True)
        except Exception as e:
            err_msg = '删除失败'
            print(str(e))
            traceback.print_exc()

        return err_msg

    @staticmethod
    def process_prod(param=None):
        err_msg = ''
        if 'product_id' not in param:
            err_msg = '请传入product_id'
            return err_msg
        product_id = param['product_id']
        if not product_id:
            err_msg = '请传入product_id'
            return err_msg
        try:
            query = Product.objects.get(product_id=product_id, is_deleted=False)
            product_sale_status = query.product_sale_status
            product_check_status = query.product_check_status
        except ObjectDoesNotExist:
            err_msg = '未找到商品'
            return err_msg

        try:
            if 'action' in param:
                action = param['action']
                if action not in [0, 1, 2]:
                    err_msg = '请传入正确的action 如 0 - 上架   1 - 下架   2 - 提交审核'
                    return err_msg
                if action == 0:
                    product_sale_status = 20
                elif action == 1:
                    product_sale_status = 10
                elif action == 2:
                    product_check_status = 30
                Product.objects.filter(product_id=product_id, is_deleted=False).update(
                    product_sale_status=product_sale_status,
                    product_check_status=product_check_status)
            else:
                err_msg = '请传入正确的action 如 0 - 上架   1 - 下架   2 - 提交审核'
                return err_msg

        except Exception as e:
            err_msg = '处理失败'
            print(str(e))
            traceback.print_exc()

        return err_msg

    @staticmethod
    def show_prod(product_category=None, product_name=None):
        rows = []
        query = Product.objects.all().filter(is_deleted=False, product_sale_status=20, product_check_status=20).order_by('-created_at')
        if product_category:
            query = query.filter(product_category=product_category)
        if product_name:
            query = query.filter(product_name=product_name)
        total = len(query)
        for item in query:
            products = {}
            products['product_id'] = item.product_id
            products['product_name'] = item.product_name
            products['product_category'] = item.product_category
            products['product_sub_category'] = item.product_sub_category
            products['product_main_img_url'] = item.img_url_1
            sku = Sku.objects.filter(product=item.product_id, is_deleted=False).aggregate(Avg('supply_price'))
            products['average_supply_price'] = str(round(sku['supply_price__avg'], 2))
            rows.append(products)

        return rows, total

    @staticmethod
    def query_distributor_product_list(user_id, query_type=None, product_name=None, outer_item_code=None):

        # 处理如果只用商家编码查询
        product_id = []
        if (product_name is None or product_name == '') and outer_item_code is not None:
            # 获取该商家编码的product_id
            sku = Sku.objects.all().filter(is_deleted=False, outer_item_code=outer_item_code).order_by('-created_at')
            for item in sku:
                product_id.append(item.product_id)

        distributor_product = ProdSupplierDistributor.objects.all().filter(distributor_id=user_id, is_deleted=False).order_by('-created_at')
        if product_id:
            distributor_product = distributor_product.filter(product__in=product_id)

        if query_type:
            if query_type == '0' or query_type == '1':
                if query_type == '0':
                    is_sell = True
                if query_type == '1':
                    is_sell = False
                distributor_product = distributor_product.filter(is_sell=is_sell)
            if query_type == '2':
                is_like = True
                distributor_product = distributor_product.filter(is_like=is_like)

        product_id = []
        for item in distributor_product:
            product_id.append(item.product_id)

        rows = []
        query = Product.objects.all().filter(product_id__in=product_id, is_deleted=False).order_by('-created_at')
        if product_name:
            query = query.filter(product_name__contains=product_name)
        total = len(query)
        for item in query:
            products = {}
            products['product_id'] = item.product_id
            products['product_name'] = item.product_name
            products['product_category'] = item.product_category
            products['product_sub_category'] = item.product_sub_category
            products['product_sale_status'] = item.product_sale_status
            products['product_check_status'] = item.product_check_status
            products['product_main_img_url'] = item.img_url_1
            sku = Sku.objects.all().filter(product=item.product_id, is_deleted=False).order_by('-created_at')
            if outer_item_code:
                sku = sku.filter(outer_item_code=outer_item_code)
            sku_list = []
            for item in sku:
                sku_details = {}
                sku_details['sku_id'] = item.sku_id
                sku_details['sku_name'] = item.sku_name
                sku_details['supply_price'] = str(item.supply_price)
                sku_details['outer_item_code'] = item.outer_item_code
                sku_details['available_quantity'] = str(item.available_quantity)
                sku_details['inventory_quantity'] = str(0)
                sku_details['distribution_limit_pct'] = str(item.distribution_limit_pct)
                sku_details['safety_stock_percent'] = str(item.safety_stock_percent)
                sku_list.append(sku_details)
            products['sku'] = sku_list
            rows.append(products)

        return rows, total

    @staticmethod
    def query_admin_product_list(query_type=None, product_name=None, outer_item_code=None):

        if query_type:
            if query_type == '0':
                query_type = 20
            if query_type == '1':
                query_type = 30
        else:
            # 默认返回待审核
            query_type = 30

        # 处理如果只用商家编码查询
        product_id = []
        if (product_name is None or product_name == '') and outer_item_code is not None:
            # 获取该商家编码的product_id
            sku = Sku.objects.all().filter(is_deleted=False, outer_item_code=outer_item_code).order_by('-created_at')
            for item in sku:
                product_id.append(item.product_id)

        query = Product.objects.all().filter(is_deleted=False, product_check_status=query_type).order_by('-created_at')
        if product_id:
            query = query.filter(product_id__in=product_id)

        # product_id = []
        # for item in product:
        #     product_id.append(item.product_id)
        #
        rows = []
        supplier_id = []
        # query = Product.objects.all().filter(product_id__in=product_id, is_deleted=False).order_by('-created_at')
        if product_name:
            query = query.filter(product_name__contains=product_name)
        total = len(query)
        for item in query:
            products = {}
            products['product_id'] = item.product_id
            products['product_name'] = item.product_name
            products['product_category'] = item.product_category
            products['product_sub_category'] = item.product_sub_category
            products['product_sale_status'] = item.product_sale_status
            products['product_check_status'] = item.product_check_status
            products['product_main_img_url'] = item.img_url_1
            products['supplier_id'] = item.supplier_id
            supplier_id.append(item.supplier_id)
            products['supplier_name'] = '张三'
            products['supplier_phone'] = '12345678901'
            sku = Sku.objects.all().filter(product=item.product_id, is_deleted=False).order_by('-created_at')
            if outer_item_code:
                sku = sku.filter(outer_item_code=outer_item_code)
            sku_list = []
            for item in sku:
                sku_details = {}
                sku_details['sku_id'] = item.sku_id
                sku_details['sku_name'] = item.sku_name
                sku_details['supply_price'] = str(item.supply_price)
                sku_details['outer_item_code'] = item.outer_item_code
                sku_details['available_quantity'] = str(item.available_quantity)
                sku_details['inventory_quantity'] = str(0)
                sku_details['distribution_limit_pct'] = str(item.distribution_limit_pct)
                sku_details['safety_stock_percent'] = str(item.safety_stock_percent)
                sku_list.append(sku_details)
            products['sku'] = sku_list
            rows.append(products)

        user_info = batch_get_user_info_list(supplier_id)
        i = 0
        for item in rows:
            if item['supplier_id'] == user_info[i]['user_id']:
                item['supplier_name'] = user_info[i]['user_name']
                item['supplier_phone'] = user_info[i]['user_phone']

        return rows, total

    @staticmethod
    def get_main_img_by_sku(sku_id=None):

        res = Sku.objects.all().select_related('product').filter(sku_id=sku_id, is_deleted=False)

        if len(list(res)) == 0:
            return '', '未找到主图'
        else:
            return {"product_id": res[0].product_id,
                    "product_name": res[0].product.product_name,
                    "product_main_img": res[0].product.img_url_1,
                    "sku_id": res[0].sku_id}, ''

    @staticmethod
    def create_sku(user_id=None, product_id=None, param=None):

        err_msg = ''

        try:
            product = Product.objects.all().get(product_id=product_id, is_deleted=False)
        except ObjectDoesNotExist:
            err_msg = '编辑商品时新增SKU未找到商品'
            return err_msg

        sku_name = ''
        supply_price = 0
        outer_item_code = ''
        available_quantity = 0
        distribution_limit_pct = 0

        if 'sku_name' in param:
            sku_name = param['sku_name']
        if 'supply_price' in param:
            supply_price = param['supply_price']
        if 'outer_item_code' in param:
            outer_item_code = param['outer_item_code']
        if 'distribution_limit_pct' in param:
            distribution_limit_pct = param['distribution_limit_pct']
        if 'available_quantity' in param:
            available_quantity = param['available_quantity']

        try:
            Sku.objects.create(
                sku_id=GenID(user_id).generate_sku_id(),
                sku_name=sku_name,
                supply_price=supply_price,
                outer_item_code=outer_item_code,
                available_quantity=available_quantity,
                distribution_limit_pct=distribution_limit_pct,
                product=product,
            )
        except Exception as e:
            err_msg = '该商品创建Sku失败'
            print(str(e))
            traceback.print_exc()

        return err_msg






