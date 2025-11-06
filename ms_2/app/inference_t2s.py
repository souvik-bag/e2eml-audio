import onnxruntime as ort
import numpy as np
from transformers import AutoTokenizer

from config import t2s_model_names

class TextToSentiment:
    def __init__(self, model_path):
        self.model_path = model_path
        for _, v in t2s_model_names.items():
            if model_path in v['ps']:
                self.model_name = v['name']
        self.tokenizer = AutoTokenizer.from_pretrained(self.model_name)
        self.session = ort.InferenceSession(model_path)

    def predict(self, text):
        inputs = self.tokenizer(text, return_tensors="np", padding=True, truncation=True)
        outputs = self.session.run(None, {
            self.session.get_inputs()[0].name: inputs["input_ids"],
            self.session.get_inputs()[1].name: inputs["attention_mask"]
        })
        probs = np.exp(outputs[0]) / np.sum(np.exp(outputs[0]))
        label = "POSITIVE" if probs[0][1] > 0.5 else "NEGATIVE"
        return {"label": label, "confidence": float(probs[0][1])}

