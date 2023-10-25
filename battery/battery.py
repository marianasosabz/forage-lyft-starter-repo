from datetime import date


class Battery:
    def __init__(self, last_service_date, current_date):
        self.last_service_date = last_service_date
        self.current_date = current_date

    def needs_service(self):
        raise NotImplementedError("Subclasses must implement this method")


class SpindlerBattery(Battery):
    def needs_service(self):
        if (self.current_date - self.last_service_date).days >= 730:
            return True
        return False


class NubbinBattery(Battery):
    def needs_service(self):
        if (self.current_date - self.last_service_date).days >= 1460:
            return True
        return False
