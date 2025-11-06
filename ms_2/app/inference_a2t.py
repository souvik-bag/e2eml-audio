import torch
import librosa
from transformers import WhisperProcessor, WhisperForConditionalGeneration

class AudioToText:
    def __init__(self, model_path: str):
        self.device = "cuda" if torch.cuda.is_available() else "cpu"
        print(f" Using device: {self.device}")

        self.model = WhisperForConditionalGeneration.from_pretrained(
            model_path, local_files_only=True
        ).to(self.device)
        self.processor = WhisperProcessor.from_pretrained(
            model_path, local_files_only=True
        )

    def transcribe(self, audio_input):
        """
        input：
        1. .wav / .mp3
        2. numpy array (raw audio)
        """

        if isinstance(audio_input, str):
            speech, sr = librosa.load(audio_input, sr=16000)
        else:
            speech = audio_input
            sr = 16000

        inputs = self.processor(
            speech,
            sampling_rate=sr,
            return_tensors="pt"
        ).input_features.to(self.device)

        predicted_ids = self.model.generate(inputs)

        transcription = self.processor.batch_decode(predicted_ids, skip_special_tokens=True)
        return transcription[0]


# from transformers import WhisperForConditionalGeneration, WhisperProcessor

# from transformers import pipeline
# import torch
# import os

# class AudioToText:
#     def __init__(self, model_path):
#         self.device = 0 if torch.cuda.is_available() else -1
        
#         self.pipe = pipeline(
#             "automatic-speech-recognition",
#             model=model_path,
#             tokenizer=model_path,
#             feature_extractor=model_path,
#             device=self.device,
#             local_files_only=True
#         )
#         print(f"Loading model from {model_path}...\n\n\n")

#     def transcribe(self, audio_path_or_bytes):
#         """
#         2 types of input:
#         - path: str
#         - raw audio: bytes
#         """
#         if isinstance(audio_path_or_bytes, str) and os.path.exists(audio_path_or_bytes):
#             result = self.pipe(audio_path_or_bytes)
#         else:
#             tmp_path = "tmp_audio.wav"
#             with open(tmp_path, "wb") as f:
#                 f.write(audio_path_or_bytes)
#             result = self.pipe(tmp_path)
#             os.remove(tmp_path)
#         return result["text"]


# from transformers import pipeline
# import torch
# import os

# class AudioToText:
#     def __init__(self, model_path):
#         self.device = 0 if torch.cuda.is_available() else -1
#         # self.pipe = pipeline(
#         #     "automatic-speech-recognition",
#         #     model=model_path,
#         #     device=self.device
#         # )
#         self.pipe = pipeline(
#             "automatic-speech-recognition",
#             model=model_path,
#             tokenizer=model_path,
#             feature_extractor=model_path,
#             device=self.device,
#             local_files_only=True
#         )

#     def transcribe(self, audio_bytes):
#         # save temp audio file
#         tmp_path = "tmp_audio.wav"
#         with open(tmp_path, "wb") as f:
#             f.write(audio_bytes)
#         result = self.pipe(tmp_path)
#         os.remove(tmp_path)
#         return result["text"]
