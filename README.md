# Poverty Level Data Extraction from Bangladesh Poverty Map 2022

This Python project extracts poverty level data from the *Poverty Map of Bangladesh 2022* PDF published by the Bangladesh Bureau of Statistics. The data is provided in table format, which is parsed and cleaned using Python libraries such as `pdfplumber` and `pandas`. The final output is a clean CSV file containing the processed data, ready for further analysis.

## Project Overview

- **Source:** *Poverty Map of Bangladesh 2022* by the Bangladesh Bureau of Statistics (BBS).
- **Objective:** Extract tabular data from the PDF, clean it, and convert it into CSV format for easy access and analysis.
- **Key Libraries Used:** `pdfplumber`, `pandas`

## Features

- Extracts structured tables from the PDF using `pdfplumber`.
- Cleans and structures the data using `pandas`.
- Outputs the cleaned data into a CSV file for further analysis.

## Prerequisites

Ensure you have Python 3.7 or higher installed. This project uses the following Python libraries:

- `pdfplumber` — to extract data from PDF files.
- `pandas` — to clean and manipulate the extracted data.

To install the required dependencies, run the following command:

```bash
pip install -r requirements.txt
