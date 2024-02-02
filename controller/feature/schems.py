import pytest

from controller.api_util.base_request import Base, BaseAssertion
from controller.api_util.common_imports import *

class Schems(Base):
    def _init_(self,settings):
        Base._init_(self,settings)
        self.settings=settings

    def get_schems(self, workspaces_data):
        res = self.send_request(
            Base.RequestMethod.POST,
            custom_url=f"{self.settings.url_prefix}/commerce-v2/scheme/{workspaces_data}?pageNo=1&pageSize=20&skuCode=&sortDirection=&sortBy=&includeCFA=true&startDate=2023-12-12&endDate=2024-01-11&dispatchFilters=true&status=&promotionType=",
            payload={
                    "cfaFilter": [],
                    "divisionFilter": []
            }
        )
        logger.warning(f"response of get_schems{res.json}")
        return res.json


