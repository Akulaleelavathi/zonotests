
from conftest import return_product
from controller.feature.products import *


def test_get_cfa_filter(return_product,setup,workspacedata):
    product = Product(setup)
    get_cfafilter=product.get_cfafilter(return_product.product_data,workspacedata)

    assert(get_cfafilter["total"])
    assert get_cfafilter["products"]
    assert get_cfafilter['products'][1]['parentSku'], "parentsku not found"
    assert get_cfafilter['products'][0]['id']
    assert get_cfafilter['products'][0]['productVariants'][0]['id']
    assert get_cfafilter['products'][0]['productVariants'][0]['minOrderQty']
    assert get_cfafilter['products'][0]['productVariants'][0]['division']
    assert get_cfafilter['products'][0]['productVariants'][0]['division'][0]['divisionId']
    assert get_cfafilter['products'][0]['productVariants'][0]['cfas'][0]['cfaId']



def test_get_division_filter(return_product,setup,workspacedata):
    product=Product(setup)
    get_divisionfilter=product.get_divisionfilter(return_product.product_data,workspacedata)

    assert get_divisionfilter[0]["total"]
    assert get_divisionfilter[0]["products"]
    assert get_divisionfilter[0]['products'][1]['parentSku'], "parentsku not found"
    assert get_divisionfilter[0]['products'][0]['id']
    assert get_divisionfilter[0]['products'][0]['productVariants'][0]['id']
    assert get_divisionfilter[0]['products'][0]['productVariants'][0]['minOrderQty']
    assert get_divisionfilter[0]['products'][0]['productVariants'][0]['division']
    assert get_divisionfilter[0]['products'][0]['productVariants'][0]['division'][0]['divisionId']
    assert get_divisionfilter[0]['products'][0]['productVariants'][0]['cfas'][0]['cfaId']



def test_get_schemsfilter(return_product,setup,workspacedata):
    product=Product(setup)
    get_schemsfilter=product.get_schemesfilter(return_product.product_data,workspacedata)
    assert get_schemsfilter["total"]
    assert get_schemsfilter["products"]
    assert get_schemsfilter['products'][1]['parentSku'], "parentsku not found"
    assert get_schemsfilter['products'][0]['id']
    assert get_schemsfilter['products'][0]['productVariants'][0]['id']
    assert get_schemsfilter['products'][0]['productVariants'][0]['minOrderQty']
    assert get_schemsfilter['products'][0]['productVariants'][0]['division']
    assert get_schemsfilter['products'][0]['productVariants'][0]['division'][0]['divisionId']
    assert get_schemsfilter['products'][0]['productVariants'][0]['cfas'][0]['cfaId']
    assert get_schemsfilter['products'][0]['productVariants'][0]['productVariantId']


def test_activeinactive(return_product,setup,workspacedata):
    products=Product(setup)
    get_activeinactive=products.get_activeinactive(return_product.product_data,workspacedata)
    assert get_activeinactive["total"]
    assert get_activeinactive["products"]
    assert get_activeinactive['products'][1]['parentSku'], "parentsku not found"
    assert get_activeinactive['products'][0]['id']
    assert get_activeinactive['products'][0]['productVariants'][0]['id']
    assert get_activeinactive['products'][0]['productVariants'][0]['minOrderQty']
    assert get_activeinactive['products'][0]['productVariants'][0]['division']
    assert get_activeinactive['products'][0]['productVariants'][0]['division'][0]['divisionId']
    assert get_activeinactive['products'][0]['productVariants'][0]['cfas'][0]['cfaId']
    assert get_activeinactive['products'][0]['productVariants'][0]['productVariantId']

def test_skufilter(return_product,setup,workspacedata):
    product=Product(setup)
    get_skufilter=product.get_skufilter(return_product.product_data,workspacedata)
    assert get_skufilter["total"]
    assert get_skufilter["products"]
    assert get_skufilter['products'][0]['parentSku'], "parentsku not found"
    assert get_skufilter['products'][0]['id']
    assert get_skufilter['products'][0]['productVariants'][0]['id']
    assert get_skufilter['products'][0]['productVariants'][0]['minOrderQty']
    assert get_skufilter['products'][0]['productVariants'][0]['division']
    assert get_skufilter['products'][0]['productVariants'][0]['division'][0]['divisionId']
    assert get_skufilter['products'][0]['productVariants'][0]['cfas'][0]['cfaId']
    assert get_skufilter['products'][0]['productVariants'][0]['productVariantId']
