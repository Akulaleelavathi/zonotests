from controller.feature.manualorder import *
from controller.feature.products import *
def test_cfafilter(return_product,setup,workspacedata):
    cfafilter=Product(setup)
    cfa1=cfafilter.get_cfafilter(return_product.product_data,workspacedata)
    cfaid=cfa1[1]
    data=cfa1[0]
    # print(data.json)
    count =0
    assert data.status_code == 201
    for i in data.json["products"]:
        # count+=1
        assert cfaid[0]==i["productVariants"][0]["cfas"][0]["cfaId"]
    # print(count)


def test_schems(return_product,setup,workspacedata):
    schems=Product(setup)
    schems1=schems.get_schemesfilter(return_product.product_data,workspacedata)
    schemtype=schems1[1]
    schemsdata=schems1[0]
    # print(schemtype)
    # print(schemsdata)

    count=0
    for i in schemsdata["products"]:
        count+=1
        assert schemtype.get('schemeType',[])[0]==i["productVariants"][0]["promotions"][0]["promotionType"]
    # print(count)








def test_status(return_product,setup,workspacedata):
    aia=Product(setup)
    aia1=aia.get_statuss(return_product.product_data,workspacedata)
    productdata=aia.get_Product(return_product.product_data)
    # print(aia1.json)
    for i in aia1.json["products"]:
        assert i["productVariants"][0]["enabled"] == False


def test_statuss(return_product, setup, workspacedata):
    aia = Product(setup)
    aia1 = aia.get_status(return_product.product_data, workspacedata)
    productdata = aia.get_Product(return_product.product_data)
    # print(aia1.json)
    for i in aia1.json["products"]:
        assert i["productVariants"][0]["enabled"] == True









def test_skufilter(return_product,setup,workspacedata):
    skufilter=Product(setup)
    skufilter1=skufilter.get_skufilter(return_product.product_data,workspacedata)
    skucode=skufilter1[1]
    skudata=skufilter1[0]
    # print(skucode)
    # print(skudata.json)


    assert skucode.get('skuCode',[])==skudata.json["products"][0]["parentSku"]



