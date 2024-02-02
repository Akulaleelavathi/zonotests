
from controller.feature.manualorder import *
from controller.feature.customersdata import *


def test_customerdata(return_customerdata):
    logger.error(f"return the customer response{return_customerdata.customersdata2.json}")





def test_customercode(setup,workspacedata,return_customerdata):
    customerdata=Customersdatas(setup)
    filternumber=customerdata.customercodefilter(return_customerdata,workspacedata)
    # print(filternumber)
    lstnumbers=filternumber[1]
    lstdata=filternumber[0]
    # print(lstnumbers)
    # print(lstdata.json)
    assert lstdata.status_code ==200
    for i in lstdata.json["customers"]:
        assert lstnumbers[0]==i["distributorCode"]

    a='2000027013'
    if a in lstnumbers:
        assert True
    else:
        assert False





def test_particalsearchinfiltercustomercode(workspacedata,return_customerdata,setup):
    customerdata=Customersdatas(setup)
    filtecustomercode=customerdata.particalsearchinfiltercustomercode(return_customerdata,workspacedata)
    # print(filtecustomercode)
    assert filtecustomercode.status_code == 200


def test_customernumber(setup,workspacedata,return_customerdata):
    customerdata=Customersdatas(setup)
    filternumber=customerdata.customernumberfilter(return_customerdata,workspacedata)
    lstnumbers=filternumber[1]
    lstdata=filternumber[0]

    # Get the total count of elements in lstnumbers
    total_count = len(lstnumbers)

    # Count non-None values in lstnumbers
    count_non_none = lstnumbers.count(None)

    # Calculate the count of actual values (subtract count_non_none from total_count)
    count_actual_values = total_count - count_non_none

    # Print or return the result
    print(f"Total count: {total_count}")
    print(f"Count of non-None values: {count_non_none}")
    print(f"Count of actual values: {count_actual_values}")

    # return count_actual_values

    assert lstdata.status_code == 200
    for i in lstdata.json["customers"]:
        assert lstnumbers[0]==i["phone"]

    a='0919647297912'
    if a in lstnumbers:
        assert True
    else:
        assert False












def test_customerlocked(setup,workspacedata,return_customerdata):
    customerdata=Customersdatas(setup)

    lockeddata=customerdata.customerlocked(return_customerdata,workspacedata)
    # print(lockeddata)
    lst=lockeddata[0]
    res=lockeddata[1]
    # print(lst)

    assert res.status_code ==200

    count=0
    for i in res.json["customers"]:
        count+=1
        assert lst[0]["isActive"]==i["isActive"]
    print(count)


def test_customerunlocked(setup,workspacedata,return_customerdata):
    customerdata = Customersdatas(setup)

    unlockeddata = customerdata.customerunlocked(return_customerdata, workspacedata)
    # print(lockeddata)
    lst = unlockeddata[0]
    res = unlockeddata[1]
    # print(lst)
    assert res.status_code ==200

    count = 0
    for i in res.json["customers"]:
        count += 1
        assert lst[0]["isActive"] == i["isActive"]
    print(count)


def test_onboardingaccepted(setup,workspacedata,return_customerdata):
    customerdata = Customersdatas(setup)
    onboardingaccepted = customerdata. onboardingaccepted(return_customerdata, workspacedata)
    lst = onboardingaccepted[0]
    res = onboardingaccepted[1]
    assert res.status_code == 200
    count = 0
    for i in res.json["customers"]:
        count += 1
        assert lst[0]["status"] == i["status"]
    print(count)



def test_onboardingnotinvited(setup,workspacedata,return_customerdata):
    customerdata = Customersdatas(setup)
    onboardingnotinvited1 = customerdata.onboardingnotinvited(return_customerdata, workspacedata)
    lst = onboardingnotinvited1[0]
    res = onboardingnotinvited1[1]
    assert res.status_code == 200
    count = 0
    for i in res.json["customers"]:
        count += 1
        assert lst[0]["status"] == i["status"]
    print(count)



def test_onboardinginvited(setup,workspacedata,return_customerdata):
    customerdata = Customersdatas(setup)
    onboardinginvited1 = customerdata. onboardinginvited(return_customerdata, workspacedata)
    lst = onboardinginvited1[0]
    res = onboardinginvited1[1]
    assert res.status_code == 200

    count = 0
    for i in res.json["customers"]:
        count += 1
        assert lst[0]["status"] == i["status"]
    print(count)




def test_searchbycustomermobilenumber(workspacedata,return_customerdata,setup):
    customerdata=Customersdatas(setup)
    filtercustomerdata=customerdata.searchbycustomernumber(return_customerdata,workspacedata)
    lst=filtercustomerdata[0]
    res=filtercustomerdata[1]
    # print(lst)
    assert res.status_code == 200

    for i in res.json["customers"]:
        assert lst[0] == i["phone"]

    a = '0919830310185'
    if a in lst:
        assert True
    else:
        assert False


def test_searchbycustomername(workspacedata,return_customerdata,setup):
    customerdata=Customersdatas(setup)
    filtename=customerdata. searchbycustomername(return_customerdata,workspacedata)
    lst=filtename[0]
    res=filtename[1]


    assert res.status_code == 200

    for i in res.json["customers"]:
        assert lst[0]==i["companyName"]

    a = 'A K MEDICAL STORES'
    if a in lst:
        assert True
    else:
        assert False


def test_searchbycustomercode(workspacedata,return_customerdata,setup):
    customerdata=Customersdatas(setup)
    filtecode=customerdata.searchbycustomercode(return_customerdata,workspacedata)
    lst=filtecode[0]
    res=filtecode[1]
    assert res.status_code == 200

    for i in res.json["customers"]:
        assert lst[0] == i["distributorCode"]

    a = '2000027013'
    if a in lst:
        assert True
    else:
        assert False

def test_searchbyparticalnameorcode(workspacedata,return_customerdata,setup):
    customerdata=Customersdatas(setup)
    filtercode=customerdata.searchbyparticalnameorcode(return_customerdata,workspacedata)
    resdata=filtercode[0]
    filter_name=filtercode[1]



    assert resdata.status_code == 200

    for i in resdata.json["customers"]:
        assert filter_name["searchKey"] in i["phone"][0] or filter_name["searchKey"] in i["distributorCode"] or filter_name["searchKey"] in i["companyName"] , "assertion failure,verify search key sku code"