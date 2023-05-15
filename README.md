# PaLM
<img src="./palm.gif" width="450px"></img>

Google PaLM mode was recently made public via Bard Chatbot. Before that, we saw some early model architecture from Phil Wang. Recently, Conceptofmind came out with a trained version of PaLM architecture on state of the art dataset. 

Unfortunately, in their repository they did not include any one line method to access the model rather a command line approach was taken in their original interference.py file. Which, I think, is not ideal for developers and limits the capabilities on what can be done using the model. 

Which is why, I rewrote the interference.py file to generate text in a single line and included a gradio interface. 

###### load the model
```Python
git clone https://github.com/conceptofmind/PaLM.git
cd PaLM/
pip3 install -r requirements.txt
```

Generate text
```Python
from interference import TextGenerator

generator = TextGenerator()
user_prompt = input("Enter your text prompt: ")
generated_text = generator.generate(prompt=user_prompt)
for text in generated_text:
    print(text)
```

###### Running the gradio interface
```run the interface.py file```

###### Citation
https://github.com/conceptofmind/PaLM

##### Status
I am currently developing the project of conceptofmind further with a few more upgrade of my own. You can be assure to get some amazing features from this side-project of mine in the coming weeks

###### Update
1. Currently, fine-tuning is not possible **(technically)** as in the original repository of conceptofmine, cofig file was not provided by default and you can only load the model itself. Which makes the task a bit tricky. Why? In the original repository, conceptofmind used `gpt-neox-20b` tokenizer and loading this model on Google Colab or even locally is a big task for both hardware and disk space. If a different model is used such as gpt-neo-1.3b, it'll produce a mismatch error.
  Now, what's the solution? If you have enough space, you can load the model `gpt-neox-20b` and start fine-tuning otherwise, you have to change the default     tokenizer in train file, re-train, save and fine-tune. 

2. I have added a `train` folder which can be used to train PaLM model on T4 GPU with give/take 12-16 GB of RAM. In the train folder I simply changed a few lines of code and modified a few more of the original `train_distrubuted.py` file. 
3. this repo can be installed using pip using the command `pip install git+https://github.com/sleepingcat4/PaLM.git`
