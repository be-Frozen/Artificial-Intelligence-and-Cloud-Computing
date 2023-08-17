import numpy as np
import sys

def main():
    data_portion = float(sys.argv[1])
    total_numbers = 100000
    numbers_per_container = int(total_numbers * data_portion)
    
    data = np.arange(1, total_numbers + 1)
    data_chunk = data[(numbers_per_container * int(sys.argv[2])): (numbers_per_container * (int(sys.argv[2]) + 1))]
    
    sum_result = np.sum(data_chunk)
    avg_result = np.mean(data_chunk)
    max_result = np.max(data_chunk)
    min_result = np.min(data_chunk)
    std_dev_result = np.std(data_chunk)
    
    print(f"Data Portion: {data_portion}")
    print(f"Sum: {sum_result}")
    print(f"Average: {avg_result}")
    print(f"Max: {max_result}")
    print(f"Min: {min_result}")
    print(f"Standard Deviation: {std_dev_result}")

if __name__ == "__main__":
    main()