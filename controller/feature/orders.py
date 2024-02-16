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
            custom_url=f"{self.settings.url_prefix}/commerce-v2/orders?workspaceId={workspaces_data}",
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
            custom_url=f"{self.settings.url_prefix}/commerce-v2/orders?workspaceId={workspacedata}",

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
            custom_url=f"{self.settings.url_prefix}/commerce-v2/orders?workspaceId={workspacedata}",

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
            custom_url=f"{self.settings.url_prefix}/commerce-v2/orders?workspaceId={workspacedata}",

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
            custom_url=f"{self.settings.url_prefix}/commerce-v2/orders?workspaceId={workspacedata}",
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
            custom_url=f"{self.settings.url_prefix}/commerce-v2/orders?workspaceId={workspacedata}",
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
            custom_url=f"{self.settings.url_prefix}/commerce-v2/orders?workspaceId={workspacedata}",
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
            custom_url=f"{self.settings.url_prefix}/commerce-v2/orders?workspaceId={workspacedata}",
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
            custom_url=f"{self.settings.url_prefix}/commerce-v2/orders?workspaceId={workspacedata}",
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
            custom_url=f"{self.settings.url_prefix}/commerce-v2/orders?workspaceId={workspacedata}",
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
            custom_url=f"{self.settings.url_prefix}/commerce-v2/orders?workspaceId={workspacedata}",
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
            custom_url=f"{self.settings.url_prefix}/commerce-v2/orders?workspaceId={workspacedata}",
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
            custom_url=f"{self.settings.url_prefix}/commerce-v2/orders/details/{workspacedata}/{lst[0][0]}?includeInvoice=true",
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
            custom_url=f"{self.settings.url_prefix}/commerce-v2/products/search/customer/{workspacedata}?pageSize=20&customerId={lst[0]}",
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
            custom_url=f"{self.settings.url_prefix}/commerce-v2/products/search/customer/{workspacedata}?pageSize=20&customerId={lst[0][0]}",
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
            custom_url=f"{self.settings.url_prefix}/commerce-v2/products/search/customer/{workspacedata}pageSize=20&customerId={lst[0][0]}",
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
            custom_url=f"{self.settings.url_prefix}/commerce-v2/orders/details/{workspacedata}/{lst[0][0]}?includeInvoice=true",

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
            custom_url=f"{self.settings.url_prefix}/commerce-v2/orders/details/{workspacedata}/{lst[0][0]}?includeInvoice=true",
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
            custom_url=f"{self.settings.url_prefix}/commerce-v2/orders/details/{workspacedata}/{lst[0][0]}?includeInvoice=true",
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
            custom_url=f"{self.settings.url_prefix}/commerce-v2/orders/details/{workspacedata}/{lst[0][0]}?includeInvoice=true",
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

    def manual_invoicedfilter(self, return_orders, workspacedata):
      customer_id="991a4e99-bd76-4d24-9f04-8a0c2e74a26c"
      id=38869

      res = self.send_request(
          Base.RequestMethod.POST,
          custom_url=f"{self.settings.url_prefix}/commerce-v2/orders/details/{workspacedata}/{id}?includeInvoice=true",
          payload={
              "filter": {
                  "invoice": "notInvoiced",
                  "divisionIds": []
              },
              "searchKey": "",
              "includeInvoice": True,
              "includeTax": True,
              "includeCustomer": True,
              "includePromotions": True,
              "sortDirection": "DESC",
              "sortBy": "",
              "customerId": customer_id
          })
      return res



    def Notinvoicedfilter(self, return_orders, workspacedata):
        response_json = return_orders.ordersdata3
        res = response_json[0]

        lst = []
        i = res.json
        lst.append((i["id"], i["customerId"], i["divisions"][0]["divisionId"]))

        res = self.send_request(
            Base.RequestMethod.POST,
            custom_url=f"{self.settings.url_prefix}/commerce-v2/orders/details/{workspacedata}/{lst[0][0]}?includeInvoice=true",
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
        return res,lst
    def manual_Notinvoicedfilter(self, return_orders, workspacedata):
      customer_id="991a4e99-bd76-4d24-9f04-8a0c2e74a26c"
      id=38869

      res = self.send_request(
          Base.RequestMethod.POST,
          custom_url=f"{self.settings.url_prefix}/commerce-v2/orders/details/8{workspacedata}/{id}?includeInvoice=true",
          payload={
              "filter": {
                  "invoice": "notInvoiced",
                  "divisionIds": []
              },
              "searchKey": "",
              "includeInvoice": True,
              "includeTax": True,
              "includeCustomer": True,
              "includePromotions": True,
              "sortDirection": "DESC",
              "sortBy": "",
              "customerId": customer_id
          })
      return res



    def schemsappiledfilter(self, return_orders, workspacedata):
        response_json = return_orders.ordersdata3
        res = response_json[0]

        lst = []
        i = res.json
        lst.append((i["id"], i["customerId"], i["divisions"][0]["divisionId"]))

        res = self.send_request(
            Base.RequestMethod.POST,
            custom_url=f"{self.settings.url_prefix}/commerce-v2/orders/details/{workspacedata}/{lst[0][0]}?includeInvoice=true",
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

    def manual_schemsappiledfilter(self, return_orders, workspacedata):
       id=38910
       customer_id="991a4e99-bd76-4d24-9f04-8a0c2e74a26c"

       res = self.send_request(
           Base.RequestMethod.POST,
           custom_url=f"{self.settings.url_prefix}/commerce-v2/orders/details/{workspacedata}/{id}?includeInvoice=true",
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
               "customerId": customer_id
           })
       return res



    def manual_schemsnotappiledfilter(self, return_orders, workspacedata):
       id=38910
       customer_id="991a4e99-bd76-4d24-9f04-8a0c2e74a26c"

       res = self.send_request(
           Base.RequestMethod.POST,
           custom_url=f"{self.settings.url_prefix}/commerce-v2/orders/details/{workspacedata}/{id}?includeInvoice=true",
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
               "customerId": customer_id
           })
       return res





    def schemsnotappiledfilter(self, return_orders, workspacedata):
        response_json = return_orders.ordersdata3
        res = response_json[0]

        lst = []
        i = res.json
        lst.append((i["id"], i["customerId"], i["divisions"][0]["divisionId"]))

        res = self.send_request(
            Base.RequestMethod.POST,
            custom_url=f"{self.settings.url_prefix}/commerce-v2/orders/details/{workspacedata}/{lst[0][0]}?includeInvoice=true",
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
            custom_url=f"{self.settings.url_prefix}/commerce-v2/orders?workspaceId={workspaces_data}",
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
                    "startDate": "2024-01-30",
                    "endDate": "2024-02-06",
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
            custom_url=f"{self.settings.url_prefix}/commerce-v2/orders?workspaceId={workspacedata}",

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
            custom_url=f"{self.settings.url_prefix}/commerce-v2/orders?workspaceId={workspacedata}",

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
            custom_url=f"{self.settings.url_prefix}/commerce-v2/orders?workspaceId={workspacedata}",

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
            custom_url=f"{self.settings.url_prefix}/commerce-v2/orders?workspaceId=8{workspacedata}",
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



    def orderstatusSubmittedwfc(self, return_orders, workspacedata):
        response_json = return_orders.ordersdata4.json
        lst = []
        for i in response_json["order"]:
            if (i["status"] == "SubmittedByCustomer"):
                lst.append(i)

        res = self.send_request(
            Base.RequestMethod.POST,
            custom_url=f"{self.settings.url_prefix}/commerce-v2/orders?workspaceId={workspacedata}",
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


    def searchbyordernumberwfc(self,return_orders, workspacedata):
        response_json = return_orders.ordersdata4.json
        lst=[]
        for i in response_json["order"]:
            lst.append(i["orderMetaData"]["refOrderNumber"])

        res = self.send_request(
            Base.RequestMethod.POST,
            custom_url=f"{self.settings.url_prefix}/commerce-v2/orders?workspaceId={workspacedata}",
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
            custom_url=f"{self.settings.url_prefix}/commerce-v2/orders?workspaceId={workspacedata}",
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
            custom_url=f"{self.settings.url_prefix}/commerce-v2/orders?workspaceId={workspacedata}",
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

    # def singleorderinwfc(self,return_orders, workspacedata):
    #     response_json = return_orders.ordersdata4.json
    #     lst = []
    #     for i in response_json["order"]:
    #         if i["customerId"] not in lst:
    #             lst.append((i["id"], i["customerId"],i["skucount"]))
    #
    #     res = self.send_request(
    #         Base.RequestMethod.POST,
    #         custom_url=f"https://api-uat.beta.pharmconnect.com/commerce-v2/orders/details/8ef5d569-3419-44e5-bb33-3ecfd260f796/{lst[1][0]}?includeInvoice=true",
    #         payload={
    #             "filter": {
    #                 "divisionIds": []
    #             },
    #             "searchKey": "",
    #             "includeInvoice": True,
    #             "includeTax": True,
    #             "includeCustomer": True,
    #             "includePromotions": True,
    #             "sortDirection": "DESC",
    #             "sortBy": "pts",
    #             "customerId":lst[1][1]
    #         })
    #
    #     return res,lst


    def singleorderinwfc(self,return_orders, workspacedata):
        response_json = return_orders.ordersdata4.json
        lst = []
        for i in response_json["order"]:
            if i["customerId"] not in lst:
                lst.append((i["id"], i["customerId"],i["skucount"]))

        res = self.send_request(
            Base.RequestMethod.POST,
            custom_url=f"{self.settings.url_prefix}/commerce-v2/orders/details/{workspacedata}/38922?includeInvoice=true",
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
                "customerId": "991a4e99-bd76-4d24-9f04-8a0c2e74a26c"
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
            custom_url=f"{self.settings.url_prefix}/commerce-v2/products/search/customer/{workspacedata}?pageSize=20&customerId={lst[0]}",
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
            custom_url=f"{self.settings.url_prefix}/commerce-v2/products/search/customer/{workspacedata}?pageSize=20&customerId={lst[0][0]}",
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
            custom_url=f"{self.settings.url_prefix}/commerce-v2/products/search/customer/{workspacedata}?pageSize=20&customerId={lst[0][0]}",
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
            custom_url=f"{self.settings.url_prefix}/commerce-v2/orders/details/{workspacedata}/{lst[0][0]}?includeInvoice=true",

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
            custom_url=f"{self.settings.url_prefix}/commerce-v2/orders/details/{workspacedata}/{lst[0][0]}?includeInvoice=true",
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

    def manualinvoicedfilterwfc(self, return_orders, workspacedata):
        customer_number="991a4e99-bd76-4d24-9f04-8a0c2e74a26c"
        id=38869
        res = self.send_request(
            Base.RequestMethod.POST,
            custom_url=f"{self.settings.url_prefix}/commerce-v2/orders/details/{workspacedata}/{id}?includeInvoice=true",
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
                "customerId":customer_number
            })
        return res

    def Notinvoicedfilterwfc(self, return_orders, workspacedata):
        response_json = return_orders.ordersdata5
        res = response_json[0]

        lst = []
        i = res.json
        lst.append((i["id"], i["customerId"], i["divisions"][0]["divisionId"]))

        res = self.send_request(
            Base.RequestMethod.POST,
            custom_url=f"{self.settings.url_prefix}/commerce-v2/orders/details/{workspacedata}/{lst[0][0]}?includeInvoice=true",
            payload={
                "filter": {
                    "invoice": "notInvoiced",
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

    def manual_Notinvoicedfilterwfc(self, return_orders, workspacedata):
      customer_id="991a4e99-bd76-4d24-9f04-8a0c2e74a26c"
      id=38869

      res = self.send_request(
          Base.RequestMethod.POST,
          custom_url=f"{self.settings.url_prefix}/commerce-v2/orders/details/{workspacedata}/{id}?includeInvoice=true",
          payload={
              "filter": {
                  "invoice": "notInvoiced",
                  "divisionIds": []
              },
              "searchKey": "",
              "includeInvoice": True,
              "includeTax": True,
              "includeCustomer": True,
              "includePromotions": True,
              "sortDirection": "DESC",
              "sortBy": "",
              "customerId": customer_id
          })
      return res

    def schemsappiledfilterwfc(self, return_orders, workspacedata):
        response_json = return_orders.ordersdata5
        res = response_json[0]

        lst = []
        i = res.json
        lst.append((i["id"], i["customerId"], i["divisions"][0]["divisionId"]))

        res = self.send_request(
            Base.RequestMethod.POST,
            custom_url=f"{self.settings.url_prefix}/commerce-v2/orders/details/{workspacedata}/{lst[0][0]}?includeInvoice=true",
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

    def manual_schemsappiledfilterwfc(self, return_orders, workspacedata):
       id=38903
       customer_id="991a4e99-bd76-4d24-9f04-8a0c2e74a26c"

       res = self.send_request(
           Base.RequestMethod.POST,
           custom_url=f"{self.settings.url_prefix}/commerce-v2/orders/details/{workspacedata}/{id}?includeInvoice=true",
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
               "customerId": customer_id
           })
       return res



    def manual_schemsnotappiledfilterwfc(self, return_orders, workspacedata):
       id=38903
       customer_id="991a4e99-bd76-4d24-9f04-8a0c2e74a26c"

       res = self.send_request(
           Base.RequestMethod.POST,
           custom_url=f"{self.settings.url_prefix}/commerce-v2/orders/details/{workspacedata}/{id}?includeInvoice=true",
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
               "customerId": customer_id
           })
       return res



    def schemsnotappiledfilterwfc(self, return_orders, workspacedata):
        response_json = return_orders.ordersdata5
        res = response_json[0]

        lst = []
        i = res.json
        lst.append((i["id"], i["customerId"], i["divisions"][0]["divisionId"]))

        res = self.send_request(
            Base.RequestMethod.POST,
            custom_url=f"{self.settings.url_prefix}/commerce-v2/orders/details/{workspacedata}/{lst[0][0]}?includeInvoice=true",
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



    def editincrement(self,return_orders, workspacedata):
        response_json = return_orders.ordersdata5
        res = response_json[0]
        lst = []
        i = res.json
        order_id = i["id"]
        customer_id = i["customerId"]
        for j in i["lines"]:
            lst.append((j["productVariant"]["id"],j["minOrderQty"]))
        res = self.send_request(
            Base.RequestMethod.POST,
            custom_url=f"{self.settings.url_prefix}/commerce-v2/orders/updatedByCfa/{workspacedata}",
            payload={
                "orderId": order_id,
                "customerId": customer_id,
                "lines": [
                    {
                        "productVariantId": lst[1][0],
                        "quantity": lst[1][1] + 1
                    }
                ]
            })
        return res,lst



    def manual_editincrement(self,return_orders, workspacedata):
        order_id = 38895
        customer_id="3eef6837-80e5-468d-b8f3-8c2cea04506a"
        productVariantId= 32825
        quantity= 10

        res = self.send_request(
            Base.RequestMethod.POST,
            custom_url=f"{self.settings.url_prefix}/commerce-v2/orders/updatedByCfa/{workspacedata}",
            payload={
                "orderId": order_id,
                "customerId": customer_id,
                "lines": [
                    {
                        "productVariantId": productVariantId,
                        "quantity": quantity + 1
                    }
                ]
            })
        return res

    def editdecrement(self, return_orders, workspacedata):
        response_json = return_orders.ordersdata5
        res = response_json[0]
        lst = []
        i = res.json
        order_id = i["id"]
        customer_id = i["customerId"]
        for j in i["lines"]:
            lst.append((j["productVariant"]["id"], j["minOrderQty"], j["quantity"]))
        min_quantity = lst[1][1]
        quantity = lst[1][2]

        if quantity > min_quantity:
            res = self.send_request(
                Base.RequestMethod.POST,
                custom_url=f"{self.settings.url_prefix}/commerce-v2/orders/updatedByCfa/{workspacedata}",
                payload={
                    "orderId": order_id,
                    "customerId": customer_id,
                    "lines": [
                        {
                            "productVariantId": lst[1][0],
                            "quantity": lst[1][1] - 1
                        }
                    ]
                })
            return res, lst
        else:
            print("Error: Quantity is already less than or equal to the minimum quantity")
            res = self.send_request(
                Base.RequestMethod.POST,
                custom_url=f"{self.settings.url_prefix}/commerce-v2/orders/updatedByCfa/{workspacedata}",
                payload={
                    "orderId": order_id,
                    "customerId": customer_id,
                    "lines": [
                        {
                            "productVariantId": lst[1][0],
                            "quantity": lst[1][1]
                        }
                    ]
                })
            return res, lst


    def manual_editdecrement(self,return_orders, workspacedata):
        order_id = 38895
        customer_id="3eef6837-80e5-468d-b8f3-8c2cea04506a"
        productVariantId= 32825
        min_quantity = 10
        quantity=20
        if quantity > min_quantity:
                res = self.send_request(
                    Base.RequestMethod.POST,
                    custom_url=f"https://api-uat.beta.pharmconnect.com/commerce-v2/orders/updatedByCfa/{workspacedata}",
                    payload={
                        "orderId": order_id,
                        "customerId": customer_id,
                        "lines": [
                            {
                                "productVariantId": productVariantId,
                                "quantity": quantity - min_quantity
                            }
                        ]
                    })
                return res
        else:
            print("Error: Quantity is already less than or equal to the minimum quantity")
            res = self.send_request(
                Base.RequestMethod.POST,
                custom_url=f"{self.settings.url_prefix}/commerce-v2/orders/updatedByCfa/{workspacedata}",
                payload={
                    "orderId": order_id,
                    "customerId": customer_id,
                    "lines": [
                        {
                             "productVariantId": productVariantId,
                                "quantity": quantity
                            }]
                })
            return res






    def editadd_product(self,return_orders, workspacedata,product_list):


        response_json = return_orders.ordersdata5
        ress = response_json[0]
        lst = []
        i = ress.json
        order_id = i["id"]
        customer_id = i["customerId"]
        for j in i["lines"]:
            lst.append((j["productVariant"]["id"], j["minOrderQty"], j["quantity"]))
        res = self.send_request(
            Base.RequestMethod.POST,
            custom_url=f"{self.settings.url_prefix}/commerce-v2/orders/updatedByCfa/{workspacedata}",
            payload={
                "orderId": order_id,
                "customerId": customer_id,
                "lines": [
                             {
                                 "productVariantId": k[0],
                                 "quantity": k[2]
                             }
                             for k in lst
                         ] + [
                             {
                                 "productVariantId": product_list[1][0],
                                 "quantity": product_list[1][1]
                             }
                             # for i in product_list
                         ]
            })
        return res,lst

    def editdelete_product(self, return_orders, workspacedata):

        response_json = return_orders.ordersdata5
        ress = response_json[0]
        lst = []
        i = ress.json
        order_id = i["id"]
        customer_id = i["customerId"]
        for j in i["lines"]:
            lst.append((j["productVariant"]["id"], j["minOrderQty"], j["quantity"]))

        payload_list = [
            {
                "productVariantId": k[0],
                "quantity": k[2],
                "count": count
            }
            for count, k in enumerate(lst[:-1], start=1)
        ]
        a=[{"productVariantId": k[0], "quantity": k[2]} for k in lst[:-1]]
        b = [{"productVariantId": lst[len(lst)-1][0], "quantity": 0}]

        main_data = []
        for i in a:
            main_data.append(i)
        for j in b:
            main_data.append(j)
        # print(payload_list)
        print(main_data)
        res = self.send_request(
            Base.RequestMethod.POST,
            custom_url=f"{self.settings.url_prefix}/commerce-v2/orders/updatedByCfa/{workspacedata}",
            payload={
                "orderId": order_id,
                "customerId": customer_id,
                "lines":main_data

            }
        )

        return res, lst




