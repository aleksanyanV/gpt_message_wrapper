import os
import requests
from dotenv import load_dotenv

load_dotenv()


class MessageService:

    @staticmethod
    def process_message(data):
        user_id = data['user_id']
        message = data['message']
        msg_id = data['msg_id']

        prompt_message = f"Simon says {message}, answer please"

        try:
            chatgpt_response = MessageService.send_to_chatgpt(prompt_message)
        except Exception as e:
            return {
                "user_id": user_id,
                "message": str(e),
                "msg_id": f"{msg_id}_resp"
            }

        return {
            "user_id": user_id,
            "message": chatgpt_response,
            "msg_id": f"{msg_id}_resp"
        }

    @staticmethod
    def send_to_chatgpt(prompt):
        api_key = os.getenv('OPENAI_API_KEY')
        if not api_key:
            raise Exception("API key not found in environment variables.")

        headers = {
            'Authorization': f'Bearer {api_key}',
            'Content-Type': 'application/json',
        }
        payload = {
            "model": "gpt-3.5-turbo",
            "messages": [{"role": "system", "content": prompt}]
        }
        response = requests.post(
            "https://api.openai.com/v1/chat/completions",
            headers=headers,
            json=payload
        )
        response_json = response.json()

        if "error" in response_json:
            raise Exception(response_json["error"]["message"])

        return response_json['choices'][0]['message']['content']
