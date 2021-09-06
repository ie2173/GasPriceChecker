import requests
import datetime
import csv


class GasTracker:
    def __init__(self, url):
        self.api_link = url

    def get_gas_info(self):
        return requests.get(self.api_link).json()

    def update_csv(self, data, filepath):
        row = [str(datetime.datetime.now()), data['result']['LastBlock'], data['result']['SafeGasPrice'], data['result']['ProposeGasPrice'], data['result']['FastGasPrice']]

        with open(filepath, mode='a') as gas_file:
            gas_passer = csv.writer(gas_file, quoting=csv.QUOTE_NONNUMERIC)
            gas_passer.writerow(row)

        gas_file.close()


if __name__ == "__main__":
    x = GasTracker("{URL GOES HERE}")
    x.update_csv(x.get_gas_info(), "{FILE PATH GOES HERE}")
