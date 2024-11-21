def bytes_to_kilobytes(bytes_value):
    return bytes_value / 1024

def kilobytes_to_bytes(kilobytes_value):
    return kilobytes_value * 1024

choice = input("Convert (1) bytes to kilobytes or (2) kilobytes to bytes? Enter 1 or 2: ")

if choice == "1":
    bytes_value = float(input("Enter value in bytes: "))
    print(f"Value in kilobytes: {bytes_to_kilobytes(bytes_value)}")
elif choice == "2":
    kilobytes_value = float(input("Enter value in kilobytes: "))
    print(f"Value in bytes: {kilobytes_to_bytes(kilobytes_value)}")
else:
    print("Invalid choice.")