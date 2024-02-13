#!/bin/bash
export PYTHONDONTWRITEBYTECODE=1
export PYTHONUNBUFFERED=1
# Add other environment variables here

# Load environment variables
export $(cat /usr/src/app/.env | xargs)


cd /usr/src/app
/usr/local/bin/python delete_expired_values.py
