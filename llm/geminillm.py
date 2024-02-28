from abc import ABC
from typing import Optional, List, Any

import google.generativeai as genai
from langchain_core.callbacks import CallbackManagerForLLMRun
from langchain_core.language_models import LLM

from config.config import GEMINI_TOKEN


class GeminiLLm(LLM, ABC):
    model: str = "gemini-1.5-pro"
    api_key: str = GEMINI_TOKEN

    def _llm_type(self):
        return "gemini"

    def _call(
            self,
            prompt: str,
            stop: Optional[List[str]] = None,
            run_manager: Optional[CallbackManagerForLLMRun] = None,
            **kwargs: Any,
    ) -> str:
        print(prompt)
        genai.configure(api_key=self.api_key)
        model = genai.GenerativeModel(self.model)
        response = model.generate_content(prompt, stream=True, generation_config={
            'temperature': 0.1
        })
        res = ""
        for i in response:
            print(i.text, end="")
            res += i.text
        return res
