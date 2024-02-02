from controller.feature.orders import *
from controller.feature.manualorder import *
from controller.feature.customersdata import *


def test_orders(return_orders,setup,workspacedata):
    logger.error(f"return the customer response{return_orders.ordersdata2.json}")


def test_importsourceuploadfilter(return_orders,setup,workspacedata):
    ordersdata=Orders(setup)
    importsourcefilter=ordersdata.importsourceuploadfilter(return_orders,workspacedata)
    res=importsourcefilter[1]
    lst=importsourcefilter[0]
    # print(res.json)
    # print(lst)

    assert res.status_code==201
    for i in res.json["order"]:
        assert lst[0]["poFile"]["importSource"]==i["poFile"]["importSource"]

def test_importsourcemanualfilter(return_orders,setup,workspacedata):
    ordersdata=Orders(setup)
    importsourcefilter=ordersdata.importsourcemanualfilter(return_orders,workspacedata)
    res=importsourcefilter[1]
    lst=importsourcefilter[0]
    # print(res.json)
    # print(lst)

    assert res.status_code==201
    for i in res.json["order"]:
        assert lst[0]["poFile"]["importSource"]==i["poFile"]["importSource"]



def test_customerfilter(setup,workspacedata,return_orders):
    ordersdata=Orders(setup)
    customerfilter=ordersdata.customerfilter(return_orders,workspacedata)
    res=customerfilter[0]
    lst=customerfilter[1]
    # print(res.json)
    # print(lst)
    assert res.status_code==201
    for i in res.json["order"]:
        assert lst[0]==i["customerId"]

def test_manualcustomerfilter(setup,workspacedata,return_orders):
    ordersdata=Orders(setup)
    customerfilter=ordersdata.manualcustomerfilter(return_orders,workspacedata)
    res=customerfilter[0]
    lst=customerfilter[1]
    # print(res.json)
    # print(lst)
    assert res.status_code==201
    for i in res.json["order"]:
        assert lst==i["customerId"]


def test_orderstatusfilterconfirmed(setup,workspacedata,return_orders):
    ordersdata=Orders(setup)
    customerfilter=ordersdata.orderstatusfilterconfirmed(return_orders,workspacedata)
    res=customerfilter[0]
    lst=customerfilter[1]
    # print(res.json)
    # print(lst)
    assert res.status_code==201
    for i in res.json["order"]:
        assert lst[0]["status"]==i["status"]


def test_orderstatusWaitingForCNFfilter(setup,workspacedata,return_orders):
    ordersdata=Orders(setup)
    customerfilter=ordersdata.orderstatusWaitingForCNFfilter(return_orders,workspacedata)
    res=customerfilter[0]
    lst=customerfilter[1]
    # print(res.json)
    # print(lst)
    assert res.status_code==201
    for i in res.json["order"]:
        assert lst[0]["status"]==i["status"]


def test_orderstatusSubmitted(setup,workspacedata,return_orders):
    ordersdata=Orders(setup)
    customerfilter=ordersdata.orderstatusSubmitted(return_orders,workspacedata)
    res=customerfilter[0]
    lst=customerfilter[1]
    # print(res.json)
    # print(lst)
    assert res.status_code==201
    for i in res.json["order"]:
        assert lst[0]["status"]==i["status"]



def test_orderstatusBilled(setup,workspacedata,return_orders):
    ordersdata=Orders(setup)
    customerfilter=ordersdata.orderstatusBilled(return_orders,workspacedata)
    res=customerfilter[0]
    lst=customerfilter[1]
    # print(res.json)
    # print(lst)
    assert res.status_code==201
    for i in res.json["order"]:
        assert lst[0]["status"]==i["status"]


def test_searchbyordernumber(setup,workspacedata,return_orders):
    ordersdata = Orders(setup)
    customerfilter = ordersdata.searchbyordernumber(return_orders, workspacedata)
    # print(customerfilter)

    res=customerfilter[1]
    lst=customerfilter[0]
    assert res.status_code==201
    for i in res.json["order"]:
        assert lst[0]==i["orderMetaData"]["refOrderNumber"]


def test_searchbyconumber(setup,workspacedata,return_orders):
    ordersdata = Orders(setup)
    customerfilter = ordersdata.searchbyconumber(return_orders, workspacedata)
    # print(customerfilter)

    res=customerfilter[0]
    lst=customerfilter[1]
    # print(res.json)
    # print(lst)
    assert res.status_code==201
    for i in res.json["order"]:
        assert lst[1]==i["erpOrderNumber"]


def test_searchbyparticalco_or_po_or_code(workspacedata,return_orders,setup):
    ordersdata=Orders(setup)
    filtercode= ordersdata.searchbyparticalco_or_po_or_code(return_orders,workspacedata)
    resdata=filtercode[0]
    lst=filtercode[1]
    assert resdata.status_code == 201
    for i in resdata.json["order"]:
        assert (lst in i["erpOrderNumber"] or lst in i["orderMetaData"]["erpOrderNumber"] or lst in i["poFile"]["poNumber"]), "assertion failure,verify search key  code"

                                        # singleinall#
def test_singleorderinall(workspacedata,return_orders,setup):
    ordersdata = Orders(setup)
    filtercode = ordersdata.singleorderinall(return_orders, workspacedata)
    resdata = filtercode[0]
    lst = filtercode[1]
    # print(resdata.json)
    # print(lst)
    assert resdata.status_code == 201
    # for i in resdata.json["order"]:
    assert lst[0][1]==resdata.json["customerId"]
    assert lst[0][2]==resdata.json["skucount"]


def test_particalsearchbysku_or_producttitle(return_orders,setup,workspacedata):

    ordersdata = Orders(setup)
    filtercode = ordersdata.particalsearchbysku_or_producttitle(return_orders, workspacedata)

    resdata = filtercode[0]
    number = filtercode[1]
    # print(resdata.json)
    # print(number)
    assert resdata.status_code == 201
    i=resdata.json
    assert (number in i["products"][0]["parentSku"] or number in i["products"][0]["productVariants"][0]["name"]), "Assertion failure: Verify search key code"




def test_searchbysku(return_orders,setup,workspacedata):

    ordersdata = Orders(setup)
    filtercode = ordersdata.searchbysku(return_orders, workspacedata)

    resdata = filtercode[0]
    number = filtercode[1]
    # lst=filtercode[2]
    # print(resdata.json)
    # print(number)
    # print(lst)
    assert resdata.status_code == 201
    i=resdata.json
    assert (number in i["products"][0]["parentSku"] or number in i["products"][0]["productVariants"][0]["name"]), "Assertion failure: Verify search key code"


def test_searchbyname(return_orders,setup,workspacedata):

    ordersdata = Orders(setup)
    filtercode = ordersdata.searchbyname(return_orders, workspacedata)

    resdata = filtercode[0]
    number = filtercode[1]
    # lst=filtercode[2]
    # print(resdata.json)
    # print(number)
    # print(lst)
    assert resdata.status_code == 201
    i=resdata.json
    assert (number in i["products"][0]["parentSku"] or number in i["products"][0]["productVariants"][0]["name"]), "Assertion failure: Verify search key code"





def test_divisionfilter(return_orders,setup,workspacedata):
    ordersdata = Orders(setup)
    filtercode = ordersdata.divisionfilter(return_orders, workspacedata)
    res=filtercode[0]
    lst=filtercode[1]
    print(res.json)
    print(lst)
    assert res.status_code == 201
    i=res.json
    assert lst[0][0]==i["id"]
    assert lst[0][2]==i["divisions"][0]["divisionId"]



def test_modifiedquantitytrue(return_orders,setup,workspacedata):
    ordersdata = Orders(setup)
    filtercode = ordersdata.modifiedquantitytrue(return_orders, workspacedata)
    res = filtercode[0]
    lst = filtercode[1]
    assert res.status_code == 201



def test_modifiedquantityfalse(return_orders,setup,workspacedata):
    ordersdata = Orders(setup)
    filtercode = ordersdata.modifiedquantitytrue(return_orders, workspacedata)
    res = filtercode[0]
    lst = filtercode[1]
    assert res.status_code == 201



def test_invoiced(return_orders,setup,workspacedata):
    ordersdata = Orders(setup)
    filtercode = ordersdata.invoicedfilter(return_orders, workspacedata)
    res = filtercode[0]
    lst = filtercode[1]
    assert res.status_code == 201



def test_Notinvoiced(return_orders,setup,workspacedata):
    ordersdata = Orders(setup)
    filtercode = ordersdata.Notinvoicedfilter(return_orders, workspacedata)
    res = filtercode[0]
    assert res.status_code == 201


def test_schemsappiledfilter(return_orders,setup,workspacedata):
    ordersdata = Orders(setup)
    filtercode = ordersdata.schemsappiledfilter(return_orders, workspacedata)
    res = filtercode[0]
    lst = filtercode[1]
    assert res.status_code == 201



def test_schemsnotappiledfilter(return_orders,setup,workspacedata):
    ordersdata = Orders(setup)
    filtercode = ordersdata.schemsnotappiledfilter(return_orders, workspacedata)
    res = filtercode[0]
    lst = filtercode[1]
    assert res.status_code == 201
    i = res.json
    assert lst[0][0] == i["id"]
    assert lst[0][1] == i["customerId"]

                                          # wfc#

def test_waitingforcfadatadetails(return_orders,setup,workspacedata):
     logger.error(f"return the customer response{return_orders.ordersdata4.json}")




def test_importsourceuploadfilterwfc(return_orders,setup,workspacedata):
    ordersdata=Orders(setup)
    importsourcefilter=ordersdata.importsourceuploadfilter(return_orders,workspacedata)
    res=importsourcefilter[1]
    lst=importsourcefilter[0]
    # print(res.json)
    # print(lst)

    assert res.status_code==201
    for i in res.json["order"]:
        assert lst[0]["poFile"]["importSource"]==i["poFile"]["importSource"]




def test_importsourcemanualfilterwfa(return_orders,setup,workspacedata):
    ordersdata=Orders(setup)
    importsourcefilter=ordersdata.importsourcemanualfilterwfc(return_orders,workspacedata)
    res=importsourcefilter[1]
    lst=importsourcefilter[0]
    # print(res.json)
    # print(lst)

    assert res.status_code==201
    for i in res.json["order"]:
        assert lst[0]["poFile"]["importSource"]==i["poFile"]["importSource"]

def test_customerfilterwfc(setup,workspacedata,return_orders):
    ordersdata=Orders(setup)
    customerfilter=ordersdata.customerfilterwfc(return_orders,workspacedata)
    res=customerfilter[0]
    lst=customerfilter[1]
    # print(res.json)
    # print(lst)
    assert res.status_code==201
    for i in res.json["order"]:
        assert lst[0]==i["customerId"]

def test_manualcustomerfilterwfc(setup,workspacedata,return_orders):
    ordersdata=Orders(setup)
    customerfilter=ordersdata.manualcustomerfilterwfc(return_orders,workspacedata)
    res=customerfilter[0]
    lst=customerfilter[1]
    # print(res.json)
    # print(lst)
    assert res.status_code==201
    for i in res.json["order"]:
        assert lst==i["customerId"]
#
#
# # def test_orderstatusWaitingForCNFfilterwfc(setup,workspacedata,return_orders):
# #     ordersdata=Orders(setup)
# #     customerfilter=ordersdata.orderstatusWaitingForCNFfilterwfc(return_orders,workspacedata)
# #     res=customerfilter[0]
# #     lst=customerfilter[1]
# #     # print(res.json)
# #     print(lst)
# #     assert res.status_code==201
# #     for i in res.json["order"]:
# #          assert lst["status"]==i["status"]
# #
# #
# #
# # def test_orderstatusfilterconfirmedwfc(setup,workspacedata,return_orders):
# #     ordersdata=Orders(setup)
# #     customerfilter=ordersdata.orderstatusfilterconfirmedwfc(return_orders,workspacedata)
# #     res=customerfilter[0]
# #     lst=customerfilter[1]
# #     # print(res.json)
# #     # print(lst)
# #     assert res.status_code==201
# #     for i in res.json["order"]:
# #         assert lst["status"]==i["status"]
# #


# #
# #
# # def test_orderstatusBilledwfc(setup,workspacedata,return_orders):
# #     ordersdata=Orders(setup)
# #     customerfilter=ordersdata.orderstatusBilledwfc(return_orders,workspacedata)
# #     res=customerfilter[0]
# #     lst=customerfilter[1]
# #     # print(res.json)
# #     # print(lst)
# #     assert res.status_code==201
# #     for i in res.json["order"]:
# #         assert lst["status"]==i["status"]
#

def test_orderstatusSubmittedwfc(setup,workspacedata,return_orders):
    ordersdata=Orders(setup)
    customerfilter=ordersdata.orderstatusSubmittedwfc(return_orders,workspacedata)
    res=customerfilter[0]
    lst=customerfilter[1]
    # print(res.json)
    # print(lst)
    assert res.status_code==201
    for i in res.json["order"]:
        assert lst[0]["status"]==i["status"]




def test_searchbyordernumberwfc(setup,workspacedata,return_orders):
    ordersdata = Orders(setup)
    customerfilter = ordersdata.searchbyordernumberwfc(return_orders, workspacedata)
    # print(customerfilter)

    res=customerfilter[1]
    lst=customerfilter[0]
    assert res.status_code==201
    for i in res.json["order"]:
        assert lst[0]==i["orderMetaData"]["refOrderNumber"]


def test_searchbyconumberwfc(setup,workspacedata,return_orders):
    ordersdata = Orders(setup)
    customerfilter = ordersdata.searchbyconumberwfc(return_orders, workspacedata)


    res=customerfilter[0]
    lst=customerfilter[1]

    assert res.status_code==201




def test_searchbyparticalco_or_po_or_codewfc(workspacedata,return_orders,setup):
    ordersdata=Orders(setup)
    filtercode= ordersdata.searchbyparticalco_or_po_or_codewfc(return_orders,workspacedata)
    resdata=filtercode[0]
    lst=filtercode[1]
    assert resdata.status_code == 201
    for i in resdata.json["order"]:
        assert (lst in i["erpOrderNumber"] or lst in i["orderMetaData"]["erpOrderNumber"] or lst in i["poFile"]["poNumber"]), "assertion failure,verify search key  code"

                                              # singleinwfc#
def test_singleorderinwfc(workspacedata,return_orders,setup):
    ordersdata = Orders(setup)
    filtercode = ordersdata.singleorderinwfc(return_orders, workspacedata)
    resdata = filtercode[0]
    lst = filtercode[1]
    # print(resdata.json)
    # print(lst)
    assert resdata.status_code == 201
    # for i in resdata.json["order"]:
    assert lst[19][1]==resdata.json["customerId"]
    assert lst[19][2]==resdata.json["skucount"]



def test_particalsearchbysku_or_producttitlewfc(return_orders,setup,workspacedata):

    ordersdata = Orders(setup)
    filtercode = ordersdata.particalsearchbysku_or_producttitlewfc(return_orders, workspacedata)

    resdata = filtercode[0]
    number = filtercode[1]
    # print(resdata.json)
    # print(number)
    assert resdata.status_code == 201
    i=resdata.json
    assert (number in i["products"][0]["parentSku"] or number in i["products"][0]["productVariants"][0]["name"]), "Assertion failure: Verify search key code"




def test_searchbyskuwfc(return_orders,setup,workspacedata):

    ordersdata = Orders(setup)
    filtercode = ordersdata.searchbyskuwfc(return_orders, workspacedata)

    resdata = filtercode[0]
    number = filtercode[1]

    assert resdata.status_code == 201
    i=resdata.json
    assert (number in i["products"][0]["parentSku"] or number in i["products"][0]["productVariants"][0]["name"]), "Assertion failure: Verify search key code"


def test_searchbynamewfc(return_orders,setup,workspacedata):

    ordersdata = Orders(setup)
    filtercode = ordersdata.searchbynamewfc(return_orders, workspacedata)

    resdata = filtercode[0]
    number = filtercode[1]

    assert resdata.status_code == 201
    i=resdata.json
    assert (number in i["products"][0]["parentSku"] or number in i["products"][0]["productVariants"][0]["name"]), "Assertion failure: Verify search key code"


def test_divisionfilterwfc(return_orders,setup,workspacedata):
    ordersdata = Orders(setup)
    filtercode = ordersdata.divisionfilterwfc(return_orders, workspacedata)
    res=filtercode[0]
    lst=filtercode[1]
    print(res.json)
    print(lst)
    assert res.status_code == 201
    i=res.json
    assert lst[0][0]==i["id"]
    assert lst[0][2]==i["divisions"][0]["divisionId"]




def test_invoicedwfc(return_orders,setup,workspacedata):
    ordersdata = Orders(setup)
    filtercode = ordersdata.invoicedfilterwfc(return_orders, workspacedata)
    res = filtercode[0]
    lst = filtercode[1]
    assert res.status_code == 201



def test_Notinvoicedwfc(return_orders,setup,workspacedata):
    ordersdata = Orders(setup)
    filtercode = ordersdata.Notinvoicedfilterwfc(return_orders, workspacedata)
    res = filtercode[0]
    assert res.status_code == 201


def test_schemsappiledfilterwfc(return_orders,setup,workspacedata):
    ordersdata = Orders(setup)
    filtercode = ordersdata.schemsappiledfilterwfc(return_orders, workspacedata)
    res = filtercode[0]
    lst = filtercode[1]
    assert res.status_code == 201



def test_schemsnotappiledfilterwfc(return_orders,setup,workspacedata):
    ordersdata = Orders(setup)
    filtercode = ordersdata.schemsnotappiledfilterwfc(return_orders, workspacedata)
    res = filtercode[0]
    lst = filtercode[1]
    assert res.status_code == 201
    i = res.json
    assert lst[0][0] == i["id"]
    assert lst[0][1] == i["customerId"]




