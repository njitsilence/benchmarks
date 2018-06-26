from ..models.product.prod_supplier_distributor import ProdSupplierDistributor
from ..models.product.product import Product
import traceback
from django.core.exceptions import ObjectDoesNotExist, MultipleObjectsReturned


class DistributorService(object):
    @staticmethod
    def get_distributor_prod_status(user_id, input=None):
        i = 0
        for item in input:
            query = ProdSupplierDistributor.objects.all().filter(product=item['product_id'], distributor_id=user_id)
            if len(query) == 0:
                input[i]['is_like'] = False
                input[i]['is_sell'] = False
                input[i]['is_cart'] = False
            else:
                input[i]['is_like'] = query[0].is_like
                input[i]['is_sell'] = query[0].is_sell
                input[i]['is_cart'] = query[0].is_cart
            i += 1

        return input

    @staticmethod
    def edit_prod(user_id, param=None):
        err_msg = ''
        product_id = param['product_id']
        if not product_id:
            err_msg = '请传入product_id'
            return err_msg
        try:
            product = Product.objects.get(product_id=product_id)
            product_id = product.product_id
            supplier_id = product.supplier_id
        except ObjectDoesNotExist:
            err_msg = '未找到商品'
            return err_msg

        try:
            query = ProdSupplierDistributor.objects.get(distributor_id=user_id,
                                                        product=product_id,
                                                        supplier_id=supplier_id)
            is_like = query.is_like
            is_sell = query.is_sell
            is_cart = query.is_cart
        except ObjectDoesNotExist:
            relationship = ProdSupplierDistributor(distributor_id=user_id,
                                                   product=product,
                                                   supplier_id=supplier_id)
            relationship.save()

        try:
            if 'is_like' in param:
                if param['is_like']:
                    is_like = param['is_like']
                else:
                    is_like = False
            if 'is_sell' in param:
                if param['is_sell']:
                    is_sell = param['is_sell']
                else:
                    is_sell = False
            if 'is_cart' in param:
                if param['is_cart']:
                    is_cart = param['is_cart']
                else:
                    is_cart = False

            ProdSupplierDistributor.objects.filter(distributor_id=user_id,
                                                   product=product_id,
                                                   supplier_id=supplier_id).update(is_like=is_like,
                                                                                   is_sell=is_sell,
                                                                                   is_cart=is_cart)
        except Exception as e:
            err_msg = '分销商更新商品失败'
            print(str(e))
            traceback.print_exc()

        return err_msg
