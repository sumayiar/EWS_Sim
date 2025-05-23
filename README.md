# EWS_Sim
Creating a lightweight web interface that can run on a device (like a Raspberry Pi) and securely control a bioreactor.

# Core Concepts demonstrated in this project:
Embedded Linux (Ubuntu Server, Raspbian)

Web server frameworks (Flask, FastAPI, Express.js)

REST APIs

HTTPS (SSL/TLS), secure headers, rate limiting

# Concepts and skills I'm developing:
Setting up a Raspberry Pi or virtual Linux machine

Creating a simple Flask app:
  GET /status – returns bioreactor status
  POST /control – accepts commands to change settings

Adding TLS with a self-signed certificate (search: Flask HTTPS self-signed)

Adding basic authentication (JWT or HTTP Basic)
