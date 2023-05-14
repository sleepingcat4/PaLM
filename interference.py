import torch
from transformers import AutoTokenizer
from einops._torch_specific import allow_ops_in_compiled_graph
import argparse


class TextGenerator:
    def __init__(self, model_name="palm_1b_8k_v0"):
        self.model_name = model_name
        self.device = torch.device("cuda" if torch.cuda.is_available() else "cpu")
        self.dtype = torch.float32

    def generate(self, prompt, seq_len=256, temperature=0.8, filter_thres=0.9):
        allow_ops_in_compiled_graph()
        torch.hub._validate_not_a_forked_repo = lambda a, b, c: True

        model = torch.hub.load("conceptofmind/PaLM", self.model_name).to(self.device).to(self.dtype)
        opt_model = torch.compile(model, backend="hidet")

        tokenizer = AutoTokenizer.from_pretrained("EleutherAI/gpt-neox-20b")

        encoded_text = tokenizer(prompt, return_tensors="pt")

        output_tensor = opt_model.generate(
            seq_len=seq_len,
            prompt=encoded_text["input_ids"].to(self.device),
            temperature=temperature,
            filter_thres=filter_thres,
            pad_value=0.0,
            eos_token=tokenizer.eos_token_id,
            return_seq_without_prompt=False,
            use_tqdm=True,
        )

        decoded_output = tokenizer.batch_decode(output_tensor, skip_special_tokens=True)

        return decoded_output