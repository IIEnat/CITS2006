# AI-Powered IDS

One of the state-of-the-art solutions in cybersecurity is the use of AI to help make IDS predictions better and more accurate. Unlike traditional IDS, which rely on static rule sets or known attack signatures, AI-powered systems are able to learn patterns of normal behavior and identify deviations that may indicate new or unknown threats. These systems often analyze massive amounts of data in real-time, using machine learning models trained to recognize attacker behaviors such as lateral movement, privilege escalation, or data exfiltration. AI helps by reducing false positives and prioritizing the most serious alerts, allowing security teams to focus on real threats instead of sifting through irrelevant noise.

A well-known example of this is Vectra AI, which uses a technology called Attack Signal Intelligence to detect and respond to attacks across cloud, data center, and enterprise networks. Vectra’s platform is designed to improve Extended Detection and Response (XDR) by providing real-time analysis and threat prioritization.

However, I will be implementing a much simpler version of this. My IDS uses a simple machine learning technique to assess network traffic. This IDS is an extended version of the one I created for the second lab quiz. 

## About My Program

Use the following command to run it in the terminal: 
```
python3 IDS.py
```

This program uses a pipeline of preprocessing steps and machine learning to classify network traffic as either **normal** or **anomalous**. Below is a breakdown of how it works:

### 1. **Data Preprocessing**

#### - **Numeric Data Standardization**
Numeric columns are standardized using the Z-Score formula. This converts the data to represent how many standard deviations each value is from the mean, ensuring consistency across different scales.

#### - **Categorical Data Encoding**
Categorical columns are converted into numerical format using **One-Hot Encoding**. For example:
- `tcp` might be encoded as `[0, 0, 1]`
- `udp` might be encoded as `[1, 0, 0]`

This ensures that categorical values can be used by machine learning algorithms.

#### - **Combining Preprocessed Data**
Both the standardized numeric data and the one-hot encoded categorical data are combined into a single matrix that represents the entire dataset in numerical form.

### 2. **Model Training**
A **Random Forest Classifier** with 100 trees is used to train the model. The classifier builds multiple decision trees by finding the best split points (cutoffs) in the data that separate normal traffic from anomalous traffic. 

For example, if the Z-Scores for a feature are:
```
[-1.5, -0.8, -0.2, 0.3, 0.9]
```
The cutoffs tested would be:
- -1.15
- -0.5
- 0.05
- 0.6

Each tree evaluates these cutoffs to build a model that can classify the data. The forest then uses **majority voting** across all trees to make a final decision.

### 3. **Train-Test Split**
The dataset is split into **70% training** and **30% testing**, with stratification to maintain the same class distribution in both sets.

### 4. **Evaluation**
After training, the model is tested on the 30% of the data not used for training. The following metrics are calculated:
- **Accuracy**
- **Precision**
- **Recall**
- **F1 Score**
- **Confusion Matrix (TP, TN, FP, FN Counts)**

## About Test Data

Included in this repository is a file named **`big_dataset.csv`**, which simulates random network traffic. The dataset contains **25,192 entries**, with **7,558** entries used for testing (30%).

The dataset **`big_dataset.csv`** was created by combining all the datasets provided during the second lab quiz along with the test data used in the demo.

## Sample Output
```
Accuracy : 0.9930 → 7505 out of 7558 packets correctly classified
Precision: 0.9949 → 3488 of 3506 predicted anomalous were actually anomalous
Recall   : 0.9901 → 3488 of 3523 actual anomalous packets were correctly detected
F1 Score : 0.9925 → harmonic mean of precision and recall
Counts   : TP=3488, TN=4017, FP=18, FN=35
```


