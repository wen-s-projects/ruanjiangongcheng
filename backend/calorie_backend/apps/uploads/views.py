from rest_framework import viewsets, status
from rest_framework.decorators import action
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from django.conf import settings
import boto3
from botocore.client import Config
from datetime import datetime, timedelta
import os


class UploadViewSet(viewsets.ViewSet):
    permission_classes = [IsAuthenticated]

    def get_s3_client(self):
        s3_endpoint = os.getenv('S3_ENDPOINT')
        s3_access_key = os.getenv('S3_ACCESS_KEY')
        s3_secret_key = os.getenv('S3_SECRET_KEY')
        s3_region = os.getenv('S3_REGION', 'us-east-1')
        s3_bucket = os.getenv('S3_BUCKET')

        s3_config = {
            'region_name': s3_region,
            'aws_access_key_id': s3_access_key,
            'aws_secret_access_key': s3_secret_key,
        }

        if s3_endpoint:
            s3_config['endpoint_url'] = s3_endpoint
            s3_config['config'] = Config(signature_version='s3v4')

        return boto3.client('s3', **s3_config), s3_bucket

    @action(detail=False, methods=['post'])
    def presigned(self, request):
        filename = request.data.get('filename')
        content_type = request.data.get('contentType')

        if not filename or not content_type:
            return Response({'error': '缺少必要参数'}, status=status.HTTP_400_BAD_REQUEST)

        s3_client, bucket = self.get_s3_client()
        key = f"uploads/{datetime.now().timestamp()}-{filename}"

        try:
            url = s3_client.generate_presigned_url(
                'put_object',
                Params={
                    'Bucket': bucket,
                    'Key': key,
                    'ContentType': content_type
                },
                ExpiresIn=600  # 10分钟
            )
            return Response({'url': url, 'key': key})
        except Exception as e:
            return Response({'error': str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)

    @action(detail=False, methods=['post'])
    def complete(self, request):
        key = request.data.get('key')

        if not key:
            return Response({'error': '缺少key参数'}, status=status.HTTP_400_BAD_REQUEST)

        try:
            result = self.process_image(key)
            return Response({'ok': True, 'result': result})
        except Exception as e:
            return Response({'error': str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)

    def process_image(self, key):
        s3_client, bucket = self.get_s3_client()

        try:
            response = s3_client.get_object(Bucket=bucket, Key=key)
            image_data = response['Body'].read()

            from PIL import Image
            import io

            img = Image.open(io.BytesIO(image_data))
            img.thumbnail((200, 200))

            thumb_buffer = io.BytesIO()
            img.save(thumb_buffer, format='JPEG')
            thumb_buffer.seek(0)

            thumb_key = key.replace('.', '-thumb.')
            s3_client.put_object(
                Bucket=bucket,
                Key=thumb_key,
                Body=thumb_buffer,
                ContentType='image/jpeg'
            )

            return {'thumb_key': thumb_key}
        except Exception as e:
            raise Exception(f'图片处理失败: {str(e)}')
