import json

import pytest
import os

from controller.api_util.base_request import Base, BaseAssertion
from controller.file_operation import *


class Product(Base):
    def __init__(self, settings=None):
        super().__init__(settings)
        self.product_data = None

    def _init_(self,settings):
        Base._init_(self,settings)
        self.settings=settings


    def get_Product(self,workspaces_data):
        payload_template = r"C:\Users\Lenovo\Downloads\zono-qa-automation-main\zono-qa-automation-main\data\product.json"
        payload_json_data = read_json(payload_template)
        res=self.send_request(
            Base.RequestMethod.POST,
            custom_url=f"{self.settings.url_prefix}/commerce-v2/products/search/{workspaces_data}?pageNo=1&pageSize=20&customerId=",
            payload=payload_json_data

        )
        # logger.warning(f"response of get_products{res.json}")

        return res

    def get_divisionfilter(self,product_data,workspacedata):
        responsejson=product_data.json
        ist_data = []

        for i in responsejson["products"]:
            for j in i["productVariants"]:
                for k in j["division"]:
                    ist_data.append(k["divisionId"])
        a = set(ist_data)
        b = list(a)
        ist=[]
        for division in b:
            payload_template = r"C:\Users\Lenovo\Downloads\zono-qa-automation-main\zono-qa-automation-main\data\product.json"
            payload_json_data = read_json(payload_template)
            update_division = {
                 "divisionIds":[division],

            }
            payload_json_data.update(update_division)
            res = self.send_request(
                Base.RequestMethod.POST,
                custom_url=f"{self.settings.url_prefix}/commerce-v2/products/search/{workspacedata}?pageNo=1&pageSize=20&customerId=",
                payload=payload_json_data

            )
            ist.append(res.json)
        return ist

    def get_cfafilter(self,product_data, workspacedata):
        response_json = product_data.json

        ist_data = []
        for i in response_json.get("products", []):
            for j in i["productVariants"]:
                for k in j["cfas"]:
                    ist_data.append(str(k["cfaId"]))

        a = set(ist_data)
        b = list(a)
        cfa1=b
        payload_template = r"C:\Users\Lenovo\Downloads\zono-qa-automation-main\zono-qa-automation-main\data\product.json"
        payload_json_data = read_json(payload_template)
        update_cfa={
            "cfaIds":
                    b

        }
        payload_json_data.update(update_cfa)
        res = self.send_request(
            Base.RequestMethod.POST,
            custom_url=f"{self.settings.url_prefix}/commerce-v2/products/search/{workspacedata}?pageNo=1&pageSize=20&customerId=",

            payload=payload_json_data



        )

        return res,cfa1


    def get_schemesfilter(self,product_data, workspacedata):
        payload_template = r"C:\Users\Lenovo\Downloads\zono-qa-automation-main\zono-qa-automation-main\data\product.json"
        payload_json_data = read_json(payload_template)
        update_schemes = {
            "schemeType": [
                "product_discount"
            ],
        }
        payload_json_data.update(update_schemes)
        res = self.send_request(
            Base.RequestMethod.POST,
            custom_url=f"{self.settings.url_prefix}/commerce-v2/products/search/{workspacedata}?pageNo=1&pageSize=20&customerId=",
            payload=payload_json_data
        )
        return res.json,update_schemes




    def get_status(self,product_data,workspace):
        payload_template = r"C:\Users\Lenovo\Downloads\zono-qa-automation-main\zono-qa-automation-main\data\product.json"
        payload_json_data = read_json(payload_template)
        update_activeinactive = {
            "statusFilter": "ACTIVE"
        }
        payload_json_data.update(update_activeinactive)
        res = self.send_request(
            Base.RequestMethod.POST,
            custom_url=f"{self.settings.url_prefix}/commerce-v2/products/search/{workspace}?pageNo=1&pageSize=20&customerId=",
            payload=payload_json_data
        )
        return res



    def get_statuss(self,product_data,workspace):
        payload_template = r"C:\Users\Lenovo\Downloads\zono-qa-automation-main\zono-qa-automation-main\data\product.json"
        payload_json_data = read_json(payload_template)
        update_activeinactive = {
            "statusFilter": "INACTIVE"
        }
        payload_json_data.update(update_activeinactive)
        res = self.send_request(
            Base.RequestMethod.POST,
            custom_url="https://api-uat.beta.pharmconnect.com/commerce-v2/products/search/8ef5d569-3419-44e5-bb33-3ecfd260f796?pageNo=1&pageSize=20&customerId=",
            payload=payload_json_data
        )
        return res






    def get_skufilter(self,product_data,workspace):
        global update_skufilter, payload_json_data
        response_json = product_data.json
        a_list = []
        for i in response_json['products']:
            a_list.append(i["parentSku"])
            payload_template = r"C:\Users\Lenovo\Downloads\zono-qa-automation-main\zono-qa-automation-main\data\product.json"
            payload_json_data = read_json(payload_template)
            update_skufilter = {
                "skuCode": a_list[0]


            }
            payload_json_data.update(update_skufilter)


        res = self.send_request(
            Base.RequestMethod.POST,
            custom_url=f"{self.settings.url_prefix}/commerce-v2/products/search/{workspace}?pageNo=1&pageSize=20&customerId=",
            payload=payload_json_data
        )

        return res,update_skufilter


