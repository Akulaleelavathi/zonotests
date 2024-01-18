import json

import pytest

from controller.api_util.base_request import Base, BaseAssertion
from controller.api_util.common_imports import *

class CustomerId(Base):
    def _init_(self,settings):
        Base._init_(self,settings)
        self.settings=settings

    def get_customerid(self,workspaces_data):
        res=self.send_request(
            Base.RequestMethod.GET,
            custom_url="https://api-uat.beta.pharmconnect.com/customers/8ef5d569-3419-44e5-bb33-3ecfd260f796?includeCustomerGroupAssignments=1&includeWorkspaceMembers=1&pageNo=4&pageSize=40&includeOrderCount=1",
        )
        # return res.json
        responsejson=res.json
        list = []

        for i in responsejson["customers"]:
            list.append({"name":i["companyName"],"id":i["id"]})
        # return list
        for i in list:
            if i["name"] == "RAJASTHAN DRUG HOUSE":
                return (i["id"])

    def upload(self,workspaces_data,get_customerid):
        file_path = r"C:\Users\Lenovo\Downloads\RAJASTHAN DRUG HOUSE.xlsx"

        res = self.send_request(
            Base.RequestMethod.POST,
            custom_url="https://api-uat.beta.pharmconnect.com/commerce-v2/poFile/upload/8ef5d569-3419-44e5-bb33-3ecfd260f796?customerId=0938ed8d-09e0-42f3-af27-126d743b4e2b&importSource=upload&parserType=C2D_ORDER",
            payload={
                "customerId": get_customerid,
                "importSource": "upload",
                "parserType": "C2D_ORDER",
            },
            headers={},
            files={'file': open(file_path, 'rb')}
        )

        # return res
        responsejson=res.json
        mapped_data = []
        unmapped_data = []
        for i in responsejson:
            if i["status"] == "MAPPED":
                a = {"pvId": i["productVariantId"], "qty": i["quantity"], "PF_line_id": i["id"], "pf_id": i["poFileId"]}
                mapped_data.append(a)
            else:
                a = {"product_name": i["distributorProductName"], "pvId": i["productVariantId"], "qty": i["quantity"],
                     "PF_line_id": i["id"], "pf_id": i["poFileId"]}
                unmapped_data.append(a)

        # result = {"mapped_data": mapped_data, "unmapped_data": unmapped_data}
        # return result

        empty_data = []
        for i in unmapped_data:
            res = self.send_request(
                Base.RequestMethod.POST,
                custom_url="https://api-uat.beta.pharmconnect.com/commerce-v2/products/search/customer/8ef5d569-3419-44e5-bb33-3ecfd260f796?customerId=0938ed8d-09e0-42f3-af27-126d743b4e2b&pageNo=1&pageSize=20",
                payload={
                    "searchKey": i["product_name"]
                })
            responsejson=res.json
            if responsejson["total"] != 0:
                if i["data"]["qty"] == 0:
                    a = {"pvId": responsejson["products"][0]["productVariants"][0]["productVariantId"],
                         "qty": responsejson["products"][0]["productVariants"][0]["minOrderQty"],
                         "PF_line_id": i["data"]["PF_line_id"], "pf_id": i["data"]["pf_id"]}
                    mapped_data.append(a)
                else:
                    a = {"pvId": responsejson["products"][0]["productVariants"][0]["productVariantId"],
                         "qty": i["data"]["qty"],
                         "PF_line_id": i["data"]["PF_line_id"], "pf_id": i["data"]["pf_id"]}
                    mapped_data.append(a)
            else:
                a = f'{i["product_name"]} not there in products'

                empty_data.append(a)

            return (mapped_data)


    def add_to_card(self,workspaces_data, upload,get_customerid):
        res=self.send_request(
            Base.RequestMethod.POST,
            custom_url="https://api-uat.beta.pharmconnect.com/commerce-v2/orders/additemtoactiveorder/8ef5d569-3419-44e5-bb33-3ecfd260f796",
            payload={

                "customerId": get_customerid,
                "sellerWorkspaceId":"8ef5d569-3419-44e5-bb33-3ecfd260f796" ,
                "source": "upload",
                "poFileId":upload[0]["pf_id"],
                "lines": [
                    {
                        "productVariantId": i["pvId"],
                        "quantity": i["qty"],
                        "poFileLineId": i["PF_line_id"]
                    } for i in upload
                ]

            })
        responsejson=res.json
        # return responsejson
        return (responsejson["orders"][0]["pofileId"])


    def check_out(self,workspaces_data,add_to_card,get_customerid):
        res = self.send_request(
            Base.RequestMethod.POST,
            custom_url="https://api-uat.beta.pharmconnect.com/commerce-v2/orders/checkout/8ef5d569-3419-44e5-bb33-3ecfd260f796",
            payload={
                "sellerWorkspaceId": "8ef5d569-3419-44e5-bb33-3ecfd260f796",
                "customerId": get_customerid,
                "poFileIds": [
                    add_to_card
                ]

            })
        responsejson=res.json
        return(responsejson)



