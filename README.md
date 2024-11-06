### README English

# IoT Monitoring Project

## Summary

The IoT Monitoring Project was designed to provide a robust real-time environmental monitoring system using sensor technologies and cloud platform integration. The system consists of an ESP32 device that collects temperature and humidity data via a DHT11 sensor and luminosity data through a photoresistor. The data is transmitted via Wi-Fi to the FIWARE system, which processes and stores it in MongoDB, located on a virtual machine instance in the Azure platform, configured via Docker.

Before sending data to the database, the ESP32 uses an algorithm to calculate the average of the readings taken over one minute, optimizing storage use and ensuring better data quality. Additionally, the application provides an interactive interface that can be accessed from anywhere with an internet connection, enabling continuous monitoring of the monitored environment.

This project also includes a virtual simulator developed through the Wokwi platform, which emulates the behavior of the ESP32 device and its sensors. The link to the simulator is available at: Wokwi IoT Project. Furthermore, a Python script (api-sth.py) simulates a simple local server to view real-time data directly in the browser.

With a focus on precision and efficiency, the project aims to be a scalable solution for environmental data monitoring in various contexts, such as study areas, controlled environments, and intelligent resource management systems.

This document provides a comprehensive overview of the system's architecture, features, and technologies, serving as a valuable guide for developers and researchers interested in IoT monitoring systems.

## Introduction

The Internet of Things (IoT) has become one of the most innovative and promising technologies in recent years, facilitating the collection, analysis, and visualization of real-time data. In the environmental context, such solutions offer an efficient way to monitor conditions such as temperature, humidity, and luminosity, being essential for automation and process optimization across various sectors.

This project was developed to provide an intelligent monitoring platform that allows high-precision environmental data collection, real-time visualization of these data, and generation of alerts based on critical conditions. The integration with technologies like FIWARE and MongoDB ensures the solution is scalable and highly efficient, while also ensuring that data is stored securely and is accessible.

## Objectives

- **Data Acquisition**: Implement a seamless system for collecting data from IoT sensors, ensuring measurement accuracy.
- **Data Visualization**: Develop an intuitive interface for users to access and monitor real-time data.
- **Alert System**: Implement a notification system to alert users about abnormal or critical conditions based on predefined limits.
- **Storage Efficiency**: Develop a mechanism for optimizing data storage by calculating the average of readings over a time interval.

## Features

1. **Real-Time Dashboard**
   - The dashboard displays real-time data from temperature, humidity, and luminosity sensors.
   - The data is presented interactively through dynamic graphs, allowing for easy interpretation and analysis.

2. **Alert System**
   - The application monitors the collected data and triggers alerts if values outside the expected limits are detected.
   - A visual alert system is activated on the dashboard, and the ESP32 can trigger an external light indicator to alert about abnormal conditions.

3. **Data Storage**
   - MongoDB is used to store historical data, allowing users to query past information and analyze trends over time.
   - The storage is optimized by sending data to the database only after calculating the average of the readings, reducing data volume and improving performance.

4. **Integration with RESTful API**
   - The application communicates with the FIWARE platform, ensuring integration between IoT devices and the backend server, facilitating efficient data exchange and communication.

## Technologies Used

- **ASP.NET Core 6.0**: A cross-platform development framework for building robust, fast, and scalable applications, used for both the backend and the dashboard.
- **MongoDB**: A NoSQL database for storing sensor data, enabling efficient analysis and visualization of data over time.
- **Azure Virtual Machine**: Cloud infrastructure hosting MongoDB, ensuring scalability and high availability of the system.
- **ESP32**: A microcontroller with Wi-Fi and Bluetooth connectivity, used to collect sensor data and send it to the FIWARE platform.
- **DHT11 Sensor**: A digital temperature and humidity sensor, used to measure environmental conditions with high precision.
- **Photoresistor (LDR)**: An electronic component used to measure the light intensity in the environment.

## Architecture Overview

The system architecture is designed to be scalable and modular. Below, we detail the main components of the system:

- **Frontend**: Developed using ASP.NET Core MVC, the interactive graphical interface allows users to monitor real-time data, view graphs, and receive alerts.
- **Backend**: Responsible for all business logic, including data collection from sensors, data processing, and alert management. Communication with the FIWARE API ensures efficient information exchange with IoT devices.
- **Database**: MongoDB stores the collected data, enabling queries and detailed reports on the monitored parameters over time.

## Installation and Configuration

To run the project locally, please follow these instructions:

- To open the implementation with ASP.NET Core 6.0 locally, you need to have Visual Studio (version 22 recommended) installed on your machine.
- The instructions to create a VM with MongoDB allocated via a Docker image are in the repository of Dr. Fabio Cabrini [here](https://github.com/fabiocabrini/fiware).
- If you want to use the Python test server to serve a local server with raw data samples, you can use the "api-sth.py" file in VS Code and install its dependencies. Don't forget to install Python first [here](https://www.python.org/downloads/). The server will be available at "localhost:8050".
- To access the FIWARE site, [Click Here](https://www.fiware.org/).
- To learn more about the ESP32, [Click Here](https://www.espressif.com/en/products/socs/esp32).

#### Other configurations if necessary:

Clone the repository:

```bash
git clone <repository-url>
cd <repository-directory>
