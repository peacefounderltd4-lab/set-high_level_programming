#!/bin/bash
# Request the message You got me!
curl -s -X PUT -d "user_id=98" "0.0.0.0:5000/catch_me"
