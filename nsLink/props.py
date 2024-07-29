from PropertyTree import PropertyNode

# Configuration
ident_node = PropertyNode('/config/identity')
specs_node = PropertyNode('/config/specs')
tecs_config_node = PropertyNode('/config/autopilot/TECS')

# Sensors
airdata_node = PropertyNode("/sensors/airdata")
imu_node = PropertyNode("/sensors/imu")
inceptors_node = PropertyNode("/sensors/inceptors")
gps_node = PropertyNode("/sensors/gps")
power_node = PropertyNode("/sensors/power")

# INS/GNSS
nav_node = PropertyNode("/filters/nav")

# Status and Comms
status_node = PropertyNode("/status")
events_node = PropertyNode("/status/events")
ann_node = PropertyNode("/status/annunciators")
remote_link_node = PropertyNode("/comms/remote_link")

# FCS
targets_node = PropertyNode("/autopilot/targets")
tecs_node = PropertyNode("/autopilot/tecs")
tecs_config_node = PropertyNode("/config/autopilot/TECS")
