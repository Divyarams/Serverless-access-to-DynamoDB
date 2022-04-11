# Serverless-access-to-DynamoDB
Using SAM CloudFormation Template, design a Serverless Microservices Architecture. The template creates serverless resources and use commands:

sam build : to build the package in our local machine provided we have the runtime environment of Lambda in the local machine.
sam deploy : to deploy the package in AWS. Any changes/updates to CloudFormation template will be reflected in the physical resources.

#Stage 1

Creation of Serverless CloudFormation template with logical resources and IAM permissions.

#Stage 2

Lambda function with Python run-time environment. Using Boto3 SDK to get item/item collection from DynamoDB tables.

#Stage 3

API Gateway integration with Lambda to fetch items from table.
