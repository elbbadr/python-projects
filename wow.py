import requests
import datetime

def download_csv_files(contract_address, start_date, end_date):
    base_url = "https://etherscan.io/exportData?type=tokentxns&contract={}&a=&decimal=18"

    start_datetime = datetime.datetime.strptime(start_date, "%Y-%m-%d")
    end_datetime = datetime.datetime.strptime(end_date, "%Y-%m-%d")

    current_datetime = start_datetime
    while current_datetime <= end_datetime:
        current_date = current_datetime.strftime("%Y-%m-%d")
        url = base_url.format(contract_address)
        file_name = f"{contract_address}_{current_date}.csv"

        response = requests.get(url)
        if response.status_code == 200:
            with open(file_name, "wb") as file:
                file.write(response.content)
            print(f"Downloaded {file_name}")
        else:
            print(f"Failed to download {file_name}")

        current_datetime += datetime.timedelta(days=1)

# Example usage
contract_address = "0x9cbf044bc535db4c93a9f11205a69631d9dcef26"
start_date = "2023-05-10"
end_date = "2023-05-14"

download_csv_files(contract_address, start_date, end_date)
