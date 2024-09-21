# Tasks Service

This repository contains the code for a serverless CRUD API for managing tasks, built using AWS CDK and Python.

## Project Structure

tasks-service/
│
├── lambda/
│   ├── create_task.py
│   ├── read_task.py
│   ├── update_task.py
│   └── delete_task.py
│
├── tasks_service/
│   └── tasks_service_stack.py
│
├── README.md
│
├── app.py
│
├── cdk.json
│
├── requirements.txt
│
└── setup.py




- `lambda/`: Contains the Lambda function code for handling CRUD operations.
- `tasks_service/`: Contains the AWS CDK stack definition.
- `README.md`: This file.
- `app.py`: Entry point for the CDK app.
- `requirements.txt`: Python dependencies.
- `setup.py`: Project setup file.

## Prerequisites

- AWS CLI configured with proper credentials.
- Node.js (v14.x or later) and npm.
- Python 3.8 or later.
- AWS CDK installed globally (`npm install -g aws-cdk`).

## Setup Instructions

1. **Clone the Repository**

   ```bash
   git clone https://github.com/himanshuagarwal1/tasks-service.git
   cd tasks-service
