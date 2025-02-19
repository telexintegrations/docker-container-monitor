# Docker Container Monitor

A Python-based (FastAPI) application that integrates with [Telex](https://telex.im) to monitor Docker containers and send alerts.

![Preview](https://github.com/user-attachments/assets/56fca051-aa0c-4016-b7d3-78a380f3eeba)

---

## **Table of Contents**
1. [Introduction](#introduction)
2. [Features](#features)
3. [Prerequisites](#prerequisites)
4. [Getting Started](#getting-started)
5. [API Documentation](#api-documentation)
6. [Testing](#testing)


## **Introduction**
This application allows you to monitor the status of Docker containers and send alerts via [Telex](https://telex.im). It is designed for developers and DevOps engineers who need to ensure their containers are running smoothly and receive notifications in case of issues.


## **Features**
- **Real-time Monitoring**: Continuously monitor Docker containers for uptime and health.
- **Telex Integration**: Send alerts to Telex channels for container status updates.


## **Prerequisites**
Before using this application, ensure you have the following:

- Python 3.8+
- **Docker Remote Access**: Configure your Docker daemon to accept requests from remote clients. Follow the [official Docker documentation](https://docs.docker.com/engine/daemon/remote-access/) to set this up.


## **Getting Started**
Follow these steps to set up and run the application locally.

### **1. Clone the Repository**
```bash
git clone https://github.com/telexintegrations/docker-container-monitor.git
```

### **2. Navigate to the Project Directory**
```bash
cd docker-container-monitor
```

### **3. Set Up a Virtual Environment**
We recommend using uv for faster dependency management:
```bash
uv venv
```

### **4. Install Dependencies**
```bash
uv pip install -r requirements.txt
```

### **5. Run the Application**
Start the FastAPI server:
```bash
uvicorn main:app --reload
```

Viola! The application will now be live at `http://localhost:8000`.

## **API Documentation**
The application provides auto-generated API documentation using Swagger UI. You can access it at:

- Swagger UI: `http://localhost:8000/docs`
- ReDoc: `http://localhost:8000/redoc`

## **Testing**
To test the application, use the following curl command to simulate a monitoring request:

```bash
curl --location 'http://localhost:8000/tick' \
--header 'Content-Type: application/json' \
--data '{
    "channel_id": "<your-test-telex-channel-id>",
    "return_url": "https://ping.telex.im/v1/return/<your-test-telex-channel-id>",
    "settings": [
        {
            "label": "Remote Host Address",
            "description": "Location of hosted Docker container (DNS or IP Address)",
            "type": "text",
            "required": true,
            "default": "<host-address e.g., 127.0.0.1>"
        },
        {
            "label": "Container ID",
            "description": "The ID of the container to monitor",
            "default": "<container-id>",
            "type": "text",
            "required": true
        },
        {
            "label": "interval",
            "type": "text",
            "required": true,
            "default": "* * * * *"
        }
    ]
}'
`
```
