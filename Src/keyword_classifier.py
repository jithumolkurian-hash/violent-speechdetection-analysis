import pandas as pd
import re

# Load dataset
def load_data(file_path):
    try:
        df = pd.read_csv(file_path, encoding='ISO-8859-1', delimiter=";", on_bad_lines='skip')
        df.columns = df.columns.str.strip().str.lower()
        return df
    except Exception as e:
        print("Error loading CSV:", e)
        return None

# Preprocess text
def preprocess_text(df):
    df['text'] = df['text'].fillna('').astype(str)
    df['cleaned_text'] = df['text'].str.lower()
    return df

# Keyword lists
violent_keywords = ["kill", "murder", "torture", "destroy", "death", "stab", "shoot"]
threatful_keywords = ["harm", "attack", "danger", "threat", "target", "injure", "strike"]

# Categorization function
def categorize_comment(text):
    def match_keywords(keywords):
        return any(re.search(r'\b' + re.escape(word) + r'\b', text) for word in keywords)

    if match_keywords(violent_keywords):
        return 'violent'
    elif match_keywords(threatful_keywords):
        return 'threatful'
    else:
        return 'uncategorized'

# Main pipeline
def main():
    df = load_data("extracted_data(Sheet1).csv")
    if df is None:
        return

    df = preprocess_text(df)

    df['category'] = df['cleaned_text'].apply(categorize_comment)

    # Filter categories
    violent_comments = df[df['category'] == 'violent']
    threatful_comments = df[df['category'] == 'threatful']

    # Save results
    violent_comments.to_csv('violent_comments.csv', index=False)
    threatful_comments.to_csv('threatful_comments.csv', index=False)

    print("\n--- Category Summary ---")
    print(df['category'].value_counts())

if __name__ == "__main__":
    main()
