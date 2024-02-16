import json

from controller.feature.cfa_member import *
from controller.api_util.common_imports import *
def test_datauserme(setup,workspacedata):
    userme= member(setup)

    filtercode = userme.get_datausersme(workspacedata)
    res=filtercode.json
    print(json.dumps(res,indent=4))
    assert filtercode.status_code == 200




def test_workspace(setup,workspacedata):
    userme= member(setup)

    filtercode = userme.get_worspace(workspacedata)
    res=filtercode.json
    print(json.dumps(res,indent=4))
    assert filtercode.status_code == 200
    # 1
    if(res[0]["businessDetails"]["companyName"]!=None):
        assert "True"
    else:
        print( "companyName does not exist or contains an empty value.")
    #2

    if("companyEmail" in res[0]["businessDetails"]!=None):
        assert "true"
    else:
        print("companyEmaildoes not exist or contains an empty value.")
    #3

    if("gstin" in res[0]["businessDetails"]!=None):
        assert "True"
    else:
        print("gstin does not exist or contains an empty value.")

    # 4
    if (res[0]["businessDetails"]["companyRefCode"] !=None and res[0]["businessDetails"]["companyRefCode"] != ""):
        assert "True"
    else:
        print( "Test case failed: 'companyRefCode' does not exist or contains an empty value.")
    # 5
    if(res[0]["businessDetails"]["physicalAddress"]["postcode"]!=None):
        assert "True"
    else:
        print("'postcode' does not exist or contains an empty value.")
    # 6
    if (res[0]["businessDetails"]["physicalAddress"]["state"] != None):
        assert "True"
    else:
        print("'state' does not exist or contains an empty value.")

    # 7

    if (res[0]["businessDetails"]["physicalAddress"]["city"] != None):
        assert "True"
    else:
        print("'city' does not exist or contains an empty value.")

    # 8

    if (res[0]["businessDetails"]["physicalAddress"]["formatted"] != None):
        assert "True"
    else:
        print("'formatted' does not exist or contains an empty value.")
    # 9

    if (res[0]["timeZone"] != None):
        assert "True"
    else:
        print("timeZone does not exist or contains an empty value.")


    # 10
    if (res[0]["defaultCurrencyCode"] != None):
        assert "True"
    else:
        print("defaultCurrencyCode does not exist or contains an empty value.")

    # 11(shortname)

    if (res[0]["spaceName"] != None):
        assert "True"
    else:
         assert print("spaceName does not exist or contains an empty value.")

    # 12
    if (res[0]["profilePic"] != None):
        assert "True"
    else:
         print("profilePic does not exist or contains an empty value.")

#
#

def test_update_users_manal_name(setup,workspacedata,return_member):
    userme = member(setup)

    filtercode = userme.update_users_manal(return_member,workspacedata)
    res = filtercode[0]
    lst1=filtercode[1]
    name=filtercode[2]
    print(res.json)
    # print(lst1)
    # print(name)
    assert res.json["data"]["firstName"]==lst1


def test_update_users_email(setup,workspacedata,return_member):
    userme = member(setup)

    filtercode = userme.update_users(return_member,workspacedata)
    res = filtercode[0]
    lst1=filtercode[1]
    email=filtercode[2]
    print(json.dumps(res.json,indent=4))
    # print(lst1)
    # print(email)
    assert res.json["data"]["email"] == lst1[1]















































#
#
# def test_updated_data_grayemail(setup, workspacedata, return_member):
#     userme = member(setup)
#     filtercode = userme.updated_data_grayemail(return_member,workspacedata)
#     res=filtercode[0]
#     lst1 = filtercode[1]
#     lst2 = filtercode[2]
#     lst3 = filtercode[3]
#     print(res)
#     # print(lst1)
#     # print(lst2)
#     # print(lst3)
#     # assert res.json["companyEmail"]==lst3[0][2]
#
# # def test_updated_data_gstnumber(setup, workspacedata, return_member):
# #     userme = member(setup)
# #     filtercode = userme.updated_data_gstnumber(return_member, workspacedata)
# #     res = filtercode[0]
# #     lst1 = filtercode[1]
# #     lst2 = filtercode[2]
# #     lst3 = filtercode[3]
# #     print(res.json)
# #     # assert res.json["gstin"]==lst3[0][1]
#
#
# # def test_updated_currency(setup, workspacedata, return_member):
# #     userme = member(setup)
# #     filtercode = userme.updated_currency(return_member, workspacedata)
# #     res = filtercode[0]
# #     lst1 = filtercode[1]
# #     lst2 = filtercode[2]
# #     lst3 = filtercode[3]
# #     print(res.json)
# #     # assert res.json["defaultCurrencyCode"] == lst2[0][2]
# #
# #
# #
# #
# # def test_updated_countrycode(setup, workspacedata, return_member):
# #     userme = member(setup)
# #
# #     filtercode = userme.updated_countrycode(return_member,workspacedata)
# #     res=filtercode[0]
# #     lst1=filtercode[1]
# #     lst2=filtercode[2]
# #     lst3=filtercode[3]
# #     print(res.json)
# #     # print(lst1)
# #     # print(lst3)
# #     # print(lst2)
# #     # assert res.json["workspace"]["isoCountryCode"]==lst2[0][4]
# #
# #
# #
# #
# #
# #
# #
# #
# #
# #
# #
# #
# #
# #
# #
# #
# #
# #
# #
# #
# #
# #
# #
# #
# #
# #
# #
# #
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
#
#
#
#
#
#
#
#
# # def test_update_users(setup,workspacedata,return_member):
# #     userme = member(setup)
# #
# #     filtercode = userme.update_users(return_member,workspacedata)
# #     res = filtercode[0]
# #     lst1=filtercode[1]
# #     print(res.json)
# #     print(lst1)