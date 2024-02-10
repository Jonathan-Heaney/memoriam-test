import boto3
from botocore.exceptions import ClientError
from django.conf import settings

def send_email(to_email, subject, body):
    ses_client = boto3.client(
        'ses',
        aws_access_key_id=settings.AWS_ACCESS_KEY_ID,
        aws_secret_access_key=settings.AWS_SECRET_ACCESS_KEY,
        region_name=settings.AWS_SES_REGION_NAME
    )

    try:
        response = ses_client.send_email(
            Source='jonathan.heaney@gmail.com',
            Destination={'ToAddresses': [to_email]},
            Message={
                'Subject': {'Data': subject},
                'Body': {'Text': {'Data': body}}
            }
        )
        return response
    except ClientError as e:
        print(e.response['Error']['Message'])