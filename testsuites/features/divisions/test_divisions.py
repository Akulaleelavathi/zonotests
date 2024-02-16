import json

from controller.feature.division import *


def test_get_divisionsdata(return_divisions,setup,workspacedata):
    ordersdata = divisions(setup)
    filtercode = ordersdata.get_divisions(return_divisions)
    res=filtercode
    assert res.status_code == 200
    # print(json.dumps(res.json, indent=4))
    # assert res.json ["divisions"][0]["name"]=="AKUNA"
    assert  res.json ["divisions"][0]["name"]
    assert res.json ["divisions"][0]["code"]
    assert res.json ["divisions"][0]["headDivision"]["name"]
    assert res.json["divisions"][0]["headDivision"]["code"]
    assert res.json ["divisions"][0]["numberOfCustomer"]
    count=0
    for i in res.json["divisions"]:
        count+=1
        assert "name" in i
    print(count)

    assert "startRecord" in res.json
    assert "endRecord" in res.json




def test_get_manual_data(return_divisions,setup,workspacedata):
    ordersdata = divisions(setup)
    filtercode = ordersdata.get_manual_data(return_divisions)
    res=filtercode
    assert res.status_code == 200
    # print(json.dumps(res.json, indent=4))

    assert res.json ["divisions"][0]["name"]=="AKUNA"
    # assert res.json["divisions"][0]["code"] == "00"
    # assert res.json["divisions"][0]["headDivision"]["name"] == "Common Division CHC"
    assert "startRecord" in res.json
    assert "endRecord" in res.json



def test_get_dec(return_divisions,setup,workspacedata):
    ordersdata = divisions(setup)
    filtercode = ordersdata.get_dec(return_divisions)
    res=filtercode
    assert res.status_code == 200
    # print(json.dumps(res.json, indent=4))
    assert res.json ["divisions"][0]["name"]=="VEGA"
    assert "startRecord" in res.json
    assert "endRecord" in res.json


def test_get_deccode(return_divisions,setup,workspacedata):
    ordersdata = divisions(setup)
    filtercode = ordersdata.get_deccode(return_divisions)
    res=filtercode
    assert res.status_code == 200
    # print(json.dumps(res.json, indent=4))
    assert res.json ["divisions"][0]["code"]=="V0"
    assert "startRecord" in res.json
    assert "endRecord" in res.json




def test_get_aeccode(return_divisions,setup,workspacedata):
    ordersdata = divisions(setup)
    filtercode = ordersdata.get_aeccode(return_divisions)
    res=filtercode
    assert res.status_code == 200
    # print(json.dumps(res.json, indent=4))
    assert res.json ["divisions"][0]["code"]=="00"
    assert "startRecord" in res.json
    assert "endRecord" in res.json



def test_get_HeadDivisionASC(return_divisions,setup,workspacedata):
    ordersdata = divisions(setup)
    filtercode = ordersdata.get_HeadDivisionASC(return_divisions)
    res=filtercode
    assert res.status_code == 200
    # print(json.dumps(res.json, indent=4))
    assert res.json ["divisions"][0]["headDivision"]["name"]=="Common Division CHC"
    assert "startRecord" in res.json
    assert "endRecord" in res.json


def test_get_HeadDivisionDESC(return_divisions,setup,workspacedata):
    ordersdata = divisions(setup)
    filtercode = ordersdata.get_HeadDivisionDESC(return_divisions)
    res=filtercode
    assert res.status_code == 200
    # print(json.dumps(res.json, indent=4))
    assert res.json ["divisions"][0]["headDivision"]["name"]=="Cross Div Pharma"
    assert "startRecord" in res.json
    assert "endRecord" in res.json



def test_get_manual_search_data(return_divisions,setup,workspacedata):
    ordersdata = divisions(setup)
    filtercode = ordersdata.get_manual_search_data(return_divisions)
    res=filtercode
    assert res.status_code == 200
    for i in res.json["divisions"]:
        assert i["headDivision"]["name"] or i["headDivision"]["name"]
    # print(json.dumps(res.json, indent=4))



def test_get_name_search_data(return_divisions,setup,workspacedata):
    ordersdata = divisions(setup)
    filtercode = ordersdata.get_name_search_data(return_divisions)
    res=filtercode
    assert res.status_code == 200
    # print(json.dumps(res.json, indent=4))



def test_get_name_search_code(return_divisions,setup,workspacedata):
    ordersdata = divisions(setup)
    filtercode = ordersdata.get_name_search_code(return_divisions)
    res=filtercode
    assert res.status_code == 200
    # print(json.dumps(res.json, indent=4))

