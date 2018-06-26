from ..models.product.product import Product
import traceback
from django.core.exceptions import ObjectDoesNotExist, MultipleObjectsReturned


class AdminService(object):
    @staticmethod
    def check_product(param=None):
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
            product_check_status = query.product_check_status
        except ObjectDoesNotExist:
            err_msg = '未找到商品'
            return err_msg

        try:
            if 'action' in param:
                action = param['action']
                if action not in [0, 1]:
                    err_msg = '请传入正确的action 如 0 - 拒绝   1 - 通过'
                    return err_msg
                if action == 0:
                    product_check_status = 40
                elif action == 1:
                    product_check_status = 20
                Product.objects.filter(product_id=product_id, is_deleted=False).update(
                    product_check_status=product_check_status)
            else:
                err_msg = '请传入正确的action 如 0 - 拒绝   1 - 通过'
                return err_msg

        except Exception as e:
            err_msg = '处理失败'
            print(str(e))
            traceback.print_exc()

        return err_msg
