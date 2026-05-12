# AI-Based Analysis of Violent and Threatening Speech

## Overview
This project is based on my Master’s thesis in Information Security at Stockholm University. The goal of the study was to analyze violent and threatening language in online communities and to evaluate how reliable automated systems are in detecting such content.

## Motivation
Automated tools are increasingly used to identify harmful content online. However, their reliability and consistency are not always clear. In this project, I explored how AI based systems behave in practice and whether their outputs can be trusted when applied to real-world data.

## What I Did
- Collected and analyzed over 1000 online comments  
- Performed manual annotation to create a reference dataset  
- Used AI-based tools (e.g., ChatGPT and Grok) for automated annotation  
- Built a rule-based classifier using Python and regex  
- Compared human annotations with AI-generated outputs  
- Investigated inconsistencies in classification results  

## Methodology

### Data Preparation
- Cleaned and preprocessed text data  
- Converted text to lowercase and handled missing values  

### Baseline Approach (Keyword-Based Classification)
As an initial step, I implemented a rule-based classifier using keyword matching to detect:
- Violent content (e.g., "kill", "murder", "shoot")  
- Threatening content (e.g., "attack", "harm", "threat")  

This served as a simple baseline for comparison.

### AI-Assisted Annotation
I used large language models such as ChatGPT and Grok to classify the same data and compared their outputs with human annotations.

### Analysis
I analyzed differences between:
- Human annotations  
- Rule-based outputs  
- AI-generated classifications  

I also examined how preprocessing and input structure influenced the results.

## Key Findings
- AI-generated outputs were sometimes inconsistent  
- Small changes in input formatting affected results  
- Keyword-based methods failed to capture context  
- Dataset bias influenced classification performance  
- Human annotation remains important for evaluation  

## Technologies Used
- Python  
- Pandas, NumPy  
- Regular Expressions (Regex)  
- Basic NLP techniques  

## Limitations
- Keyword-based classification cannot understand context  
- AI outputs depend on input structure  
- Limited dataset size  

## Future Work
- Apply machine learning models for classification  
- Improve preprocessing techniques  
- Extend to cybersecurity applications such as threat detection  
- Explore methods for verifying AI outputs  

## Author
**Jithumol Kurian**

