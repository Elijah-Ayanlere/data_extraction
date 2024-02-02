# Weather Analysis using Pandas and NumPy

This Python script analyzes weather data from a CSV file using the Pandas and NumPy libraries. The analysis focuses on precipitation values and performs various statistical calculations.

## Requirements

- Python 3.x
- Pandas (`pip install pandas`)
- NumPy (`pip install numpy`)

## Setup

1. **CSV File:**
   - Ensure you have the weather data CSV file (e.g., 'BicycleWeather.csv') in the specified path.
   - Adjust the file path in the `pd.read_csv()` function if needed.

2. **Dependencies:**
   - Install the required Python packages using the following commands:
     ```
     pip install pandas
     pip install numpy
     ```

3. **Run the Script:**
   - Run the script using Python:
     ```
     python weather_analysis.py
     ```

## Analysis Steps

1. **Read CSV File and Extract PRCP Column:**
   - Reads the CSV file using Pandas and extracts the 'PRCP' column.

2. **Convert PRCP Column to NumPy Array:**
   - Converts the 'PRCP' column to a NumPy array for numerical operations.

3. **Separate Numbers from NaN:**
   - Separates numbers from NaN (missing values) in the PRCP array.

4. **Separate Zeros and Non-Zeros:**
   - Separates zeros and non-zeros from the non-NaN values using boolean masking.

5. **Modify Non-Zeros:**
   - Multiplies every value in the non-zeros array by 100 and divides by 250.

6. **Calculate Statistics:**
   - Calculates various statistics such as median precipitation on rainy days, median precipitation on non-zero days, maximum precipitation on all days, and median precipitation on non-zero rainy days.

7. **Print Results:**
   - Prints the calculated statistics.

## Usage

1. Run the script, ensuring the CSV file is in the correct path.
2. Review the printed statistics based on the weather data analysis.

## Note

- This script is a basic example of weather data analysis and is intended for educational purposes.
- Adapt and customize the script for more complex analyses or use it as a starting point for your projects.

For any questions or issues, please refer to the Pandas and NumPy documentation or seek assistance from the community.
