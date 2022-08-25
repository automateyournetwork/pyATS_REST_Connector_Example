import json
import logging
from pyats import aetest
from pyats.log.utils import banner
from tabulate import tabulate

# ----------------
# Get logger for script
# ----------------

log = logging.getLogger(__name__)

# ----------------
# AE Test Setup
# ----------------
class common_setup(aetest.CommonSetup):
    """Common Setup section"""
# ----------------
# Connected to devices
# ----------------
    @aetest.subsection
    def connect_to_devices(self, testbed):
        """Connect to all the devices"""
        testbed.connect()
# ----------------
# Mark the loop for Input Discards
# ----------------
    @aetest.subsection
    def loop_mark(self, testbed):
        aetest.loop.mark(Test_Interfaces, device_name=testbed.devices)
        aetest.loop.mark(Test_System, device_name=testbed.devices)
# ----------------
# Test Case #1
# ----------------
class Test_Interfaces(aetest.Testcase):
    """Parse all the commands"""

    @aetest.test
    def setup(self, testbed, device_name):
        """ Testcase Setup section """
        # connect to device
        self.device = testbed.devices[device_name]
        # Loop over devices in tested for testing
    
    @aetest.test
    def get_yang_data(self):
        # Use the RESTCONF OpenConfig YANG Model 
        parsed_openconfig_interfaces = self.device.rest.get("/restconf/data/openconfig-interfaces:interfaces")
        # Get the JSON payload
        self.parsed_json=parsed_openconfig_interfaces.json()

    @aetest.test
    def create_files(self):
        # Create .JSON file
        with open(f'{self.device.alias}_OpenConfig_Interfaces.json', 'w') as f:
            f.write(json.dumps(self.parsed_json, indent=4, sort_keys=True))
    
    @aetest.test
    def test_interface_input_discards(self):
        # Test for input discards
        in_discards_threshold = 0
        self.failed_interfaces = {}
        table_data = []
        for intf in self.parsed_json['openconfig-interfaces:interfaces']['interface']:
            counter = intf['state']['counters']['in-discards']
            if counter:
                table_row = []
                table_row.append(self.device.alias)
                table_row.append(intf['name'])
                table_row.append(counter)
                if int(counter) > in_discards_threshold:
                    table_row.append('Failed')
                    self.failed_interfaces[intf['name']] = int(counter)
                    self.interface_name = intf['name']
                    self.error_counter = self.failed_interfaces[intf['name']]
                else:
                    table_row.append('Passed')
            else:
                table_row.append(self.device.alias)
                table_row.append(intf)
                table_row.append('N/A')
                table_row.append('N/A')
            table_data.append(table_row)
            # display the table
        log.info(tabulate(table_data,
                            headers=['Device', 'Interface',
                                    'Input Discard Counter',
                                    'Passed/Failed'],
                            tablefmt='orgtbl'))
        # should we pass or fail?
        if self.failed_interfaces:
            aetest.loop.mark(name = self.failed_interfaces.keys())
            self.failed('Some interfaces have input discards')
        else:
            self.passed('No interfaces have input discards')

    @aetest.test
    def test_interface_input_errors(self):
        # Test for input discards
        in_errors_threshold = 0
        self.failed_interfaces = {}
        table_data = []
        for intf in self.parsed_json['openconfig-interfaces:interfaces']['interface']:
            counter = intf['state']['counters']['in-errors']
            if counter:
                table_row = []
                table_row.append(self.device.alias)
                table_row.append(intf['name'])
                table_row.append(counter)
                if int(counter) > in_errors_threshold:
                    table_row.append('Failed')
                    self.failed_interfaces[intf['name']] = int(counter)
                    self.interface_name = intf['name']
                    self.error_counter = self.failed_interfaces[intf['name']]
                else:
                    table_row.append('Passed')
            else:
                table_row.append(self.device.alias)
                table_row.append(intf)
                table_row.append('N/A')
                table_row.append('N/A')
            table_data.append(table_row)
            # display the table
        log.info(tabulate(table_data,
                            headers=['Device', 'Interface',
                                    'Input Errors Counter',
                                    'Passed/Failed'],
                            tablefmt='orgtbl'))
        # should we pass or fail?
        if self.failed_interfaces:
            aetest.loop.mark(name = self.failed_interfaces.keys())
            self.failed('Some interfaces have input errors')
        else:
            self.passed('No interfaces have input errors')

    @aetest.test
    def test_interface_input_fcs_errors(self):
        # Test for input discards
        in_fcs_errors_threshold = 0
        self.failed_interfaces = {}
        table_data = []
        for intf in self.parsed_json['openconfig-interfaces:interfaces']['interface']:
            counter = intf['state']['counters']['in-fcs-errors']
            if counter:
                table_row = []
                table_row.append(self.device.alias)
                table_row.append(intf['name'])
                table_row.append(counter)
                if int(counter) > in_fcs_errors_threshold:
                    table_row.append('Failed')
                    self.failed_interfaces[intf['name']] = int(counter)
                    self.interface_name = intf['name']
                    self.error_counter = self.failed_interfaces[intf['name']]
                else:
                    table_row.append('Passed')
            else:
                table_row.append(self.device.alias)
                table_row.append(intf)
                table_row.append('N/A')
                table_row.append('N/A')
            table_data.append(table_row)
            # display the table
        log.info(tabulate(table_data,
                            headers=['Device', 'Interface',
                                    'Input FCS Errors Counter',
                                    'Passed/Failed'],
                            tablefmt='orgtbl'))
        # should we pass or fail?
        if self.failed_interfaces:
            aetest.loop.mark(name = self.failed_interfaces.keys())
            self.failed('Some interfaces have input fcs errors')
        else:
            self.passed('No interfaces have input fcs errors')

    @aetest.test
    def test_interface_input_unknown_protocols(self):
        # Test for input discards
        in_unknown_protocols_threshold = 0
        self.failed_interfaces = {}
        table_data = []
        for intf in self.parsed_json['openconfig-interfaces:interfaces']['interface']:
            counter = intf['state']['counters']['in-unknown-protos']
            if counter:
                table_row = []
                table_row.append(self.device.alias)
                table_row.append(intf['name'])
                table_row.append(counter)
                if int(counter) > in_unknown_protocols_threshold:
                    table_row.append('Failed')
                    self.failed_interfaces[intf['name']] = int(counter)
                    self.interface_name = intf['name']
                    self.error_counter = self.failed_interfaces[intf['name']]
                else:
                    table_row.append('Passed')
            else:
                table_row.append(self.device.alias)
                table_row.append(intf)
                table_row.append('N/A')
                table_row.append('N/A')
            table_data.append(table_row)
            # display the table
        log.info(tabulate(table_data,
                            headers=['Device', 'Interface',
                                    'Input Unknown Protocols Counter',
                                    'Passed/Failed'],
                            tablefmt='orgtbl'))
        # should we pass or fail?
        if self.failed_interfaces:
            aetest.loop.mark(name = self.failed_interfaces.keys())
            self.failed('Some interfaces have input unknown protocols')
        else:
            self.passed('No interfaces have input unknwon protocols')

    @aetest.test
    def test_interface_output_discards(self):
        # Test for input discards
        out_discards_threshold = 0
        self.failed_interfaces = {}
        table_data = []
        for intf in self.parsed_json['openconfig-interfaces:interfaces']['interface']:
            counter = intf['state']['counters']['out-discards']
            if counter:
                table_row = []
                table_row.append(self.device.alias)
                table_row.append(intf['name'])
                table_row.append(counter)
                if int(counter) > out_discards_threshold:
                    table_row.append('Failed')
                    self.failed_interfaces[intf['name']] = int(counter)
                    self.interface_name = intf['name']
                    self.error_counter = self.failed_interfaces[intf['name']]
                else:
                    table_row.append('Passed')
            else:
                table_row.append(self.device.alias)
                table_row.append(intf)
                table_row.append('N/A')
                table_row.append('N/A')
            table_data.append(table_row)
            # display the table
        log.info(tabulate(table_data,
                            headers=['Device', 'Interface',
                                    'Output Discards Counter',
                                    'Passed/Failed'],
                            tablefmt='orgtbl'))
        # should we pass or fail?
        if self.failed_interfaces:
            aetest.loop.mark(name = self.failed_interfaces.keys())
            self.failed('Some interfaces have output discards')
        else:
            self.passed('No interfaces have output discards')

    @aetest.test
    def test_interface_output_errors(self):
        # Test for input discards
        out_errors_threshold = 0
        self.failed_interfaces = {}
        table_data = []
        for intf in self.parsed_json['openconfig-interfaces:interfaces']['interface']:
            counter = intf['state']['counters']['out-errors']
            if counter:
                table_row = []
                table_row.append(self.device.alias)
                table_row.append(intf['name'])
                table_row.append(counter)
                if int(counter) > out_errors_threshold:
                    table_row.append('Failed')
                    self.failed_interfaces[intf['name']] = int(counter)
                    self.interface_name = intf['name']
                    self.error_counter = self.failed_interfaces[intf['name']]
                else:
                    table_row.append('Passed')
            else:
                table_row.append(self.device.alias)
                table_row.append(intf)
                table_row.append('N/A')
                table_row.append('N/A')
            table_data.append(table_row)
            # display the table
        log.info(tabulate(table_data,
                            headers=['Device', 'Interface',
                                    'Output Errors Counter',
                                    'Passed/Failed'],
                            tablefmt='orgtbl'))
        # should we pass or fail?
        if self.failed_interfaces:
            aetest.loop.mark(name = self.failed_interfaces.keys())
            self.failed('Some interfaces have output errors')
        else:
            self.passed('No interfaces have output errors')

    @aetest.test
    def test_interface_full_duplex(self):
        # Test for input discards
        duplex_threshold = "FULL"
        self.failed_interfaces = {}
        table_data = []
        for intf in self.parsed_json['openconfig-interfaces:interfaces']['interface']:
            if 'openconfig-if-ethernet:ethernet' in intf:
                counter = intf['openconfig-if-ethernet:ethernet']['state']['negotiated-duplex-mode']
                if counter:
                    table_row = []
                    table_row.append(self.device.alias)
                    table_row.append(intf['name'])
                    table_row.append(counter)
                    if counter != duplex_threshold:
                        table_row.append('Failed')
                        self.failed_interfaces[intf['name']] = counter
                        self.interface_name = intf['name']
                        self.error_counter = self.failed_interfaces[intf['name']]
                    else:
                        table_row.append('Passed')
                else:
                    table_row.append(self.device.alias)
                    table_row.append(intf)
                    table_row.append('N/A')
                    table_row.append('N/A')
                table_data.append(table_row)
                # display the table
        log.info(tabulate(table_data,
                            headers=['Device', 'Interface',
                                    'Duplex Mode',
                                    'Passed/Failed'],
                            tablefmt='orgtbl'))
        # should we pass or fail?
        if self.failed_interfaces:
            aetest.loop.mark(name = self.failed_interfaces.keys())
            self.failed('Some interfaces have are half duplex')
        else:
            self.passed('All interfaces are full duplex')

# ----------------
# Test Case #1
# ----------------
class Test_System(aetest.Testcase):
    """Parse all the commands"""

    @aetest.test
    def setup(self, testbed, device_name):
        """ Testcase Setup section """
        # connect to device
        self.device = testbed.devices[device_name]
        # Loop over devices in tested for testing
    
    @aetest.test
    def get_yang_data(self):
        # Use the RESTCONF OpenConfig YANG Model 
        parsed_openconfig_interfaces = self.device.rest.get("/restconf/data/openconfig-system:system")
        # Get the JSON payload
        self.parsed_json=parsed_openconfig_interfaces.json()

    @aetest.test
    def create_files(self):
        # Create .JSON file
        with open(f'{self.device.alias}_OpenConfig_System.json', 'w') as f:
            f.write(json.dumps(self.parsed_json, indent=4, sort_keys=True))
    
    @aetest.test
    def test_motd(self):
        # Test for input discards
        self.failed_banner={}
        table_data = []
        table_row = []
        if 'motd-banner' in self.parsed_json['openconfig-system:system']['state']:
            table_row.append(self.device.alias)
            table_row.append("Has a Banner")
            table_row.append('Passed')
        else:
            table_row.append(self.device.alias)            
            table_row.append("No Banner")          
            table_row.append('Failed')
            self.failed_banner = "No Banner"
        table_data.append(table_row)
        # display the table
        log.info(tabulate(table_data,
                            headers=['Device', 'Has Banner', 'Passed/Failed'],
                            tablefmt='orgtbl'))
        # should we pass or fail?
        if self.failed_banner:
            self.failed('Device Does Not Have A MOTD Banner')
        else:
            self.passed('Device Has A MOTD Banner')

    @aetest.test
    def test_domain_name(self):
        # Test for input discards
        self.domain_name={}
        table_data = []
        table_row = []
        if 'domain-name' in self.parsed_json['openconfig-system:system']['state']:
            table_row.append(self.device.alias)
            table_row.append(self.parsed_json['openconfig-system:system']['state']['domain-name'])
            table_row.append('Passed')
        else:
            table_row.append(self.device.alias)            
            table_row.append("No Domain")          
            table_row.append('Failed')
            self.domain_name = "No Domain"
        table_data.append(table_row)
        # display the table
        log.info(tabulate(table_data,
                            headers=['Device', 'Has Domain', 'Passed/Failed'],
                            tablefmt='orgtbl'))
        # should we pass or fail?
        if self.domain_name:
            self.failed('Device Does Not Have A Domain Name')
        else:
            self.passed('Device Has A Domain Name')