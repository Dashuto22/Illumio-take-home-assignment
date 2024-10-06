import csv

def load_lookup_table(lookup_file):
    lookup_table = {}
    try:
        with open(lookup_file, 'r') as file:
            reader = csv.reader(file)
            next(reader)  

            is_empty = True
            for row in reader:
                is_empty = False  
                
                
                if len(row) != 3:
                    print(f"Invalid row in lookup file: {row}")
                    continue
                dstport = row[0].strip()
                protocol = row[1].strip().lower()  
                tag = row[2].strip()
                lookup_table[(dstport, protocol)] = tag

            if is_empty:
                print(f"Warning: The lookup table '{lookup_file}' is empty (or contains only the header row).")

    except FileNotFoundError:
        print(f"Error: The lookup file '{lookup_file}' was not found.")
        raise  
    except Exception as e:
        print(f"An error occurred while reading the lookup file: {e}")
        raise
    
    return lookup_table


def parse_flow_logs(flow_log_file, lookup_table):
    tag_counts = {}
    port_protocol_counts = {}
    
    try:
        with open(flow_log_file, 'r') as file:
            for line in file:
                fields = line.split()
                
                
                if len(fields) < 12:
                    print(f"Skipping invalid flow log line: {line}")
                    continue
                
                dstport = fields[5].strip() 
                protocol_num = fields[7].strip()  

               
                protocol_map = {'6': 'tcp', '17': 'udp', '1': 'icmp'}
                protocol = protocol_map.get(protocol_num, None)

                if protocol:
                    port_protocol = (dstport, protocol)

          
                    tag = lookup_table.get(port_protocol, 'Untagged')

                    
                    if tag not in tag_counts:
                        tag_counts[tag] = 0
                    tag_counts[tag] += 1

                  
                    if port_protocol not in port_protocol_counts:
                        port_protocol_counts[port_protocol] = 0
                    port_protocol_counts[port_protocol] += 1
                else:
                    print(f"Unknown protocol number: {protocol_num} in line: {line}")
    except FileNotFoundError:
        print(f"Error: The flow log file '{flow_log_file}' was not found.")
        raise
    except Exception as e:
        print(f"An error occurred while reading the flow log file: {e}")
        raise
    
    return tag_counts, port_protocol_counts


def output_results(tag_counts, port_protocol_counts):
    try:
       
        print("Tag Counts:")
        if tag_counts:
            print("Tag,Count")
            for tag, count in sorted(tag_counts.items()):
                print(f"{tag},{count}")
        else:
            print("No tags were found in the logs.")
        
      
        print("\nPort/Protocol Combination Counts:")
        if port_protocol_counts:
            print("Port,Protocol,Count")
            for (port, protocol), count in sorted(port_protocol_counts.items()):
                print(f"{port},{protocol},{count}")
        else:
            print("No port/protocol combinations were found in the logs.")
    except Exception as e:
        print(f"An error occurred while outputting results: {e}")
        raise


def main():
    lookup_file = './sample_lookup.csv'  
    flow_log_file = './sample_flow_logs.txt'  

    try:
        
        lookup_table = load_lookup_table(lookup_file)

     
        tag_counts, port_protocol_counts = parse_flow_logs(flow_log_file, lookup_table)

    
        output_results(tag_counts, port_protocol_counts)
        
    except Exception as e:
        print(f"An unexpected error occurred during execution: {e}")

if __name__ == "__main__":
    main()
