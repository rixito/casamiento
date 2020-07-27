import os

CACHE_TYPE = "simple"
BASE_DIR = os.path.dirname(os.path.abspath(__file__))
TEMPLATE_XLSX_FOLDER = os.path.join(BASE_DIR, 'monitoring/static')
TEMPLATE_XLSX_FILE = os.path.join(TEMPLATE_XLSX_FOLDER, 'report.xlsx')
EXCEL_HEADERS = {
    'Tenant':'TenantID',
    'Business Group': 'GroupName',
    'Name': 'VirtualMachineName',
    'DNS name': 'VMDNSName',
    'Power State': 'VirtualMachineState',
    'CPU [quantity]': 'VMCPUs',
    'Memory [GB]': 'VMTotalMemoryMB',
    'Storage [GB]': 'VMTotalStorageGB',
    'Guest OS': 'GuestOS',
    'Last PowerOn': 'LastPowerOnDate'
}

EXCEL_TABS = {
    'vms': 'VirtualMachines',
    'bgs': 'BusinessGroups',
    'tenants': 'Tenants'
}

MONITORING_API = {
    'monitoring_api_url': 'http://localhost:8091',
    'cache_disabled': True,
    'resource_properties': {
        'Backup Type': 'summary|customTag:BackupType|customTagValue'
    }
}

CHARTS_DEFAULT_INTERVAL = 'MINUTES'
#Agregamos umbrales para definir cuando debe cambiar el intervalo en el modo CUSTOM
DAYS_INTERVALTYPE_THRESHOLD = 1000*60*60*24 *3 #3 dias en ms
MINUTES_INTERVALTYPE_THRESHOLD = 1000*60*60*12 #12 hs

CHARTS = [
    {
        'id': 'cpu_chart',
        'name': 'CPU Usage %',
        'series_label': ['cpu usage'],
        'series_stat_key': ['cpu|usage_average'],
        'label_y': 'Percentage (%)',
        'min': 0,
        'max': 100,
        'multiplier': 1,
        'round_decimals': 0
    },
    {
        'id': 'mem_chart',
        'name': 'Mem Usage %',
        'series_label': ['mem usage'],
        'series_stat_key': ['mem|usage_average'],
        'label_y': 'Percentage (%)',
        'min': 0,
        'max': 100,
        'multiplier': 1,
        'round_decimals': 0
    },
    {
        'id': 'disk_chart',
        'name': 'Disk Usage (GB)',
        'series_label': ['disk usage'],
        'series_stat_key': ['diskspace|used'],
        'label_y': 'GB',
        'min': 0,
        'max': None,
        'multiplier': 1,
        'round_decimals': 2
    }
]

MAJOR_VERSION = 1
MINOR_VERSION = 6
HOTFIX = 0

VERSION = "{}.{}.{}".format(MAJOR_VERSION, MINOR_VERSION, HOTFIX)
