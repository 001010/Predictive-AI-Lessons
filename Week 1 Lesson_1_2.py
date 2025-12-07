import numpy as np
import time

print("="*60)
print(" NUMPY SPEED DEMONSTRATION")
print("="*60)

# Test with regular Python lists
size = 1000000
python_list1 = list(range(size))
python_list2 = list(range(size))

start_time = time.time()
python_result = [a + b for a, b in zip(python_list1, python_list2)]
python_time = time.time() - start_time

print(f"\n⏱️  Python Lists: {python_time:.4f} seconds")

# Test with NumPy arrays
numpy_array1 = np.arange(size)
numpy_array2 = np.arange(size)

start_time = time.time()
numpy_result = numpy_array1 + numpy_array2
numpy_time = time.time() - start_time

print(f"⚡ NumPy Arrays: {numpy_time:.4f} seconds")
print(f"\n🚀 NumPy is {python_time/numpy_time:.1f}x FASTER!")
print("\nThis is why we use NumPy for AI/ML work!")