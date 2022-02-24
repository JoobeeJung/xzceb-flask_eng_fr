"""
This file translates lang to lang
"""

import os
from ibm_watson import LanguageTranslatorV3
from ibm_cloud_sdk_core.authenticators import IAMAuthenticator
from dotenv import load_dotenv

load_dotenv()

apikey = os.environ['apikey']
url = os.environ['url']

authenticator = IAMAuthenticator(apikey)
language_translator = LanguageTranslatorV3(
    version='2018-05-01',
    authenticator=authenticator
)

language_translator.set_service_url('https://api.us-south.language-translator.watson.cloud.ibm.com')

def english_to_french(english_text):
    """
    This function translates engish to french
    """

    if english_text == '':
        french_text = ''
    else:
        french_text=language_translator.translate(
        text=english_text , model_id='en-fr').get_result()
        french_text = french_text['translations'][0]['translation']
    return french_text

def french_to_english(french_text):
    """
    This function translates french to english
    """
    if french_text == '':
        english_text = ''
    else:
        english_text=language_translator.translate(
        text=french_text , model_id='fr-en').get_result()
        english_text = english_text['translations'][0]['translation']
    return english_text
