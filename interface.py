import gradio as gr
from interference import TextGenerator

def generate_text(prompt):
    generated_text = generator.generate(prompt=prompt)
    return generated_text


generator = TextGenerator()

# Create a Gradio interface
iface = gr.Interface(
    fn=generate_text,
    inputs="text",
    outputs="text",
    title="Text Generator",
    description="Generate text using the PaLM model",
    theme="default",
    layout="vertical",
    allow_screenshot=True,
)

# Launch the interface
iface.launch()