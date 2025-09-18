
import boto3

class Textract:
    type_extract = 'local'
    path = None
    plaintext = None
    response = None

    def __init__(self, **kwargs) -> None:
        self.textract_client = boto3.client('textract')
        self.type_extract = kwargs.pop('type_extract', None)
        self.path = kwargs.pop('path', None)    

    def _local_extract(self) -> None:
        with open(self.path, 'rb') as image_file:
            image_bytes = bytearray(image_file.read())
            self.response = self.textract_client.detect_document_text(Document={'Bytes': image_bytes})
    
    def _s3_path_info(self):
        if not self.path.startswith('https://') or 'amazonaws.com' not in self.path:
            raise ValueError('Invalid S3 path')
        
        self.path = self.path.replace('https://', '')
        partes_url = self.path.split('/')
        bucket_name = partes_url[0].split('.')[0]
        file_name = partes_url[-1]
        region = partes_url[0].split('.')[2]

        return bucket_name, file_name, region

    def _aws_s3_extract(self) -> None:
        bucket_name, file_name, region = self._s3_path_info()
        self.response = self.textract_client.detect_document_text(
            Document={
                'S3Object': {
                    'Bucket': bucket_name,
                    'Name': file_name
                }
            }
        )

    def get_plaintext(self) -> str:
        if self.response is None:
            return ''
        else:
            text = ''
            for item in self.response['Blocks']:
                if item['BlockType'] == 'LINE':
                    text += item['Text'] + '\n'
            return text

    def extract(self) -> None:
        if self.path is None:
            raise ValueError('Path must be set')
        else:
            if self.type_extract == 'local':
                self._local_extract()
            elif self.type_extract == 's3':
                self._aws_s3_extract()
            else:
                raise ValueError('Invalid type. Must be "local" or "aws"')
        
    