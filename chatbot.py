import openai
import os
import sys

try:
  openai.api_key = os.environ['OPENAI_API_KEY']
except KeyError:
  sys.stderr.write("""
  You haven't set up your API key yet.
  
  If you don't have an API key yet, visit:
  
  https://platform.openai.com/signup

  1. Make an account or sign in
  2. Click "View API Keys" from the top right menu.
  3. Click "Create new secret key"

  Then, open the Secrets Tool and add OPENAI_API_KEY as a secret.
  """)
  exit(1)

question = input("\nAsk your question:\n")
response = openai.ChatCompletion.create(
  model="gpt-3.5-turbo",
 and nothing else  messages=[{
    "role":
    "system",
    "content":
    "You are a teacher, you can answer questions which are related to school subjects, if something else is asked, you should tell them that you can't answer it."
  }, {
    "role": "user",
    "content": f"{question}"
  }])

print(response.choices[0].message.content)
