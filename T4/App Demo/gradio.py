from transformers import pipeline
from klaam import SpeechClassification
from transformers import AutoProcessor, AutoModelForSpeechSeq2Seq

import gradio as gr
import random
import Post_Tweet
import numpy as np
import torch
import torch.nn as nn

# PyTorch model
class Multiclass(nn.Module):
    def __init__(self):
        super().__init__()
        self.hidden = nn.Linear(4, 8)
        self.act = nn.ReLU()
        self.output = nn.Linear(8, 3)
        self.logsoftmax = nn.LogSoftmax(dim=1)
 
    def forward(self, x):
        x = self.act(self.hidden(x))
        x = self.logsoftmax(self.output(x))
        return x
 
model = Multiclass()
# asr = pipeline("automatic-speech-recognition", "facebook/wav2vec2-base-960h")
# classifier = pipeline("text-classification")
classes = ['نجدية','شرقية','غربية','شمالية','جنوبية']
dialect_dic = {
    'Hijazi':'H',
    'Najdi':'N',
    'Tunisian': 'T',
    'Egyptian': 'E'
}
def speech_to_text(speech):
    # text = asr(speech)["text"]
    # Use a pipeline as a high-level helper

    pipe = pipeline("automatic-speech-recognition", model="Seyfelislem/whisper-medium-arabic")
    # Load model directly
    processor = AutoProcessor.from_pretrained("Seyfelislem/whisper-medium-arabic")
    model = AutoModelForSpeechSeq2Seq.from_pretrained("Seyfelislem/whisper-medium-arabic")
    print(pipe(speech))
    return pipe(speech)


def classify_dialect(text, option):
    # return dialect_dic[option]
    from transformers import pipeline
    classifier = pipeline("zero-shot-classification",
                        model="morit/arabic_xlm_xnli", max_length=128)
    result = classifier(
        text,
        candidate_labels=["مصري"," حجازي","نجدي","تونسي"],
    )
    print(result)
    index = result['scores'].index(max(result['scores']));
    print(result['labels'][index])
    return result['labels'][index]

def PostTweet(text):
    Post_Tweet.post_tweet({"text": text})

def predict(input):
    with torch.no_grad():
        output = model(input)
        predicted_class = torch.argmax(output).item()
        return predicted_class
    

try:
    with gr.Blocks(title="Saudi Dialect")as demo:
        gr.Markdown("Saudi Dialect App")

        label = gr.Label("Saudi Dialect App")
        dropdown_option = gr.Dropdown(
                    ['حجازي' , 'نجدي', 'تونسي','مصري'], label="Dialect", info="How would you like to convert the Dialect to?"
                ),
        with gr.Tab("Text"):
            text = gr.Textbox() 
            classify_text_button = gr.Button("Classify text")
            classify_text_button.click(classify_dialect, inputs=text, outputs=label)
        with gr.Tab("publish the campaign"):
            publish_tweet = gr.Button("Publish the campaign")
            publish_tweet.click(PostTweet, inputs=text, outputs=label)
except Exception as ee:
    print("Error", ee)

if __name__ == "__main__":
    # Create new model and load states
    speech_model = SpeechClassification()
    # model = Multiclass()
    # model.load_state_dict(torch.load("bert_model_with_info.pth",map_location=torch.device('cpu')))
    # model.eval()
    demo.launch()