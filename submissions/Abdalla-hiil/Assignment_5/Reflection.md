# My Project Report: Catching spam Emails

## 1. What did I do?

I built a system to help a computer separate "Good Emails" (Ham) from "Junk Emails" (Spam). I used three different "AI Brains" to see which one was the smartest:

1. **Logistic Regression** (It weighs words like a scale).
2. **Random Forest** (It acts like a group of people voting on the answer).
3. **Naive Bayes** (It counts how often words appear in junk mail).

I fed the computer a list of thousands of emails. I used a tool called `TF-IDF` which is just a fancy way of saying: "Make the important words stand out and ignore the boring words like 'the' or 'is'."

## 2. All about "Naive Bayes"

**What is it?**
Think of Naive Bayes like a child learning about fruit. If most red things the child sees are apples, the child decides: "If it is red, it is probably an apple." Naive Bayes looks at an email and says: "If this has the word 'FREE' and 'WINNER,' there is a very high chance it is junk."

**Why use it for junk mail?**

* It is **super fast**. It doesn't need to think hard.
* It is great for text because it is very good at spotting "bad" words.

**The Good and the Bad:**

* **The Good:** It works even if you don't have a lot of data.
* **The Bad:** it is a bit "simple." It doesn't understand that words work together in pairs. It just looks at each word one by one.

## 3. Comparing the 3 Brains (The Test)

I gave the models three test sentences to see if they could guess correctly.
One message was: *"Congratulations, you won a free ticket."*

* **Did they agree?** Yes! All three models said this was "Ham" (Good Mail).
* **Was that right?** Even though "free ticket" sounds like a scam, the models were being very careful. They don't want to accidentally delete a real email you might need. They prefer to stay safe.

## 4. The Scores (How they performed)

I looked at the "Report Card" for each model:

* **Accuracy:** This is the total grade. **Random Forest** got the highest grade (**98.3%**).
* **Precision:** This asks: "When the AI says it's Junk, is it telling the truth?" My models were **100%** truthful! They never called a good email "Junk."
* **Recall:** This asks: "Did you catch ALL the junk?" This is where the models struggled. They caught most of it, but some junk still got through.

**The Confusion Matrix:**
This is just a table that shows the AI's mistakes.

* **False Positive:** This is a **bad mistake**. It’s when the AI puts a message from your mom in the Junk folder. My models made **zero** mistakes like this!
* **False Negative:** This is an **annoying mistake**. It’s when a junk email about a "Free Prize" shows up in your Inbox. My models made about **36** mistakes like this.

## 5. My Final Choice
**My Choice:** I recommend **Random Forest**. It was the most accurate and caught the most junk mail. It is better to have a slightly slower "brain" that catches more junk than a fast one that misses everything!