import os

def fill_template(template_file, output_file, params):
    if os.path.exists(template_file):
        # Template-Datei öffnen und Inhalt lesen
        with open(template_file, 'r') as file:
            template = file.read()
        if 'div' in params:
            params['mul']=1/float(params['div'])
            if 'decimals' not in params:
                if params['mul'] == 1:
                    params['decimals']=0
                if params['mul'] == 10:
                    params['decimals']=1
                if params['mul'] == 100:
                    params['decimals']=2        
        # Platzhalter durch Parameter ersetzen
        for key, value in params.items():
            template = template.replace(f'{{{{{key}}}}}', str(value))

        # Ergebnis in die Ausgabedatei schreiben
        with open(output_file, 'a') as file:
            file.write(template)

def main():
    

    # Mehrere Parameter-Sätze 
    # deviceclass see: https://www.home-assistant.io/integrations/sensor/#device-class
    parameters_list = [
        {'varname': 'R0_differential',  'address': 769, 'file': 'ModbusRW', 'type': 'U_WORD', 'div': '1',  'min': '2', 'max': '100','unit':'C','deviceclass':'temperature'},
        {'varname': 'A1_min',  'address': 774, 'file': 'ModbusRW', 'type': 'S_WORD', 'div': '1',  'min': '-45', 'max': '99','unit':'C','deviceclass':'temperature'},
        {'varname': 'A2_max',  'address': 775, 'file': 'ModbusRW', 'type': 'S_WORD', 'div': '1',  'min': '-45', 'max': '99','unit':'C','deviceclass':'temperature'},
        {'varname': 'ALD_Alarm_delay', 'address': 779, 'file': 'ModbusRW', 'type': 'S_WORD', 'div': '0.1', 'min': '0', 'max': '240', 'unit':'s','deviceclass':'duration'},
        {'varname': 'CAL_Calibration', 'address': 781, 'file': 'ModbusRW', 'type': 'S_WORD', 'div': '1',  'min': '-100', 'max': '100', 'unit':'""','deviceclass':'""'},
        {'varname': 'LSE_min_setpoint', 'address': 786, 'file': 'ModbusRW', 'type': 'S_WORD', 'div': '1',  'min': '-45', 'max': '99', 'unit':'C','deviceclass':'temperature'},
        {'varname': 'HSE_max_setpoint', 'address': 787, 'file': 'ModbusRW', 'type': 'S_WORD', 'div': '1',  'min': '-45', 'max': '99', 'unit':'C','deviceclass':'temperature'},
        {'varname': 'nSC_night_diff', 'address': 794, 'file': 'ModbusRW', 'type': 'S_WORD', 'div': '1',  'min': '-200', 'max': '200', 'unit':'C','deviceclass':'temperature'},
        {'varname': 'Pump_down', 'address': 1287, 'file': 'Modbus_B_R'},
        {'varname': 'Remote_standby', 'address': 1288, 'file': 'Modbus_B_R'},
        {'varname': 'Night_dig', 'address': 1291, 'file': 'Modbus_B_R'},
        {'varname': 'C1_compress_delay', 'address': 780, 'file': 'ModbusRW', 'type': 'S_WORD', 'div': '1', 'min': '0', 'max': '15', 'unit':'s','deviceclass':'duration'},
        {'varname': 'CE1_on_compress_error', 'address': 792, 'file': 'ModbusRW', 'type': 'S_WORD', 'div': '0.1', 'min': '0', 'max': '240', 'unit':'s','deviceclass':'duration'},
        {'varname': 'CE2_off_compress_error', 'address': 793, 'file': 'ModbusRW', 'type': 'S_WORD', 'div': '0.1', 'min': '5', 'max': '240', 'unit':'s','deviceclass':'duration'},
        {'varname': 'Compressor_state', 'address': 1279, 'file': 'Modbus_B_R'},
        {'varname': 'Compressor_prot_input', 'address': 1285, 'file': 'Modbus_B_R'},
        {'varname': 'D1_Defrost_type', 'address': 512, 'file': 'ModbusRW', 'type': 'S_WORD', 'div': '1', 'min': '0', 'max': '2', 'unit':'""','deviceclass':'""'},
        {'varname': 'D0_defrost', 'address': 769, 'file': 'ModbusRW', 'type': 'S_WORD', 'div': '1', 'min': '0', 'max': '4', 'unit':'""','deviceclass':'""'},
        {'varname': 'D2_defrost_limit', 'address': 770, 'file': 'ModbusRW', 'type': 'S_WORD', 'div': '1', 'min': '-35', 'max': '45', 'unit':'C','deviceclass':'temperature'},
        {'varname': 'D3_defrost_time', 'address': 771, 'file': 'ModbusRW', 'type': 'S_WORD', 'div': '0.1', 'min': '1', 'max': '240', 'unit':'s','deviceclass':'duration'},
        {'varname': 'D7_dripping_time', 'address': 772, 'file': 'ModbusRW', 'type': 'S_WORD', 'div': '1', 'min': '0', 'max': '10', 'unit':'s','deviceclass':'duration'},
        {'varname': 'F5_fan_pause', 'address': 773, 'file': 'ModbusRW', 'type': 'S_WORD', 'div': '1', 'min': '1', 'max': '10', 'unit':'s','deviceclass':'duration'},
        {'varname': 'F4_defrost_fan_state', 'address': 777, 'file': 'ModbusRW', 'type': 'S_WORD', 'div': '1', 'min': '0', 'max': '1', 'unit':'""','deviceclass':'""'},
        {'varname': 'DE_defrost_probe_enable', 'address': 778, 'file': 'ModbusRW', 'type': 'S_WORD', 'div': '1', 'min': '0', 'max': '1', 'unit':'""','deviceclass':'""'},
        {'varname': 'DPO_defrost_power_on', 'address': 779, 'file': 'ModbusRW', 'type': 'S_WORD', 'div': '1', 'min': '0', 'max': '1', 'unit':'""','deviceclass':'""'},
        {'varname': 'DSE_smart_defrost', 'address': 790, 'file': 'ModbusRW', 'type': 'S_WORD', 'div': '1', 'min': '0', 'max': '1', 'unit':'""','deviceclass':'""'},
        {'varname': 'DST_smart_defrost_temp', 'address': 790, 'file': 'ModbusRW', 'type': 'S_WORD', 'div': '1', 'min': '-30', 'max': '30', 'unit':'C','deviceclass':'temperature'},
        {'varname': 'Turn_on_defrost', 'address': 1012, 'file': 'ModbusRW', 'type': 'S_WORD', 'div': '1', 'min': '0', 'max': '1', 'unit':'""','deviceclass':'""'},
        {'varname': 'Defrost_state', 'address': 1280, 'file': 'Modbus_B_R'},
        {'varname': 'Dripping_state', 'address': 1283, 'file': 'Modbus_B_R'},
        {'varname': 'Remote_start_Defrost', 'address': 1289, 'file': 'Modbus_B_R'},
        {'varname': 'Remote_stop_Defrost', 'address': 1290, 'file': 'Modbus_B_R'},
        {'varname': 'Input_1_setting', 'address': 514, 'file': 'ModbusRW', 'type': 'S_WORD', 'div': '1', 'min': '-8', 'max': '8', 'unit':'""','deviceclass':'""'},
        {'varname': 'Input_2_setting', 'address': 515, 'file': 'ModbusRW', 'type': 'S_WORD', 'div': '1', 'min': '-8', 'max': '8', 'unit':'""','deviceclass':'""'},
        {'varname': 'Aux_1_control', 'address': 516, 'file': 'ModbusRW', 'type': 'S_WORD', 'div': '1', 'min': '-6', 'max': '6', 'unit':'""','deviceclass':'""'},
        {'varname': 'Aux_2_control', 'address': 517, 'file': 'ModbusRW', 'type': 'S_WORD', 'div': '1', 'min': '-6', 'max': '6', 'unit':'""','deviceclass':'""'},
        {'varname': 'DQC_door_open', 'address': 782, 'file': 'ModbusRW', 'type': 'S_WORD', 'div': '1', 'min': '0', 'max': '5', 'unit':'""','deviceclass':'""'},
        {'varname': 'TDO_door_open', 'address': 783, 'file': 'ModbusRW', 'type': 'S_WORD', 'div': '0.1', 'min': '0', 'max': '240', 'unit':'C','deviceclass':'temperature'},
        {'varname': 'STA_Aux_temp', 'address': 788, 'file': 'ModbusRW', 'type': 'S_WORD', 'div': '1', 'min': '-45', 'max': '99', 'unit':'C','deviceclass':'temperature'},
        {'varname': 'BEE_Buzzer_enable', 'address': 795, 'file': 'ModbusRW', 'type': 'S_WORD', 'div': '1', 'min': '0', 'max': '1', 'unit':'""','deviceclass':'""'},
        {'varname': 'Light_state', 'address': 1282, 'file': 'Modbus_B_R'},
        {'varname': 'Door_state', 'address': 1284, 'file': 'Modbus_B_R'},
        {'varname': 'Turn_on_light', 'address': 1536, 'file': 'Modbus_B_R'},
        {'varname': 'F3_fan_state', 'address': 776, 'file': 'ModbusRW', 'type': 'S_WORD', 'div': '1', 'min': '0', 'max': '2', 'unit':'""','deviceclass':'""'},
        {'varname': 'FST_Fan_stop', 'address': 784, 'file': 'ModbusRW', 'type': 'S_WORD', 'div': '1', 'min': '-45', 'max': '99', 'unit':'C','deviceclass':'temperature'},
        {'varname': 'FD_Fan_stop_diff', 'address': 787, 'file': 'ModbusRW', 'type': 'S_WORD', 'div': '1', 'min': '1', 'max': '10', 'unit':'C','deviceclass':'temperature'},
        {'varname': 'F6_fans_recir_on', 'address': 796, 'file': 'ModbusRW', 'type': 'S_WORD', 'div': '0.1', 'min': '1', 'max': '240', 'unit':'C','deviceclass':'temperature'},
        {'varname': 'F7_fans_recir_off', 'address': 797, 'file': 'ModbusRW', 'type': 'S_WORD', 'div': '0.1', 'min': '1', 'max': '240', 'unit':'C','deviceclass':'temperature'},
        {'varname': 'Fans_state', 'address': 1281, 'file': 'Modbus_B_R'},
        {'varname': 'E0_Ambient_error', 'address': 19999, 'file': 'Modbus_B_R'},
        {'varname': 'E1_Defrost_error', 'address': 20000, 'file': 'Modbus_B_R'},
        {'varname': 'EEPROM_error', 'address': 20001, 'file': 'Modbus_B_R'},
        {'varname': 'Alarm_High_temp', 'address': 20002, 'file': 'Modbus_B_R'},
        {'varname': 'Alarm_Low_temp', 'address': 20003, 'file': 'Modbus_B_R'},
        {'varname': 'ED_Door_open', 'address': 20004, 'file': 'Modbus_B_R'},
        {'varname': 'E8_man_in_room', 'address': 20005, 'file': 'Modbus_B_R'},
        {'varname': 'EC_Compromize_alarm', 'address': 20006, 'file': 'Modbus_B_R'},
        {'varname': 'E9_Light_alarm', 'address': 20007, 'file': 'Modbus_B_R'},
        {'varname': 'Ambient_temp', 'address': 255, 'file': 'ModbusR', 'type': 'S_WORD', 'div': '0.1', 'unit':'C','deviceclass':'temperature'},
        {'varname': 'Evapor_temp', 'address': 256, 'file': 'ModbusR', 'type': 'S_WORD', 'div': '0.1', 'unit':'C','deviceclass':'temperature'},
        {'varname': 'Setpoint', 'address': 797, 'file': 'ModbusRW', 'type': 'S_WORD', 'div': '0.1', 'min': '-45', 'max': '99', 'unit':'C','deviceclass':'temperature'},
        {'varname': 'man_in_room', 'address': 1286, 'file': 'Modbus_B_R'},
        {'varname': 'Turn_on_standby', 'address': 1535, 'file': 'ModbusRW', 'type': 'S_WORD', 'div': '1', 'min': '0', 'max': '1', 'unit':'""','deviceclass':'""'},

    ]

    # Ordner für Ausgabedateien erstellen, falls nicht vorhanden
    output_dir = '../gen'
    os.makedirs(output_dir, exist_ok=True)
        

    #    {'file': 'ModbusRW', 'type': 'S_WORD', 'div': '0.1', 'mul': '10', 'min': '0', 'max': '10', 'varname': 'test1', 'address': 771,'unit':'C','deviceclass':'temperature'},
    #    {'file': 'ModbusRW', 'type': 'S_WORD', 'div': '0.1', 'mul': '10', 'min': '0', 'max': '10', 'varname': 'test2', 'address

    typelist = ['sensor','binary_sensor','number','switch']
    for num, type in enumerate(typelist, start=1):
        # Template für jeden Satz von Parametern füllen und speichern
        output_file = os.path.join(output_dir, f"danfoss-optyma_{type}.yaml")
        if os.path.exists(output_file):
            os.remove(output_file)
        with open(output_file, 'w') as file:
            file.write("\n")
        for i, params in enumerate(parameters_list, start=1):
            print(params)
            template_file = params['file']
            fill_template(f"template/{template_file}_{type}.yaml", output_file, params)

    typelist = ['sensor','binary_sensor','number','switch']
    for num, type in enumerate(typelist, start=1):
        # Template für jeden Satz von Parametern füllen und speichern
        output_file = os.path.join(output_dir, f"MQTT_danfoss-optyma_{type}.yaml")
        if os.path.exists(output_file):
            os.remove(output_file)
        with open(output_file, 'w') as file:
            file.write("\n")
        for i, params in enumerate(parameters_list, start=1):
            print(params)
            template_file = params['file']
            fill_template(f"template/MQTT{template_file}_{type}.yaml", output_file, params)




if __name__ == '__main__':
    main()
