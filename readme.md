# Lambda CloudWatch Metrics

## Description

This repository contains an AWS Lambda function that publishes custom metrics to Amazon CloudWatch. The function serves as an example of how to create and manage custom metrics in CloudWatch using Python.

## Features

- **AWS Lambda Function**: Executes a function to publish custom metrics.
- **CloudWatch Integration**: Sends metrics data to Amazon CloudWatch.

## Setup

### Prerequisites

- AWS Account
- AWS CLI configured with appropriate permissions
- Python 3.12 (or compatible version)
- `boto3` library installed

### Installation

1. **Clone the Repository**:
    ```bash
    git clone https://github.com/alikhanu980/lambda-cloudwatch-metrics.git
    cd lambda-cloudwatch-metrics
    ```

2. **Install Dependencies**:
    If you have any dependencies listed, you can include them here. For example:
    ```bash
    pip install -r requirements.txt
    ```

### Deploying the Lambda Function

1. **Navigate to the Lambda Function Code Directory**:
    ```bash
    cd lambda-function
    ```

2. **Package Your Code**:
    Zip the Lambda function code and dependencies if necessary.

3. **Deploy the Lambda Function Using AWS CLI**:
    ```bash
    aws lambda create-function --function-name MyFunctionName \
      --runtime python3.12 \
      --role arn:aws:iam::your-account-id:role/your-role-name \
      --handler lambda_function.lambda_handler \
      --zip-file fileb://function.zip \
      --region your-region
    ```

4. **Configure CloudWatch Metrics**:
    Ensure your Lambda function is correctly configured to publish metrics to CloudWatch. Adjust the Lambda function code if needed to reflect your metrics and data.

## Usage

To test the Lambda function, you can invoke it manually using the AWS CLI or set up appropriate triggers.

### Example Invocation

```bash
aws lambda invoke --function-name MyFunctionName \
  --payload '{"key1": "value1", "key2": "value2"}' \
  response.json
