from netmiko import ConnectHandler

router = {
    'device_type': 'cisco_ios',
    'host': '192.168.1.1',      
    'username': 'admin',
    'password': 'cisco',
}

router_connection = ConnectHandler(**router)

router_connection.enable()

current_config = router_connection.send_command("show running-config")

with open("current_config.txt", "w") as file:
    file.writelines(current_config)

router_connection.disconnect()