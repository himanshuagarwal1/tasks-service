from aws_cdk import (
    Stack,
    aws_dynamodb as dynamodb,
    aws_lambda as _lambda,
    aws_apigateway as apigateway
)
from constructs import Construct

class TasksServiceStack(Stack):

    def __init__(self, scope: Construct, id: str, **kwargs) -> None:
        super().__init__(scope, id, **kwargs)

        # DynamoDB Table
        tasks_table = dynamodb.Table(self, "TasksTable",
                                     partition_key=dynamodb.Attribute(name="taskId",
                                                                      type=dynamodb.AttributeType.STRING),
                                     billing_mode=dynamodb.BillingMode.PAY_PER_REQUEST)

        # Lambda Functions
        create_task_lambda = _lambda.Function(self, "CreateTaskLambda",
                                              runtime=_lambda.Runtime.PYTHON_3_9,
                                              handler="create_task.handler",
                                              code=_lambda.Code.from_asset("lambda"),
                                              environment={
                                                  "TABLE_NAME": tasks_table.table_name
                                              })

        read_task_lambda = _lambda.Function(self, "ReadTaskLambda",
                                            runtime=_lambda.Runtime.PYTHON_3_9,
                                            handler="read_task.handler",
                                            code=_lambda.Code.from_asset("lambda"),
                                            environment={
                                                "TABLE_NAME": tasks_table.table_name
                                            })

        update_task_lambda = _lambda.Function(self, "UpdateTaskLambda",
                                              runtime=_lambda.Runtime.PYTHON_3_9,
                                              handler="update_task.handler",
                                              code=_lambda.Code.from_asset("lambda"),
                                              environment={
                                                  "TABLE_NAME": tasks_table.table_name
                                              })

        delete_task_lambda = _lambda.Function(self, "DeleteTaskLambda",
                                              runtime=_lambda.Runtime.PYTHON_3_9,
                                              handler="delete_task.handler",
                                              code=_lambda.Code.from_asset("lambda"),
                                              environment={
                                                  "TABLE_NAME": tasks_table.table_name
                                              })

        # Grant Lambda functions access to DynamoDB
        tasks_table.grant_read_write_data(create_task_lambda)
        tasks_table.grant_read_write_data(read_task_lambda)
        tasks_table.grant_read_write_data(update_task_lambda)
        tasks_table.grant_read_write_data(delete_task_lambda)

        # API Gateway
        api = apigateway.RestApi(self, "TasksApi",
                                 rest_api_name="Tasks Service",
                                 description="This service serves tasks.")

        tasks = api.root.add_resource("tasks")

        # API Integrations
        tasks.add_method("POST", apigateway.LambdaIntegration(create_task_lambda))  # POST /tasks
        task_item = tasks.add_resource("{taskId}")
        task_item.add_method("GET", apigateway.LambdaIntegration(read_task_lambda))  # GET /tasks/{taskId}
        task_item.add_method("PUT", apigateway.LambdaIntegration(update_task_lambda))  # PUT /tasks/{taskId}
        task_item.add_method("DELETE", apigateway.LambdaIntegration(delete_task_lambda))  # DELETE /tasks/{taskId}
