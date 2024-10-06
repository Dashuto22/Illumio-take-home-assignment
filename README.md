# Illumio-take-home-assignment

A brief description of the project.

## Table of Contents
- [Assumptions](#Assumptions)
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
