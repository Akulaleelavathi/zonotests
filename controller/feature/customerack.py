import json

import pytest

from controller.api_util.base_request import Base, BaseAssertion
from controller.api_util.common_imports import *

class Customerack(Base):
    def _init_(self,settings):
        Base._init_(self,settings)
        self.settings=settings


    def waitingforack(self,workspaces_data):
        res=self.send_request(
            Base.RequestMethod.POST,
            custom_url="https://api-uat.beta.pharmconnect.com/commerce-v2/orders?workspaceId=8ef5d569-3419-44e5-bb33-3ecfd260f796",
            payload={
            "workspaceId": "8ef5d569-3419-44e5-bb33-3ecfd260f796",
            "customerId": "",
            "pageNo": 1,
            "pageSize": 20,
            "sortBy": "orderPlacedAt",
            "sortDirection": "DESC",
            "includeSummary": True,
            "includeInvoice": True,
            "includeCustomer": True,
            "includeStatus": True,
            "includeCFA": True,
            "includeDivision": True,
            "searchKeyword": "",
            "startDate": "2024-01-09",
            "endDate": "2024-01-16",
            "filterModel": {
                "cfaIds": [],
                "status": [
                    "SubmittedByCustomer"
                ],
                "customerIds": []
            },
            "skip": 1
        }
)

        responsejson=res.json
        data_list = []
        # return responsejson
        for i in responsejson["order"]:
            if i["status"] == "SubmittedByCustomer":
                data_list.append({"orderId": i["id"], "customerId": i["customerId"]})

                # print(data_list)
        return data_list


    def singlecustomer(self,workspaces_data,waitingforack):
        submitted_orders_info=waitingforack
        customer_id = submitted_orders_info[0]["customerId"]
        order_id= submitted_orders_info[0]["orderId"]
        # return customer_id
        res=self.send_request(
            Base.RequestMethod.POST,
            custom_url=f"https://api-uat.beta.pharmconnect.com/commerce-v2/orders/details/8ef5d569-3419-44e5-bb33-3ecfd260f796/{order_id}?includeInvoice=true",
            payload={
                "filter": {
                    "divisionIds": []
                },
                "searchKey": "",
                "includeInvoice": True,
                "includeTax": True,
                "includeCustomer": True,
                "includePromotions": True,
                "sortDirection": "DESC",
                "sortBy": "pts",
                "customerId":customer_id
})
        responsejson=res.json
        # return responsejson
        for key in responsejson:
            if key == "id":
                return (responsejson[key])







    def checkout(self,workspaces_data,singlecustomer):
       res=self.send_request(
           Base.RequestMethod.POST,
           custom_url="https://api-uat.beta.pharmconnect.com/commerce-v2/orders/8ef5d569-3419-44e5-bb33-3ecfd260f796",
           payload= [
               {
                "orderId":singlecustomer,
                "status": "Approved"
       }
           ])
       responsejson=res.json
       return responsejson






