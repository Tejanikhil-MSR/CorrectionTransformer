# CorrectionTransformer
This repository provides a lightweight, language‑aware post‑OCR correction module for Telugu text, designed to slot seamlessly between your OCR output and text‑to‑speech (TTS) engine. By automatically detecting and repairing common recognition mistakes it delivers cleaner, more accurate input to your TTS pipeline.

---

## Table of Contents

1. Features  
2. Installation  
3. Usage  
4. Text Correction  
   - Tokenization  
     1. Character‑level  
     2. Word‑level  
     3. Subword‑level  
   - Tools for Tokenization  
     1. SentencePiece  
     2. Existing Tokenizers  
5. Configuration  
6. Modes  
7. Contributing  
8. License

---

## Features

- **Diacritic Restoration**: Reattach missing or misplaced matras for accurate syllables.  
- **Character‑Swap Corrections**: Fix visually similar glyph confusions using frequency‑based heuristics and a compact language model.  
- **Missing‑Glyph Recovery**: Infer and reinstate dropped characters by analyzing surrounding context.  
- **Contextual Homograph Disambiguation**: Use POS tags and a pronunciation lexicon to select correct phonetic forms.  
- **Lightweight & Customizable**: Pure Python, minimal dependencies, configurable thresholds, and extendable lexicon.  
- **Batch & Real‑Time**: Support for bulk processing and low‑latency single‑utterance correction.

---

## Installation

```bash
pip install telugu-ocr-fixer
```

---

## Usage

```python
from telugu_ocr_fixer import Corrector

fix = Corrector(config_path="config.yaml")
cleaned_text = fix.process(raw_ocr_text)
# Pass `cleaned_text` into your TTS engine
```

---

## Text Correction

### Tokenization  
Tokenization is critical for training language models. The chosen strategy affects word‑generation capability, handling of out‑of‑vocabulary (OOV) terms, and model perplexity. Below are three common strategies:

#### 1. Character‑level tokenization  
- **Description**: Splits text into individual characters (including diacritics).  
- **Pros**:  
  - Handles OOV words natively.  
  - Enables model to generate novel word forms.  
- **Cons**:  
  - Longer sequences; more parameters needed.  
  - Higher perplexity with limited data.  
- **Example**:  
  ```
  "నమస్తే ప్రపంచం" →
  ['న', 'మ', 'స', '్', 'త', 'ే', '▁', 'ప', '్', 'ర', 'ప', 'ం', 'చ', 'ం']
  ```

#### 2. Word‑level tokenization  
- **Description**: Splits on whitespace.  
- **Pros**:  
  - Shorter sequences; simpler training.  
  - Lower perplexity on seen words.  
- **Cons**:  
  - Poor OOV handling.  
  - Large vocabulary requirements.  
- **Example**:  
  ```
  "నమస్తే ప్రపంచం" → ['నమస్తే', 'ప్రపంచం']
  ```

#### 3. Subword‑level tokenization  
- **Description**: Breaks words into frequent subword units (e.g., BPE, Unigram).  
- **Pros**:  
  - Handles OOV efficiently.  
  - Balances vocabulary size and sequence length.  
- **Cons**:  
  - Can be noisy on agglutinative scripts.  
- **Example**:  
  ```
  "నమస్తే ప్రపంచం" →
  ['▁న', 'మ', 'స్తే', '▁ప్ర', 'పంచం']
  ```

> **Note:** Since OCR errors occur at the character/diacritic level, this implementation uses **character‑level tokenization**.

---

### Tools for Tokenization

Indic languages are agglutinative; modeling character+diacritic units (aksharas) is often preferable.

#### 1. SentencePiece  
Google’s tool supporting BPE and Unigram LM. Train on your Telugu corpus:

```python
import sentencepiece as spm

# Train
spm.SentencePieceTrainer.train(
    input="telugu_corpus.txt",
    model_prefix="telugu_model",
    vocab_size=16000
)

# Encode
sp = spm.SentencePieceProcessor(model_file="telugu_model.model")
tokens = sp.encode("నమస్తే ప్రపంచం")
print(tokens)  # ['▁న', 'మ', 'స్తే', '▁ప్ర', 'పంచం']
```

#### 2. Existing Tokenizers  
Hugging Face offers pretrained Indic tokenizers. Example:

```python
from transformers import AutoTokenizer

tokenizer = AutoTokenizer.from_pretrained("ai4bharat/indic-bert")
print(tokenizer.tokenize("నమస్తే ప్రపంచం"))
```

This work leverages the `ai4bharat/IndicBART` tokenizer.

---

## Configuration

Customize `config.yaml` to adjust error‑thresholds, add domain terms, or extend the lexicon.

---

## Modes

- **Batch Mode**: Process large document sets.  
- **Real‑Time Mode**: Low‑latency correction for live applications.

---

## Contributing

1. Fork the repo  
2. Create a feature branch  
3. Submit a pull request  

---

## License

MIT License. See [LICENSE](LICENSE) for details.