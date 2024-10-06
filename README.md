# Illumio-take-home-assignment

Please go through the instructions step by step in order to utilize the script and understand its working.

## Table of Contents
- [Assumptions](#Assumptions)
- [Prerequisites](#Prerequisites)
- [Usage](#Usage)
- [Tests-covered](#Tests-covered)


## Assumptions

The following key assumptions were made while implementing the solution:

1. **Correct File Structure**
   - **Lookup Table (`lookup_table.csv`):**
     - I assumed the lookup table file is a valid CSV with exactly 3 columns: `dstport`, `protocol`, and `tag`.
     - I assumed the first row of the CSV file contains headers and is skipped in the processing.
     - Each row contains valid `dstport`, `protocol`, and `tag` values.
   - **Flow Logs (`flow_logs.txt`):**
     - I assumed that each line in the flow log file follows a consistent format, with at least 12 fields separated by spaces.
     - I assumed that the `dstport` is found at the 6th field (index 5), and the `protocol` number at the 8th field (index 7).

2. **Known Protocol Mappings**
   - I assumed the following mappings for protocol numbers:
     - `6` maps to TCP.
     - `17` maps to UDP.
     - `1` maps to ICMP.
   - Any other protocol number not mapped in the `protocol_map` dictionary will result in a log entry being skipped (treated as invalid).

3. **Case Insensitivity**
   - The protocol values in the lookup table are treated as case-insensitive. For example, both `TCP` and `tcp` are considered the same.

4. **Default Action for Unmatched Entries**
   - If no match is found in the lookup table for a combination of `dstport` and `protocol`, the log is classified as "Untagged."
   - My program counts these "Untagged" entries separately.

5. **Handling Invalid or Incomplete Flow Log Lines**
   - My program assumes that lines with fewer than 12 fields in the flow log file are invalid and skips them without processing.
   - If a flow log entry has an unknown protocol (i.e., not `6`, `17`, or `1`), it is skipped, and the user is informed via a printed message.

6. **No Overlapping Ports in Lookup Table**
   - My solution assumes that each combination of `dstport` and `protocol` in the lookup table is unique. If there were multiple tags for the same port/protocol combination, the program would select the first occurrence.

7. **Input Size Constraints**
   - My solution assumes that both the flow log file (up to 10 MB) and the lookup table (up to 10,000 mappings) are within the given limits and can be processed in memory without performance issues.

8. **Port and Protocol Values are Integers**
   - I assumed that `dstport` and `protocol` values are always integer-like strings in the flow logs and lookup table. If non-integer values are encountered, they would not be parsed correctly.

9. **Default Libraries**
   - I assumed that the solution can only rely on Python's built-in libraries (such as `csv`) and avoids using external libraries like `pandas` or `numpy`, as requested.

10. **No Relocation for Files**
    - I assumed that the input files (`lookup_table.csv` and `flow_logs.txt`) are available at the specified paths and are accessible for reading.

These assumptions help simplify the implementation while ensuring the solution works efficiently under the given constraints and requirements.


### Prerequisites
Make sure you have the following installed:
- **Python 3.x**: The program is written in Python, so you need to have Python installed on your system. You can download it from [here](https://www.python.org/downloads/).
  

## Usage
These are the files which are present in the repository-
- `main.py`: The main script containing the program logic.
- `sample_flow_logs.txt`: A sample flow log file used to test the program.
- `sample_lookup.csv`: A sample lookup table with port and protocol mappings.
  
To run the program, follow these steps:

1. **Clone the Repository**:
   
   Open your terminal or command prompt and clone the repository using the following command:
   
   ```bash
   git clone https://github.com/Dashuto22/Illumio-take-home-assignment.git

2. **Navigate to the project directory**

   After cloning the repository, navigate to the project directory using the following command:

   ```bash
   cd Illumio-take-home-assignment

3. **Run the Program**

   Use the following command to run the program, it will execute the program with the provided sample flow log (sample_flow_logs.txt) and lookup table (sample_lookup.csv) files in the same project directory.

   ```bash
   python main.py

4. **Expected Output**

   The program will process the flow log and lookup table and provide the following outputs:

   Tag Counts: The number of times each tag from the lookup table is used.
   
   Untagged Entries: The count of entries from the flow log that do not match any tag in the lookup table.

## Tests-covered
To thoroughly test my above solution, I designed test cases that cover a range of scenarios, including typical, edge, and erroneous cases. Below are the test categories with specific test cases to ensure the solution works correctly:

| **Test Case ID** | **Description**                             | **Input**                                                                                           | **Expected Outcome**                                                                              | **Purpose**                                                                                     |
|-------------------|---------------------------------------------|-----------------------------------------------------------------------------------------------------|---------------------------------------------------------------------------------------------------|-------------------------------------------------------------------------------------------------|
| **Test Case 1**   | Valid Flow Log and Lookup Table            | - Flow log: A valid log file with several entries.<br>- Lookup table: A valid CSV with tags mapped to different ports and protocols. | The program outputs correct tag counts and port/protocol counts.                                 | To ensure the program correctly matches entries, counts tags, and handles valid data.          |
| **Test Case 2**   | Multiple Untagged Entries                  | - Flow log: Contains several entries with `dstport` and `protocol` combinations not in the lookup table.<br>- Lookup table: Only includes a few ports and protocols. | The program assigns "Untagged" to unmatched flow log entries and counts them correctly.          | To verify that untagged entries are counted accurately.                                        |
| **Test Case 3**   | Empty Flow Log File                        | - Flow log: An empty file.<br>- Lookup table: A valid CSV with several mappings.                  | No tag or port/protocol counts are printed (empty output), or an appropriate message indicating no data is processed. | To ensure the program can handle an empty flow log without crashing.                          |
| **Test Case 4**   | Empty Lookup Table File                    | - Flow log: A valid file with multiple entries.<br>- Lookup table: An empty file or just a header row. | All flow log entries should be classified as "Untagged."                                        | To check how the program behaves when no lookup table entries are available.                  |
| **Test Case 5**   | Missing Lookup Table or Flow Log File      | - Lookup table or flow log: File not found or inaccessible.                                      | The program should raise a `FileNotFoundError` and print an appropriate error message.           | To ensure proper error handling when files are missing.                                       |
| **Test Case 6**   | Unmatched Protocol Numbers                 | - Flow log: Contains entries with a protocol number that doesn’t map to TCP, UDP, or ICMP.<br>- Lookup table: A valid table. | The program skips the log entries with unmatched protocols and prints a message, counting them as invalid. | To ensure the program handles unknown protocol numbers correctly.                              |
| **Test Case 7**   | Large Flow Log and Lookup Table            | - Flow log: A large file approaching the 10 MB size limit.<br>- Lookup table: A large CSV with around 10,000 entries. | The program processes all entries efficiently without running out of memory or crashing.          | To test the scalability of the solution and ensure it handles the maximum input size.          |
| **Test Case 8**   | Single Entry in Flow Log and Lookup Table  | - Flow log: Contains only one log entry.<br>- Lookup table: Contains only one corresponding tag entry. | The program correctly matches the single log entry and produces the expected count.              | To verify the program works correctly with the smallest possible inputs.                       |
| **Test Case 9**   | Different Case for Protocols               | - Flow log: Contains entries where the protocol numbers map to TCP, UDP, or ICMP.<br>- Lookup table: Includes protocol values like TCP, udp, and Icmp with different capitalizations. | The program matches the protocol case-insensitively.                                            | To ensure the program treats protocols as case-insensitive, as required by the problem.       |
