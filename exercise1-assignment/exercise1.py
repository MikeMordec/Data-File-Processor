for num in range(1,6):
    input_filename = "in"+str(num)+".txt"
    output_filename = "out"+str(num)+"_sample_actual.txt"
    print(input_filename)
    print(output_filename)
    file = open(input_filename)
    file_out = open(output_filename,'w')
    linesRaw = file.readlines()
    if(len(linesRaw)>=3):
        lines = []
        for line in linesRaw:
            lines.append(line.strip())
        target = lines[1]
        nums = lines[2].split()
        file_out.write(target+"\r\n")
        file_out.write("SumOfK\r\n")
        for num in nums:
            file_out.write(num+" ")
        file_out.write("\r\n")
        file_out.write("Exercise1 calculation complexity O(n^2)\r\n")    
        dub="No"
        for num in nums:
            if(int(target)>1):
                dub="Yes"
        file_out.write(dub+"\r\n")
        count = 0
        for x in nums:
            for y in nums:
                if(count==0 and int(x)+int(y)==int(target)):
                    file_out.write(x+"+"+y+"="+target+"\r\n")
                    count = count + 1
