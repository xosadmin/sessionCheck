# sessionCheck
A python-based automated BGP Session Uptime Monitor - Work with API webhook.
  
## Installation
- Clone this project
- Use ``install.sh`` by ``bash install.sh``
- Finish ``config.yaml``. For more detail, please refers to [example-config.yaml](https://github.com/xosadmin/sessionCheck/blob/main/example-config.yaml)
- Use ``systemctl start axbgpmon`` to start the service
  
## Note
- This monitor is tested and passed with Uptime Kuma, and works with any API webhook with GET method.
- This monitor requires ``python3`` and ``python3-pip`` package, please install it before install this monitor.
  