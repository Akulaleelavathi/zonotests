from controller.feature.schems import *
def test_get_schems(workspacedata,setup):
    schems=Schems(setup)
    get_schems=schems.get_schems(workspacedata)
    assert (get_schems["startRecord"])
    assert get_schems["promotions"][0]["promotionCode"]
    assert get_schems["promotions"][0]["promotionType"]
    assert get_schems["promotions"][0]["sku"]
    assert get_schems["promotions"][0]["skusX"]
    assert get_schems["promotions"][0]["skusY"]
    assert get_schems["promotions"][0]["slabs"][0]["code"]
    assert get_schems["promotions"][0]["slabs"][0]["args"][0]["name"]
    assert get_schems["promotions"][0]["minimumQty"]


