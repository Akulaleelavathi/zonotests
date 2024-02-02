import pytest

from controller.feature.manualorder import *
def test_get_placeorderdetails(return_manual,setup,workspacedata):
    placeorderdetails= CustomerIds(setup)
    # customer_data=placeorderdetails.get_customerid(workspacedata)
    customerdata=placeorderdetails.get_placeorderdetails(return_manual.customer_data, workspacedata)
    assert customerdata.status_code==201
    assert customerdata.json["total"]

    list = []
    for i in customerdata.json["products"]:
        for j in i["productVariants"]:
            list.append({"productId": j["productVariantId"], "minquty": j["minOrderQty"]})

    return (list)


    # print(customerdata.json)


@pytest.fixture(scope="module")
def test_getaddtocard(return_manual, setup, workspacedata):
    get_placeorderdetails1 = test_get_placeorderdetails(return_manual, setup, workspacedata)
    getaddtocard = CustomerIds(setup)
    placeorderdetails=getaddtocard.get_placeorderdetails(return_manual.customer_data,workspacedata)
    getaddtocard1 = getaddtocard.get_addtocard(return_manual.customer_data, workspacedata, get_placeorderdetails1)
    logger.error(get_placeorderdetails1)
    assert getaddtocard1.json["orders"]
    assert getaddtocard1.json["orders"][0]["id"]
    assert getaddtocard1.json["orders"][0]["status"]
    assert getaddtocard1.json["orders"][0]["orderLine"][0]["id"]
    assert getaddtocard1.json["orders"][0]["orderLine"][0]["sku"]
    assert getaddtocard1.json["orders"][0]["orderLine"][0]["productVariantId"]
    assert getaddtocard1.json["orders"][0]["orderLine"][0]["suggestedQuantity"]
    assert getaddtocard1.json["orders"][0]["orderLine"][0]["productVariantId"]
    assert getaddtocard1.json["orders"][0]["orderLine"][0]["productVariantId"] == placeorderdetails.json["products"][0]["productVariants"][0]["productVariantId"]
    assert getaddtocard1.json["orders"][0]["importSource"] == "manual", "Assertion failure verify_manual_order body{}".format(placeorderdetails.json)
    # print(getaddtocard1)
    # print(placeorderdetails.json)



    responsejson=getaddtocard1.json

    data_list = []

    for i in responsejson["orders"]:
        data_list.append({"pofileId": i["pofileId"], "id": i["id"]})
        for k in i["orderLine"]:
            data_list.append({"ids": k["id"], "productVariantId": k["productVariantId"], "quantity": k["quantity"]})

    return data_list
    # print(data_list)


def test_afterinc(return_manual, setup, workspacedata,test_getaddtocard):
    increment = CustomerIds(setup)
    get_placeorderdetails1 = test_get_placeorderdetails(return_manual, setup, workspacedata)
    getaddtocard1 = increment.get_addtocard(return_manual.customer_data, workspacedata, get_placeorderdetails1)
    get_aftinc=increment.get_afterinc(workspacedata,return_manual.customer_data,test_getaddtocard)
    print(get_aftinc.json)
    assert get_aftinc.json["orders"][0]["orderLine"][0]["quantity"] % getaddtocard1.json["orders"][0]["orderLine"][0]["quantity"] ==0
    assert get_aftinc.json["orders"][0]["id"]==getaddtocard1.json["orders"][0]["id"]
    assert get_aftinc.json["orders"][0]["status"]==getaddtocard1.json["orders"][0]["status"]
    assert get_aftinc.json["orders"][0]["orderLine"][0]["id"]==getaddtocard1.json["orders"][0]["orderLine"][0]["id"]
    assert get_aftinc.json["orders"][0]["orderLine"][0]["sku"]==getaddtocard1.json["orders"][0]["orderLine"][0]["sku"]
    assert get_aftinc.json["orders"][0]["orderLine"][0]["productVariantId"]== getaddtocard1.json["orders"][0]["orderLine"][0]["productVariantId"]









def test_dec(return_manual,setup,workspacedata,test_getaddtocard):
    dec=CustomerIds(setup)
    get_placeorderdetails1 = test_get_placeorderdetails(return_manual, setup, workspacedata)
    getaddtocard1 = dec.get_addtocard(return_manual.customer_data, workspacedata, get_placeorderdetails1)
    get_dec=dec.getdec(workspacedata,return_manual.customer_data,test_getaddtocard)
    print(get_dec)
    # assert get_dec.json["orders"][0]["orderLine"][0]["productVariantId"] == getaddtocard1.json["orders"][0]["orderLine"][0]["productVariantId"]







def test_delete(return_manual,setup,workspacedata,test_getaddtocard):
    delete=CustomerIds(setup)
    get_placeorderdetails1 = test_get_placeorderdetails(return_manual, setup, workspacedata)
    getaddtocard1 = delete.get_addtocard(return_manual.customer_data, workspacedata, get_placeorderdetails1)
    get_delete=delete.get_delete(workspacedata,return_manual.customer_data,test_getaddtocard)
    print(get_delete)



















def test_checkout(return_manual,setup,workspacedata,test_getaddtocard):
    get_addtocard=test_getaddtocard
    checkout= CustomerIds(setup)
    checkout1=checkout.get_checkout(return_manual.customer_data,workspacedata,get_addtocard)
    # print(checkout1.json)

    assert checkout1.status_code == 201
    for order in checkout1.json["orders"]:
        assert "id" in order






