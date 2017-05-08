import datetime
import json
from datetime import date

class JsonCustomEncoder(json.JSONEncoder):
    def default(self, field):

        if isinstance(field, datetime.datetime):
            return field.strftime('%Y-%m-%d %H:%M:%S')
        elif isinstance(field,date):
            return field.strftime('%Y-%m-%d')
        else:
            return json.JSONEncoder.default(self, field)


data={
    'k1':12,
    'k2':datetime.datetime.now()
}

a=json.dumps(data,cls=JsonCustomEncoder)
print(a)
