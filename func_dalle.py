import openai

class DALLE:
  # def __init__(self, key: str, api: str, proxy: str) -> None:
  def __init__(self, api, key, version, type) -> None:
        openai.api_type = type
        openai.api_base = api
        openai.api_version = version
        openai.api_key = key

  def generate_images(self, prompt) -> str | False:
    try:
      response = openai.Image.create(
      prompt=prompt,
      size='1024x1024',
      n=1
      )
      image_url = response["data"][0]["url"]
      return image_url
    except Exception as e:
       print(e)
       return False

