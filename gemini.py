from abc import ABC
from typing import Optional, List, Any

import google.generativeai as genai
from langchain_core.callbacks import CallbackManagerForLLMRun
from langchain_core.language_models import LLM


class GeminiLLm(LLM, ABC):
    # model: str = "gemini-pro"
    model: str = "gemini-ultra"
    api_key: str = "AIzaSyCZDJnxfGT_QoxlkwFlRaWlAyrCi8VWBoI"

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
        model = genai.GenerativeModel('gemini-pro')
        response = model.generate_content(prompt, stream=True, generation_config={
            'temperature': 1
        })
        res = ""
        for i in response:
            res += i.text
        return res
