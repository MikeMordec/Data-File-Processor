for each of the 5 files
    open the file to read
    open the file to write
    target = target from input file
    nums = list of numbers from input file
    if target < 1 then write to "No" else "Yes" to file
    for each x in nums:
        for each y in nums:
            if count == 0 and x + y == target:
                write x + y == target to file
                count = count + 1

