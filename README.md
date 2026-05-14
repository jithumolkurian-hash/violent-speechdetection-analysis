# AI-Based Analysis of Violent and Threatening Speech

## Overview
This project is based on my Master’s thesis in Information Security at Stockholm University. The goal of the study was to analyze violent and threatening language in online communities and to evaluate how reliable automated systems are in detecting such content.

## Motivation
Automated tools are increasingly used to identify harmful content online. However, their reliability and consistency are not always clear. In this project, I explored how AI based systems behave in practice and whether their outputs can be trusted when applied to real world data.

## Research Questions

To address the main research objective, this study explores the following questions:

- How frequently does violent speech occur on *blackpill.club*?  
- Who are the primary targets of such speech?  
- How severe is the identified violent content?  
- How do ChatGPT and Grok differ in annotating violent speech, and which tool demonstrates higher accuracy and consistency?


### Data Preparation
- Cleaned and preprocessed text data  
- Converted text to lowercase and handled missing values  

## Data Collection and Processing

The dataset used in this study originates from the online forum *blackpill.club*. The original dataset contained over 700,000 posts stored in a compressed JSON (.zst) format. For this research, posts from 2021 to 2024 were selected, resulting in approximately 350,000 comments.

### Data Extraction
A Python-based pipeline was used to:
- Decompress the dataset  
- Extract relevant fields:
  - Post ID  
  - Timestamp  
  - Content (text)  
- Convert the extracted data into a structured format (CSV/Excel) for further analysis  

### Sampling Strategy

The sampling process was conducted in multiple stages:

1. **Initial Random Sampling**
   - 600 comments were randomly selected  
   - Used to estimate the prevalence of violent content  

2. **Keyword-Based Filtering**
   - Comments containing keywords such as *kill*, *murder*, *harm*, and *attack* were extracted  
   - Resulted in 12,445 relevant comments  

3. **Final Sample Selection**
   - Sample size calculated using:
     - 95% confidence level  
     - 3% margin of error  
   - Final dataset: **1,181 comments**

4. **Annotation**
   - Comments were annotated manually  
   - AI-based tools were also used for comparison  

### Summary of Dataset

| Stage | Description | Number of Comments |
|------|------------|------------------|
| Original dataset | All posts | 700,000 |
| Selected timeframe | 2021–2024 | 350,000 |
| Random sample | Initial estimation | 600 |
| Filtered subset | Keyword-based filtering | 12,445 |
| Final dataset | Annotated sample | 1,181 |

> Note: A small sample of the dataset is included in this repository for demonstration purposes.

### AI-Assisted Annotation
I used large language models such as ChatGPT and Grok to classify the same data and compared their outputs with human annotations.

### Analysis
I analyzed differences between:
- Human annotations  
- Rule-based outputs  
- AI-generated classifications  

I also examined how preprocessing and input structure influenced the results.

## Dataset

Due to size limitations, a sample dataset of 100 comments is included in this repository.

- `Sample_raw_data.xlsx` – original comments  
- `annotated_comments_first_100.xlsx` – manually labeled comments  

The full dataset used in the thesis contains approximately 2000 comments.
## Results

### Frequency of Violent Speech

From an initial random sample of 600 comments:
- 52 comments (9%) were identified as violent  
- 548 comments (91%) were non-violent  

Using a keyword-based filtering approach:
- 12,445 comments were identified as potentially violent  
- A manually annotated sample of 1,181 comments showed:
  - 72% were actually violent  
  - 28% were non-violent  

This highlights that keyword-based methods tend to overestimate violent content and require further validation.

---

### Primary Targets of Violent Speech

From the 1,181 annotated comments:
- 851 comments were identified as violent  

The most frequently targeted groups were:

- Women: 294 comments  
- Other groups: 340 comments (~40%)  
- Politicians: 60 comments (~7%)  
- LGBTQ+ individuals: 45 comments (~5%)  
- Non-white individuals: 38 comments (~4%)  
- Jews: 36 comments (~4%)  
- Immigrants: 23 comments (~3%)  
- Muslims: 15 comments (~2%)  

This shows that violent speech is not uniformly distributed but focused on specific groups.

---

### Severity of Violent Speech

Among the 851 violent comments:

- High severity: 312 comments (~37%)  
- Moderate severity: 252 comments (~29%)  
- Low severity: 287 comments (~34%)  

High severity comments often included explicit threats or detailed descriptions of violence, while lower severity comments reflected general hostility without direct threats.

---

### AI Annotation Comparison (ChatGPT vs Grok)

The performance of ChatGPT and Grok was evaluated against human annotations using Krippendorff’s alpha:

#### Full Dataset (1,181 comments)
- ChatGPT vs Human: 0.521  
- Grok vs Human: 0.379  
- ChatGPT vs Grok: 0.602  

#### Smaller Batch Size (25 comments)
- ChatGPT vs Human: 0.708  
- Grok vs Human: 0.512  
- ChatGPT vs Grok: 0.549  

### Key Observations

- ChatGPT showed higher agreement with human annotations compared to Grok  
- Smaller batch sizes improved annotation consistency  
- AI tools were sensitive to input structure and batching  
- Grok occasionally produced less relevant outputs  

These findings highlight important challenges in relying on AI systems for consistent and trustworthy annotation of violent speech.
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

