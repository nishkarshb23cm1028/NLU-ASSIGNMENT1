# Assignment-1

**Name:** Nishkarsh Verma\
**Roll Number:** B23CM1028

------------------------------------------------------------------------

## Declaration

I confirm that this assignment has been implemented entirely by me using
only Python standard libraries, as required.\
All algorithms were written from scratch without using any external NLP
or machine learning libraries.\
The work follows the naming conventions and submission guidelines
provided in the assignment document.

------------------------------------------------------------------------

# Assignment Overview

This assignment consists of four problems covering:

1.  Regex-based Chatbot Extension\
2.  Byte Pair Encoding Tokenization\
3.  Naive Bayes Sentiment Classification\
4.  Sports vs Politics Document Classification (Comparative Study)

All problems were implemented according to the constraints mentioned in
the instructions.

------------------------------------------------------------------------

# PROBLEM 1 -- REGGY++ (Regex-Based Chatbot)

### Files Submitted:

-   B23CM1028_prob1.py\
-   B23CM1028_prob1.log\
-   B23CM1028_prob1.txt

### Description:

The chatbot was extended using only: - `import re` -
`from datetime import date`

### Functionalities Implemented:

1.  Birthday Extraction & Age Calculation
    -   Supports multiple formats:
        -   dd-mm-yyyy\
        -   mm-dd-yyyy\
        -   dd Month yyyy\
        -   Two-digit year formats\
    -   Computes age dynamically.
2.  Mood Detection
    -   Uses regex keyword matching.\
    -   Handles minor spelling variations.\
    -   Responds appropriately to positive and negative sentiments.
3.  Surname Detection
    -   Extracts last name from full name input.
4.  Multiple Execution Runs
    -   Log file demonstrates:
        -   Different date formats\
        -   Typographical errors\
        -   Invalid date handling\
        -   Ambiguous inputs

### Reflection:

The reflection file discusses: - Naturalness of regex-based systems\
- Strengths (speed, predictability)\
- Limitations (context blindness, negation issues)

------------------------------------------------------------------------

# PROBLEM 2 -- Byte Pair Encoding (BPE)

### File:

-   B23CM1028_prob2.py

### Execution:

    python B23CM1028_prob2.py corpus.txt

### Implementation Details:

-   Vocabulary initialized at character level.
-   Iteratively merges most frequent symbol pairs.
-   Merge count K configurable.
-   Implemented fully from scratch.
-   Only standard libraries used.

------------------------------------------------------------------------

# PROBLEM 3 -- Naive Bayes Sentiment Classifier

### File:

-   B23CM1028_prob3.py

### Execution:

    python B23CM1028_prob3.py

### Implementation Details:

-   Whitespace tokenization\
-   Lowercase normalization\
-   Laplace smoothing\
-   Log-space probability computation\
-   Interactive prediction mode after training

Model predicts: - POSITIVE\
- NEGATIVE

No external ML libraries were used.

------------------------------------------------------------------------

# PROBLEM 4 -- Sports vs Politics Classification

### File:

-   B23CM1028_prob4.pdf

### Description:

A binary classifier was designed to classify news articles as: - SPORTS\
- POLITICS

### Feature Representation:

-   Custom Bag-of-Words implementation\
-   Vocabulary built from training data\
-   Count-based vector encoding

### Algorithms Compared:

1.  Multinomial Naive Bayes\
2.  Logistic Regression (Batch Gradient Descent)\
3.  K-Nearest Neighbors (k=5, Euclidean distance)

### Report Includes:

-   Data collection methodology\
-   Dataset filtering and sampling\
-   Text preprocessing steps\
-   Algorithm explanations\
-   Quantitative comparison\
-   Limitations and scalability discussion

------------------------------------------------------------------------

# Submission Checklist

The final zip file:\
`B23CM1028_A1.zip`

Contains:

-   B23CM1028_prob1.py\
-   B23CM1028_prob1.log\
-   B23CM1028_prob1.txt\
-   B23CM1028_prob2.py\
-   B23CM1028_prob3.py\
-   B23CM1028_prob4.pdf

------------------------------------------------------------------------

# Deadline

February 15, 2026 (Firm Deadline)

------------------------------------------------------------------------

# Final Note

This assignment demonstrates:

-   Understanding of regular expressions\
-   Implementation of subword tokenization\
-   Probabilistic modeling\
-   Comparative machine learning evaluation

All components were implemented independently to reflect conceptual
clarity and originality.
