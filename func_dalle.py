import openai

class DALLE:
  # def __init__(self, key: str, api: str, proxy: str) -> None:
  def __init__(self, api, key, version, type) -> None:
        self.api_type = type
        self.api_base = api
        self.api_version = version
        self.api_key = key

  def generate_images(self, prompt):
    try:
      response = openai.Image.create(
      prompt=prompt,
      size='1024x1024',
      n=1,
      api_type = self.api_type,
      api_base = self.api_base,
      api_version = self.api_version,
      api_key = self.api_key,
      )
      image_url = response["data"][0]["url"]
      return image_url
    except Exception as e:
       print(e)
       return False

