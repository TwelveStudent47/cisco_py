from netmiko import ConnectHandler

router = {
    'device_type': 'cisco_ios',
    'host': '192.168.1.1',      
    'username': 'admin',
    'password': 'cisco',
}

router_connection = ConnectHandler(**router)

router_connection.enable()

commands = [
    "int s0/1/0",
    "ip add 10.0.0.1 255.255.255.0",
    "no sh"
]

change_ip = router_connection.send_config_set(commands)

print(router_connection.send_command("show ip interface brief"))

router_connection.disconnect()