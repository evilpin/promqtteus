#!/usr/bin/env python3
# -*- encoding: utf8 -*-

import paho.mqtt.client as mqtt
from prometheus_client import start_http_server, Gauge

known_topics = {}
faulty_topics = set()

def on_connect(client, userdata, flags, rc):
    print("Connected to MQTT with result code "+str(rc))

    # Subscribing to everything. This might not suit your setup :)
    client.subscribe("#")

def on_message(client, userdata, msg):
    global known_topics, faulty_topics
    t = msg.topic.replace('/', '_') # seperator conversion mqtt->prometheus
    if t.startswith('_'): t = t[1:] ## workaround for quirks in my own setup
    if t in faulty_topics: return

    if t not in known_topics.keys():
      print("Adding %s to known_topics" % t)
      known_topics[t] = Gauge(t, msg.topic)
   
    try:
      known_topics[t].set(msg.payload)
      print("Updating %s -> %0.2f" % (t, float(msg.payload)))
    except:
      print("Adding %s to faulty_topics" % t)
      faulty_topics.add(t)


if __name__ == '__main__':
    start_http_server(9119)

    client = mqtt.Client()
    client.on_connect = on_connect
    client.on_message = on_message
    client.connect("localhost", 1883, 60)

    client.loop_forever()

