# %%
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

# %%
print("="*60)
print(" Understanding Outliers")
print("="*60)

# %%
np.random.seed(42)
normal_salaries = np.random.normal(50000,15000,95) # Normal Employees
executive_salaries = np.array([250000,500000,750000,1000000,2000000])
all_salaries = np.concatenate([normal_salaries, executive_salaries])

# %%
print(" Salary Data:")
print(f"    Count: {len(all_salaries)}")
print(f"    Mean: ${all_salaries.mean():,.0f}")
print(f"    Median: ${np.median(all_salaries):,.0f}")
print(f"    Std Dev: ${all_salaries.std():,.0f}")


# %%
print(f"    Mean is ${all_salaries.mean() - np.median(all_salaries):,.0f} higher than the median!")

# %%
# Visualize the problem
fig, axes = plt.subplots(1, 2, figsize=(14, 5))

# Histogram
axes[0].hist(all_salaries, bins=30, color='#2E86AB', edgecolor='black', alpha=0.7)
axes[0].axvline(all_salaries.mean(), color='red', linestyle='--', linewidth=2, label=f'Mean: ${all_salaries.mean():,.0f}')
axes[0].axvline(np.median(all_salaries), color='green', linestyle='--', linewidth=2, label=f'Median: ${np.median(all_salaries):,.0f}')
axes[0].set_title('Salary Distribution with Outliers', fontsize=14, fontweight='bold')
axes[0].set_xlabel('Salary ($M)')
axes[0].set_ylabel('Frequency')
axes[0].legend()
axes[0].grid(True, alpha=0.3)

# Box plot (great for spotting outliers!)
axes[1].boxplot(all_salaries, vert=True)
axes[1].set_title('Box Plot - Outliers Clearly Visible', fontsize=14, fontweight='bold')
axes[1].set_ylabel('Salary ($M)')
axes[1].grid(True, alpha=0.3, axis='y')
axes[1].text(1.15, 2000000, 'Outliers!', fontsize=12, fontweight='bold', 
             bbox=dict(boxstyle='round', facecolor='yellow', alpha=0.7))

plt.tight_layout()
plt.savefig('outliers_visualization.png', dpi=300, bbox_inches='tight')
plt.show()

print("\n✓ Visualization shows outliers clearly!")

# %%
print("\n" + "="*60)
print(" IQR METHOD FOR OUTLIER DETECTION")
print("="*60)

def detect_outliers_iqr(data, column):
    Q1 = data[column].quantile(0.25)
    Q3 = data[column].quantile(0.75)
    IQR = Q3 - Q1
    
    lower_bound = Q1 - (1.5 * IQR)
    upper_bound = Q3 + (1.5 * IQR)
    
    outliers = data[(data[column] < lower_bound) | (data[column] > upper_bound)]
    
    print(f"\n📊 {column} Analysis:")
    print(f"   Q1 (25th percentile): {Q1:,.2f}")
    print(f"   Q3 (75th percentile): {Q3:,.2f}")
    print(f"   IQR: {IQR:,.2f}")
    print(f"   Lower Bound: {lower_bound:,.2f}")
    print(f"   Upper Bound: {upper_bound:,.2f}")
    print(f"   Outliers Found: {len(outliers)} ({len(outliers)/len(data)*100:.1f}%)")
    
    return outliers, lower_bound, upper_bound

# %%
np.random.seed(42)
sales_data = pd.DataFrame({
    'Day': range(1, 101),
    'Sales': np.concatenate([
        np.random.normal(1000,200,95),  #Normal Days
        [5000,6000,7500,8000,10000]     # Black Friday, holidays, etc.
    ])
})

# %%
outliers, lower, upper = detect_outliers_iqr(sales_data, 'Sales')

print(f"\n Outlier Values:")
print(outliers[['Day', 'Sales']].to_string(index=False))

# %%
plt.figure(figsize=(12,6))
plt.scatter(sales_data['Day'], sales_data['Sales'], alpha=0.6, s=50, label='Data Points')
plt.scatter(outliers['Day'], outliers['Sales'], color='red', s=100, label='Outliers')
plt.axhline(upper, color='orange', linestyle='--', linewidth=2, label=f'Upper Bound: ${upper:,.0f}')
plt.axhline(lower, color='orange', linestyle='--', linewidth=2, label=f'Lower Bound: ${lower:,.0f}')
plt.fill_between(sales_data['Day'], lower, upper, alpha=0.2, color='green', label='Normal Range')
plt.title('Sales Data with Outlier Detection (IQR Method)', fontsize=14, fontweight='bold')
plt.xlabel('Day')
plt.ylabel('Sales ($)')
plt.legend
plt.grid(True, alpha=0.3)
plt.tight_layout()
plt.savefig('iqr_outlier_detection.png', dpi=300, bbox_inches='tight')
plt.show()

print("\n Visualization saved!")

# %%
