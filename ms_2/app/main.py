from fastapi import FastAPI, UploadFile, File
from inference_a2t import AudioToText
from inference_t2s import TextToSentiment
import os

app = FastAPI()

A2T_MODEL_PATH = os.getenv("A2T_MODEL_PATH")
T2S_MODEL_PATH = os.getenv("T2S_MODEL_PATH")

a2t = AudioToText(A2T_MODEL_PATH)
t2s = TextToSentiment(T2S_MODEL_PATH)

@app.post("/predict")
async def predict(audio: UploadFile = File(...)):
    temp_path = f"/tmp/{audio.filename}"
    with open(temp_path, "wb") as f:
        f.write(await audio.read())

    transcript = a2t.transcribe(temp_path)

    sentiment = t2s.predict(transcript)

    os.remove(temp_path)

    return {"transcript": transcript, "sentiment": sentiment}

# from fastapi import FastAPI, UploadFile
# from inference_a2t import AudioToText
# from inference_t2s import TextToSentiment
# import os

# app = FastAPI()

# A2T_MODEL_PATH = os.getenv("A2T_MODEL_PATH")
# T2S_MODEL_PATH = os.getenv("T2S_MODEL_PATH")

# a2t = AudioToText(A2T_MODEL_PATH)
# t2s = TextToSentiment(T2S_MODEL_PATH)

# @app.post("/predict")
# async def predict(audio: UploadFile):
#     transcript = a2t.transcribe(await audio.read())
#     sentiment = t2s.predict(transcript)

#     return {
#         "transcript": transcript,
#         "sentiment": sentiment
#     }



# # main.py
# from fastapi import FastAPI, UploadFile, File, Form
# from inference import SpeechToEmotionPipeline
# import tempfile
# import os

# app = FastAPI(title="Speech Emotion Recognition API")

# a2t_key_default = "wav2vec2"
# a2t_precision_default = "fp32"
# t2s_key_default = "distilbert"
# t2s_precision_default = "fp32"
# pipeline = SpeechToEmotionPipeline(a2t_key_default, a2t_precision_default,
#                                    t2s_key_default, t2s_precision_default)


# @app.get("/")
# def root():
#     return {"message": f"Speech-to-emotion service ready (default model={a2t_key_default}-{a2t_precision_default}; {t2s_key_default}-{t2s_precision_default}.)"}


# @app.post("/predict/")
# async def predict_audio(
#     file: UploadFile = File(...),
#     a2t_key: str = Form("wav2vec2"),
#     a2t_precision: str = Form("fp32"),
#     t2s_key: str = Form("distilbert"),
#     t2s_precision: str = Form("fp32"),
# ):
#     """
#     t2s keys:
#     - distilbert
#     - roberta
#     - twitter
#     """
#     # save audio to file
#     with tempfile.NamedTemporaryFile(delete=False, suffix=".wav") as tmp:
#         contents = await file.read()
#         tmp.write(contents)
#         tmp_path = tmp.name

#     # change default pipeline if needed
#     if a2t_key != a2t_key_default \
#         or a2t_precision != a2t_precision_default \
#         or t2s_key != t2s_key_default \
#         or t2s_precision != t2s_precision_default:
#         pipeline = SpeechToEmotionPipeline(a2t_key, a2t_precision,
#                                            t2s_key, t2s_precision)
#     else:
#         pipeline = pipeline

#     # inference
#     result = pipeline.predict_from_audio(tmp_path)

#     # remove audio file
#     os.remove(tmp_path)

#     return result
