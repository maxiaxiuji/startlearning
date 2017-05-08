import requests

host_data={
    'status':True,
    'data':{
        'hostname':'c1.com',
        'disk':{'status':True,'data':'disk1111'},
        'memery':{'status':True,'data':'memery1111'},
    }
}
requests.post(
    url='http://127.0.0.1:8000/api/asset/?k2=122',

    # params={'k1':'ABC'},
    # data={'username':123}
    json=host_data

)