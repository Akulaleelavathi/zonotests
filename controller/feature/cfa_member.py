from controller.api_util.base_request import Base, BaseAssertion
# 6565656565
class member(Base):
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




    def update_users_manal(self, return_member, workspacedata):
        response_json = return_member.memberdata.json
        lst = []
        firstname = "qawsedrftgyhujikolp "

        lst.append(response_json["email"])

        res = self.send_request(
            Base.RequestMethod.PUT,
            custom_url="https://api-uat.beta.pharmconnect.com/users",
            payload={
                "email": lst[0],
                "firstName": firstname
            })
        return res, firstname, lst

    def update_users(self, return_member, workspacedata):
        response_json = return_member.memberdata.json
        lst = []
        email = "ab@gmail.com"

        lst.append(response_json["firstName"])
        lst.append(response_json["email"])

        res = self.send_request(
            Base.RequestMethod.PUT,
            custom_url="https://api-uat.beta.pharmconnect.com/users",
            payload={
                "email": email,
                "firstName": lst[0]
            })
        return res, lst, email
















































    # def updated_data_grayemail(self, return_member, workspacedata):
    #     lst1 = []
    #     lst2 = []
    #     lst3 = []
    #     response_json = return_member.memberdata1.json
    #
    #     email="qwerfdrtghyujiko@gmail.com"
    #
    #     for i in response_json:
    #         lst1.append(
    #             [i["businessDetails"]["physicalAddress"]["state"], i["businessDetails"]["physicalAddress"]["postcode"],
    #              i["businessDetails"]["physicalAddress"]["city"],
    #              i["businessDetails"]["physicalAddress"]["neighborhood"],
    #              i["businessDetails"]["physicalAddress"]["formatted"],
    #              i["businessDetails"]["physicalAddress"]["suburb"]])
    #
    #     for l in response_json:
    #         lst3.append([l["businessDetails"]["companyRefCode"], l["businessDetails"]["gstin"],
    #                      l["businessDetails"]["companyEmail"], l["businessDetails"]["legalName"]])
    #
    #     for j in response_json:
    #         lst2.append([j["id"], j["spaceName"], j["defaultCurrencyCode"], j["timeZone"],j["isoCountryCode"]])
    #
    #     res = self.send_request(
    #         Base.RequestMethod.PUT,
    #         custom_url=f"{self.settings.url_prefix}/workspace/details",
    #         payload={
    #             "physicalAddress": {
    #                 "postcode": lst1[0][1],
    #                 "city": lst1[0][2],
    #                 "state": lst1[0][0],
    #                 "neighborhood": lst1[0][3],
    #                 "formatted": lst1[0][4],
    #                 "suburb": lst1[0][5],
    #                 "isoCountryCode": lst2[0][4]
    #             },
    #             "workspaceId": lst2[0][0],
    #             "legalName": lst3[0][3],
    #             "companyRefCode": lst3[0][0],
    #             "defaultCurrencyCode": lst2[0][2],
    #             "timeZone": lst2[0][3],
    #             "spaceName": lst2[0][1],
    #             "companyEmail": email,
    #             "gstin": lst3[0][1]
    #         }
    #
    #     )
    #     return res, lst1, lst2, lst3
    #
    # def updated_data_gstnumber(self, return_member, workspacedata):
    #     lst1 = []
    #     lst2 = []
    #     lst3 = []
    #     response_json = return_member.memberdata1.json
    #
    #     gstnumber = "19AFOPP9479B4ZN"
    #
    #     for i in response_json:
    #         lst1.append(
    #             [i["businessDetails"]["physicalAddress"]["state"], i["businessDetails"]["physicalAddress"]["postcode"],
    #              i["businessDetails"]["physicalAddress"]["city"],
    #              i["businessDetails"]["physicalAddress"]["neighborhood"],
    #              i["businessDetails"]["physicalAddress"]["formatted"],
    #              i["businessDetails"]["physicalAddress"]["suburb"]])
    #
    #     for l in response_json:
    #         lst3.append([l["businessDetails"]["companyRefCode"], l["businessDetails"]["gstin"],
    #                      l["businessDetails"]["companyEmail"], l["businessDetails"]["legalName"]])
    #
    #     for j in response_json:
    #         lst2.append([j["id"], j["spaceName"], j["defaultCurrencyCode"], j["timeZone"],j["isoCountryCode"]])
    #
    #     res = self.send_request(
    #         Base.RequestMethod.PUT,
    #         custom_url=f"{self.settings.url_prefix}/workspace/details",
    #         payload={
    #             "physicalAddress": {
    #                 "postcode": lst1[0][1],
    #                 "city": lst1[0][2],
    #                 "state": lst1[0][0],
    #                 "neighborhood": lst1[0][3],
    #                 "formatted": lst1[0][4],
    #                 "suburb": lst1[0][5],
    #                 "isoCountryCode": lst2[0][4]
    #             },
    #             "workspaceId": lst2[0][0],
    #             "legalName": lst3[0][3],
    #             "companyRefCode": lst3[0][0],
    #             "defaultCurrencyCode": lst2[0][2],
    #             "timeZone": lst2[0][3],
    #             "spaceName": lst2[0][1],
    #             "companyEmail": lst3[0][2],
    #             "gstin": gstnumber
    #         }
    #
    #     )
    #     return res, lst1, lst2, lst3
    #
    # def updated_currency(self,return_member, workspacedata):
    #     lst1 = []
    #     lst2 = []
    #     lst3 = []
    #     response_json = return_member.memberdata1.json
    #
    #     currency = "SZL"
    #
    #     for i in response_json:
    #         lst1.append(
    #             [i["businessDetails"]["physicalAddress"]["state"], i["businessDetails"]["physicalAddress"]["postcode"],
    #              i["businessDetails"]["physicalAddress"]["city"],
    #              i["businessDetails"]["physicalAddress"]["neighborhood"],
    #              i["businessDetails"]["physicalAddress"]["formatted"],
    #              i["businessDetails"]["physicalAddress"]["suburb"]])
    #
    #     for l in response_json:
    #         lst3.append([l["businessDetails"]["companyRefCode"], l["businessDetails"]["gstin"],
    #                      l["businessDetails"]["companyEmail"], l["businessDetails"]["legalName"]])
    #
    #     for j in response_json:
    #         lst2.append([j["id"], j["spaceName"], j["defaultCurrencyCode"], j["timeZone"],j["isoCountryCode"]])
    #
    #     res = self.send_request(
    #         Base.RequestMethod.PUT,
    #         custom_url=f"{self.settings.url_prefix}/workspace/details",
    #         payload={
    #             "physicalAddress": {
    #                 "postcode": lst1[0][1],
    #                 "city": lst1[0][2],
    #                 "state": lst1[0][0],
    #                 "neighborhood": lst1[0][3],
    #                 "formatted": lst1[0][4],
    #                 "suburb": lst1[0][5],
    #                 "isoCountryCode": lst2[0][4]
    #             },
    #             "workspaceId": lst2[0][0],
    #             "legalName": lst3[0][3],
    #             "companyRefCode": lst3[0][0],
    #             "defaultCurrencyCode": currency,
    #             "timeZone": lst2[0][3],
    #             "spaceName": lst2[0][1],
    #             "companyEmail": lst3[0][2],
    #             "gstin": lst3[0][1]
    #         }
    #
    #     )
    #     return res, lst1, lst2, lst3
    #
    # def updated_countrycode(self, return_member, workspacedata):
    #     lst1 = []
    #     lst2 = []
    #     lst3 = []
    #     response_json = return_member.memberdata1.json
    #
    #     country = "USA"
    #
    #     for i in response_json:
    #         lst1.append(
    #             [i["businessDetails"]["physicalAddress"]["state"], i["businessDetails"]["physicalAddress"]["postcode"],
    #              i["businessDetails"]["physicalAddress"]["city"],
    #              i["businessDetails"]["physicalAddress"]["neighborhood"],
    #              i["businessDetails"]["physicalAddress"]["formatted"],
    #              i["businessDetails"]["physicalAddress"]["suburb"]])
    #
    #     for l in response_json:
    #         lst3.append([l["businessDetails"]["companyRefCode"], l["businessDetails"]["gstin"],
    #                      l["businessDetails"]["companyEmail"], l["businessDetails"]["legalName"]])
    #
    #     for j in response_json:
    #         lst2.append([j["id"], j["spaceName"], j["defaultCurrencyCode"], j["timeZone"], j["isoCountryCode"]])
    #
    #     res = self.send_request(
    #         Base.RequestMethod.PUT,
    #         custom_url=f"{self.settings.url_prefix}/workspace/details",
    #         payload={
    #             "physicalAddress": {
    #                 "postcode": lst1[0][1],
    #                 "city": lst1[0][2],
    #                 "state": lst1[0][0],
    #                 "neighborhood": lst1[0][3],
    #                 "formatted": lst1[0][4],
    #                 "suburb": lst1[0][5],
    #                 "isoCountryCode": country
    #             },
    #             "workspaceId": lst2[0][0],
    #             "legalName": lst3[0][3],
    #             "companyRefCode": lst3[0][0],
    #             "defaultCurrencyCode": lst2[0][2],
    #             "timeZone": lst2[0][3],
    #             "spaceName": lst2[0][1],
    #             "companyEmail": lst3[0][2],
    #             "gstin": lst3[0][1]
    #         }
    #
    #     )
    #     return res, lst1, lst2, lst3
    #
