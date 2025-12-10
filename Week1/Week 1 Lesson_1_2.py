import numpy as np

print("="*60)
print(" PRACTICE: CUSTOMER PURCHASE ANALYSIS")
print("="*60)

# Create sample customer data
np.random.seed(42)
num_customers = 100

# Customer purchase amounts ($)
purchases = np.random.uniform(20, 500, size=num_customers)

ages = np.random.randint(18, 70, size=num_customers)

items = np.random.randint(1, 20, size=num_customers)

print(f"\n📊 Analyzing {num_customers} customers...")

# YOUR TASKS:
# 1. Calculate average purchase amount
avg_purchase = np.mean(purchases)
print(f"\n1️⃣Average Purchase: ${avg_purchase:.2f}")

# 2. Find customers who spent more than $300 (high-value customers)
high_value = purchases > 300
num_high_value = np.sum(high_value)
high_value_avg = np.mean(purchases[high_value])
print(f"\n2️⃣ High-Value Customers (>$300):")
print(f"   Count: {num_high_value}")
print(f"   Avg Spend: ${high_value_avg:.2f}")

# 3. Calculate average spend by age group
young = (ages >= 18) & (ages < 30)
middle = (ages >= 30) & (ages < 50)
older = (ages >= 50)

print(f"\n3️⃣ Average Spend by Age Group:")
print(f"   18-29: ${np.mean(purchases[young]):.2f} ({np.sum(young)} customers)")
print(f"   30-49: ${np.mean(purchases[middle]):.2f} ({np.sum(middle)} customers)")
print(f"   50+:   ${np.mean(purchases[older]):.2f} ({np.sum(older)} customers)")

# 4. Find correlation between items purchased and total spend
correlation = np.corrcoef(items, purchases)[0, 1]
print(f"\n4️⃣ Correlation (items vs spend): {correlation:.3f}")
if correlation > 0.5:
    print("   ✓ Strong positive correlation - more items = higher spend")
elif correlation > 0.3:
    print("   ~ Moderate correlation")
else:
    print("   ✗ Weak correlation")
    
# 5. Identify top 10 customers
top_10_indices = np.argsort(purchases)[-10:]
top_10_amounts = purchases[top_10_indices]
print(f"\n5️⃣ Top 10 Customers")
for i, (idx, amount) in enumerate(zip(top_10_indices, top_10_amounts), 1):
    print(f"   #{i}: Customer {idx} - ${amount:.2f}")
    
print("\n" + "="*60)
print(" ANALYSIS COMPLETE!")
print("="*60)