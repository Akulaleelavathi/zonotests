from controller.api_util.base_request import Base, BaseAssertion

class Setting(Base):
    def _init_(self,settings):
        Base._init_(self,settings)
        self.settings=settings

    def get_datausersme(self,workspacedata):
        res = self.send_request(
            Base.RequestMethod.GET,
            custom_url=f"{self.settings.url_prefix}/users/me/v2?includeCFA=true&sellerWorkspaceId={workspacedata}",
        )
        return res

    def get_worspace(self, workspacedata):
        res = self.send_request(
            Base.RequestMethod.GET,
            custom_url=f"{self.settings.url_prefix}/workspaces",
        )
        return res


    def updated_data(self,return_settings,workspacedata):
        lst1=[]
        lst2=[]
        lst3=[]
        response_json = return_settings.settingsdata1.json

        for i in response_json:
            lst1.append(
                [i["businessDetails"]["physicalAddress"]["state"], i["businessDetails"]["physicalAddress"]["postcode"], i["businessDetails"]["physicalAddress"]["city"],
                 i["businessDetails"]["physicalAddress"]["neighborhood"], i["businessDetails"]["physicalAddress"]["formatted"],
                 i["businessDetails"]["physicalAddress"]["suburb"]])


        for l in response_json:
            lst3.append([l["businessDetails"]["companyRefCode"], l["businessDetails"]["gstin"],l["businessDetails"]["companyEmail"],l["businessDetails"]["legalName"]])

        for j in response_json:
            lst2.append([j["id"], j["spaceName"], j["defaultCurrencyCode"], j["timeZone"],j["isoCountryCode"]])

        res=self.send_request(
            Base.RequestMethod.PUT,
            custom_url=f"{self.settings.url_prefix}/workspace/details",
            payload={
                "physicalAddress": {
                    "postcode": lst1[0][1],
                    "city": lst1[0][2],
                    "state": lst1[0][0],
                    "neighborhood": lst1[0][3],
                    "formatted": lst1[0][4],
                    "suburb": lst1[0][5]
                },
                "workspaceId": lst2[0][0],
                "legalName": lst3[0][3],
                "companyRefCode":lst3[0][0],
                "defaultCurrencyCode": lst2[0][2],
                "timeZone": lst2[0][3],
                "spaceName": lst2[0][1],
                "companyEmail": lst3[0][2],
                "gstin": lst3[0][1]
            }


        )
        return res,lst1,lst2,lst3

    def updated_data_grayemail(self, return_settings, workspacedata):
        lst1 = []
        lst2 = []
        lst3 = []
        response_json = return_settings.settingsdata1.json

        email="sunpharmaqa_sq@yopmail.com"


        for i in response_json:
            lst1.append(
                [i["businessDetails"]["physicalAddress"]["state"], i["businessDetails"]["physicalAddress"]["postcode"],
                 i["businessDetails"]["physicalAddress"]["city"],
                 i["businessDetails"]["physicalAddress"]["neighborhood"],
                 i["businessDetails"]["physicalAddress"]["formatted"],
                 i["businessDetails"]["physicalAddress"]["suburb"]])

        for l in response_json:
            lst3.append([l["businessDetails"]["companyRefCode"], l["businessDetails"]["gstin"],
                         l["businessDetails"]["companyEmail"], l["businessDetails"]["legalName"]])

        for j in response_json:
            lst2.append([j["id"], j["spaceName"], j["defaultCurrencyCode"], j["timeZone"],j["isoCountryCode"]])

        res = self.send_request(
            Base.RequestMethod.PUT,
            custom_url=f"{self.settings.url_prefix}/workspace/details",
            payload={
                "physicalAddress": {
                    "postcode": lst1[0][1],
                    "city": lst1[0][2],
                    "state": lst1[0][0],
                    "neighborhood": lst1[0][3],
                    "formatted": lst1[0][4],
                    "suburb": lst1[0][5],
                    "isoCountryCode": lst2[0][4]
                },
                "workspaceId": lst2[0][0],
                "legalName": lst3[0][3],
                "companyRefCode": lst3[0][0],
                "defaultCurrencyCode": lst2[0][2],
                "timeZone": lst2[0][3],
                "spaceName": lst2[0][1],
                "companyEmail": email,
                "gstin": lst3[0][1]
            }

        )
        return res, lst1, lst2, lst3

    def updated_data_gstnumber(self, return_settings, workspacedata):
        lst1 = []
        lst2 = []
        lst3 = []
        response_json = return_settings.settingsdata1.json

        gstnumber = "19AFOPP9479B4ZN"

        for i in response_json:
            lst1.append(
                [i["businessDetails"]["physicalAddress"]["state"], i["businessDetails"]["physicalAddress"]["postcode"],
                 i["businessDetails"]["physicalAddress"]["city"],
                 i["businessDetails"]["physicalAddress"]["neighborhood"],
                 i["businessDetails"]["physicalAddress"]["formatted"],
                 i["businessDetails"]["physicalAddress"]["suburb"]])

        for l in response_json:
            lst3.append([l["businessDetails"]["companyRefCode"], l["businessDetails"]["gstin"],
                         l["businessDetails"]["companyEmail"], l["businessDetails"]["legalName"]])

        for j in response_json:
            lst2.append([j["id"], j["spaceName"], j["defaultCurrencyCode"], j["timeZone"],j["isoCountryCode"]])

        res = self.send_request(
            Base.RequestMethod.PUT,
            custom_url=f"{self.settings.url_prefix}/workspace/details",
            payload={
                "physicalAddress": {
                    "postcode": lst1[0][1],
                    "city": lst1[0][2],
                    "state": lst1[0][0],
                    "neighborhood": lst1[0][3],
                    "formatted": lst1[0][4],
                    "suburb": lst1[0][5],
                    "isoCountryCode": lst2[0][4]
                },
                "workspaceId": lst2[0][0],
                "legalName": lst3[0][3],
                "companyRefCode": lst3[0][0],
                "defaultCurrencyCode": lst2[0][2],
                "timeZone": lst2[0][3],
                "spaceName": lst2[0][1],
                "companyEmail": lst3[0][2],
                "gstin": gstnumber
            }

        )
        return res, lst1, lst2, lst3

    def updated_currency(self, return_settings, workspacedata):
        lst1 = []
        lst2 = []
        lst3 = []
        response_json = return_settings.settingsdata1.json

        currency = "SZL"

        for i in response_json:
            lst1.append(
                [i["businessDetails"]["physicalAddress"]["state"], i["businessDetails"]["physicalAddress"]["postcode"],
                 i["businessDetails"]["physicalAddress"]["city"],
                 i["businessDetails"]["physicalAddress"]["neighborhood"],
                 i["businessDetails"]["physicalAddress"]["formatted"],
                 i["businessDetails"]["physicalAddress"]["suburb"]])

        for l in response_json:
            lst3.append([l["businessDetails"]["companyRefCode"], l["businessDetails"]["gstin"],
                         l["businessDetails"]["companyEmail"], l["businessDetails"]["legalName"]])

        for j in response_json:
            lst2.append([j["id"], j["spaceName"], j["defaultCurrencyCode"], j["timeZone"],j["isoCountryCode"]])

        res = self.send_request(
            Base.RequestMethod.PUT,
            custom_url=f"{self.settings.url_prefix}/workspace/details",
            payload={
                "physicalAddress": {
                    "postcode": lst1[0][1],
                    "city": lst1[0][2],
                    "state": lst1[0][0],
                    "neighborhood": lst1[0][3],
                    "formatted": lst1[0][4],
                    "suburb": lst1[0][5],
                    "isoCountryCode": lst2[0][4]
                },
                "workspaceId": lst2[0][0],
                "legalName": lst3[0][3],
                "companyRefCode": lst3[0][0],
                "defaultCurrencyCode": currency,
                "timeZone": lst2[0][3],
                "spaceName": lst2[0][1],
                "companyEmail": lst3[0][2],
                "gstin": lst3[0][1]
            }

        )
        return res, lst1, lst2, lst3

    def updated_countrycode(self, return_settings, workspacedata):
        lst1 = []
        lst2 = []
        lst3 = []
        response_json = return_settings.settingsdata1.json

        country = "USA"

        for i in response_json:
            lst1.append(
                [i["businessDetails"]["physicalAddress"]["state"], i["businessDetails"]["physicalAddress"]["postcode"],
                 i["businessDetails"]["physicalAddress"]["city"],
                 i["businessDetails"]["physicalAddress"]["neighborhood"],
                 i["businessDetails"]["physicalAddress"]["formatted"],
                 i["businessDetails"]["physicalAddress"]["suburb"]])

        for l in response_json:
            lst3.append([l["businessDetails"]["companyRefCode"], l["businessDetails"]["gstin"],
                         l["businessDetails"]["companyEmail"], l["businessDetails"]["legalName"]])

        for j in response_json:
            lst2.append([j["id"], j["spaceName"], j["defaultCurrencyCode"], j["timeZone"], j["isoCountryCode"]])

        res = self.send_request(
            Base.RequestMethod.PUT,
            custom_url=f"{self.settings.url_prefix}/workspace/details",
            payload={
                "physicalAddress": {
                    "postcode": lst1[0][1],
                    "city": lst1[0][2],
                    "state": lst1[0][0],
                    "neighborhood": lst1[0][3],
                    "formatted": lst1[0][4],
                    "suburb": lst1[0][5],
                    "isoCountryCode": country
                },
                "workspaceId": lst2[0][0],
                "legalName": lst3[0][3],
                "companyRefCode": lst3[0][0],
                "defaultCurrencyCode": lst2[0][2],
                "timeZone": lst2[0][3],
                "spaceName": lst2[0][1],
                "companyEmail": lst3[0][2],
                "gstin": lst3[0][1]
            }

        )
        return res, lst1, lst2, lst3


    def update_users(self,return_settings, workspacedata):
        response_json=return_settings.settingsdata.json
        lst = []
        email="sunpharmaqa_sq@yopmail.com"


        lst.append(response_json["firstName"])
        lst.append(response_json["email"])

        res = self.send_request(
                Base.RequestMethod.PUT,
                custom_url="https://api-uat.beta.pharmconnect.com/users",
                payload={
                        "email": email,
                        "firstName":lst[0]
            })
        return res,lst,email


    def update_users_manal(self, return_settings, workspacedata):
        response_json = return_settings.settingsdata.json
        lst = []
        firstname="sun"

        lst.append(response_json["email"])

        res = self.send_request(
            Base.RequestMethod.PUT,
            custom_url="https://api-uat.beta.pharmconnect.com/users",
            payload={
                "email": lst[0],
                "firstName": firstname
            })
        return res, firstname,lst





    def updated_data_address(self,return_settings,workspacedata):
        lst1=[]
        lst2=[]
        lst3=[]
        response_json = return_settings.settingsdata1.json
        address="jubilee hills"

        for i in response_json:
            lst1.append(
                [i["businessDetails"]["physicalAddress"]["state"], i["businessDetails"]["physicalAddress"]["postcode"], i["businessDetails"]["physicalAddress"]["city"],
                 i["businessDetails"]["physicalAddress"]["neighborhood"], i["businessDetails"]["physicalAddress"]["formatted"],
                 i["businessDetails"]["physicalAddress"]["suburb"]])


        for l in response_json:
            lst3.append([l["businessDetails"]["companyRefCode"], l["businessDetails"]["gstin"],l["businessDetails"]["companyEmail"],l["businessDetails"]["legalName"]])

        for j in response_json:
            lst2.append([j["id"], j["spaceName"], j["defaultCurrencyCode"], j["timeZone"],j["isoCountryCode"]])

        res=self.send_request(
            Base.RequestMethod.PUT,
            custom_url=f"{self.settings.url_prefix}/workspace/details",
            payload={
                "physicalAddress": {
                    "postcode": lst1[0][1],
                    "city": lst1[0][2],
                    "state": lst1[0][0],
                    "neighborhood": lst1[0][3],
                    "formatted": address,
                    "suburb": lst1[0][5]
                },
                "workspaceId": lst2[0][0],
                "legalName": lst3[0][3],
                "companyRefCode":lst3[0][0],
                "defaultCurrencyCode": lst2[0][2],
                "timeZone": lst2[0][3],
                "spaceName": lst2[0][1],
                "companyEmail": lst3[0][2],
                "gstin": lst3[0][1]
            }


        )
        return res,address


    def updated_postcode(self,return_settings,workspacedata):
        lst1=[]
        lst2=[]
        lst3=[]
        response_json = return_settings.settingsdata1.json
        postcode="500001"

        for i in response_json:
            lst1.append(
                [i["businessDetails"]["physicalAddress"]["state"], i["businessDetails"]["physicalAddress"]["postcode"], i["businessDetails"]["physicalAddress"]["city"],
                 i["businessDetails"]["physicalAddress"]["neighborhood"], i["businessDetails"]["physicalAddress"]["formatted"],
                 i["businessDetails"]["physicalAddress"]["suburb"]])


        for l in response_json:
            lst3.append([l["businessDetails"]["companyRefCode"], l["businessDetails"]["gstin"],l["businessDetails"]["companyEmail"],l["businessDetails"]["legalName"]])

        for j in response_json:
            lst2.append([j["id"], j["spaceName"], j["defaultCurrencyCode"], j["timeZone"],j["isoCountryCode"]])

        res=self.send_request(
            Base.RequestMethod.PUT,
            custom_url=f"{self.settings.url_prefix}/workspace/details",
            payload={
                "physicalAddress": {
                    "postcode": postcode,
                    "city": lst1[0][2],
                    "state": lst1[0][0],
                    "neighborhood": lst1[0][3],
                    "formatted": lst1[0][4],
                    "suburb": lst1[0][5]
                },
                "workspaceId": lst2[0][0],
                "legalName": lst3[0][3],
                "companyRefCode":lst3[0][0],
                "defaultCurrencyCode": lst2[0][2],
                "timeZone": lst2[0][3],
                "spaceName": lst2[0][1],
                "companyEmail": lst3[0][2],
                "gstin": lst3[0][1]
            }


        )
        return res,postcode












    def updated_data_city(self,return_settings,workspacedata):
        lst1=[]
        lst2=[]
        lst3=[]
        response_json = return_settings.settingsdata1.json
        city="bhimavaram"

        for i in response_json:
            lst1.append(
                [i["businessDetails"]["physicalAddress"]["state"], i["businessDetails"]["physicalAddress"]["postcode"], i["businessDetails"]["physicalAddress"]["city"],
                 i["businessDetails"]["physicalAddress"]["neighborhood"], i["businessDetails"]["physicalAddress"]["formatted"],
                 i["businessDetails"]["physicalAddress"]["suburb"]])


        for l in response_json:
            lst3.append([l["businessDetails"]["companyRefCode"], l["businessDetails"]["gstin"],l["businessDetails"]["companyEmail"],l["businessDetails"]["legalName"]])

        for j in response_json:
            lst2.append([j["id"], j["spaceName"], j["defaultCurrencyCode"], j["timeZone"],j["isoCountryCode"]])

        res=self.send_request(
            Base.RequestMethod.PUT,
            custom_url=f"{self.settings.url_prefix}/workspace/details",
            payload={
                "physicalAddress": {
                    "postcode": lst1[0][1],
                    "city": city,
                    "state": lst1[0][0],
                    "neighborhood": lst1[0][3],
                    "formatted": lst1[0][4],
                    "suburb": lst1[0][5]
                },
                "workspaceId": lst2[0][0],
                "legalName": lst3[0][3],
                "companyRefCode":lst3[0][0],
                "defaultCurrencyCode": lst2[0][2],
                "timeZone": lst2[0][3],
                "spaceName": lst2[0][1],
                "companyEmail": lst3[0][2],
                "gstin": lst3[0][1]
            }


        )
        return res,city


    def updated_data_state(self,return_settings,workspacedata):
        lst1=[]
        lst2=[]
        lst3=[]
        response_json = return_settings.settingsdata1.json
        state="bihar"

        for i in response_json:
            lst1.append(
                [i["businessDetails"]["physicalAddress"]["state"], i["businessDetails"]["physicalAddress"]["postcode"], i["businessDetails"]["physicalAddress"]["city"],
                 i["businessDetails"]["physicalAddress"]["neighborhood"], i["businessDetails"]["physicalAddress"]["formatted"],
                 i["businessDetails"]["physicalAddress"]["suburb"]])


        for l in response_json:
            lst3.append([l["businessDetails"]["companyRefCode"], l["businessDetails"]["gstin"],l["businessDetails"]["companyEmail"],l["businessDetails"]["legalName"]])

        for j in response_json:
            lst2.append([j["id"], j["spaceName"], j["defaultCurrencyCode"], j["timeZone"],j["isoCountryCode"]])

        res=self.send_request(
            Base.RequestMethod.PUT,
            custom_url=f"{self.settings.url_prefix}/workspace/details",
            payload={
                "physicalAddress": {
                    "postcode": lst1[0][1],
                    "city": lst1[0][2],
                    "state": state,
                    "neighborhood": lst1[0][3],
                    "formatted": lst1[0][4],
                    "suburb": lst1[0][5]
                },
                "workspaceId": lst2[0][0],
                "legalName": lst3[0][3],
                "companyRefCode":lst3[0][0],
                "defaultCurrencyCode": lst2[0][2],
                "timeZone": lst2[0][3],
                "spaceName": lst2[0][1],
                "companyEmail": lst3[0][2],
                "gstin": lst3[0][1]
            }


        )
        return res,state

    def updated_data_single_data(self, return_settings, workspacedata):
        lst1 = []
        lst2 = []
        lst3 = []
        response_json = return_settings.settingsdata1.json

        for i in response_json:
            lst1.append(
                [i["businessDetails"]["physicalAddress"]["state"], i["businessDetails"]["physicalAddress"]["postcode"],
                 i["businessDetails"]["physicalAddress"]["city"],
                 i["businessDetails"]["physicalAddress"]["neighborhood"],
                 i["businessDetails"]["physicalAddress"]["formatted"],
                 i["businessDetails"]["physicalAddress"]["suburb"]])

        for l in response_json:
            lst3.append([l["businessDetails"]["companyRefCode"], l["businessDetails"]["gstin"],
                         l["businessDetails"]["companyEmail"], l["businessDetails"]["legalName"]])

        for j in response_json:
            lst2.append([j["id"], j["spaceName"], j["defaultCurrencyCode"], j["timeZone"], j["isoCountryCode"]])

        res = self.send_request(
            Base.RequestMethod.PUT,
            custom_url=f"{self.settings.url_prefix}/workspace/details",
            payload={
                "physicalAddress": {
                    "postcode": "501301",
                    "city": "",
                    "state": lst1[0][0],
                    "neighborhood": "",
                    "formatted": lst1[0][4],
                    "suburb":""
                },
                "workspaceId": lst2[0][0],
                "legalName": lst3[0][3],
                "companyRefCode": lst3[0][0],
                "defaultCurrencyCode": lst2[0][2],
                "timeZone": lst2[0][3],
                "spaceName": lst2[0][1],
                "companyEmail": lst3[0][2],
                "gstin": lst3[0][1]
            }

        )
        return res









