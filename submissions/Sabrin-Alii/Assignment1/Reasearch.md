# Introduction Of Machine Learning



1.Define **Machine Learning** using a real-life example.

Ans: **Machine Learning** is a branch of artificial intelligence,
concerned with the design and development of algorithms that allow
computers to evolve behaviours based on empirical data.

**Machine learning:**  is a subset of artificial intelligence (AI) that
enables computers to learn from data, identify patterns, and make
decisions without being explicitly programmed. It uses algorithms---such
as linear regression, decision trees, or neural networks---to analyze
data, improve performance over time, and predict outcomes. 

**Real world example:** Facial recognition is one of the more obvious
applications of machine learning. People previously received name
suggestions for their mobile photos and Facebook tagging, but now
someone is immediately tagged and verified by comparing and analyzing
patterns through facial contours. And facial recognition paired with
deep learning has become highly useful in healthcare to help detect
genetic diseases or track a patient's use of medication more accurately.
It's also used to combat important social issues such as child sex
trafficking or sexual exploitation of children. The list of applications
and industries influenced by it is steadily on the rise.
## Supervised and UNsupervised learning 
2\. Compare **Supervised Learning** and **Unsupervised Learning**,
giving an example of each.


Ans: As we know supervised and unsupervised machine learning are two
main types machine learning although there is other types pf machine
learning but these two are main types so let's compare these two:

**Supervised learning** is a model trained with labeled data where each
input has a corresponding output. On the other hand, **unsupervised
learning** involves training the model with unlabeled data which helps
to uncover patterns, structures or relationships within the data without
predefined outputs.

**Example of supervised** is: suppose we train the machine by showing it
fruits one by one:

- If the fruit is round, has a small depression at the top and is red,
  it is labeled as an Apple.

<!-- -->

- If the fruit is long, curved and greenish-yellow, it is labeled as a
  Banana.

Now after this training, if we give the machine a new fruit (say a
banana) from the basket and ask it to identify it, the machine will use
what it has learned during training. It will analyze the shape and color
of the new fruit and classify it as a Banana placing it in the correct
category. In this way, the machine learns from the training data (the
basket with labeled fruits) and applies that knowledge to recognize new,
unseen fruits.

**Example of unsupervised is:** Imagine we have a machine learning model
trained on many unlabeled images of dogs and cats. The model has never
seen any labeled example that says "dog" or "cat" before so it doesn't
know how these animals look like.

Now, if we give the model a new image that contains both dogs and cats
it won't be able to directly label them as "dog" or "cat." It will group
parts of the image based on similarities and differences in features
like shape or texture. It might separate the image into two groups one
with dog-like features and other with cat-like features.

This happens because unsupervised learning doesn't rely on prior
knowledge or training with labeled data. It finds patterns and organizes
data on its own helps in discovering information that wasn't given
before.

  -----------------------------------------------------------------------
  **Feature**         **Supervised           **Unsupervised Learning**
                      Learning**             
  ------------------- ---------------------- ----------------------------
  **Data Type**       Uses labeled data      Uses unlabeled data

  **Main Goal**       Predict known outputs  Discover hidden patterns

  **Human             Requires data labeling No labeling required
  Involvement**                              

  **Common Tasks**    Classification,        Clustering, Pattern
                      Regression             discovery

  **Example           Logistic Regression,   K-Means, Hierarchical
  Algorithm**         SVM                    Clustering

  **Real-Life         Medical Diagnosis and     Customer segmentation
  Example**                                  
  -----------------------------------------------------------------------
## Overfitting
3\. What causes **Overfitting**? How can it be prevented?

Ans: Overfitting is a modelling error in statistics that occurs when a
function is too closely aligned to a limited set of data points.

Main causes are:

- **Very complex model** -- too many parameters or layers for a small
  dataset

- **Small training data** -- not enough examples to learn general
  patterns

- **Too many features** -- some features are irrelevant but the model
  still memorizes them

- **Training too long** -- the model keeps fitting noise instead of
  stopping at the right time

- **No regularization** -- nothing limits the model's complexity

The result that comes is **High accuracy on training data** and **Poor
performance on new/unseen data**

**We can prevent as:**

- **Use more data** -- more examples help the model generalize

- **Simplify the model** -- reduce layers, parameters, or features

- **Regularization** -- use techniques like L1 / L2 regularization

- **Early stopping** -- stop training when validation error starts
  increasing

- **Feature selection** -- remove unnecessary or irrelevant features

- **Cross-validation** -- test the model on different data splits

- **Dropout (for neural networks)** -- randomly drop neurons during
  training
## Training Data
4.Explain how **training data** and **test data** are split, and why
this process is necessary.

Ans: **Training data** and **test data** are created by **splitting a
dataset into two parts** so a model can be built and fairly evaluated.

**How Data is Split**

The primary goal of splitting data is to create separate datasets for
the model to learn from and to be evaluated on \[1\]. 

- **Hold-out Method:** This is the simplest and most common method. The
  dataset is randomly partitioned into a training set and a test set
  \[1\].

  - **Training Set:** This data is used to train the machine learning
    model, allowing it to learn the underlying patterns and
    relationships \[2\]. A typical split might allocate 70% to 80% of
    the data for training.

  - **Test Set:** This data, which the model has never seen during
    training, is used to evaluate the model\'s performance on unseen
    data \[1\]. The remaining 20% to 30% of the data is typically used
    for testing.

- **k-Fold Cross-Validation:** This method is used when a simple
  hold-out might lead to an evaluation that is too dependent on the
  specific random split \[2\]. The original dataset is divided into
  \'k\' equal-sized folds. The model is trained k times; each time, one
  fold is used as the test set, and the remaining k-1 folds are used for
  training \[2\]. The results from all k iterations are then averaged to
  provide a more robust evaluation of the model\'s performance \[2\]. 

**Why the Process is Necessary**

The separation of training and test data is crucial for several reasons:

- **Objective Evaluation:** The test set serves as an independent
  benchmark to assess how well the model generalizes to new, unseen data
  \[1, 2\].

- **Avoiding Overfitting:** Overfitting occurs when a model performs
  exceptionally well on the training data but poorly on new data because
  it has essentially memorized the training set\'s specific noise and
  details rather than learning the general patterns \[1, 2\]. By
  evaluating on a separate test set, developers can identify and
  mitigate overfitting.

- **Model Validation:** The process ensures the model is robust and
  reliable, providing a realistic estimate of its accuracy and
  effectiveness in real-world scenarios \[2\]. Without a separate test
  set, one might have an artificially inflated sense of a model\'s
  performance. 

## Case Study
5.Find one **case study** (research paper or article) that explains how
Machine Learning has been applied in healthcare, business, or
transportation. Summarize its findings.



Ans: **Case Study**: ***Supply Chain Optimization in a Logistics
Company***

The title is: ***Leveraging Machine Learning for Business Success: A
Case Study of Supply Chain Optimization in a Logistics Company***

His **background** is: This research paper examines how Machine Learning
was applied to improve the supply chain processes of a logistics
company. In today's business environment, efficiency in delivering
products to customers is crucial, and Machine Learning was used to
perform data-driven analysis to optimize these operations.

***The action was taken:*** The company utilized Machine Learning to:

- Analyze large datasets related to supply, demand, finance, and
  transportation

- Extract hidden insights from data to reduce time and operational costs

- Identify bottlenecks and errors within the supply chain

- Continuously monitor data to enhance managerial decision-making for
  supply chain optimization

> ***How ML was helped by the company*:**

- ML algorithms provided early warnings of potential supply chain issues

- Facilitated analysis of large and complex supply chain datasets

- Resulted in improved decision-making, increased efficiency, and
  reduced operational costs

***Business impact:***

- ML enabled the company to understand hidden patterns in supply chain
  data, leading to better market-aligned decisions

- It not only improved supply chain operations but also enhanced overall
  organizational efficiency

- Data-driven insights allowed the company to better understand customer
  needs, thereby increasing competitiveness in the market

## References:

<https://doi.org/10.62674/ijabmr.2023.v1i01.001>

<https://www.investopedia.com/terms/o/overfitting.asp?utm_source=chatgpt.com>

<https://sis.pitt.edu/jjoshi/courses/IS2955/Fall18/ML_Healthcare.pdf?utm_source=chatgpt.com>

<https://sis.pitt.edu/jjoshi/courses/IS2955/Fall18/ML_Healthcare.pdf?utm_source=chatgpt.com>

<https://sis.pitt.edu/jjoshi/courses/IS2955/Fall18/ML_Healthcare.pdf?utm_source=chatgpt.com>
