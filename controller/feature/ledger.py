from controller.api_util.base_request import Base, BaseAssertion

class ledger(Base):
    def _init_(self,settings):
        Base._init_(self,settings)
        self.settings=settings


    def get_ledgerdata(self,workspacedata):
        res = self.send_request(
            Base.RequestMethod.GET,
            custom_url=f"{self.settings.url_prefix}/customers/{workspacedata}?includeCustomerGroupAssignments=1&includeWorkspaceMembers=1&pageNo=1&pageSize=20&includeOrderCount=1",
        )
        return res


    def get_singleledgerdata(self,return_ledger,workspacedata):
        response_json=return_ledger.ledgerdata.json
        lst=[]
        for i in response_json["customers"]:
            lst.append(i["id"])
        res = self.send_request(
            Base.RequestMethod.GET,
            custom_url=f"{self.settings.url_prefix}/invoiceservice/partyAccountBook/list?sellerWorkspaceId={workspacedata}&inviteId={lst[0]}&startDate=2024-01-09&endDate=2024-02-08&filter=&pageSize=20&pageNo=1&searchKey=&sortBy=transactionDate&sortDirection=DESC",
        )
        return res,lst

    def get_manual_singleledgerdata(self, return_ledger, workspacedata):
        lst="05ea35f1-5438-43ff-a654-c3abb7f91073"


        res = self.send_request(
            Base.RequestMethod.GET,
            custom_url=f"{self.settings.url_prefix}/invoiceservice/partyAccountBook/list?sellerWorkspaceId={workspacedata}&inviteId={lst}&startDate=2024-01-09&endDate=2024-02-08&filter=&pageSize=20&pageNo=1&searchKey=&sortBy=transactionDate&sortDirection=DESC",
        )
        return res
    def manual_downloadfile(self,workspacedata):
        lst = "05ea35f1-5438-43ff-a654-c3abb7f91073"


        res = self.send_request(
            Base.RequestMethod.GET,
            custom_url=f"{self.settings.url_prefix}/invoiceservice/partyaccountbook/list/download?sellerWorkspaceId={workspacedata}&inviteId={lst}&startDate=2024-01-09&endDate=2024-02-08&filter=&searchKey=&pageNo=1&pageSize=20&downloadContentType=csv",
        )
        return res


    def downloadfile(self,return_ledger,workspacedata):
        response_json = return_ledger.ledgerdata.json
        lst = []
        for i in response_json["customers"]:
            lst.append(i["id"])


        res = self.send_request(
            Base.RequestMethod.GET,
            custom_url=f"{self.settings.url_prefix}/invoiceservice/partyaccountbook/list/download?sellerWorkspaceId={workspacedata}&inviteId={lst[0]}&startDate=2024-01-09&endDate=2024-02-08&filter=&searchKey=&pageNo=1&pageSize=20&downloadContentType=csv",
        )
        return res








