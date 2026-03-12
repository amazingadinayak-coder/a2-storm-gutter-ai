# SmartGutter AI

**Preventing Floods with Predictive Drain Management**

A Django-based website showcasing the SmartGutter AI proposal—an innovative system that uses data science and sensor technology to prevent flooding by predicting which drains are most likely to clog and when, coordinating cleaning efforts between city workers and local homeowners.

## Overview

SmartGutter AI addresses two main challenges:

1. **Resource Scheduling** — Efficiently schedule city workers to unclog drains using real-time sensor data and historical weather patterns.
2. **Community Mobilization** — Predict when a storm will overwhelm city capacity and mobilize local homeowners to provide organized assistance.

## Features

- **Gutter Sensors** — Collect water level and debris buildup data in real time
- **Predictive AI** — Uses weather and sensor data to predict flood severity
- **Notification System** — Automated alerts to city workers and homeowners
- **Collaborative Platform** — Connects cities with willing homeowners

## Setup

```bash
# Create and activate a virtual environment (recommended)
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate

# Install dependencies
pip install -r requirements.txt

# Run migrations
python manage.py migrate

# Start the development server (port 8080)
python manage.py runserver 8080
```

Visit [http://127.0.0.1:8080/](http://127.0.0.1:8080/) to view the site.

## Project Structure

```
a2-storm-gutter-ai/
├── manage.py
├── requirements.txt
├── smartgutter_project/     # Django project config
│   ├── settings.py
│   ├── urls.py
│   └── ...
└── smartgutter/            # Main app
    ├── templates/
    ├── static/
    ├── views.py
    └── urls.py
```

## Pages

- **Home** — Overview and key features
- **Problem** — Problem statement and challenges
- **Solution** — System design and technology
- **How It Works** — User experience for city and homeowners
- **Get Involved** — Registration information

## Based On

This project is based on the YAIS Abstract Proposal by Aditya.
