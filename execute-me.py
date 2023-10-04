
    # Open the binary file in read mode
with open('/tmp/execute-me', 'rb') as file:
        binary_data = file.read()
        text_data = binary_data.decode('utf-8', errors='ignore')
        print(text_data)