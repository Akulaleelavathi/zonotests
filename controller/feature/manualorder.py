
from controller.api_util.base_request import Base, BaseAssertion
from controller.api_util.common_imports import *

class CustomerIds(Base):
    def _init_(self,settings):
        Base._init_(self,settings)
        self.settings=settings

    def get_customerid(self,workspaces_data):
        res=self.send_request(
            Base.RequestMethod.GET,
            custom_url=f"{self.settings.url_prefix}/customers/{workspaces_data}?includeCustomerGroupAssignments=1&includeWorkspaceMembers=1&pageNo=1&pageSize=20&includeOrderCount=1",
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
            custom_url=f"{self.settings.url_prefix}/commerce-v2/products/search/customer/{workspacedata}?pageNo=1&pageSize=20&customerId={customer_data[1]}",
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
        return res





    def get_addtocard(self,customer_data,workspacedata,get_placeorderdetails):

        res=self.send_request(
            Base.RequestMethod.POST,
            custom_url=f"{self.settings.url_prefix}/commerce-v2/orders/additemtoactiveorder/{workspacedata}",
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
        return res
        # responsejson=res.json

        # data_list = []
        #
        # for i in responsejson["orders"]:
        #     data_list.append({"pofileId": i["pofileId"], "id": i["id"]})
        #     for k in i["orderLine"]:
        #         data_list.append({"ids": k["id"], "productVariantId": k["productVariantId"], "quantity": k["quantity"]})
        #
        # return data_list
    def get_afterinc(self, workspaces_data,customer_data,test_getaddtocard):
        original_quantity = test_getaddtocard[1]["quantity"]

        doubled_quantity = original_quantity + 1
        res = self.send_request(
            Base.RequestMethod.POST,
            custom_url=f"{self.settings.url_prefix}/commerce-v2/orders/additemtoactiveorder/{workspaces_data}",
            payload={
                "customerId": customer_data[1],
                "sellerWorkspaceId": "8ef5d569-3419-44e5-bb33-3ecfd260f796",
                "poFileId": test_getaddtocard[0]["pofileId"],
                "source": "manual",
                "lines": [
                    {
                        "productVariantId": test_getaddtocard[1]["productVariantId"],
                        "quantity": doubled_quantity,
                        "operator": "add",
                        "poFileLineId": test_getaddtocard[1]["ids"]
                    }
                ]
            })
        return res


    def get_delete(self, workspaces_data,customer_data,test_getaddtocard):
        res = self.send_request(
            Base.RequestMethod.POST,
            custom_url=f"{self.settings.url_prefix}/commerce-v2/orders/deleteLines/{workspaces_data}",
            payload={
                    "sellerWorkspaceId": "8ef5d569-3419-44e5-bb33-3ecfd260f796",
                    "customerId": customer_data[1],
                    "importSource": "manual",
                    "poFileId":test_getaddtocard[0]["pofileId"],
                    "lines": [
                        {
                            "orderId": test_getaddtocard[0]["id"],
                            "orderLineId": test_getaddtocard[1]["ids"]
                        }
                    ]
                })
        print(res)


#     def getdec(self, workspaces_data,customer_data,test_getaddtocard):
#         res = self.send_request(
#             Base.RequestMethod.POST,
#             custom_url="https://api-uat.beta.pharmconnect.com/commerce-v2/orders/additemtoactiveorder/8ef5d569-3419-44e5-bb33-3ecfd260f796",
#             payload={
#             "customerId":customer_data[1],
#             "sellerWorkspaceId": "8ef5d569-3419-44e5-bb33-3ecfd260f796",
#             "poFileId": test_getaddtocard[0]["pofileId"],
#             "source": "manual",
#             "lines": [
#                 {
#                     "productVariantId": test_getaddtocard[1]["productVariantId"],
#                     "quantity": 9,
#                     "operator": "minus",
#                     "poFileLineId":test_getaddtocard[1]["ids"]
#                 }
#             ]
# })

    def getdec(self, workspaces_data, customer_data, test_getaddtocard):
        min_quantity = test_getaddtocard[1]["quantity"]

        initial_quantity = test_getaddtocard[1]["quantity"]

        if initial_quantity <= min_quantity:
            return "Error: Quantity is already less than or equal to the minimum quantity."

        new_quantity = initial_quantity - min_quantity

        payload = {
            "customerId": customer_data[1],
            "sellerWorkspaceId": "8ef5d569-3419-44e5-bb33-3ecfd260f796",
            "poFileId": test_getaddtocard[0]["pofileId"],
            "source": "manual",
            "lines": [
                {
                    "productVariantId": test_getaddtocard[1]["productVariantId"],
                    "quantity": new_quantity,
                    "operator": "minus",
                    "poFileLineId": test_getaddtocard[1]["ids"]
                }
            ]
        }

        res = self.send_request(
            Base.RequestMethod.POST,
            custom_url=f"{self.settings.url_prefix}/commerce-v2/orders/additemtoactiveorder/{workspaces_data}",
            payload=payload
        )

        return res

    def get_checkout(self, customer_data, workspacedata,get_addtocard ):
        res = self.send_request(
            Base.RequestMethod.POST,
            custom_url=f"{self.settings.url_prefix}/commerce-v2/orders/checkout/{workspacedata}",
            payload={
                    "sellerWorkspaceId": "8ef5d569-3419-44e5-bb33-3ecfd260f796",
                    "customerId":  customer_data[1],
                    "poFileIds": [
                        get_addtocard[0]["pofileId"],
                    ]
                }
        )
        return res



