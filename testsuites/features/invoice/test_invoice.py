import json
import io
import pandas as pd
import json

from controller.feature.invoice import *
from controller.api_util.common_imports import *


# def test_get_invoice(setup,workspacedata):
#     invoicedata= Invoice(setup)
#     params={}
#     filtercode = invoicedata.get_Invoice_data(workspacedata,params)
#     res=filtercode.json
#     # print(res)
#     assert filtercode.status_code == 200
#     count=0
#     for i in res["invoices"]:
#         count+=1
#         assert i["id"]
#     print(count)
#
#
# def test_get_singleinvoicedata(return_invoice,setup,workspacedata):
#     invoicedata= Invoice(setup)
#     filtercode = invoicedata.get_singleinvoicedata(return_invoice,workspacedata)
#     res=filtercode.json
#     # print(json.dumps(res,indent=4))
#     assert filtercode.status_code == 200
#     for i in res["lines"]:
#         assert i["sku"], "Assertion Failure, Invoice details Invalid sku"
#         assert i["productTitle"], "Assertion Failure, Invoice details Invalid productTitle"
#
#
# def test_get_manual_singleinvoicedata(return_invoice,setup,workspacedata):
#     invoicedata= Invoice(setup)
#     filtercode = invoicedata.get_manual_singleinvoicedata(workspacedata)
#     res=filtercode.json
#     # print(json.dumps(res,indent=4))
#     assert filtercode.status_code == 200
#     for i in res["lines"]:
#         assert i["sku"], "Assertion Failure, Invoice details Invalid sku"
#         assert i["productTitle"], "Assertion Failure, Invoice details Invalid productTitle"
#


def test_manual_filter_invoice_statuses(return_invoice,setup,workspacedata):
    invoicedata= Invoice(setup)
    params={}
    filtercode = invoicedata.manual_filter_invoice_statuses(workspacedata,params)
    res=filtercode.json
    # print(res)
    assert filtercode.status_code == 200
    count = 0
    for i in res["invoices"]:
        count += 1
        assert i["id"]
    print(count)


#
# invoicestatues=["PD","C","PP","OD","P"]
# @pytest.mark.parametrize("each_params", invoicestatues)
# def test_filter_invoice_statues(return_invoice,setup,workspacedata,each_params):
#     invoicedata= Invoice(setup)
#     params = {
#         "invoiceStatus": each_params
#     }
#
#
#     filtercode = invoicedata.filter_invoice_statues(workspacedata,params)
#     res=filtercode.json
#     # print(res)
#     assert filtercode.status_code == 200
#     for i in res["invoices"]:
#         assert i["invoiceStatus"] == each_params
#     count = 0
#     for i in res["invoices"]:
#         count += 1
#         assert i["id"]
#     print(count)
#
#
#
#
# def test_manual_search_default(return_invoice,setup,workspacedata):
#     invoicedata= Invoice(setup)
#     filtercode = invoicedata.manual_search_default(workspacedata)
#     res=filtercode.json
#     # print(res)
#     assert filtercode.status_code == 200
#
#
#
# def test_search_default(return_invoice,setup,workspacedata):
#     invoicedata= Invoice(setup)
#     filtercode = invoicedata.search_default(workspacedata,return_invoice)
#     res=filtercode[0]
#     lst=filtercode[1]
#
#     # print(lst)
#     assert res.status_code == 200
#     for i in res.json["invoices"]:
#         assert lst == i["docNumber"]
#
#
# def test_manual_downloadfile(return_invoice,setup,workspacedata):
#     invoicedata= Invoice(setup)
#     filtercode = invoicedata.manual_downloadfile(workspacedata)
#     res=filtercode
#     # print(res)
#     data=res.text
#     df = pd.read_csv(io.StringIO(data))
#
#     # Specify the Excel file path where you want to save the data
#     excel_file_path = "output_invoice.xlsx"
#
#     # Save the DataFrame to Excel
#     df.to_excel(excel_file_path, index=False)
#
#     # Optionally, print a message to confirm that the Excel file has been saved
#     print(f"Data saved to {excel_file_path}")
#     assert res.status_code == 200
#
#
# def test_downloadfile(return_invoice,setup,workspacedata):
#     invoicedata= Invoice(setup)
#     filtercode = invoicedata.downloadfile(return_invoice,workspacedata,)
#     res=filtercode
#     # print(res)
#     data=res.text
#     df = pd.read_csv(io.StringIO(data))
#
#     # Specify the Excel file path where you want to save the data
#     excel_file_path = "outputs_invoice.xlsx"
#
#     # Save the DataFrame to Excel
#     df.to_excel(excel_file_path, index=False)
#
#     # Optionally, print a message to confirm that the Excel file has been saved
#     print(f"Data saved to {excel_file_path}")
#     assert res.status_code == 200
#
#
#
# def test_get_aggregated(setup,workspacedata):
#     invoicedata= Invoice(setup)
#     filtercode = invoicedata.get_aggregated(workspacedata)
#     res=filtercode.json
#     # print(res)
#     assert filtercode.status_code == 200
#     assert "paid" in res
#     assert "unpaid" in res
#     assert "overdue" in res
#     assert "total" in res
#
#
#
#
#
#
#
