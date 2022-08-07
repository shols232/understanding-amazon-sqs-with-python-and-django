import json
import boto3

from rest_framework.views import APIView
from rest_framework.response import Response
from .models import File

session = boto3.Session(
    aws_access_key_id='<AWS_ACCESS_KEY_ID>',
    aws_secret_access_key='<AWS_SECRET_ACCESS_KEY>',
)
sqs = session.resource('sqs', region_name='<AWS_REGION_NAME>')


class FileView(APIView):
    """
    Process file and saves its data.
    :param file_path: path to file.
    :return: status
    """
    def post(self, request):
        file_path = request.data.get('file_path')
        file_obj = File.objects.create(file_path=file_path) # save file unprocessed.
        
        # Get our recently created queue.
        queue = sqs.get_queue_by_name(QueueName="MyFileProcessingQueue.fifo")
        message_body = {
            'file_id': str(file_obj.id)
        }

        # Send a message to the queue, so we can process this particular file eventually.
        response = queue.send_message(
            MessageBody=json.dumps(message_body),
            MessageGroupId='messageGroupId'
        )

        # Let the user know the file has been sent to queue and is PENDING processing.
        return Response({"message": "File has been scheduled for processing..."}, status=200)
        

