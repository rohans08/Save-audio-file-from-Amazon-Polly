# Save-audio-file-from-Amazon-Polly

Introduction
  This is a simple API which fetches mp3 audio from Amazon Polly, saves it onto the server and sends the information as JSON response. It is built using Python language(Python3.6) and uses Python's simple web interface.

Pre-requisite
  1) AWS Account with Access Key, Secret Key, Region
  2) Python3.6
  3) Boto3 installed into the server.
  4) BeautifulSoup(optional if there is html tags in the text)
  
Usage
  There are two files present - polly_process.py and get-audio.py.
  1) polly_process.py - It is a module which uses Amazon's boto client to call Polly api with text, language, voice as parameters. You need to set the AWS_ACCESS_KEY, AWS_SECRET_KEY AND REGION. You also need to set file path where audio will be saved and url where audio will be accessed. URL is optional and it will depend on your requirement whether you want to send full url or filename. Filename is also subjected to logic you wwant to implement as per your requirement.
  
  2) get-audio.py -  It is the file which you will make call to with required parameters. It uses polly_process module to get the information and serve it to the caller.
  
Note: This example is shown with mp3 files and english language. Amazon Polly supports other audio formats and languages as well. Please refer to Amazon Polly docs for reference.
