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
I am currently developing the project of Concept of mine further with a few more upgrade of my own. You can be assure to get some amazing features from this side-project of mine in the coming weeks
