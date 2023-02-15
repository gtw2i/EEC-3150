# Enter a valid IP Address
valid_ipaddr = False
while (not valid_ipaddr):
    ipaddr = input('IP Address: ')
    # Convert string to list delimited by period
    ipaddr = ipaddr.split('.')
    # Must have 3 periods, or 4 strings in the list
    if (len(ipaddr) != 4):
        print('ERROR: Enter a valid IP Address with 4 octets')
        continue
    # The 4 strings must contain all 0-9 characters
    if (not (ipaddr[0].isnumeric() and \
        ipaddr[1].isnumeric() and \
        ipaddr[2].isnumeric() and \
        ipaddr[3].isnumeric())):
        print('ERROR: Enter a valid IP Address with 4 numbers')
        continue
    # The integers in the list must be 0 <= x <= 255
    if (not (0 <= int(ipaddr[0]) <= 255 and \
        0 <= int(ipaddr[1]) <= 255 and \
        0 <= int(ipaddr[2]) <= 255 and \
        0 <= int(ipaddr[3]) <= 255)):
        print('ERROR: Enter a valid IP Address with octets 0 to 255')
        continue
    # If I get here I have a list of 4 valid IP address strings
    valid_ipaddr = True;

print(ipaddr)
