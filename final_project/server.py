from machinetranslation import translator
from flask import Flask, render_template, request
import json
import machinetranslation
from translator import french_to_english, english_to_french

app = Flask("Web Translator")

@app.route("/englishToFrench")
def englishToFrench_server():
    textToTranslate = request.args.get('textToTranslate')
    # Write your code here
    result_ef = english_to_french(textToTranslate)
    return result_ef

@app.route("/frenchToEnglish")
def frenchToEnglish_server():
    textToTranslate = request.args.get('textToTranslate')
    result_fe = french_to_english(textToTranslate)
    return result_fe

@app.route("/")
def renderIndexPage():
    return "Render Index Page"

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8080)
