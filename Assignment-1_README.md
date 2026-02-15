# Assignment-1

**Anand Mishra**\
**Submission Date: January 19, 2026**

------------------------------------------------------------------------

## Academic Integrity Notice

This assignment has been implemented entirely from scratch using only
Python standard libraries, as required in the problem statement.\
No external NLP, ML, or third-party libraries were used in Problems
1--3.\
All algorithms, preprocessing logic, and probability computations were
manually implemented to demonstrate conceptual understanding.

------------------------------------------------------------------------

# Overview

This assignment consists of four independent problems covering:

1.  Rule-Based Conversational Agent (Regex Only)
2.  Byte Pair Encoding Tokenization
3.  Naive Bayes Sentiment Classification
4.  Sports vs. Politics Document Classification (Comparative ML Study)

Each problem strictly follows the constraints mentioned in the
assignment guidelines.

------------------------------------------------------------------------

# PROBLEM 1 -- Regex-Based Conversational Assistant

### File:

`b23cm1028prob1.py`\
`b23cm1028prob1.log`\
`b23cm1028prob1.txt`

### Objective:

Extend a toy regex-based chatbot to:

-   Extract surname from full name\
-   Accept multiple birthday formats and compute age\
-   Detect mood and respond appropriately\
-   Handle minor spelling variations\
-   Demonstrate multiple execution runs

### Implementation Details:

-   Uses only:
    -   `import re`
    -   `from datetime import date`
-   Supports formats such as:
    -   dd-mm-yyyy
    -   mm-dd-yyyy
    -   dd Month YYYY
    -   dd-mm-yy (2-digit year normalization)
-   Age calculation adjusts if birthday has not occurred yet this year.
-   Mood detection uses regex keyword matching.
-   Minor spelling variations handled via flexible pattern matching.

### Log File:

`b23cm1028prob1.log` contains multiple chatbot sessions including:

-   Textual and numeric date formats
-   Uppercase inputs
-   Typographical errors
-   Failure cases (invalid dates, ambiguous inputs)

### Reflection File:

`b23cm1028prob1.txt` discusses:

-   Naturalness of rule-based interaction
-   Strengths of regex systems
-   Limitations such as negation handling and semantic understanding

------------------------------------------------------------------------

# PROBLEM 2 -- Byte Pair Encoding (BPE) Tokenizer

### File:

`b23cm1028prob2.py`

### Objective:

Implement Byte Pair Encoding from scratch.

### Execution:

    python b23cm1028prob2.py corpus.txt [K]

### Key Features:

-   Reads corpus line-by-line
-   Initializes vocabulary as character-level tokens
-   Computes pair frequencies
-   Iteratively merges most frequent pairs (K merges)
-   Uses only:
    -   collections
    -   re
    -   sys

No external tokenization library used.

------------------------------------------------------------------------

# PROBLEM 3 -- Naive Bayes Sentiment Classifier

### File:

`b23cm1028prob3.py`

### Objective:

Build a sentiment classifier using Naive Bayes from scratch.

### Training Data:

-   pos.txt (positive sentences)
-   neg.txt (negative sentences)

### Implementation Details:

-   Whitespace tokenization
-   Lowercasing
-   Laplace smoothing
-   Log-probability computation for numerical stability
-   Interactive prediction mode after training

### Execution:

    python b23cm1028prob3.py

After training, the system accepts user input and predicts: - POSITIVE -
NEGATIVE

No ML or NLP libraries used.

------------------------------------------------------------------------

# PROBLEM 4 -- Sports vs Politics Classification

### Files:

-   Machine Learning implementation (custom vectorizer + classifiers)
-   Final_Rewritten_Document_Classification_Report.pdf

### Objective:

Design a classifier to categorize news articles as: - SPORTS - POLITICS

### Feature Engineering:

A custom Bag-of-Words vectorizer was built:

-   Lowercase normalization
-   Removal of non-alphabetic characters
-   Vocabulary construction from training data
-   Count-based vector encoding

### Algorithms Compared:

1.  Multinomial Naive Bayes (Laplace smoothing, log-space)
2.  Logistic Regression (Batch Gradient Descent)
3.  K-Nearest Neighbors (Euclidean distance, k=5)

### Evaluation:

-   80/20 train-test split
-   Comparative analysis of:
    -   Accuracy
    -   Training speed
    -   Prediction speed
    -   Performance in high-dimensional sparse space

### Report Includes:

-   Data collection methodology
-   Dataset analysis
-   Mathematical background
-   Quantitative comparisons
-   Limitations of Bag-of-Words representation
-   Scalability concerns

------------------------------------------------------------------------

# Execution Requirements

All Python programs are executable via terminal:

    python b23cm1028prob1.py
    python b23cm1028prob2.py corpus.txt
    python b23cm1028prob3.py

No external dependencies are required beyond Python standard library.

------------------------------------------------------------------------

# Submission Structure

The final zip file should contain:

-   b23cm1028prob1.py
-   b23cm1028prob1.log
-   b23cm1028prob1.txt
-   b23cm1028prob2.py
-   b23cm1028prob3.py
-   b23cm1028prob4.pdf

------------------------------------------------------------------------

# Final Remarks

This assignment demonstrates:

-   Understanding of regex-based systems
-   Implementation of subword tokenization algorithms
-   Probabilistic modeling using Naive Bayes
-   Comparative machine learning analysis
-   Manual implementation without relying on high-level libraries

All components were built from foundational principles to ensure clarity
of understanding and originality.
