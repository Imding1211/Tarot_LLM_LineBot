import ollama
import re

def AI_response(question):

  response = ollama.chat(model='gemma2:2b', messages=[
    {
      'role': 'user',
      'content': f'用繁體中文並在100-150字內回答以下問題:{question}',
    },
  ])

  return response['message']['content']


def remove_emojis(text):

    emoji_pattern = re.compile(
      "["
      u"\U0001F600-\U0001F64F"  # emoticons
      u"\U0001F300-\U0001F5FF"  # symbols & pictographs
      u"\U0001F680-\U0001F6FF"  # transport & map symbols
      u"\U0001F1E0-\U0001F1FF"  # flags (iOS)
      "]+", flags=re.UNICODE)

    return emoji_pattern.sub(r'', text)


def generate_response(question):

  answer = AI_response(question)

  answer = remove_emojis(answer)

  return answer


if __name__ == "__main__":

  question = input()

  ans = generate_response(question)

  print(ans)