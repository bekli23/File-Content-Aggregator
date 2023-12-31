File Content Aggregator
Description

This script is designed to search for specific text files across multiple directories and aggregate their contents into a single output file. It's useful for scenarios where there's a need to consolidate information from dispersed .txt files.
Features

    Recursively searches directories for target files.
    Supports multiple encodings (utf-8, cp1252, latin1, ISO-8859-1) to handle a variety of file formats.
    Skips files that cannot be opened due to encoding issues and provides a warning for such cases.
    Aggregates content with separation lines for clarity.

Usage

    Adjust the director_start variable to specify the starting directory of the search.
    List the target filenames in the nume_fisiere list.
    Specify the desired name for the output file in the fisier_iesire variable.
    Run the script.

Example:
director_start = '.'  # This specifies the current directory. Modify as needed.
nume_fisiere = ['All Passwords.txt', 'passwords.txt']
fisier_iesire = 'out.txt'


Password Extractor

Description:
This script recursively scans files within a specified directory, extracting lines that contain the keywords "Password:", "pass:", or "PASS:". It then saves the unique lines (without the keywords) to an output file. If the output file or its directories don't exist, they will be automatically created.

Usage:
Set the director_start to your starting directory and fisier_iesire for the output file name, then run the script.
