import json
import io
import pandas as pd
import json

from controller.feature.ledger import *

def test_get_ledger(return_ledger,setup,workspacedata):
    ledgerdata= ledger(setup)
    filtercode = ledgerdata.get_ledgerdata(workspacedata)
    res=filtercode.json
    # print(res)
    assert filtercode.status_code == 200




def test_get_singleledgerdata(return_ledger,setup,workspacedata):
    ledgerdata = ledger(setup)
    filtercode = ledgerdata. get_singleledgerdata(return_ledger,workspacedata)
    res = filtercode[0]
    lst=filtercode[1]
    # print(lst)
    print(res.json)
    assert res.status_code == 200
    count=0
    for i in res.json["partyAccountBook"]:
        count += 1
        assert "id" in i

    print(count)




def test_get_manual_singleledgerdata(return_ledger,setup,workspacedata):
    ledgerdata = ledger(setup)
    filtercode = ledgerdata. get_manual_singleledgerdata(return_ledger,workspacedata)
    res = filtercode
    print(res.json)
    assert res.status_code == 200
    assert res.json["endRecord"]==3
    count=0
    for i in res.json["partyAccountBook"]:
        count+=1
        assert "id" in i

    print(count)


def test_manual_downloadfile(return_ledger,setup,workspacedata):
    ledgerdata = ledger(setup)
    filtercode = ledgerdata. manual_downloadfile(workspacedata)
    res = filtercode
    print(res.json)
    data=res.text
    df = pd.read_csv(io.StringIO(data))

    # Specify the Excel file path where you want to save the data
    excel_file_path = "output.xlsx"

    # Save the DataFrame to Excel
    df.to_excel(excel_file_path, index=False)

    # Optionally, print a message to confirm that the Excel file has been saved
    print(f"Data saved to {excel_file_path}")
    assert res.status_code == 200


def test_downloadfile(return_ledger,setup,workspacedata):
    ledgerdata = ledger(setup)
    filtercode = ledgerdata.downloadfile(return_ledger,workspacedata)
    res = filtercode
    print(res.json)
    data=res.text
    df = pd.read_csv(io.StringIO(data))

    # Specify the Excel file path where you want to save the data
    excel_file_path = "outputs.xlsx"

    # Save the DataFrame to Excel
    df.to_excel(excel_file_path, index=False)

    # Optionally, print a message to confirm that the Excel file has been saved
    print(f"Data saved to {excel_file_path}")
    assert res.status_code == 200








