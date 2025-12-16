from datetime import  datetime
import ipaddress

class IPv4Convertor:
    regex = r'(?:[0-9]{1,3}\.){3}[0-9]{1,3}'

    def to_python(self, value):
        try:
            return ipaddress.IPv4Address(value)
        except ipaddress.AddressValueError:
            return ValueError(f"Invalid IPv4 address: {value}")
        
    def to_url(se;f, value):
        return str(value)

class DateCOnverter:
    regex = "\d{4}-\d{1,2}-\d{1,2}"

    def to_python(self,value):
        return datetime.strptime(value, '%Y-%m-%d').date()
    
    def to_url(self, value):
        return datetime.strftime('%Y-%m-%d')