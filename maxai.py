import json
from abc import ABC
from typing import Optional, List, Any

import requests
from langchain_core.callbacks import CallbackManagerForLLMRun
from langchain_core.language_models import LLM


class MaxAi(LLM, ABC):
    model: str = "gpt-4-turbo-preview"
    api_key: str = "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJzdWJqZWN0Ijp7InVzZXJfaWQiOiJjNzBlNDhlYS0zNTBiLTQ1NDgtYTk1Yy0xNDE4MDcyYzkwZjYifSwidHlwZSI6InJlZnJlc2giLCJleHAiOjE3MTU2ODM3MDUsImlhdCI6MTcwNzkwNzcwNSwianRpIjoiN2M2YTZmNDgtYzhkZC00MjgwLTllZWMtMzEwMTEyYTgyZjdkIn0.hVEzUjH8tNx4queHcRVepBxz9HdzxhfEGIE0TqbU-hk"

    def _llm_type(self):
        return "maxai"

    def _call(
            self,
            prompt: str,
            stop: Optional[List[str]] = None,
            run_manager: Optional[CallbackManagerForLLMRun] = None,
            **kwargs: Any,
    ) -> str:
        print(prompt)
        headers = {
            "Authorization": f"Bearer {self.api_key}",
            "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36"
        }
        data = {"chat_history": [], "streaming": True, "message_content": [{"type": "text", "text": prompt}],
                "chrome_extension_version": "3.0.0", "model_name": "gpt-4-turbo-preview", "prompt_id": "chat",
                "prompt_name": "chat", "temperature": 0.1}
        response = requests.post("https://api.maxai.me/gpt/get_chatgpt_response", json=data, stream=True,
                                 headers=headers)
        res = ""
        for i in response.iter_lines():
            if i.startswith(b'data: '):
                print(json.loads(i.decode("utf-8").replace('data: ', ''))['text'], end="")
                res += json.loads(i.decode("utf-8").replace('data: ', ''))['text']
        return res
