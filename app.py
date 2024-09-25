from mlx_lm import load, generate

class InferlessPythonModel:
    def initialize(self):
        self.model, self.tokenizer model, tokenizer = load("mlx-community/Phi-3.5-MoE-instruct-8bit")
         

    def infer(self, inputs):
        response = generate(model, tokenizer, prompt="hello", verbose=True)
        return {'generated_result': response }

    def finalize(self):
        pass
