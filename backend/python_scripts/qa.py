#!/usr/bin/python3.6

import sys
import spacy
import urllib
import requests
from bs4 import BeautifulSoup
from transformers import pipeline

question = sys.argv[1]
# Recherche GOOGLE
# desktop user-agent
USER_AGENT = "Mozilla/5.0 (Macintosh; Intel Mac OS X 10.14; rv:65.0) Gecko/20100101 Firefox/65.0"
# mobile user-agent
MOBILE_USER_AGENT = "Mozilla/5.0 (Linux; Android 7.0; SM-G930V Build/NRD90M) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/59.0.3071.125 Mobile Safari/537.36"

URL = f"https://google.com/search?q={question}"

headers = {"user-agent": USER_AGENT}
resp = requests.get(URL, headers=headers)

texts = []

if resp.status_code == 200:
    soup = BeautifulSoup(resp.content, "html.parser")

    # Get First Block (Petit encadré au dessus de tout, en general des journaux)
    for g in soup.find_all('span', class_="hgKElc"):
      texts.append(g.text)

    # Get Wikipedia block (Petit encadré sur le coté)
    for g in soup.find_all('div', class_="Kot7x"):
      texts.append(g.find_all('span')[0].text)

    # Get all sites descriptions
    for g in soup.find_all('div', class_='uUuwM'): # data-content-feature="1" dans une div, peut etre mieux ?
      texts.append(g.text)
else:
  print("Google respond " + str(resp.status_code))

# Répondre a la question d'apres les texts (si trouve pas de reponse adequate pour le premier texte, essaye le suivant)
nlpqa = pipeline('question-answering', model='etalab-ia/camembert-base-squadFR-fquad-piaf', tokenizer='etalab-ia/camembert-base-squadFR-fquad-piaf')

if len(texts) <= 0:
  print("No text found")
else:
  responses = []
  for t in texts:
    if not t:
      continue
    responses.append(nlpqa(question=question, context=t))

  final = responses[0]

  for r in responses:
    # print(r)
    if r['score'] > final['score']:
      final = r

  result = final['answer']

  # Format result
  result = result.strip(" ,.;:")
  result = result[0].upper() + result[1:] + "."

  # Show result
  print(u"" + result)