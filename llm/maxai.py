import json
from abc import ABC
from typing import Optional, List, Any

import requests
from langchain_core.callbacks import CallbackManagerForLLMRun
from langchain_core.language_models import LLM

from config.config import MAX_AI_TOKEN


class MaxAi(LLM, ABC):
    model: str = "gpt-4-turbo-preview"
    api_key: str = MAX_AI_TOKEN

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
            "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36",
            "Cookie": "_ga_98QRV9PQP6=GS1.1.1707907672.2.1.1707908586.0.0.0",
            "Origin": "chrome-extension://mhnlakgilnojmhinhkckjpncpbhabphi"
        }
        data = {"chat_history": [], "streaming": True, "message_content": [{"type": "text", "text": prompt}],
                "chrome_extension_version": "3.0.0", "model_name": self.model, "prompt_id": "chat",
                "prompt_name": "chat", "temperature": 0.1, "regenerate": False}
        url = {
            "gpt-4-0125-preview": "get_chatgpt_response",
            "gpt-4-turbo-preview": "get_chatgpt_response",
            "gpt-4": "get_chatgpt_response",
            "mistral-7b-instruct": "get_freeai_chat_response",
            "claude-2": "get_claude_response",
        }
        response = requests.post(f"https://api.maxai.me/gpt/{url[self.model]}", json=data, stream=True,
                                 headers=headers)
        res = ""
        for i in response.iter_lines():
            if i.startswith(b'data: '):
                print(json.loads(i.decode("utf-8").replace('data: ', ''))['text'], end="")
                res += json.loads(i.decode("utf-8").replace('data: ', ''))['text']
        return res
