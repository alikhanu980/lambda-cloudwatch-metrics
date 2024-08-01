# Lambda CloudWatch Metrics

This repository contains an AWS Lambda function for publishing custom metrics to CloudWatch.

## Lambda Function

The Lambda function code is in `lambda_function.py`. This function publishes a metric named `DummyMetric` to CloudWatch.

## CloudWatch Setup

- **Namespace:** `MyCustomMetrics`
- **Metric Name:** `DummyMetric`

## Setup Instructions

1. **Create a Lambda Function** in the AWS Console using the provided code.
2. **Set up CloudWatch Metrics** and **Alarms** as needed.
3. **Test the Lambda Function** to ensure it publishes metrics successfully.

For more details, refer to the AWS Lambda and CloudWatch documentation.
