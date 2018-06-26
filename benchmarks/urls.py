"""benchmarks URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.11/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url
from django.contrib import admin
from bm.views.supplier_view import CreatedProductView, GetProductListView, GetProductDetail, \
    EditProdSku, EditSku, DeleteProduct, DeleteSku, ProcessProduct
from bm.views.distributor_view import ShowAllProductListView, EditProd, GetDistributorProductListView
from bm.views.admin_view import CheckProduct, AdminGetProductListView
from bm.views.util_view import GetSkuListView, GetProdMainImg, GetSupplierId

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    # 供应商URL
    url(r'^bm/supplier/create_product', CreatedProductView.as_view()),
    url(r'^bm/supplier/get_product_list', GetProductListView.as_view()),
    url(r'^bm/supplier/get_product_detail', GetProductDetail.as_view()),
    url(r'^bm/supplier/edit_product', EditProdSku.as_view()),
    url(r'^bm/supplier/edit_sku', EditSku.as_view()),
    url(r'^bm/supplier/delete_product', DeleteProduct.as_view()),
    url(r'^bm/supplier/delete_sku', DeleteSku.as_view()),
    url(r'^bm/supplier/process_product', ProcessProduct.as_view()),
    # 分销商URL
    url(r'^bm/distributor/show_product', ShowAllProductListView.as_view()),
    url(r'^bm/distributor/edit_product', EditProd.as_view()),
    url(r'^bm/distributor/get_product_list', GetDistributorProductListView.as_view()),
    url(r'^bm/distributor/get_product_detail', GetProductDetail.as_view()),
    # 管理员URL
    url(r'^bm/admin/check_product', CheckProduct.as_view()),
    url(r'^bm/admin/get_product_list', AdminGetProductListView.as_view()),
    # util URL
    url(r'^bm/util/get_sku_list', GetSkuListView.as_view()),
    url(r'^bm/util/get_product_main_img', GetProdMainImg.as_view()),
    url(r'^bm/util/get_supplier_id', GetSupplierId.as_view()),

]
