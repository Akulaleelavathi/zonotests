from controller.api_util.base_request import Base, BaseAssertion
from controller.file_operation import *

class Customersdatas(Base):
    def _init_(self,settings):
        Base._init_(self,settings)
        self.settings=settings

    def customersdata1(self, workspaces_data):
        res = self.send_request(
            Base.RequestMethod.GET,
            custom_url=f"{self.settings.url_prefix}/customers/{workspaces_data}?includeCustomerGroupAssignments=1&includeWorkspaceMembers=1&pageNo=1&pageSize=198&includeOrderCount=1",

        )
        return res


    def customerdatafororders(self,return_customerdata,workspaces_data,return_orders):
        response_json = return_orders.ordersdata5
        # print(f"return the response_json single customer{response_json}")
        res = response_json[0].json
        customer_id_res=res["customerId"]


        res = self.send_request(
            Base.RequestMethod.POST,
            custom_url=f"https://api-uat.beta.pharmconnect.com/commerce-v2/products/search/customer/{workspaces_data}?pageNo=1&pageSize=20&customerId={customer_id_res}",
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
            "customerId":customer_id_res
        })
        return res
















































    def customercodefilter(self,return_customerdata,workspaces_data):
        response_json=return_customerdata.customersdata2.json
        # print(f"return the response_customer{response_json}")
        lst=[]
        for i in response_json["customers"]:
            lst.append(i["distributorCode"])


        res=self.send_request(
            Base.RequestMethod.GET,
            custom_url=f"{self.settings.url_prefix}/customers/{workspaces_data}?includeCustomerGroupAssignments=1&includeWorkspaceMembers=1&pageNo=1&pageSize=20&customerCode={lst[0]}&includeOrderCount=1"

        )
        return res,lst


    def customernumberfilter(self,return_customerdata,workspaces_data):
        response_json = return_customerdata.customersdata2.json
        lst=[]
        for i in response_json["customers"]:
            lst.append(i["phone"])

        res = self.send_request(
            Base.RequestMethod.GET,
            custom_url=f"{self.settings.url_prefix}/customers/{workspaces_data}?includeCustomerGroupAssignments=1&includeWorkspaceMembers=1&pageNo=1&pageSize=120&searchKey={lst[0]}&includeOrderCount=1",
        )
        return res,lst

    def particalsearchinfiltercustomercode(self, return_customerdata, workspaces_data):
        lst = '2000028'

        res = self.send_request(
            Base.RequestMethod.GET,
            custom_url=f"{self.settings.url_prefix}/customers/{workspaces_data}?includeCustomerGroupAssignments=1&includeWorkspaceMembers=1&pageNo=1&pageSize=20&customerCode={lst}&includeOrderCount=1",
        )
        return res


    def customerlocked(self,return_customerdata,workspaces_data):
        response_json = return_customerdata.customersdata2.json
        lst = []
        for i in response_json["customers"]:
            if i["isActive"] == 0:
                lst.append(i)

        res = self.send_request(
            Base.RequestMethod.GET,
            custom_url=f"{self.settings.url_prefix}/customers/{workspaces_data}?includeCustomerGroupAssignments=1&includeWorkspaceMembers=1&pageNo=1&pageSize=20&isActive=0&includeOrderCount=1",
        )
        return lst,res

    def customerunlocked(self,return_customerdata,workspaces_data):
        response_json=return_customerdata.customersdata2.json
        lst=[]
        for i in response_json["customers"]:
            if i["isActive"] == 1:
                lst.append(i)

        res = self.send_request(
            Base.RequestMethod.GET,
            custom_url=f"{self.settings.url_prefix}/customers/{workspaces_data}?includeCustomerGroupAssignments=1&includeWorkspaceMembers=1&pageNo=1&pageSize=20&isActive=1&includeOrderCount=1",
        )
        return lst,res

    def onboardingaccepted(self,return_customerdata,workspaces_data):
        response_json = return_customerdata.customersdata2.json
        lst = []
        for i in response_json["customers"]:
            if i["status"] == "A":
                lst.append(i)

        res = self.send_request(
            Base.RequestMethod.GET,
            custom_url=f"{self.settings.url_prefix}/customers/{workspaces_data}?includeCustomerGroupAssignments=1&includeWorkspaceMembers=1&pageNo=1&pageSize=20&onboardingStatus=A&includeOrderCount=1",
        )
        return lst,res





    

    def onboardingnotinvited(self, return_customerdata, workspaces_data):
        response_json = return_customerdata.customersdata2.json
        lst = []
        for i in response_json["customers"]:
            if i["status"] == "N":
                lst.append(i)

        res = self.send_request(
            Base.RequestMethod.GET,
            custom_url=f"{self.settings.url_prefix}/customers/{workspaces_data}?includeCustomerGroupAssignments=1&includeWorkspaceMembers=1&pageNo=1&pageSize=20&onboardingStatus=N&includeOrderCount=1",
        )
        return lst, res


    def onboardinginvited(self, return_customerdata, workspaces_data):
        response_json = return_customerdata.customersdata2.json
        lst = []
        for i in response_json["customers"]:
            if i["status"] == "P":
                lst.append(i)

        res = self.send_request(
            Base.RequestMethod.GET,
            custom_url=f"{self.settings.url_prefix}/customers/{workspaces_data}?includeCustomerGroupAssignments=1&includeWorkspaceMembers=1&pageNo=1&pageSize=20&onboardingStatus=P&includeOrderCount=1",
        )
        return lst,res


    def searchbycustomernumber(self,return_customerdata, workspaces_data):
        response_json=return_customerdata.customersdata2.json
        lst=[]
        for i in response_json["customers"]:
            lst.append(i["phone"])

        res = self.send_request(
            Base.RequestMethod.GET,
            custom_url=f"{self.settings.url_prefix}/customers/{workspaces_data}?includeCustomerGroupAssignments=1&includeWorkspaceMembers=1&searchKey={lst[0]}",
        )
        return lst,res

    def searchbycustomername(self,return_customerdata, workspaces_data):
        response_json = return_customerdata.customersdata2.json
        lst = []
        for i in response_json["customers"]:
            lst.append(i["companyName"])

        filter_name = {
            "searchKey":lst[0]
        }
        res = self.send_request(
            Base.RequestMethod.GET,
            custom_url=f"{self.settings.url_prefix}/customers/{workspaces_data}?includeCustomerGroupAssignments=1&includeWorkspaceMembers=1",
            params=filter_name
    )
        return lst,res

    def searchbycustomercode(self,return_customerdata, workspaces_data):
        response_json = return_customerdata.customersdata2.json
        lst = []
        for i in response_json["customers"]:
            lst.append(i["distributorCode"])
        res = self.send_request(
            Base.RequestMethod.GET,
            custom_url=f"{self.settings.url_prefix}/customers/{workspaces_data}?includeCustomerGroupAssignments=1&includeWorkspaceMembers=1&searchKey={lst[0]}",
        )
        return lst,res



    def searchbyparticalnameorcode(self,return_customerdata, workspaces_data):
        response_json = return_customerdata.customersdata2.json
        lst='leela'
        filter_name = {
            "searchKey": lst
        }
        res = self.send_request(
            Base.RequestMethod.GET,
            custom_url=f"{self.settings.url_prefix}/customers/{workspaces_data}?includeCustomerGroupAssignments=1&includeWorkspaceMembers=1",
            params=filter_name
        )
        return res,filter_name


