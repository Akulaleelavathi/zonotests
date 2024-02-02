import json

from controller.api_util.base_request import Base, BaseAssertion
from controller.file_operation import *


class Orders(Base):
    def _init_(self,settings):
        Base._init_(self,settings)
        self.settings=settings


    def ordersdata(self,workspaces_data):
        res=self.send_request(
            Base.RequestMethod.POST,
            custom_url="https://api-uat.beta.pharmconnect.com/commerce-v2/orders?workspaceId=8ef5d569-3419-44e5-bb33-3ecfd260f796",
            payload={
            "workspaceId": "8ef5d569-3419-44e5-bb33-3ecfd260f796",
            "customerId": "",
            "pageNo": 1,
            "pageSize": 197,
            "sortBy": "orderPlacedAt",
            "sortDirection": "DESC",
            "includeSummary": True,
            "includeInvoice": True,
            "includeCustomer": True,
            "includeStatus": True,
            "includeCFA": True,
            "includeDivision": True,
            "searchKeyword": "",
            "startDate": "2024-01-24",
            "endDate": "2024-01-31",
            "filterModel": {
                "headDivisionIds": [],
                "divisionIds": [],
                "cfaIds": [],
                "status": [],
                "customerIds": []
            },
            "skip": 1
        })
        return res


    def importsourceuploadfilter(self,return_orders,workspacedata):
        response_json=return_orders.ordersdata2.json
        lst=[]
        for i in response_json["order"]:
            if i["poFile"]["importSource"] == "upload":
                lst.append(i)



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
                "includeCustomer":True,
                "includeStatus": True,
                "includeCFA": True,
                "includeDivision": True,
                "searchKeyword": "",
                "startDate": "2024-01-25",
                "endDate": "2024-02-01",
                "filterModel": {
                    "headDivisionIds": [],
                    "cfaIds": [],
                    "status": [],
                    "customerIds": [],
                    "importSource": "upload"
                },
                "skip": 1
            }
        )
        return lst,res


    def importsourcemanualfilter(self,return_orders,workspacedata):
        response_json=return_orders.ordersdata2.json
        lst=[]
        for i in response_json["order"]:
            if i["poFile"]["importSource"] == "manual":
                lst.append(i)



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
                "includeCustomer":True,
                "includeStatus": True,
                "includeCFA": True,
                "includeDivision": True,
                "searchKeyword": "",
                "startDate": "2024-01-25",
                "endDate": "2024-02-01",
                "filterModel": {
                    "headDivisionIds": [],
                    "cfaIds": [],
                    "status": [],
                    "customerIds": [],
                    "importSource": "manual"
                },
                "skip": 1
            }
        )
        return lst,res






    def customerfilter(self,return_orders,workspacedata):
        response_json=return_orders.ordersdata2.json
        lst=[]
        for i in response_json["order"]:
            if i["customerId"] not in lst:
                lst.append(i["customerId"])


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
                "startDate": "2024-01-25",
                "endDate": "2024-02-01",
                "filterModel": {

                    "customerIds": [
                        lst[0]
                    ]
                },
                "skip": 1
            }

         )
        return res,lst



    def manualcustomerfilter(self,return_orders,workspacedata):
        response_json=return_orders.ordersdata2.json
        lst='2e5e59bf-2a77-4e6b-8e4e-10ea25d72e8d'



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
                "startDate": "2024-01-25",
                "endDate": "2024-02-01",
                "filterModel": {
                    "headDivisionIds": [],
                    "cfaIds": [],
                    "status": [],
                    "customerIds": [
                        lst
                    ]
                },
                "skip": 1
            }


         )
        return res,lst

    def orderstatusfilterconfirmed(self, return_orders, workspacedata):
        response_json = return_orders.ordersdata2.json
        lst = []
        for i in response_json["order"]:
            if(i["status"]=="Confirmed"):
                lst.append(i)


        res = self.send_request(
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
                    "startDate": "2024-01-25",
                    "endDate": "2024-02-01",
                    "filterModel": {
                        "headDivisionIds": [],
                        "cfaIds": [],
                        "status": [
                            "Confirmed"
                        ],
                        "customerIds": []
                    },
                    "skip": 1
                }
            )
        return res, lst


    def orderstatusWaitingForCNFfilter(self, return_orders, workspacedata):
        response_json = return_orders.ordersdata2.json
        lst = []
        for i in response_json["order"]:
            if (i["status"] == "WaitingForCNF"):
                lst.append(i)


        res = self.send_request(
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
            "startDate": "2024-01-25",
            "endDate": "2024-02-01",
            "filterModel": {
                "headDivisionIds": [],
                "cfaIds": [],
                "status": [
                    "WaitingForCNF"
                ],
                "customerIds": []
            },
            "skip": 1
        }

        )
        return res, lst

    def orderstatusSubmitted(self, return_orders, workspacedata):
        response_json = return_orders.ordersdata2.json
        lst = []
        for i in response_json["order"]:
            if (i["status"] == "SubmittedByCustomer"):
                lst.append(i)


        res = self.send_request(
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
                "startDate": "2024-01-25",
                "endDate": "2024-02-01",
                "filterModel": {
                    "headDivisionIds": [],
                    "cfaIds": [],
                    "status": [
                        "SubmittedByCustomer"
                    ],
                    "customerIds": []
                },
                "skip": 1
            }

        )
        return res, lst



    def orderstatusBilled(self, return_orders, workspacedata):
        response_json = return_orders.ordersdata2.json
        lst = []
        for i in response_json["order"]:
            if (i["status"] == "Billed"):
                lst.append(i)


        res = self.send_request(
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
                "startDate": "2024-01-25",
                "endDate": "2024-02-01",
                "filterModel": {
                    "headDivisionIds": [],
                    "cfaIds": [],
                    "status": [
                        "Billed"
                    ],
                    "customerIds": []
                },
                "skip": 1
            }

        )
        return res, lst

    def searchbyordernumber(self,return_orders, workspacedata):
        response_json = return_orders.ordersdata2.json
        lst=[]
        for i in response_json["order"]:
            lst.append(i["orderMetaData"]["refOrderNumber"])

        res = self.send_request(
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
                    "searchKeyword": lst[0],
                    "startDate": "2024-01-25",
                    "endDate": "2024-02-01",
                    "filterModel": {
                        "headDivisionIds": [],
                        "divisionIds": [],
                        "cfaIds": [],
                        "status": [],
                        "customerIds": []
                    },
                    "skip": 1
                })



        return(lst,res)

    def searchbyconumber(self, return_orders, workspacedata):
        response_json = return_orders.ordersdata2.json
        lst = []

        for i in response_json["order"]:
            if i["erpOrderNumber"] not in lst:
                lst.append(i["erpOrderNumber"])

        res = self.send_request(
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
                    "searchKeyword": lst[1],
                    "startDate": "2024-01-25",
                    "endDate": "2024-02-01",
                    "filterModel": {
                        "headDivisionIds": [],
                        "divisionIds": [],
                        "cfaIds": [],
                        "status": [],
                        "customerIds": []
                    },
                    "skip": 1
                })


        return res,lst

    def searchbyparticalco_or_po_or_code(self, return_orders, workspacedata):
        lst = "3080875"
        res = self.send_request(
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
                    "searchKeyword": lst,
                    "startDate": "2024-01-25",
                    "endDate": "2024-02-01",
                    "filterModel": {
                        "headDivisionIds": [],
                        "divisionIds": [],
                        "cfaIds": [],
                        "status": [],
                        "customerIds": []
                    },
                    "skip": 1
                })

        return res,lst






                                                    # single order in all #



    def singleorderinall(self,return_orders, workspacedata):
        response_json = return_orders.ordersdata2.json
        lst = []
        for i in response_json["order"]:
            if i["customerId"] not in lst:
                lst.append((i["id"], i["customerId"],i["skucount"]))

        res = self.send_request(
            Base.RequestMethod.POST,
            custom_url=f"https://api-uat.beta.pharmconnect.com/commerce-v2/orders/details/8ef5d569-3419-44e5-bb33-3ecfd260f796/{lst[0][0]}?includeInvoice=true",
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
                "customerId": lst[0][1]
            })

        return res,lst


    def particalsearchbysku_or_producttitle(self, return_orders, workspacedata):
        response_json= return_orders.ordersdata3
        res=response_json[0]
        lst = []
        lst.append(res.json["customerId"])


        number = "0000000000011"
        res = self.send_request(
            Base.RequestMethod.POST,
            custom_url=f"https://api-uat.beta.pharmconnect.com/commerce-v2/products/search/customer/8ef5d569-3419-44e5-bb33-3ecfd260f796?pageSize=20&customerId={lst[0]}",
            payload={

                "includeFacets": True,
                "includeDivisions": True,
                "includeCfas": True,
                "includeCollections": True,
                "searchKey": number,
                "customerId": lst[0]
            })

        return res,number

    def searchbysku(self, return_orders, workspacedata):
        response_json = return_orders.ordersdata3
        res = response_json[0]
        lst = []
        i=res.json
        lst.append((i["customerId"],i["lines"][0]["productVariant"]["sku"]))

        number = lst[0][1]
        res = self.send_request(
            Base.RequestMethod.POST,
            custom_url=f"https://api-uat.beta.pharmconnect.com/commerce-v2/products/search/customer/8ef5d569-3419-44e5-bb33-3ecfd260f796?pageSize=20&customerId={lst[0][0]}",
            payload={

                "includeFacets": True,
                "includeDivisions": True,
                "includeCfas": True,
                "includeCollections": True,
                "searchKey": number,
                "customerId": lst[0][0]
            })

        return res, number

    def searchbyname(self, return_orders, workspacedata):
        response_json = return_orders.ordersdata3
        res = response_json[0]
        lst = []
        i = res.json
        lst.append((i["customerId"], i["distributorName"][0]))

        number = lst[0][1]
        res = self.send_request(
            Base.RequestMethod.POST,
            custom_url=f"https://api-uat.beta.pharmconnect.com/commerce-v2/products/search/customer/8ef5d569-3419-44e5-bb33-3ecfd260f796?pageSize=20&customerId={lst[0][0]}",
            payload={

                "includeFacets": True,
                "includeDivisions": True,
                "includeCfas": True,
                "includeCollections": True,
                "searchKey": number,
                "customerId": lst[0][0]
            })

        return res, number


    def divisionfilter(self, return_orders, workspacedata):
        response_json = return_orders.ordersdata3
        res = response_json[0]
        lst = []
        i = res.json
        lst.append((i["id"],i["customerId"], i["divisions"][0]["divisionId"]))

        res = self.send_request(
            Base.RequestMethod.POST,
            custom_url=f"https://api-uat.beta.pharmconnect.com/commerce-v2/orders/details/8ef5d569-3419-44e5-bb33-3ecfd260f796/{lst[0][0]}?includeInvoice=true",

            payload={
                    "filter": {
                        "divisionIds": [
                            lst[0][2]

                        ]
                    },
                    "searchKey": "",
                    "includeInvoice": True,
                    "includeTax": True,
                    "includeCustomer": True,
                    "includePromotions": True,
                    "sortDirection": "DESC",
                    "sortBy": "",
                    "customerId": lst[0][1]
                })
        return res,lst

    def modifiedquantitytrue(self, return_orders, workspacedata):
        response_json = return_orders.ordersdata3
        res = response_json[0]

        lst = []
        i = res.json
        lst.append((i["id"], i["customerId"], i["divisions"][0]["divisionId"]))

        res = self.send_request(
            Base.RequestMethod.POST,
            custom_url=f"https://api-uat.beta.pharmconnect.com/commerce-v2/orders/details/8ef5d569-3419-44e5-bb33-3ecfd260f796/{lst[0][0]}?includeInvoice=true",
            payload={
                "filter": {
                    "divisionIds": [],
                    "modifiedQty": "Applied"
                },
                "searchKey": "",
                "includeInvoice": True,
                "includeTax": True,
                "includeCustomer": True,
                "includePromotions": True,
                "sortDirection": "DESC",
                "sortBy": "",
                "customerId": lst[0][1]
            })
        return res,lst


    def modifiedquantityfalse(self, return_orders, workspacedata):
        response_json = return_orders.ordersdata3
        res = response_json[0]

        lst = []
        i = res.json
        lst.append((i["id"], i["customerId"], i["divisions"][0]["divisionId"]))

        res = self.send_request(
            Base.RequestMethod.POST,
            custom_url=f"https://api-uat.beta.pharmconnect.com/commerce-v2/orders/details/8ef5d569-3419-44e5-bb33-3ecfd260f796/{lst[0][0]}?includeInvoice=true",
            payload={
                "filter": {
                    "divisionIds": [],
                    "modifiedQty": "NotApplied"
                },
                "searchKey": "",
                "includeInvoice": True,
                "includeTax": True,
                "includeCustomer": True,
                "includePromotions": True,
                "sortDirection": "DESC",
                "sortBy": "",
                "customerId": lst[0][1]
            })
        return res,lst


    def invoicedfilter(self, return_orders, workspacedata):
        response_json = return_orders.ordersdata3
        res = response_json[0]

        lst = []
        i = res.json
        lst.append((i["id"], i["customerId"], i["divisions"][0]["divisionId"]))

        res = self.send_request(
            Base.RequestMethod.POST,
            custom_url=f"https://api-uat.beta.pharmconnect.com/commerce-v2/orders/details/8ef5d569-3419-44e5-bb33-3ecfd260f796/{lst[0][0]}?includeInvoice=true",
            payload={
                "filter": {
                    "invoice": "invoiced",
                    "divisionIds": []
                },
                "searchKey": "",
                "includeInvoice": True,
                "includeTax": True,
                "includeCustomer": True,
                "includePromotions": True,
                "sortDirection": "DESC",
                "sortBy": "",
                "customerId": lst[0][1]
            })
        return res,lst


    def Notinvoicedfilter(self, return_orders, workspacedata):
        response_json = return_orders.ordersdata3
        res = response_json[0]

        lst = []
        i = res.json
        lst.append((i["id"], i["customerId"], i["divisions"][0]["divisionId"]))

        res = self.send_request(
            Base.RequestMethod.POST,
            custom_url=f"https://api-uat.beta.pharmconnect.com/commerce-v2/orders/details/8ef5d569-3419-44e5-bb33-3ecfd260f796/{lst[0][0]}?includeInvoice=true",
            payload={
                "filter": {
                    "invoice": "Notinvoiced",
                    "divisionIds": []
                },
                "searchKey": "",
                "includeInvoice": True,
                "includeTax": True,
                "includeCustomer": True,
                "includePromotions": True,
                "sortDirection": "DESC",
                "sortBy": "",
                "customerId": lst[0][1]
            })
        return res,

    def schemsappiledfilter(self, return_orders, workspacedata):
        response_json = return_orders.ordersdata3
        res = response_json[0]

        lst = []
        i = res.json
        lst.append((i["id"], i["customerId"], i["divisions"][0]["divisionId"]))

        res = self.send_request(
            Base.RequestMethod.POST,
            custom_url=f"https://api-uat.beta.pharmconnect.com/commerce-v2/orders/details/8ef5d569-3419-44e5-bb33-3ecfd260f796/{lst[0][0]}?includeInvoice=true",
            payload={
                "filter": {
                    "scheme": "Applied",
                    "divisionIds": []
                },
                "searchKey": "",
                "includeInvoice": True,
                "includeTax": True,
                "includeCustomer": True,
                "includePromotions": True,
                "sortDirection": "DESC",
                "sortBy": "",
                "customerId": lst[0][1]
            })
        return res, lst



    def schemsnotappiledfilter(self, return_orders, workspacedata):
        response_json = return_orders.ordersdata3
        res = response_json[0]

        lst = []
        i = res.json
        lst.append((i["id"], i["customerId"], i["divisions"][0]["divisionId"]))

        res = self.send_request(
            Base.RequestMethod.POST,
            custom_url=f"https://api-uat.beta.pharmconnect.com/commerce-v2/orders/details/8ef5d569-3419-44e5-bb33-3ecfd260f796/{lst[0][0]}?includeInvoice=true",
            payload={
                "filter": {
                    "scheme": "NotApplied",
                    "divisionIds": []
                },
                "searchKey": "",
                "includeInvoice": True,
                "includeTax": True,
                "includeCustomer": True,
                "includePromotions": True,
                "sortDirection": "DESC",
                "sortBy": "",
                "customerId": lst[0][1]
            })
        return res, lst



                                           # waiting for cfa#

    def waitingforcfadatadetails(self,workspaces_data):
        res = self.send_request(
            Base.RequestMethod.POST,
            custom_url="https://api-uat.beta.pharmconnect.com/commerce-v2/orders?workspaceId=8ef5d569-3419-44e5-bb33-3ecfd260f796",
            payload={
                "workspaceId": "8ef5d569-3419-44e5-bb33-3ecfd260f796",
                "customerId": "",
                "pageNo": 1,
                "pageSize": 105,
                "sortBy": "orderPlacedAt",
                "sortDirection": "DESC",
                "includeSummary": True,
                "includeInvoice": True,
                "includeCustomer": True,
                "includeStatus": True,
                "includeCFA": True,
                "includeDivision": True,
                "searchKeyword": "",
                "startDate": "2024-01-26",
                "endDate": "2024-02-02",
                "filterModel": {
                    "cfaIds": [],
                    "status": [
                        "SubmittedByCustomer"
                    ],
                    "customerIds": []
                },
                "skip": 1
            })
        return res

    def importsourceuploadfilterwfc(self, return_orders, workspacedata):
        response_json = return_orders.ordersdata4.json
        lst = []
        for i in response_json["order"]:
            if i["poFile"]["importSource"] == "upload":
                lst.append(i)

        res = self.send_request(
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
                "startDate": "2024-01-25",
                "endDate": "2024-02-01",
                "filterModel": {
                    "headDivisionIds": [],
                    "cfaIds": [],
                    "status": [],
                    "customerIds": [],
                    "importSource": "upload"
                },
                "skip": 1
            }
        )
        return lst, res


    def importsourcemanualfilterwfc(self,return_orders,workspacedata):
        response_json=return_orders.ordersdata4.json
        lst=[]
        for i in response_json["order"]:
            if i["poFile"]["importSource"] == "manual":
                lst.append(i)



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
                "includeCustomer":True,
                "includeStatus": True,
                "includeCFA": True,
                "includeDivision": True,
                "searchKeyword": "",
                "startDate": "2024-01-25",
                "endDate": "2024-02-01",
                "filterModel": {
                    "headDivisionIds": [],
                    "cfaIds": [],
                    "status": [],
                    "customerIds": [],
                    "importSource": "manual"
                },
                "skip": 1
            }
        )
        return lst,res

    def customerfilterwfc(self, return_orders, workspacedata):
        response_json = return_orders.ordersdata4.json
        lst = []
        for i in response_json["order"]:
            if i["customerId"] not in lst:
                lst.append(i["customerId"])

        res = self.send_request(
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
                "startDate": "2024-01-25",
                "endDate": "2024-02-01",
                "filterModel": {

                    "customerIds": [
                        lst[0]
                    ]
                },
                "skip": 1
            }

        )
        return res, lst

    def manualcustomerfilterwfc(self, return_orders, workspacedata):
        response_json = return_orders.ordersdata4.json
        lst = '2e5e59bf-2a77-4e6b-8e4e-10ea25d72e8d'

        res = self.send_request(
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
                "startDate": "2024-01-25",
                "endDate": "2024-02-01",
                "filterModel": {
                    "headDivisionIds": [],
                    "cfaIds": [],
                    "status": [],
                    "customerIds": [
                        lst
                    ]
                },
                "skip": 1
            }

        )
        return res, lst


    # def orderstatusWaitingForCNFfilterwfc(self, return_orders, workspacedata):
    #     response_json = return_orders.ordersdata4.json
    #     lst = []
    #     for i in response_json["order"]:
    #         if (i["status"] == "WaitingForCNF"):
    #             lst.append(i)
    #
    #     res = self.send_request(
    #         Base.RequestMethod.POST,
    #         custom_url="https://api-uat.beta.pharmconnect.com/commerce-v2/orders?workspaceId=8ef5d569-3419-44e5-bb33-3ecfd260f796",
    #         payload={
    #             "workspaceId": "8ef5d569-3419-44e5-bb33-3ecfd260f796",
    #             "customerId": "",
    #             "pageNo": 1,
    #             "pageSize": 20,
    #             "sortBy": "orderPlacedAt",
    #             "sortDirection": "DESC",
    #             "includeSummary": True,
    #             "includeInvoice": True,
    #             "includeCustomer": True,
    #             "includeStatus": True,
    #             "includeCFA": True,
    #             "includeDivision": True,
    #             "searchKeyword": "",
    #             "startDate": "2024-01-25",
    #             "endDate": "2024-02-01",
    #             "filterModel": {
    #                 "headDivisionIds": [],
    #                 "cfaIds": [],
    #                 "status": [
    #                     "WaitingForCNF"
    #                 ],
    #                 "customerIds": []
    #             },
    #             "skip": 1
    #         }
    #
    #     )
    #     return res, lst


    # def orderstatusfilterconfirmedwfc(self, return_orders, workspacedata):
    #     response_json = return_orders.ordersdata4.json
    #     lst = []
    #     for i in response_json["order"]:
    #         if (i["status"] == "Confirmed"):
    #             lst.append(i)
    #
    #     res = self.send_request(
    #         Base.RequestMethod.POST,
    #         custom_url="https://api-uat.beta.pharmconnect.com/commerce-v2/orders?workspaceId=8ef5d569-3419-44e5-bb33-3ecfd260f796",
    #         payload={
    #             "workspaceId": "8ef5d569-3419-44e5-bb33-3ecfd260f796",
    #             "customerId": "",
    #             "pageNo": 1,
    #             "pageSize": 20,
    #             "sortBy": "orderPlacedAt",
    #             "sortDirection": "DESC",
    #             "includeSummary": True,
    #             "includeInvoice": True,
    #             "includeCustomer": True,
    #             "includeStatus": True,
    #             "includeCFA": True,
    #             "includeDivision": True,
    #             "searchKeyword": "",
    #             "startDate": "2024-01-25",
    #             "endDate": "2024-02-01",
    #             "filterModel": {
    #                 "headDivisionIds": [],
    #                 "cfaIds": [],
    #                 "status": [
    #                     "Confirmed"
    #                 ],
    #                 "customerIds": []
    #             },
    #             "skip": 1
    #         }
    #     )
    #     return res, lst


    def orderstatusSubmittedwfc(self, return_orders, workspacedata):
        response_json = return_orders.ordersdata4.json
        lst = []
        for i in response_json["order"]:
            if (i["status"] == "SubmittedByCustomer"):
                lst.append(i)

        res = self.send_request(
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
                "startDate": "2024-01-25",
                "endDate": "2024-02-01",
                "filterModel": {
                    "headDivisionIds": [],
                    "cfaIds": [],
                    "status": [
                        "SubmittedByCustomer"
                    ],
                    "customerIds": []
                },
                "skip": 1
            }

        )
        return res, lst

    # def orderstatusBilledwfc(self, return_orders, workspacedata):
    #     response_json = return_orders.ordersdata4.json
    #     lst = []
    #     for i in response_json["order"]:
    #         if (i["status"] == "Billed"):
    #             lst.append(i)
    #
    #     res = self.send_request(
    #         Base.RequestMethod.POST,
    #         custom_url="https://api-uat.beta.pharmconnect.com/commerce-v2/orders?workspaceId=8ef5d569-3419-44e5-bb33-3ecfd260f796",
    #         payload={
    #             "workspaceId": "8ef5d569-3419-44e5-bb33-3ecfd260f796",
    #             "customerId": "",
    #             "pageNo": 1,
    #             "pageSize": 20,
    #             "sortBy": "orderPlacedAt",
    #             "sortDirection": "DESC",
    #             "includeSummary": True,
    #             "includeInvoice": True,
    #             "includeCustomer": True,
    #             "includeStatus": True,
    #             "includeCFA": True,
    #             "includeDivision": True,
    #             "searchKeyword": "",
    #             "startDate": "2024-01-25",
    #             "endDate": "2024-02-01",
    #             "filterModel": {
    #                 "headDivisionIds": [],
    #                 "cfaIds": [],
    #                 "status": [
    #                     "Billed"
    #                 ],
    #                 "customerIds": []
    #             },
    #             "skip": 1
    #         }
    #
    #     )
    #     return res, lst


    def searchbyordernumberwfc(self,return_orders, workspacedata):
        response_json = return_orders.ordersdata4.json
        lst=[]
        for i in response_json["order"]:
            lst.append(i["orderMetaData"]["refOrderNumber"])

        res = self.send_request(
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
                    "searchKeyword": lst[0],
                    "startDate": "2024-01-25",
                    "endDate": "2024-02-01",
                    "filterModel": {
                        "headDivisionIds": [],
                        "divisionIds": [],
                        "cfaIds": [],
                        "status": [],
                        "customerIds": []
                    },
                    "skip": 1
                })



        return(lst,res)

    def searchbyconumberwfc(self, return_orders, workspacedata):
        response_json = return_orders.ordersdata4.json
        lst = []

        for i in response_json["order"]:
            if i["erpOrderNumber"] not in lst:
                lst.append(i["erpOrderNumber"])

        res = self.send_request(
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
                    "searchKeyword": lst[0],
                    "startDate": "2024-01-25",
                    "endDate": "2024-02-01",
                    "filterModel": {
                        "headDivisionIds": [],
                        "divisionIds": [],
                        "cfaIds": [],
                        "status": [],
                        "customerIds": []
                    },
                    "skip": 1
                })


        return res,lst

    def searchbyparticalco_or_po_or_codewfc(self, return_orders, workspacedata):
        lst = "3080875"
        res = self.send_request(
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
                    "searchKeyword": lst,
                    "startDate": "2024-01-25",
                    "endDate": "2024-02-01",
                    "filterModel": {
                        "headDivisionIds": [],
                        "divisionIds": [],
                        "cfaIds": [],
                        "status": [],
                        "customerIds": []
                    },
                    "skip": 1
                })

        return res,lst

                                                 # wfc singleorder#

    def singleorderinwfc(self,return_orders, workspacedata):
        response_json = return_orders.ordersdata4.json
        lst = []
        for i in response_json["order"]:
            if i["customerId"] not in lst:
                lst.append((i["id"], i["customerId"],i["skucount"]))

        res = self.send_request(
            Base.RequestMethod.POST,
            custom_url=f"https://api-uat.beta.pharmconnect.com/commerce-v2/orders/details/8ef5d569-3419-44e5-bb33-3ecfd260f796/{lst[19][0]}?includeInvoice=true",
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
                "customerId": lst[19][1]
            })

        return res,lst

    def particalsearchbysku_or_producttitlewfc(self, return_orders, workspacedata):
        response_json= return_orders.ordersdata5
        res=response_json[0]
        lst = []
        lst.append(res.json["customerId"])


        number = "0000000000011"
        res = self.send_request(
            Base.RequestMethod.POST,
            custom_url=f"https://api-uat.beta.pharmconnect.com/commerce-v2/products/search/customer/8ef5d569-3419-44e5-bb33-3ecfd260f796?pageSize=20&customerId={lst[0]}",
            payload={

                "includeFacets": True,
                "includeDivisions": True,
                "includeCfas": True,
                "includeCollections": True,
                "searchKey": number,
                "customerId": lst[0]
            })

        return res,number

    def searchbyskuwfc(self, return_orders, workspacedata):
        response_json = return_orders.ordersdata5
        res = response_json[0]
        lst = []
        i=res.json
        lst.append((i["customerId"],i["lines"][0]["productVariant"]["sku"]))

        number = lst[0][1]
        res = self.send_request(
            Base.RequestMethod.POST,
            custom_url=f"https://api-uat.beta.pharmconnect.com/commerce-v2/products/search/customer/8ef5d569-3419-44e5-bb33-3ecfd260f796?pageSize=20&customerId={lst[0][0]}",
            payload={

                "includeFacets": True,
                "includeDivisions": True,
                "includeCfas": True,
                "includeCollections": True,
                "searchKey": number,
                "customerId": lst[0][0]
            })

        return res, number

    def searchbynamewfc(self, return_orders, workspacedata):
        response_json = return_orders.ordersdata5
        res = response_json[0]
        lst = []
        i = res.json
        lst.append((i["customerId"], i["distributorName"][0]))

        number = lst[0][1]
        res = self.send_request(
            Base.RequestMethod.POST,
            custom_url=f"https://api-uat.beta.pharmconnect.com/commerce-v2/products/search/customer/8ef5d569-3419-44e5-bb33-3ecfd260f796?pageSize=20&customerId={lst[0][0]}",
            payload={

                "includeFacets": True,
                "includeDivisions": True,
                "includeCfas": True,
                "includeCollections": True,
                "searchKey": number,
                "customerId": lst[0][0]
            })

        return res, number

    def divisionfilterwfc(self, return_orders, workspacedata):
        response_json = return_orders.ordersdata5
        res = response_json[0]
        lst = []
        i = res.json
        lst.append((i["id"], i["customerId"], i["divisions"][0]["divisionId"]))

        res = self.send_request(
            Base.RequestMethod.POST,
            custom_url=f"https://api-uat.beta.pharmconnect.com/commerce-v2/orders/details/8ef5d569-3419-44e5-bb33-3ecfd260f796/{lst[0][0]}?includeInvoice=true",

            payload={
                "filter": {
                    "divisionIds": [
                        lst[0][2]

                    ]
                },
                "searchKey": "",
                "includeInvoice": True,
                "includeTax": True,
                "includeCustomer": True,
                "includePromotions": True,
                "sortDirection": "DESC",
                "sortBy": "",
                "customerId": lst[0][1]
            })
        return res, lst

    def invoicedfilterwfc(self, return_orders, workspacedata):
        response_json = return_orders.ordersdata5
        res = response_json[0]

        lst = []
        i = res.json
        lst.append((i["id"], i["customerId"], i["divisions"][0]["divisionId"]))

        res = self.send_request(
            Base.RequestMethod.POST,
            custom_url=f"https://api-uat.beta.pharmconnect.com/commerce-v2/orders/details/8ef5d569-3419-44e5-bb33-3ecfd260f796/{lst[0][0]}?includeInvoice=true",
            payload={
                "filter": {
                    "invoice": "invoiced",
                    "divisionIds": []
                },
                "searchKey": "",
                "includeInvoice": True,
                "includeTax": True,
                "includeCustomer": True,
                "includePromotions": True,
                "sortDirection": "DESC",
                "sortBy": "",
                "customerId": lst[0][1]
            })
        return res, lst

    def Notinvoicedfilterwfc(self, return_orders, workspacedata):
        response_json = return_orders.ordersdata5
        res = response_json[0]

        lst = []
        i = res.json
        lst.append((i["id"], i["customerId"], i["divisions"][0]["divisionId"]))

        res = self.send_request(
            Base.RequestMethod.POST,
            custom_url=f"https://api-uat.beta.pharmconnect.com/commerce-v2/orders/details/8ef5d569-3419-44e5-bb33-3ecfd260f796/{lst[0][0]}?includeInvoice=true",
            payload={
                "filter": {
                    "invoice": "Notinvoiced",
                    "divisionIds": []
                },
                "searchKey": "",
                "includeInvoice": True,
                "includeTax": True,
                "includeCustomer": True,
                "includePromotions": True,
                "sortDirection": "DESC",
                "sortBy": "",
                "customerId": lst[0][1]
            })
        return res,

    def schemsappiledfilterwfc(self, return_orders, workspacedata):
        response_json = return_orders.ordersdata5
        res = response_json[0]

        lst = []
        i = res.json
        lst.append((i["id"], i["customerId"], i["divisions"][0]["divisionId"]))

        res = self.send_request(
            Base.RequestMethod.POST,
            custom_url=f"https://api-uat.beta.pharmconnect.com/commerce-v2/orders/details/8ef5d569-3419-44e5-bb33-3ecfd260f796/{lst[0][0]}?includeInvoice=true",
            payload={
                "filter": {
                    "scheme": "Applied",
                    "divisionIds": []
                },
                "searchKey": "",
                "includeInvoice": True,
                "includeTax": True,
                "includeCustomer": True,
                "includePromotions": True,
                "sortDirection": "DESC",
                "sortBy": "",
                "customerId": lst[0][1]
            })
        return res, lst

    def schemsnotappiledfilterwfc(self, return_orders, workspacedata):
        response_json = return_orders.ordersdata5
        res = response_json[0]

        lst = []
        i = res.json
        lst.append((i["id"], i["customerId"], i["divisions"][0]["divisionId"]))

        res = self.send_request(
            Base.RequestMethod.POST,
            custom_url=f"https://api-uat.beta.pharmconnect.com/commerce-v2/orders/details/8ef5d569-3419-44e5-bb33-3ecfd260f796/{lst[0][0]}?includeInvoice=true",
            payload={
                "filter": {
                    "scheme": "NotApplied",
                    "divisionIds": []
                },
                "searchKey": "",
                "includeInvoice": True,
                "includeTax": True,
                "includeCustomer": True,
                "includePromotions": True,
                "sortDirection": "DESC",
                "sortBy": "",
                "customerId": lst[0][1]
            })
        return res, lst



