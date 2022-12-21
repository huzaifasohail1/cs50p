file = input("File Name: ")
file1 = file.lower()
file2 = file1.strip()
if ".gif" in file2:
    print("image/gif")
elif ".jpg" in file2:
    print("image/jpeg")
elif ".jpeg" in file2:
    print("image/jpeg")
elif ".png" in file2:
    print("image/png")
elif ".pdf" in file2:
    print("application/pdf")
elif ".txt" in file2:
    print("text/plain")
elif ".zip" in file2:
    print("application/zip")
else:
    print("application/octet-stream")
    