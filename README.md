# CSV to SQL Insert Script

This script reads CSV files from a specified directory and generates SQL `INSERT` statements for each CSV file into `csv-files` directory. The generated SQL scripts are saved in a specified output directory (`sql-files`). 

## Usage

1. **Place your CSV files** in the `csv-files` directory. Each CSV file should have a `.csv` extension.

2. **Run the script** to generate SQL `INSERT` statements:
    ```sh
    python generate_inserts.py
    ```

3. **Find the generated SQL files** in the `sql-files` directory. Each SQL file will be named after the corresponding CSV file.

4. NOTE: table names for INSERT statement will be based on file name.

## Example

If you have a CSV file named `users.csv` in the `csv-files` directory, running the script will generate a file named `users.sql` in the `sql-files` directory with the corresponding `INSERT` statements.

## Script Details

The script performs the following steps:

1. Ensures the output directory (`sql-files`) exists.
2. Iterates over all CSV files in the `csv-files` directory.
3. For each CSV file:
    - Reads the file and generates `INSERT` statements based on the CSV content.
    - Writes the `INSERT` statements to a corresponding SQL file in the `sql-files` directory.
4. Prints a success message for each processed CSV file.

## Requirements

- Python 3.x

## Notes

- The script assumes that the first row of each CSV file contains the column headers.
- All values in the CSV files are treated as strings and are enclosed in single quotes in the generated SQL statements.

## License

This project is licensed under the MIT License.
