import json
import logging
import re

from datetime import datetime, timezone
from os.path import exists


data_template = ["mac", "timestamp", "value"]


class DeviceInterface:
    def __init__(self, device):
        if self.check_file(device):
            self.device_data = self.read_from_device(device)
            self.trim_data(self.device_data)
            if self.check_data_format(self.device_data):
                self.device_data.update(self.retrieve_db_data(self.device_data["mac"]))
        else:
            self.device_data = {}

    @classmethod
    def check_data_format(cls, device_data):
        """Take in mac_address, determine if its format is valid

        :param device_data: mac address for a device
        :type device_data: dict
        ...
        :return: true if valid, false if not
        :rtype: bool
        """
        if not all([data_type in device_data for data_type in data_template]):
            logging.warning("Missing data fields")
            return False
        if not cls.check_mac_format(device_data["mac"]):
            logging.warning(f"Invalid mac address: {device_data['mac']}")
            return False

        return True

    @classmethod
    def check_file(cls, file_path):
        """Take in file path, determine if file exists and is json

        :param file_path: path to a file
        :type file_path: string
        ...
        :return: true if valid, false if not
        :rtype: bool
        """
        if exists(file_path):
            file_type = file_path.split(".")[-1]
            if file_type == "json":
                return True
            else:
                logging.warning(f"{file_path} is not a json file")
                return False
        else:
            logging.warning(f"{file_path} does not exist")
            return False

    @classmethod
    def check_mac_format(cls, mac):
        """Take in mac_address, determine if its format is valid

        :param mac: mac address for a device
        :type mac: string
        ...
        :return: true if valid, false if not
        :rtype: bool
        """
        if not isinstance(mac, str):
            return False
        return bool(re.match("([0-9A-Fa-f]{2}[:-]){5}([0-9A-Fa-f]{2})$", mac))

    @classmethod
    def read_from_device(cls, device):
        """Take in mac_address and readout_value of a given device

        :param device: path to file for a given device
        :type device: string
        ...
        :return: a dictionary of device data, UTC timestamp, and error codes
        :rtype: dict
        """
        with open(device) as f:
            device_data = json.load(f)
        device_data["timestamp"] = datetime.now(timezone.utc)

        return device_data

    @classmethod
    def retrieve_db_data(cls, mac_address):
        """Look up device information given its mac_address

        :param mac_address: identifier for device
        :type mac_address: string
        ...
        :return: a dictionary of device information
        :rtype: dict
        """
        return {}

    @classmethod
    def trim_data(cls, device_data):
        """Removes unnecessary data from device stream

        :param device_data: data from device
        :type device_data: dict
        """
        excess_keys = [key for key in device_data if key not in data_template]
        [device_data.pop(field) for field in excess_keys]


if __name__ == "__main__":
    data = DeviceInterface("data/device/device_in_1.json").device_data
    print(data)