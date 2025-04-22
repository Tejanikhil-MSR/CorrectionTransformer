# CorrectionTransformer
This repository provides a lightweight, language‑aware post‑OCR correction module for Telugu text, designed to slot seamlessly between your OCR output and text‑to‑speech (TTS) engine. By automatically detecting and repairing common recognition mistakes it delivers cleaner, more accurate input to your TTS pipeline.

---

## Tokenization
Tokenization is a critical step in training language models. The choice of tokenization strategy impacts the model's ability to generate new words, handle out-of-vocabulary (OOV) terms, and affect the perplexity of generated text. Here’s a breakdown of different tokenization strategies:

### 1. Character-level tokenization:

- Character-level tokenization breaks text into individual characters (including diacritics), enabling the model to generate multiple word or sentence formations.
- It handles out-of-vocabulary (OOV) words efficiently since it learns from basic building blocks.
- However, this method increases sequence length and often requires more model parameters to learn meaningful patterns, especially when training data is limited. This can result in higher perplexity during inference.
- **Example**: "నమస్తే ప్రపంచం" could be tokenized as `['_న', 'మ', 'స', '్', త, 'ే', '▁ప', '్', 'ర', 'ప', 'ం' 'చ', 'ం']`.

### 2. Word-level tokenization:

- Word-level tokenization splits the sentence based on whitespaces.
- While this reduces sequence length and simplifies training, it struggles with OOV words, making it less flexible.
- Also, it requires a large and diverse vocabulary, leading to increased training data and time.
- However, it typically yields lower perplexity during inference for seen words.
- **Example**: "నమస్తే" would be tokenized as `['_నమస్తే']`.

### 3. Subword-level tokenization:

- Subword tokenization offers a balanced approach, breaking words into frequently occurring subword units (e.g., Byte-Pair Encoding or SentencePiece).
- It efficiently handles OOV words and avoids vocabulary explosion while maintaining reasonable perplexity.
- Often used in models like BERT, GPT, and T5.
- **Example**: "నమస్తే ప్రపంచం" → `['▁న', 'మ', 'స్తే', '▁ప్ర', 'పంచం']`.

>> Since the errors are induced at the character and diacritic level, this implementation employs character level tokenization

## Tools for tokenization

Generally the indic language tokenizers are trained for character level tokenization only for the following reasons : 
- Indic languages are highly agglutinative, and subword segmentation can be noisy.
- It's better to model individual aksharas (syllables) or character+diacritic units instead of full words or arbitrary subwords.

### 1. SentencePiece
- This tools is developed by the Google using BPE(`BPE`) and Unigram language model(`ULM`) for creating custom tokenizer based on your dataset. Its simple to use tool for training a custom tokenizer based on the words or vocab present in your custom dataset. 

```python
import sentencepiece as spm

# for training with custom datasets
sp = spm.SentencePieceTrainer.train(input="telugu_corpus.txt", model_prefix="telugu_model", vocab_size=16000)

tokens = sp.encode("నమస్తే ప్రపంచం") # gives ['▁న', 'మ', 'స్తే', '▁ప్ర', 'పంచం'] 
```

### 2. Existing tokenizers
- There are already existing tokenizer that are training on larger vocabularies. Some of them include `ai4bharat/indic-bert`, `ai4bharat/IndicBart`, etc. 

```python
from transformers import AutoTokenizer
tokenizer = AutoTokenizer.from_pretrained("ai4bharat/indic-bert")
tokenizer.tokenize("నమస్తే ప్రపంచం")
```

This works employs already existing tokenizer called `ai4bharat/IndicBART` from hugging face.