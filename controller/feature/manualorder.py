
from controller.api_util.base_request import Base, BaseAssertion
from controller.api_util.common_imports import *

class CustomerId(Base):
    def _init_(self,settings):
        Base._init_(self,settings)
        self.settings=settings

    def get_customerid(self,workspaces_data):
        res=self.send_request(
            Base.RequestMethod.GET,
            custom_url="https://api-uat.beta.pharmconnect.com/customers/8ef5d569-3419-44e5-bb33-3ecfd260f796?includeCustomerGroupAssignments=1&includeWorkspaceMembers=1&pageNo=1&pageSize=20&includeOrderCount=1",
        )
        # return res.json
        responsejson=res.json
        list = []

        for i in responsejson["customers"]:
            list.append(i["id"])
        return list
    def get_placeorderdetails(self,customer_data,workspacedata):
        res=self.send_request(
            Base.RequestMethod.POST,
            custom_url="https://api-uat.beta.pharmconnect.com/commerce-v2/products/search/customer/8ef5d569-3419-44e5-bb33-3ecfd260f796?pageNo=1&pageSize=20&customerId=36917aa5-b58d-4ff6-8b28-94fff14c8624",
            payload={
            "includeFacets": True,
            "includeDivisions": True,
            "includeCfas": True,
            "skuCode": "",
            "sortDirection": "ASC",
            "sortBy": "",
            "inventoryFilter": "",
            "stockFilter": "",
            "divisionIds": [],
            "cfaIds": [],
            "statusFilter": "",
            "collectionIds": [],
            "customerId": customer_data[1],
        }
        )
        # return res.json
        responsejson=res.json

        list = []
        for i in responsejson["products"]:
            for j in i["productVariants"]:
                list.append({"productId": j["productVariantId"], "minquty": j["minOrderQty"]})

        return (list)


    def get_addtocard(self,customer_data,workspacedata,get_placeorderdetails):
        res=self.send_request(
            Base.RequestMethod.POST,
            custom_url="https://api-uat.beta.pharmconnect.com/commerce-v2/orders/additemtoactiveorder/8ef5d569-3419-44e5-bb33-3ecfd260f796",
            payload={
                "customerId": customer_data[1],
                "sellerWorkspaceId": "8ef5d569-3419-44e5-bb33-3ecfd260f796",
                "source": "manual",
                "lines": [
                    {
                        "productVariantId": i["productId"],
                        "quantity": i["minquty"],
                        "operator": "add"
                    } for i in get_placeorderdetails
                ]
            }
        )
        # return res.json
        responsejson=res.json
        data_list = []
        for i in responsejson["orders"]:
            data_list.append({"pofileId": i["pofileId"], "id": i["id"]})
            for k in i["orderLine"]:
                data_list.append({"ids": k["id"], "productVariantId": k["productVariantId"], "quantity": k["quantity"]})

        return data_list

    def get_checkout(self, customer_data, workspacedata,get_addtocard ):
        res = self.send_request(
            Base.RequestMethod.POST,
            custom_url="https://api-uat.beta.pharmconnect.com/commerce-v2/orders/checkout/8ef5d569-3419-44e5-bb33-3ecfd260f796",
            payload={
                    "sellerWorkspaceId": "8ef5d569-3419-44e5-bb33-3ecfd260f796",
                    "customerId":  customer_data[1],
                    "poFileIds": [
                        get_addtocard[0]["pofileId"],
                    ]
                }
        )
        return res.json



