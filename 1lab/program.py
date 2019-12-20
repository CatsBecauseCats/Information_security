from doKey import checkCPUsum, getCPUsum

if __name__ == "__main__":
    isExistAccess = checkCPUsum(getCPUsum())

    if isExistAccess:
        print("All OK! You have access!")
    else:
        print("You are a hacker! You do not have access!")
