# 库存类型
INVENTORY_TYPE = (
    ('ZP', '正品'),
    ('CC', '残次'),
    ('JS', '机损'),
    ('XS', '箱损'),
    ('ZT', '在途库存'),
)

DISTRIBUTOR_PROD_SALE_STATUS_CHOICES= (
    (10, '出售中'),
    (20, '已下架'),
)

SUPPLIER_PROD_SALE_STATUS_CHOICES= (
    (10, '仓库中'),
    (20, '分销中'),
)

PROD_CHECK_STATUS_CHOICES = (
    (10, '未审核'),
    (20, '已审核'),
    (30, '待审核'),
    (40, '审核未通过'),
)

