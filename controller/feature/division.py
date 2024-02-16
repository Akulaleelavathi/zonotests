
from controller.api_util.base_request import Base, BaseAssertion

class divisions(Base):
    def _init_(self,settings):
        Base._init_(self,settings)
        self.settings=settings



    def get_divisions(self, workspacedata):
        res = self.send_request(
            Base.RequestMethod.GET,
            custom_url="https://api-uat.beta.pharmconnect.com/division?workspaceId=8ef5d569-3419-44e5-bb33-3ecfd260f796&sortDirection=ASC&sortBy=",
        )
        return res

    def get_manual_data(self, workspacedata):
        order = "ASC"
        end = "Division.name"

        res = self.send_request(
            Base.RequestMethod.GET,
            custom_url=f"https://api-uat.beta.pharmconnect.com/division?workspaceId=8ef5d569-3419-44e5-bb33-3ecfd260f796&pageSize=20&pageNo=1&sortDirection={order}&sortBy={end}",
        )
        return res



    def get_dec(self, workspacedata):
        res = self.send_request(
            Base.RequestMethod.GET,
            custom_url="https://api-uat.beta.pharmconnect.com/division?workspaceId=8ef5d569-3419-44e5-bb33-3ecfd260f796&pageSize=20&pageNo=1&sortDirection=DESC&sortBy=Division.name",
        )
        return res


    def get_deccode(self, workspacedata):
        res = self.send_request(
            Base.RequestMethod.GET,
            custom_url=f"https://api-uat.beta.pharmconnect.com/division?workspaceId=8ef5d569-3419-44e5-bb33-3ecfd260f796&pageSize=20&pageNo=1&sortDirection=DESC&sortBy=Division.code",
        )
        return res


    def get_aeccode(self, workspacedata):
        res = self.send_request(
            Base.RequestMethod.GET,
            custom_url=f"https://api-uat.beta.pharmconnect.com/division?workspaceId=8ef5d569-3419-44e5-bb33-3ecfd260f796&pageSize=20&pageNo=1&sortDirection=ASC&sortBy=Division.code",
        )
        return res


    def get_HeadDivisionASC(self, workspacedata):
        res = self.send_request(
            Base.RequestMethod.GET,
            custom_url="https://api-uat.beta.pharmconnect.com/division?workspaceId=8ef5d569-3419-44e5-bb33-3ecfd260f796&pageSize=20&pageNo=1&sortDirection=ASC&sortBy=HeadDivision.name",
        )
        return res


    def get_HeadDivisionDESC(self, workspacedata):
        res = self.send_request(
            Base.RequestMethod.GET,
            custom_url="https://api-uat.beta.pharmconnect.com/division?workspaceId=8ef5d569-3419-44e5-bb33-3ecfd260f796&pageSize=20&pageNo=1&sortDirection=DESC&sortBy=HeadDivision.name",
        )
        return res



    def get_manual_search_data(self,workspacedata):
        search="00"

        res = self.send_request(
            Base.RequestMethod.GET,
            custom_url=f"https://api-uat.beta.pharmconnect.com/division?workspaceId=8ef5d569-3419-44e5-bb33-3ecfd260f796&searchKey={search}",
        )
        return res

    def get_name_search_data(self, workspacedata):


        res = self.send_request(
            Base.RequestMethod.GET,
            custom_url=f"https://api-uat.beta.pharmconnect.com/division?workspaceId=8ef5d569-3419-44e5-bb33-3ecfd260f796&searchKey=00",
        )
        return res

    def get_name_search_code(self, workspacedata):


        res = self.send_request(
            Base.RequestMethod.GET,
            custom_url=f"https://api-uat.beta.pharmconnect.com/division?workspaceId=8ef5d569-3419-44e5-bb33-3ecfd260f796&searchKey=VEGA",
        )
        return res