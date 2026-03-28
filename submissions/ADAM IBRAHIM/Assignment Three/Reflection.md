Why median vs mode  
For continuous variables like Odometer_km, I chose the median because mileage values are skewed and contain extreme outliers. The median is robust to these extremes and gives a more representative central tendency. For discrete variables such as Doors and Accidents, I used the mode since these are categorical counts where the most common value is the most realistic replacement. Using mean would produce non‑integer values that don’t make sense in this context.


Why IQR capping  
Outliers in Price and Odometer_km could distort statistical measures and model training. Instead of removing rows, I applied IQR capping to clip values within reasonable bounds. This preserves dataset size while reducing the influence of extreme values. It balances robustness with completeness, ensuring the dataset remains representative without losing information.


Which features I engineered and why

CarAge = current year – Year: captures how old the car is, a key factor in price.

Km_per_year = Odometer / CarAge: measures usage intensity, providing insight into wear and tear.

Is_Urban = 1 if Location is City/Suburb, else 0: distinguishes urban vs rural environments, which can affect car condition and value.

LogPrice = log(Price+1): created as an alternative target to reduce skewness in the price distribution, making modeling more stable.