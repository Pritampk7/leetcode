import requests


class ciscoOpenConfig:
    def __init__(self, username, password, switch_ip):
        self.username = username
        self.password = password
        self.switch_ip = switch_ip
        self.headers = {"Content-type": "application/yang.data+json", "Accept": "application/yang.data+json"}

    def connect(self):
        request = requests.get(url=
                               f"https://{self.switch_ip}/restconf/data/openconfig-system:system/", verify=False,
                            headers=self.headers,
                            auth=(self.username, self.password))

        print(request.text)
        if request.status_code == 200:
            return request
        return request.status_code

obj = ciscoOpenConfig(username='admin', password="Admin_1234!", switch_ip="sbx-nxos-mgmt.cisco.com")
print(obj.connect())
