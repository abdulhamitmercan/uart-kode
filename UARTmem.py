class setDataval:
    
    def __init__(self):
        self._max_charge_val = None
        self._baz_val = None
        self._transection_val = None
    # max_charge_val 
    def set_max_charge_val(self, value):
        self._max_charge_val = value

    def get_max_charge_val(self):
        return self._max_charge_val

    # baz_val   
    def set_baz_val(self, value):
        self._baz_val = value

    def get_baz_val(self):
        return self._baz_val
    
    def set_transection_val(self, value):
        self._transection_val = value

    def get_transection_val(self):
        return self._transection_val   
    
    
class SetDataResponse:
    def __init__(self):
        self._runControl = None
        self._clearChargeSession = None
        self._endTransaction = None

    def setRunControl(self, value):
        self._runControl = value
    def getRunControl(self):
        return self._runControl

    def setClearChargeSession(self, value):
        self._clearChargeSession = value
    def getClearChargeSession(self):
        return self._clearChargeSession

    def setEndTransaction(self, value):
        self._endTransaction = value
    def getEndTransaction(self):
        return self._endTransaction


class ReadDataResponse:
    def __init__(self):
        self._chargingStartStop = None
        self._energyTotalComplate = None
        self._timeSeconds = None
        self._timeMinutes = None
        self._timeHours = None
        self._rmsPowerValue = None
        self._errorType = None
        self._chargeFinished = None
        self._chargeComplete = None
        self._chargingStatus = None
        self._connectorStatus = None
        self._deviceId = None

    def setChargingStartStop(self, value):
        self._chargingStartStop = value
    def getChargingStartStop(self):
        return self._chargingStartStop

    def setEnergyTotalComplate(self, value):
        self._energyTotalComplate = value
    def getEnergyTotalComplate(self):
        return self._energyTotalComplate

    def setTimeSeconds(self, value):
        self._timeSeconds = value
    def getTimeSeconds(self):
        return self._timeSeconds

    def setTimeMinutes(self, value):
        self._timeMinutes = value
    def getTimeMinutes(self):
        return self._timeMinutes
    
    def setTimeHours(self, value):
        self._timeHours = value
    def getTimeHours(self):  
        return self._timeHours

    def setRmsPowerValue(self, value):
        self._rmsPowerValue = value
    def getRmsPowerValue(self):
        return self._rmsPowerValue

    def setErrorType(self, value):
        self._errorType = value
    def getErrorType(self):
        return self._errorType
    
    def setChargeFinished(self, value):
        self._chargeFinished = value
    def getChargeFinished(self):
        return self._chargeFinished
    
    def setChargeComplete(self, value):
        self._chargeComplete = value
    def getChargeComplete(self):
        return self._chargeComplete

    def setChargingStatus(self, value):
        self._chargingStatus = value
    def getChargingStatus(self):
        return self._chargingStatus
    
    def setConnectorStatus(self, value):
        self._connectorStatus = value
    def getConnectorStatus(self):
        return self._connectorStatus   
    

    def setDeviceId(self, value):
        self._deviceId = value
    def getDeviceId(self):
        return self._deviceId
 
