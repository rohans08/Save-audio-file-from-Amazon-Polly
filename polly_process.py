#!PATH TO PYTHON INTERPRETER e.g: /usr/local/bin/python3.6
import boto3
import traceback
import json

class Polly:
    _voiceDict  = {'en':{'m': 'Matthew', 'f': 'Joanna'}}
    _access_key = 'AWS_ACCESS_KEY'
    _secret_key = 'AWS_SECRET_KEY'
    _region     = 'SELECTED_REGION_IN_AWS'
    _filePath   = 'PATH_WHERE_AUDIO_WILL_BE_SAVED'
    _fileUrl    = 'URL_TO_SEND_AUDIO_INO_RESPONSE'

    def __init__(self, txt, language, gender):
        self.txt      = txt
        self.language = language
        self.gender   = gender

    def _saveFile(self, filePath, fileName, fileContent):
        try:
            f = open(filePath + fileName + '.mp3','wb')
            f.write(fileContent.read())
            f.close()
            return True
        except Exception as e:
            f = open('log.txt', 'w')
            f.write(str(e))
            f.close()
            return False

    def sendPollyRequest(self):
        response = {}
        response['status'] = False
        fileName = 'USE_LOGIC_AS_PER_REQUIREMENT'
        
        try:
            polly_client = boto3.Session(
                                aws_access_key_id=Polly._access_key,                     
                    aws_secret_access_key=Polly._secret_key,
                    region_name=Polly._region).client('polly')

            responsePolly = polly_client.synthesize_speech(VoiceId=Polly._voiceDict[self.language][self.gender],
                                    OutputFormat='mp3', 
                                    Text = self.txt)

            if (responsePolly['ResponseMetadata']['HTTPStatusCode'] == 200):
                if self._saveFile(Polly._filePath, fileName, responsePolly['AudioStream']):
                    response['status'] = True
                    response['msg'] = 'File saved suucessfully.'
                    response['file'] = Polly._fileUrl + fileName + '.mp3'
                else:
                    response['msg'] = 'File could not be saved.'
            else:
                response['msg'] = 'Could not get Polly to work.'
                response['api_error_no'] = responsePolly.status_code
        except Exception as e:
            f = open('log.txt', 'w')
            f.write(str(e))
            f.write(traceback.format_exc())
            f.close()
            response['msg'] = 'Getting exception'
        
        return json.dumps(response)
