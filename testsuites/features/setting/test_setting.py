import json
#9677696307
from controller.feature.settings import *
from controller.api_util.common_imports import *

def test_datauserme(setup,workspacedata):
    userme= Setting(setup)

    filtercode = userme.get_datausersme(workspacedata)
    res=filtercode.json
    # print(json.dumps(res,indent=4))
    assert filtercode.status_code == 200
    assert "firstName" in res and res["firstName"], "firstName does not exist or contains an empty value."
    assert "email" in res and res["email"],"email does not exist or contains an empty value."




def test_workspace(setup,workspacedata):
    userme= Setting(setup)

    filtercode = userme.get_worspace(workspacedata)
    res=filtercode.json
    # print(json.dumps(res,indent=4))
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




def test_updated_data(setup, workspacedata, return_settings):
    userme = Setting(setup)

    filtercode = userme.updated_data(return_settings,workspacedata)
    res=filtercode[0]
    lst1=filtercode[1]
    lst2=filtercode[2]
    lst3=filtercode[3]
    # print(res.json)
    # print(lst1)
    # print(lst3)
    # print(lst2)
    assert res.json["spaceName"]==lst2[0][1]
    assert res.status_code==200

def test_updated_data_grayemail(setup, workspacedata, return_settings):
    userme = Setting(setup)
    filtercode = userme.updated_data_grayemail(return_settings,workspacedata)
    res=filtercode[0]
    lst1 = filtercode[1]
    lst2 = filtercode[2]
    lst3 = filtercode[3]
    # print(res.json)
    assert res.status_code==200

    assert res.json["companyEmail"]==lst3[0][2]

def test_updated_data_gstnumber(setup, workspacedata, return_settings):
    userme = Setting(setup)
    filtercode = userme.updated_data_gstnumber(return_settings, workspacedata)
    res = filtercode[0]
    lst1 = filtercode[1]
    lst2 = filtercode[2]
    lst3 = filtercode[3]
    # print(res.json)
    assert res.status_code==200

    assert res.json["gstin"]==lst3[0][1]


def test_updated_currency(setup, workspacedata, return_settings):
    userme = Setting(setup)
    filtercode = userme.updated_currency(return_settings, workspacedata)
    res = filtercode[0]
    lst1 = filtercode[1]
    lst2 = filtercode[2]
    lst3 = filtercode[3]
    # print(res.json)
    assert res.status_code==200

    assert res.json["defaultCurrencyCode"] == lst2[0][2]




def test_updated_countrycode(setup, workspacedata, return_settings):
    userme = Setting(setup)

    filtercode = userme.updated_countrycode(return_settings,workspacedata)
    res=filtercode[0]
    lst1=filtercode[1]
    lst2=filtercode[2]
    lst3=filtercode[3]
    # print(res.json)
    # print(lst1)
    # print(lst3)
    # print(lst2)
    assert res.status_code==200

    assert res.json["workspace"]["isoCountryCode"]==lst2[0][4]




def test_update_users_email(setup,workspacedata,return_settings):
    userme = Setting(setup)

    filtercode = userme.update_users(return_settings,workspacedata)
    res = filtercode[0]
    lst1=filtercode[1]
    email=filtercode[2]
    # print(json.dumps(res.json,indent=4))
    # print(lst1)
    # print(email)
    assert res.status_code==200

    assert res.json["data"]["email"] == email






def test_update_users_manal_name(setup,workspacedata,return_settings):
    userme = Setting(setup)

    filtercode = userme.update_users_manal(return_settings,workspacedata)
    res = filtercode[0]
    lst1=filtercode[1]
    name=filtercode[2]
    # print(res.json)
    # print(lst1)
    # print(name)
    assert res.status_code==200

    assert res.json["data"]["firstName"]==lst1


def test_updated_data_address(setup, workspacedata, return_settings):
    userme = Setting(setup)
    filtercode = userme.updated_data_address(return_settings,workspacedata)
    res=filtercode[0]
    address = filtercode[1]

    # print(res.json)
    assert res.status_code==200

    assert res.json["physicalAddress"]["formatted"]==address


def test_updated_postcode(setup, workspacedata, return_settings):
    userme = Setting(setup)
    filtercode = userme.updated_postcode(return_settings,workspacedata)
    res=filtercode[0]
    postcode = filtercode[1]

    # print(res.json)
    assert res.status_code==200

    assert res.json["physicalAddress"]["postcode"]==postcode



def test_updated_city(setup, workspacedata, return_settings):
    userme = Setting(setup)
    filtercode = userme.updated_data_city(return_settings,workspacedata)
    res=filtercode[0]
    city= filtercode[1]

    # print(res.json)
    assert res.status_code==200

    assert res.json["physicalAddress"]["city"]==city
#



def test_updated_state(setup, workspacedata, return_settings):
    userme = Setting(setup)
    filtercode = userme.updated_data_state(return_settings,workspacedata)
    res=filtercode[0]
    state= filtercode[1]

    # print(res.json)
    assert res.status_code==200

    assert res.json["physicalAddress"]["state"]==state






# def test_workspace(setup,workspacedata):
#     userme= Setting(setup)
#
#     filtercode = userme.get_worspace(workspacedata)
#     res=filtercode.json
#     print(json.dumps(res,indent=4))
#     assert filtercode.status_code == 200





def test_updated_data_single_data(setup,workspacedata,return_settings):
    userme= Setting(setup)

    filtercode = userme.updated_data_single_data(return_settings,workspacedata)
    res=filtercode
    print(json.dumps(res.json,indent=4))
    assert filtercode.status_code == 422
#
#
#
#
# def test_number(setup,workspacedata):
#     var=setup.token
#     print(json.dumps(var.json,indent=4))
#     for i in var.json







