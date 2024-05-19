Explanation:
Function generate_ip_range(start_ip, count):

Input Parameters: Takes a starting IP address and the number of IP addresses to generate.
IP Generation: Uses the ip_address function to convert the starting IP to an IPv4Address object. Then, it generates a list of IP addresses by incrementing the starting IP address by the required count.
Main Script:

Starting IP and Number of Servers: Defines the starting IP address and the number of servers.
Generate IP List: Calls generate_ip_range(start_ip, num_servers) to generate a list of 10 IP addresses starting from the given IP.
Port Range: Defines the range of ports to scan (from 75 to 85).
Port Checking Loop: Iterates over each generated IP address and each port within the specified range, calling the check_port_status function for each combination and printing the results.

This approach is more scalable and efficient, especially when dealing with a large number of sequential IP addresses. The script will dynamically generate the required IP addresses based on the starting IP and the count, and then check the port status for the specified range.
