from bm.models.product.product import Product
from bm.models.product.sku import Sku
from ..models.product.prod_supplier_distributor import ProdSupplierDistributor
import traceback
from django.core.exceptions import ObjectDoesNotExist, MultipleObjectsReturned


class SkuService(object):
    @staticmethod
    # 获取分销商正在售卖的商品
    def get_sku_list(user_id):

        product = ProdSupplierDistributor.objects.all().filter(is_deleted=False, distributor_id=user_id, is_sell=True)

        product_id = []
        for item in product:
            product_id.append(item.product_id)

        rows = []
        query = Sku.objects.all().select_related('product').filter(product__in=product_id, is_deleted=False).order_by('-created_at')
        total = len(query)

        for item in query:
            supplier = ProdSupplierDistributor.objects.all().get(product=item.product_id, is_deleted=False)
            product = Product.objects.all().get(product_id=item.product_id, is_deleted=False)
            sku_details = {}
            sku_details['sku_id'] = item.sku_id
            sku_details['supplier_id'] = supplier.supplier_id
            sku_details['product_name'] = product.product_name
            sku_details['sku_name'] = item.sku_name
            sku_details['supply_price'] = str(item.supply_price)
            sku_details['outer_item_code'] = item.outer_item_code
            sku_details['available_quantity'] = str(item.available_quantity)
            sku_details['inventory_quantity'] = str(0)
            sku_details['distribution_limit_pct'] = str(item.distribution_limit_pct)
            sku_details['safety_stock_percent'] = str(item.safety_stock_percent)
            rows.append(sku_details)

        return rows, total

    @staticmethod
    # distributor_id + item_code 获取supplier_id
    def get_distributor_id(distributor_id=None, item_code=None):

        err_msg = ''
        product_id = []
        results = []
        try:
            product = ProdSupplierDistributor.objects.all().filter(distributor_id=distributor_id, is_deleted=False)
            for item in product:
                product_id.append(item.product_id)

            product_from_sku = Sku.objects.all().filter(product__in=product_id, outer_item_code__in=item_code,
                                                        is_deleted=False)

            for item in product_from_sku:
                row = {}
                row['distributor_id'] = distributor_id
                row['item_code'] = item.outer_item_code
                row['sku_id'] = item.sku_id
                row['sku_name'] = item.sku_name
                res = Product.objects.all().get(product_id=item.product_id)
                row['supplier_id'] = res.supplier_id
                results.append(row)
        except Exception as e:
            err_msg = '查询失败'
            print(str(e))

        return results, err_msg





