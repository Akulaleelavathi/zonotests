import pytest
import logging
from controller.settings import Settings
from controller.feature.users import *
from controller.feature.products import Product
from controller.feature.schems import Schems
from controller.feature.manualorder import CustomerId
from controller.feature.uploadorder import CustomerId
from controller.feature.customerack import Customerack



def pytest_addoption(parser):
    parser.addoption('--env', action='store',
                     help='setup environment; STAGING, PROD')
    parser.addoption('--dataset', action='store',
                     help='setup name of test data set (ex: test_data_set_1)')
    parser.addoption('--disable_ssh_tunnel', action='store_true', default=False,
                     help='Setup SSH Tunnel to connect with MongoDB (ex: True=1 or False=0)')
    parser.addoption('--settings_file', action='store', default=None,
                     help='setup settings data (ex: AIXON , EDP ; Default is AIXON)')
    parser.addoption("--api_version", action="store", metavar="api_version", default=None,
                     help="only run tests matching the api version as api_version.")


def pytest_configure(config):
    # register an additional marker
    config.addinivalue_line("markers",
                            "version(number): mark test to run only on named version")


@pytest.fixture(scope="session", autouse=True)
def setup(request):
    setup = Settings(request)
    setup.logic_controller = Users(setup)
    setup.otp = setup.logic_controller.send_otp()

    if (setup.otp["mfaStatus"]):
        setup.mobile_otp = setup.logic_controller.verify_mobile_otp(setup.otp)


        setup.token = setup.logic_controller.verify_email_otp(setup.otp,setup.mobile_otp)
    else:
        setup.token = setup.logic_controller.verify_otp(setup.otp)

    setup.logic_controller = Users(setup)
    setup.workspaces = setup.logic_controller.get_workspaces()

    yield setup

@pytest.fixture(scope="session")
def workspacedata(setup):
    workspaceId=(setup.logic_controller.get_workspaces()).json
    workspaceId_res=None
    for i in workspaceId:
        workspaceId_res=i["id"]

    return workspaceId_res


@pytest.fixture(scope="session")
def return_product(setup,workspacedata):
    product = Product(setup)
    product.product_data = product.get_Product(workspacedata)
    product.get_divisionfilter=product.get_divisionfilter(product.product_data,workspacedata)
    product.get_cfafilter=product.get_cfafilter(product.product_data,workspacedata)
    product.get_schemesfilter=product.get_schemesfilter(product.product_data,workspacedata)
    product.get_activiinactive=product.get_activeinactive(product.product_data,workspacedata)
    product.get_skufilter=product.get_skufilter(product.product_data,workspacedata)
    return product

@pytest.fixture(scope="session")
def return_schems(setup,workspacedata):
    product = Schems(setup)
    product.product_data = product.get_schems(workspacedata)

    return Schems

@pytest.fixture(scope="session")
def return_manual(setup,workspacedata):
    manualorder= CustomerId(setup)
    manualorder.customer_data=manualorder.get_customerid(workspacedata)
    manualorder.placeorderdetails=manualorder.get_placeorderdetails(manualorder.customer_data,workspacedata)
    manualorder.addtocard=manualorder.get_addtocard(manualorder.customer_data,workspacedata, manualorder.placeorderdetails)
    manualorder.checkout=manualorder.get_checkout(manualorder.customer_data,workspacedata,manualorder.addtocard)
    return manualorder

@pytest.fixture(scope="session")
def uploadorder(setup,workspacedata):
    uploadorder=CustomerId(setup)
    uploadorder.Customerdata=uploadorder.get_customerid(workspacedata)
    uploadorder.upload=uploadorder.upload(workspacedata,uploadorder.Customerdata)
    uploadorder.add_to_card=uploadorder.add_to_card(workspacedata,uploadorder.upload, uploadorder.Customerdata)
    uploadorder.check_out=uploadorder.check_out(workspacedata, uploadorder.add_to_card,uploadorder.Customerdata)
    return uploadorder

@pytest.fixture(scope="session")
def customerack(setup,workspacedata):
    customerack=Customerack(setup)
    customerack.waitingforack=customerack.waitingforack(workspacedata)
    customerack.singlecustomer=customerack.singlecustomer(workspacedata,customerack.waitingforack)
    customerack.checkout=customerack.checkout(workspacedata,customerack.singlecustomer)
    return customerack












def pytest_runtest_setup(item):
    version_marker = item.get_closest_marker("version")
    assigned_version = item.config.getoption("--api_version")
    if version_marker:
        version = version_marker.args[0]
        if not item.config.getoption("--api_version"):
            logging.warning("Not assigned api_version argument, but test case requires version as {}"
                            .format(version))
        elif version != assigned_version:
            pytest.skip(
                "test requires running on api version {}".format(version))
    else:
        logging.warning("Not found marker of the api version")
        logging.warning("Run test case by assigned api version as {}".format(
            assigned_version if assigned_version else Settings.DEFAULT_API_VERSION))
