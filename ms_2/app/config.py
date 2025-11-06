a2t_model_names = {
    "whisper": {
        "name": "AventIQ-AI/whisper-audio-to-text",
        "precision": {
            "fp32": "./models/a2t_AventIQ-AI_whisper-audio-to-text_fp32",
            "fp16": "./models/a2t_AventIQ-AI_whisper-audio-to-text_fp16",
            "int8": "./models/a2t_AventIQ-AI_whisper-audio-to-text_int8",
        }
    }
}

t2s_model_names = {
    "distilbert": {
        "name": "distilbert-base-uncased-finetuned-sst-2-english",
        "ps": [
            "/models/t2s_distilbert-base-uncased-finetuned-sst-2-english_fp32.onnx",
            "/models/t2s_distilbert-base-uncased-finetuned-sst-2-english_fp16.onnx",
            "/models/t2s_distilbert-base-uncased-finetuned-sst-2-english_int8.onnx",
        ],
        "precision": {
            "fp32": "./models/t2s_distilbert-base-uncased-finetuned-sst-2-english_fp32.onnx",
            "fp16": "./models/t2s_distilbert-base-uncased-finetuned-sst-2-english_fp16.onnx",
            "int8": "./models/t2s_distilbert-base-uncased-finetuned-sst-2-english_int8.onnx",
        }
    },
    "roberta": {
        "name": "siebert/sentiment-roberta-large-english",
        "ps": [
            "/models/t2s_siebert_sentiment-roberta-large-english_fp32.onnx",
            "/models/t2s_siebert_sentiment-roberta-large-english_fp16.onnx",
            "/models/t2s_siebert_sentiment-roberta-large-english_int8.onnx",
        ],
        "precision": {
            "fp32": "./models/t2s_siebert_sentiment-roberta-large-english_fp32.onnx",
            "fp16": "./models/t2s_siebert_sentiment-roberta-large-english_fp16.onnx",
            "int8": "./models/t2s_siebert_sentiment-roberta-large-english_int8.onnx",
        },
    },
    "twitter": {
        "name": "cardiffnlp/twitter-roberta-base-sentiment-latest",
        "ps": [
            "/models/t2s_cardiffnlp_twitter-roberta-base-sentiment-latest_fp32.onnx",
            "/models/t2s_cardiffnlp_twitter-roberta-base-sentiment-latest_fp16.onnx",
            "/models/t2s_cardiffnlp_twitter-roberta-base-sentiment-latest_int8.onnx",
        ],
        "precision": {
            "fp32": "./models/t2s_cardiffnlp_twitter-roberta-base-sentiment-latest_fp32.onnx",
            "fp16": "./models/t2s_cardiffnlp_twitter-roberta-base-sentiment-latest_fp16.onnx",
            "int8": "./models/t2s_cardiffnlp_twitter-roberta-base-sentiment-latest_int8.onnx",
        }
    }
}