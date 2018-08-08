#promqtteus

MQTT data exporter for Prometheus

Listens to your MQTT and makes integers/floats available for Prometheus. This code does nothing at all to monitor the performance of your MQTT server. I use this in my IOT-setup to let Grafana graph the output of my temperature sensors.

If you need to monitor a mosquitto or similar, I'd recommend https://github.com/inovex/mqtt_blackbox_exporter

These MQTT events:
```
home/alarm disarmed
sensors/climate/livingroom/temperature  25.36
sensors/climate/livingroom/humidity  54.82
```
Would result in this data to Prometheus:
```
sensors_climate_livingroom_humidity 54.82
sensors_climate_livingroom_temperatur 25.36
```

