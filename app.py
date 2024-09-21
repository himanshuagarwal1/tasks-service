#!/usr/bin/env python3
import aws_cdk as cdk
from tasks_service.tasks_service_stack import TasksServiceStack

app = cdk.App()
TasksServiceStack(app, "TasksServiceStack")

app.synth()
