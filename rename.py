import os


# Function to rename multiple files
def main():
    imgext = ["png", "jpg", "jpeg", "webp"]
    folder = "Phone"
    i = 0
    for _, filename in enumerate(os.listdir(folder)):
        gg = filename.split(".")
        name = (8 - len(str(i))) * "0" + str(i) + "." + gg[-1]
        src = f"{folder}/{filename}"
        dst = f"{folder}/{name}"
        if gg[-1] in imgext:
            os.rename(src, dst)
            i = i + 1


# Driver Code
if __name__ == "__main__":
    # Calling main() function
    main()
