import json

class GatewayDeviceService:
    def __init__(self, message):
        self.message = message;

    def conversionHatInfo(self):
        f = open('gatewayCode.txt' ,mode = 'r');
        line = f.readline();
        print("SERVICE | code : ", line);
        print("SERVICE | message : ", self.message);

        dataList = self.message.split('/');
        dataList.insert(0, line);

        print("SERVICE | dataList : ", dataList);

        keyList = ['gatewayCode', 'safeHatCode', 'cardNumber', 'latitude', 'longitude', 'time', 'isWear'];

        dataJson = dict(zip(keyList, dataList));
        dataJson = json.dumps(dataJson);

        print("SERVICE | final Json : ", dataJson);

        return dataJson;
