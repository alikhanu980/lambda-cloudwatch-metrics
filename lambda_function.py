import json
import boto3

def lambda_handler(event, context):
    cloudwatch = boto3.client('cloudwatch')
    try:
        response = cloudwatch.put_metric_data(
            Namespace='MyCustomMetrics',
            MetricData=[
                {
                    'MetricName': 'DummyMetric',
                    'Dimensions': [
                        {
                            'Name': 'FunctionName',
                            'Value': 'MyLambdaFunction'
                        },
                    ],
                    'Value': 1.0,
                    'Unit': 'Count'
                },
            ]
        )
        return {
            'statusCode': 200,
            'body': json.dumps('Metric data published successfully')
        }
    except Exception as e:
        return {
            'statusCode': 500,
            'body': json.dumps(f'Error: {str(e)}')
        }
