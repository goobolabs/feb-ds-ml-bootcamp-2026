# 🎓 Assignment 6: Customer Segmentation Report
**By: Atika Isse Ali**

### 1. What I did in this Project 🛠️
For this assignment, I analyzed how customers spend money based on their annual income. I started by cleaning the data and filling any missing values with the median. I then scaled the features using StandardScaler so that the "Income" numbers (which are large) wouldn't overwhelm the "Spending Score" (which is small). Finally, I used the K-Means algorithm to group the customers into clusters.

### 2. Why I chose K=5 🎯
I ran an Elbow Check from $k=1$ to $10$. Looking at my results:
* **SSE:** My SSE dropped from 400.00 down to **65.57** at $k=5$. After 5, the drop became very small, which means 5 is the "Elbow" or the perfect point.
* **Metrics:** I got a **Silhouette Score of 0.555** and a **Davies-Bouldin index of 0.572**. These numbers prove that the 5 groups are well-separated and not overlapping.

### 3. Understanding the Customer Groups 🧠
Based on my Cluster Centers, here is how I describe the 5 types of customers:

* **Cluster 0 (The Middle Class):** Income ~$55k, Spending ~49. These are average earners and average spenders. 
  * *Action:* Send them standard monthly newsletters.
* **Cluster 1 (The VIPs):** Income ~$86k, Spending ~82. These are the best customers because they have money and love to spend it.
  * *Action:* **Target them for luxury VIP events.**
* **Cluster 2 (The Big Spenders):** Income ~$25k, Spending ~79. They don't earn much but they spend a lot. 
  * *Action:* Send them "buy now, pay later" or credit offers.
* **Cluster 3 (The Careful Wealthy):** Income ~$88k, Spending ~17. They have high income but spend very little. 
  * *Action:* Focus on "Value for Money" luxury ads to encourage them to spend.
* **Cluster 4 (The Budgeters):** Income ~$26k, Spending ~20. Low income and low spending.
  * *Action:* Send them discount coupons to get them through the door.

### 4. Limitations & Next Steps 🚀
The main limitation is that we only used two numbers (Income and Spending). I think adding **Age** would be very helpful because younger people might spend differently than older people. My next step would be to try 3 features or use **DBSCAN** to see if there are any "weird" customers who don't fit into these 5 groups.