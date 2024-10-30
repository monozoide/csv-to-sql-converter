# CSV and JSON to SQL Insert Script

This project contains scripts to read CSV and JSON files from specified directories and generate SQL `INSERT` statements. The generated SQL scripts are saved in a specified output directory (`sql-files`).

## Usage

### CSV Files

1. **Place your CSV files** in the `csv-files` directory. Each CSV file should have a `.csv` extension.

2. **Run the script** to generate SQL `INSERT` statements:

   ```sh
   python csv_generate_inserts.py
   ```

3. **Find the generated SQL files** in the `sql-files` directory. Each SQL file will be named after the corresponding CSV file.

4. NOTE: Table names for `INSERT` statements will be based on the file name.

### JSON Files

1. **Place your JSON files** in the `json-files` directory. Each JSON file should have a `.json` extension.

2. **Run the script** to generate SQL `INSERT` statements:

   ```sh
   python json_generate_inserts.py
   ```

3. **Find the generated SQL files** in the `sql-files` directory. Each SQL file will be named after the corresponding JSON file.

4. NOTE: Table names for `INSERT` statements will be based on the file name.

## Example

### CSV Example

If you have a CSV file named `users.csv` in the `csv-files` directory, running the script will generate a file named `users.sql` in the `sql-files` directory with the corresponding `INSERT` statements.

### JSON Example

If you have a JSON file named `products.json` in the `json-files` directory, running the script will generate a file named `products.sql` in the `sql-files` directory with the corresponding `INSERT` statements.

## Script Details

The scripts perform the following steps:

1. Ensure the output directory (`sql-files`) exists.
2. Iterate over all files in the respective directories (`csv-files` or `json-files`).
3. For each file:
   - Read the file and generate `INSERT` statements based on the content.
   - Write the `INSERT` statements to a corresponding SQL file in the `sql-files` directory.
4. Print a success message for each processed file.

## Requirements

- Python 3.x

## Notes

- The scripts assume that the first row of each CSV file contains the column headers.
- All values in the CSV and JSON files are treated as strings and are enclosed in single quotes in the generated SQL statements.

## License

This project is licensed under the MIT License.
