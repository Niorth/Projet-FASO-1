#!/bin/bash

API="o.OZwVI3zr98FrH5Exr0zKe6WkQ8uhqpeB"
MSG="$1"

curl -u $API: https://api.pushbullet.com/v2/pushes -d type=note -d title="Alert" -d body="$MSG"