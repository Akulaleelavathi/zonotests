
from controller.feature.manualorder import *
from controller.feature.customersdata import *
from controller.feature.products import *

#
#
#
# # def test_product(return_product):
# #     print(return_product.get_skufilter)
#
# # def test_Schems(return_schems):
# #     print(return_schems.get_schems)
# #
# # def test_cfafilter(return_cfafilter):
# #     print(return_cfafilter.get_cfafilter)
# # #
# #
# # def test_returnproduct(return_product):
# #     print(return_product.get_skufilter)
#
#
# # def test_placeorder(return_manual):
# #     print(return_manual.inc)
#
# # # def test_uploadorder(uploadorder):
# #     print(uploadorder.check_out)
# #
# # def test_customerack(customerack):
# #     print(customerack.checkout)
#
# # def test_addtocard(return_manual):
# #     print(return_manual.addtocard)
#
#
#
# def test_get_cfa_filter(return_product,setup,workspacedata):
#     product = Product(setup)
#     get_cfafilter=product.get_cfafilter(return_product.product_data,workspacedata)
#
#     assert(get_cfafilter["total"])
#     assert get_cfafilter["products"]
#     assert get_cfafilter['products'][1]['parentSku'], "parentsku not found"
#     assert get_cfafilter['products'][0]['id']
#     assert get_cfafilter['products'][0]['productVariants'][0]['id']
#     assert get_cfafilter['products'][0]['productVariants'][0]['minOrderQty']
#     assert get_cfafilter['products'][0]['productVariants'][0]['division']
#     assert get_cfafilter['products'][0]['productVariants'][0]['division'][0]['divisionId']
#     assert get_cfafilter['products'][0]['productVariants'][0]['cfas'][0]['cfaId']
#
#
#
# def test_get_division_filter(return_product,setup,workspacedata):
#     product=Product(setup)
#     get_divisionfilter=product.get_divisionfilter(return_product.product_data,workspacedata)
#
#     assert get_divisionfilter[0]["total"]
#     assert get_divisionfilter[0]["products"]
#     assert get_divisionfilter[0]['products'][1]['parentSku'], "parentsku not found"
#     assert get_divisionfilter[0]['products'][0]['id']
#     assert get_divisionfilter[0]['products'][0]['productVariants'][0]['id']
#     assert get_divisionfilter[0]['products'][0]['productVariants'][0]['minOrderQty']
#     assert get_divisionfilter[0]['products'][0]['productVariants'][0]['division']
#     assert get_divisionfilter[0]['products'][0]['productVariants'][0]['division'][0]['divisionId']
#     assert get_divisionfilter[0]['products'][0]['productVariants'][0]['cfas'][0]['cfaId']
#
#
#
# def test_get_schemsfilter(return_product,setup,workspacedata):
#     product=Product(setup)
#     get_schemsfilter=product.get_schemesfilter(return_product.product_data,workspacedata)
#     assert get_schemsfilter["total"]
#     assert get_schemsfilter["products"]
#     assert get_schemsfilter['products'][1]['parentSku'], "parentsku not found"
#     assert get_schemsfilter['products'][0]['id']
#     assert get_schemsfilter['products'][0]['productVariants'][0]['id']
#     assert get_schemsfilter['products'][0]['productVariants'][0]['minOrderQty']
#     assert get_schemsfilter['products'][0]['productVariants'][0]['division']
#     assert get_schemsfilter['products'][0]['productVariants'][0]['division'][0]['divisionId']
#     assert get_schemsfilter['products'][0]['productVariants'][0]['cfas'][0]['cfaId']
#     assert get_schemsfilter['products'][0]['productVariants'][0]['productVariantId']
#
#
# def test_activeinactive(return_product,setup,workspacedata):
#     products=Product(setup)
#     get_activeinactive=products.get_activeinactive(return_product.product_data,workspacedata)
#     assert get_activeinactive["total"]
#     assert get_activeinactive["products"]
#     assert get_activeinactive['products'][1]['parentSku'], "parentsku not found"
#     assert get_activeinactive['products'][0]['id']
#     assert get_activeinactive['products'][0]['productVariants'][0]['id']
#     assert get_activeinactive['products'][0]['productVariants'][0]['minOrderQty']
#     assert get_activeinactive['products'][0]['productVariants'][0]['division']
#     assert get_activeinactive['products'][0]['productVariants'][0]['division'][0]['divisionId']
#     assert get_activeinactive['products'][0]['productVariants'][0]['cfas'][0]['cfaId']
#     assert get_activeinactive['products'][0]['productVariants'][0]['productVariantId']
#
# def test_skufilter(return_product,setup,workspacedata):
#     product=Product(setup)
#     get_skufilter=product.get_skufilter(return_product.product_data,workspacedata)
#     assert get_skufilter["total"]
#     assert get_skufilter["products"]
#     assert get_skufilter['products'][0]['parentSku'], "parentsku not found"
#     assert get_skufilter['products'][0]['id']
#     assert get_skufilter['products'][0]['productVariants'][0]['id']
#     assert get_skufilter['products'][0]['productVariants'][0]['minOrderQty']
#     assert get_skufilter['products'][0]['productVariants'][0]['division']
#     assert get_skufilter['products'][0]['productVariants'][0]['division'][0]['divisionId']
#     assert get_skufilter['products'][0]['productVariants'][0]['cfas'][0]['cfaId']
#     assert get_skufilter['products'][0]['productVariants'][0]['productVariantId']
#
#
# def test_get_schems(workspacedata,setup):
#     schems=Schems(setup)
#     get_schems=schems.get_schems(workspacedata)
#     assert (get_schems["startRecord"])
#     assert get_schems["promotions"][0]["promotionCode"]
#     assert get_schems["promotions"][0]["promotionType"]
#     assert get_schems["promotions"][0]["sku"]
#     assert get_schems["promotions"][0]["skusX"]
#     assert get_schems["promotions"][0]["skusY"]
#     assert get_schems["promotions"][0]["slabs"][0]["code"]
#     assert get_schems["promotions"][0]["slabs"][0]["args"][0]["name"]
#     assert get_schems["promotions"][0]["minimumQty"]
#
#
# #
# #
#
# def test_get_placeorderdetails(return_manual,setup,workspacedata):
#     placeorderdetails= CustomerIds(setup)
#     # customer_data=placeorderdetails.get_customerid(workspacedata)
#     customerdata=placeorderdetails.get_placeorderdetails(return_manual.customer_data, workspacedata)
#     assert customerdata.status_code==201
#     assert customerdata.json["total"]
#
#     list = []
#     for i in customerdata.json["products"]:
#         for j in i["productVariants"]:
#             list.append({"productId": j["productVariantId"], "minquty": j["minOrderQty"]})
#
#     return (list)
#
#
#     # print(customerdata.json)
#
#
# def test_getaddtocard(return_manual, setup, workspacedata):
#     get_placeorderdetails1 = test_get_placeorderdetails(return_manual, setup, workspacedata)
#     getaddtocard = CustomerIds(setup)
#     get_placeorderdetails=getaddtocard.get_placeorderdetails(return_manual.customer_data,workspacedata)
#     getaddtocard1 = getaddtocard.get_addtocard(return_manual.customer_data, workspacedata, get_placeorderdetails1)
#     assert getaddtocard1.json["orders"]
#     assert getaddtocard1.json["orders"][0]["id"]
#     assert getaddtocard1.json["orders"][0]["status"]
#     assert getaddtocard1.json["orders"][0]["orderLine"][0]["id"]
#     assert getaddtocard1.json["orders"][0]["orderLine"][0]["sku"]
#     assert getaddtocard1.json["orders"][0]["orderLine"][0]["productVariantId"]
#     assert getaddtocard1.json["orders"][0]["orderLine"][0]["suggestedQuantity"]
#     assert getaddtocard1.json["orders"][0]["orderLine"][0]["productVariantId"]
#     assert getaddtocard1.json["orders"][0]["orderLine"][0]["productVariantId"] == get_placeorderdetails.json["products"][0]["productVariants"][0]["productVariantId"]
#     assert getaddtocard1.json["orders"][0]["importSource"] == "manual", "Assertion failure verify_manual_order body{}".format(get_placeorderdetails.json)
#
#
#     responsejson=getaddtocard1.json
#
#     data_list = []
#
#     for i in responsejson["orders"]:
#         data_list.append({"pofileId": i["pofileId"], "id": i["id"]})
#         for k in i["orderLine"]:
#             data_list.append({"ids": k["id"], "productVariantId": k["productVariantId"], "quantity": k["quantity"]})
#
#     return data_list
#
#
#
#
#
#
# def test_checkout(return_manual,setup,workspacedata):
#     get_addtocard=test_getaddtocard(return_manual,setup,workspacedata)
#     checkout= CustomerIds(setup)
#     checkout1=checkout.get_checkout(return_manual.customer_data,workspacedata,get_addtocard)
#     print(checkout1.json)
#
#     assert checkout1.status_code == 201
#     for order in checkout1.json["orders"]:
#         assert "id" in order
#
#
#
# def test_upload(uploadorder,workspacedata,setup):
#
#     upload1=(setup)
#
#
#
#
#
#
#
#
#
#
# def test_cfafilter(return_product,setup,workspacedata):
#     cfafilter=Product(setup)
#     cfa1=cfafilter.get_cfafilter(return_product.product_data,workspacedata)
#     cfaid=cfa1[1]
#     data=cfa1[0]
#     # print(data.json)
#     count =0
#     assert data.status_code == 201
#     for i in data.json["products"]:
#         # count+=1
#         assert cfaid[0]==i["productVariants"][0]["cfas"][0]["cfaId"]
#     # print(count)
#
#
# def test_schems(return_product,setup,workspacedata):
#     schems=Product(setup)
#     schems1=schems.get_schemesfilter(return_product.product_data,workspacedata)
#     schemtype=schems1[1]
#     schemsdata=schems1[0]
#     # print(schemtype)
#     # print(schemsdata)
#
#     count=0
#     for i in schemsdata["products"]:
#         count+=1
#         assert schemtype.get('schemeType',[])[0]==i["productVariants"][0]["promotions"][0]["promotionType"]
#     # print(count)
#
#
# #
# # def test_status(return_product,setup,workspacedata):
# #     aia=Product(setup)
# #     aia1=aia.get_status(return_product.product_data,workspacedata)
# #     aiatype=aia1[1]
# #     aiadata=aia1[0]
# #     print(aiatype.json)
# #     print(aiatype.json)
#
#     # count=0
#     # for i in aiadata["products"]:
#     #     count+=1
#     #     assert aiatype.get('statusFilter',[])[0]==i["productVariants"][0]
#     #
#
# def test_skufilter(return_product,setup,workspacedata):
#     skufilter=Product(setup)
#     skufilter1=skufilter.get_skufilter(return_product.product_data,workspacedata)
#     skucode=skufilter1[1]
#     skudata=skufilter1[0]
#     # print(skucode)
#     # print(skudata.json)
#
#
#     assert skucode.get('skuCode',[])==skudata.json["products"][0]["parentSku"]
#
#
#
#
#
#
#
#
#
#
#
#
#
#
# def test_customerdata(return_customerdata):
#     logger.error(f"return the customer response{return_customerdata.customersdata2.json}")
#
#
#
#
# def test_customercode(setup,workspacedata,return_customerdata):
#     customerdata=Customersdatas(setup)
#     filternumber=customerdata.customercodefilter(return_customerdata,workspacedata)
#     # print(filternumber)
#     lstnumbers=filternumber[1]
#     lstdata=filternumber[0]
#     # print(lstnumbers)
#     # print(lstdata.json)
#     for i in lstdata.json["customers"]:
#         assert lstnumbers[0]==i["distributorCode"]
#
#
# def test_customernumber(setup,workspacedata,return_customerdata):
#     customerdata=Customersdatas(setup)
#     filternumber=customerdata.customernumberfilter(return_customerdata,workspacedata)
#     # print(filternumber)
#     lstnumbers=filternumber[1]
#     lstdata=filternumber[0]
#     for i in lstdata.json["customers"]:
#         assert lstnumbers[0]==i["phone"]
#
#
#
#
#
# def test_customerlocked(setup,workspacedata,return_customerdata):
#     customerdata=Customersdatas(setup)
#
#     lockeddata=customerdata.customerlocked(return_customerdata,workspacedata)
#     # print(lockeddata)
#     lst=lockeddata[0]
#     res=lockeddata[1]
#     # print(lst)
#
#
#     count=0
#     for i in res.json["customers"]:
#         count+=1
#         assert lst[0]["isActive"]==i["isActive"]
#     print(count)
#
#
# def test_customerunlocked(setup,workspacedata,return_customerdata):
#     customerdata = Customersdatas(setup)
#
#     unlockeddata = customerdata.customerunlocked(return_customerdata, workspacedata)
#     # print(lockeddata)
#     lst = unlockeddata[0]
#     res = unlockeddata[1]
#     # print(lst)
#
#     count = 0
#     for i in res.json["customers"]:
#         count += 1
#         assert lst[0]["isActive"] == i["isActive"]
#     print(count)
#
#
# def test_onboardingaccepted(setup,workspacedata,return_customerdata):
#     customerdata = Customersdatas(setup)
#     onboardingaccepted = customerdata. onboardingaccepted(return_customerdata, workspacedata)
#     lst = onboardingaccepted[0]
#     res = onboardingaccepted[1]
#     count = 0
#     for i in res.json["customers"]:
#         count += 1
#         assert lst[0]["status"] == i["status"]
#     print(count)
#
#
#
# def test_onboardingnotinvited(setup,workspacedata,return_customerdata):
#     customerdata = Customersdatas(setup)
#     onboardingnotinvited1 = customerdata.onboardingnotinvited(return_customerdata, workspacedata)
#     lst = onboardingnotinvited1[0]
#     res = onboardingnotinvited1[1]
#     count = 0
#     for i in res.json["customers"]:
#         count += 1
#         assert lst[0]["status"] == i["status"]
#     print(count)
#
#
#
# def test_onboardinginvited(setup,workspacedata,return_customerdata):
#     customerdata = Customersdatas(setup)
#     onboardinginvited1 = customerdata. onboardinginvited(return_customerdata, workspacedata)
#     lst = onboardinginvited1[0]
#     res = onboardinginvited1[1]
#     count = 0
#     for i in res.json["customers"]:
#         count += 1
#         assert lst[0]["status"] == i["status"]
#     print(count)
#
# #
# def test_filternumber(workspacedata,return_customerdata,setup):
#     customerdata=Customersdatas(setup)
#     filtercustomerdata=customerdata.searchnumber(return_customerdata,workspacedata)
#     lst=filtercustomerdata[0]
#     res=filtercustomerdata[1]
#     for i in res.json["customers"]:
#         assert lst[0] == i["phone"]
#
#
# def test_filtername(workspacedata,return_customerdata,setup):
#     customerdata=Customersdatas(setup)
#     filtename=customerdata. searchbyname(return_customerdata,workspacedata)
#     lst=filtename[0]
#     res=filtename[1]
#     for i in res.json["customers"]:
#         assert lst[0]==i["companyName"]
#
# def test_filtermobile(workspacedata,return_customerdata,setup):
#     customerdata=Customersdatas(setup)
#     filtecode=customerdata.searchbycode(return_customerdata,workspacedata)
#     lst=filtecode[0]
#     res=filtecode[1]
#
#     for i in res.json["customers"]:
#         assert lst[0] == i["distributorCode"]


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


