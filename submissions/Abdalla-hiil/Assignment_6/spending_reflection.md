What did I do?
In this project, I acted like a detective for a store. I looked at how much money people make and how much they like to spend. I used a tool called K-Means Clustering to put these people into "friendship groups" based on their habits. First, I cleaned the data and made all the numbers the same size (scaling). Then, I let the computer group them together.

Why did I pick K=3?
I looked at the "SSE" numbers. It's like a game: as you add more groups, the error goes down. However, after K=3, the error didn't drop very fast anymore. My Silhouette Score was also good, which tells me the groups are spread out and not messy or overlapping.

Explaining the Groups
Group 0 (High Income / Low Spending): These people are "Savers." They have a lot of money but don't buy much.

Idea: Show them high-quality, long-lasting items that are worth the investment.

Group 1 (Low Income / High Spending): These are "Fans." They love shopping even if they don't earn much.

Idea: Offer them "buy now, pay later" options or special coupons.

Group 2 (High Income / High Spending): These are "VIPs." They have the money and they love to shop.

Idea: Invite them to a special "Gold Member" event with free snacks and early access to new items.

What's next?
Right now, we only know about money. But what if we knew their Age? A 20-year-old and a 70-year-old might spend money very differently!
Next Step: I want to try adding a third piece of information, like how many times they visit the store each month, to make the groups even more accurate.