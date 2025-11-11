from netmiko import ConnectHandler

def router_start(ip):
    router = {
    'device_type': 'cisco_ios',
    'host': ip,      
    'username': 'admin',
    'password': 'cisco',
    }

    router_connection = ConnectHandler(**router)

    router_connection.enable()
    
    return router_connection

def router_end(router_connection):
    router_connection.end()
