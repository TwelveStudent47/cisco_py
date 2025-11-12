from netmiko import ConnectHandler
import datetime as time

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
    router_connection.disconnect()

def save_default_config(ip):
    router_connection = router_start(ip)
    default_config = router_connection.send_command("show startup-config")

    with open("default_config.txt", "w") as file:
        file.writelines(default_config)

    router_end(router_connection)

    print("Sikeresen lementetted az alapértelmezett konfigurációt")

def save_current_config(ip):
    now = time.datetime.now()

    formatted_time = now.strftime("%Y_%m_%d_%H_%M_%S")
    config_name = f"config_{formatted_time}.txt"
    router_connection = router_start(ip)
    current_config = router_connection.send_command("show running-config")

    with open(config_name, "w") as file:
        file.writelines(current_config)

    router_end(router_connection)

    print(f"Sikeresen lementetted a jelenleg futó configot ebbe a fájlba: {config_name}")

def run_custom_code(ip, list_of_commands):
    router_connection = router_start(ip)

    router_connection.send_config_set(list_of_commands)

    config = router_connection.send_command("show running-config")

    print(config)

    router_end(router_connection)

    print("Sikeresen lefuttattad a kódot.")