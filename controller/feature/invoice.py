from controller.api_util.base_request import Base, BaseAssertion
from datetime import datetime
from urllib.parse import quote



current_date = datetime.now()


formatted_date = current_date.strftime("%Y-%m-%d")

class Invoice(Base):
    def _init_(self,settings):
        Base._init_(self,settings)
        self.settings=settings


    def get_Invoice_data(self,workspacedata,params):
        default_params = {
            "endDate": f"{formatted_date}",

        }
        default_params.update(params)
        workspacedata1=workspacedata
        res = self.send_request(
            Base.RequestMethod.GET,
            custom_url="https://api-uat.beta.pharmconnect.com/invoiceservice/invoices/8ef5d569-3419-44e5-bb33-3ecfd260f796?&startDate=2024-01-10%2000%3A00%3A00&pageNo=1&pageSize=198",
            params=default_params
        )
        return res

    def get_singleinvoicedata(self,return_invoice,workspacedata):
        response_json=return_invoice.invoicedata.json
        lst=[]

        for i in response_json["invoices"]:
            lst.append(i["id"])
        res = self.send_request(
            Base.RequestMethod.GET,
            custom_url=f"{self.settings.url_prefix}/invoiceservice/invoice/{lst[0]}?includePayment=true&workspaceId={workspacedata}",

        )
        return res

    def get_manual_singleinvoicedata(self,workspacedata):
        lst="2a66ebb5-d341-4dde-9c1c-040ad1a2078b"

        res = self.send_request(
            Base.RequestMethod.GET,
            custom_url=f"{self.settings.url_prefix}/invoiceservice/invoice/{lst}?includePayment=true&workspaceId={workspacedata}",

        )
        return res


    def manual_filter_invoice_statuses(self,workspacedata,params):
        default_params = {
            "endDate": f"{formatted_date}",

        }
        default_params.update(params)
        invoicestatues="PD"
        res = self.send_request(
            Base.RequestMethod.GET,
            custom_url=f"{self.settings.url_prefix}/invoiceservice/invoices/{workspacedata}?invoiceStatus={invoicestatues}&&startDate=2024-01-10%2000%3A00%3A00&pageNo=1&pageSize=500",
            params=default_params
        )
        return res

    def filter_invoice_statues(self,workspacedata,params):
        default_params = {
            "endDate": f"{formatted_date}",

        }
        default_params.update(params)

        res = self.send_request(
            Base.RequestMethod.GET,
            custom_url=f"{self.settings.url_prefix}/invoiceservice/invoices/{workspacedata}?&&startDate=2024-01-10%2000%3A00%3A00&",
            params=default_params
        )
        return res


    def manual_search_default(self,workspacedata):
        searchkey="9063014617"
        res = self.send_request(
            Base.RequestMethod.GET,
            custom_url=f"{self.settings.url_prefix}/invoiceservice/invoices/{workspacedata}?searchKey={searchkey}",
        )
        return res

    def search_default(self, workspacedata, return_invoice):
        response_json = return_invoice.invoicedata.json
        lst = []

        for i in response_json["invoices"]:
            lst.append(i["docNumber"])

        res = self.send_request(
            Base.RequestMethod.GET,
            custom_url=f"{self.settings.url_prefix}/invoiceservice/invoices/{workspacedata}?searchKey={lst[0]}",

        )
        return res,lst[0]

    def manual_downloadfile(self, workspacedata):
        lst = "2a66ebb5-d341-4dde-9c1c-040ad1a2078b"

        res = self.send_request(
            Base.RequestMethod.POST,
            custom_url=f"{self.settings.url_prefix}/invoiceservice/invoices/download/{workspacedata}",
            payload={
                "invoiceIds": [
                        lst
                ],
                "downloadType": "AIOCD",
                "downloadFormat": "text/csv",
                "includePayment": True,
                "startDate": "",
                "endDate": ""
            }



        )
        return res

    def downloadfile(self,return_invoice, workspacedata):
        response_json = return_invoice.invoicedata.json
        lst = []

        for i in response_json["invoices"]:
            lst.append(i["id"])

        res = self.send_request(
            Base.RequestMethod.POST,
            custom_url=f"{self.settings.url_prefix}/invoiceservice/invoices/download/{workspacedata}",
            payload={
                "invoiceIds": [
                    lst[0]
                ],
                "downloadType": "AIOCD",
                "downloadFormat": "text/csv",
                "includePayment": True,
                "startDate": "",
                "endDate": ""
            }

        )
        return res

    def get_aggregated(self, workspacedata):


        res = self.send_request(
            Base.RequestMethod.GET,
            custom_url=f"{self.settings.url_prefix}/invoiceservice/invoices/aggregated/{workspacedata}?endDate=2024-02-09+23%3A59%3A59&startDate=2024-01-10+00%3A00%3A00",

        )
        return res

















