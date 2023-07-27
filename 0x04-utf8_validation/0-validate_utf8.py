def validUTF8(data):
    # Helper function to check if a given number is a valid start byte for UTF-8 character
    def is_start_byte(byte):
        return (byte & 0x80) == 0 or (byte & 0xE0) == 0xC0 or (byte & 0xF0) == 0xE0 or (byte & 0xF8) == 0xF0

    # Helper function to check if a given number is a valid continuation byte for UTF-8 character
    def is_continuation_byte(byte):
        return (byte & 0xC0) == 0x80

    # Variable to keep track of the number of continuation bytes needed for the current character
    num_continuation_bytes = 0

    for byte in data:
        if num_continuation_bytes > 0:
            # Check if the current byte is a valid continuation byte
            if not is_continuation_byte(byte):
                return False
            num_continuation_bytes -= 1
        else:
            # Check if the current byte is a valid start byte for UTF-8 character
            if not is_start_byte(byte):
                return False
            # Determine the number of continuation bytes needed based on the start byte
            if (byte & 0xE0) == 0xC0:
                num_continuation_bytes = 1
            elif (byte & 0xF0) == 0xE0:
                num_continuation_bytes = 2
            elif (byte & 0xF8) == 0xF0:
                num_continuation_bytes = 3

    # If all bytes have been processed and there are no remaining continuation bytes needed, it's a valid UTF-8 encoding
    return num_continuation_bytes == 0
