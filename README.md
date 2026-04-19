# sessionCheck  
A Python-based automated BIRD2 BGP session uptime monitor with API webhook support.  
  
## Installation
- Clone this project.
- Run `bash install.sh`.
- Complete `config.yaml`. For more details, refer to [example-config.yaml](https://github.com/xosadmin/sessionCheck/blob/main/example-config.yaml).
- Start the service with `systemctl start axbgpmon`.
  
## Notes
- This monitor has been tested with Uptime Kuma and should also work with any API webhook that accepts GET requests.
- Each webhook push includes a `msg` field. The value of `msg` is the time when the session was last established, as reported by BIRD.
- For use with Uptime Kuma, it is recommended to set the `Heartbeat Interval` of the passive push monitor to 120 seconds.
- This monitor requires the `python3` and `python3-pip` packages. Please install them before running the installer.