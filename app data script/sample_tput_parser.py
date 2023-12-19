def getParseData(filename):
    fh = open(filename, "r")
    data = fh.readlines()
    tput_list = []
    for d in data:
        d = d.strip()
        if "sec" in d and "bps" in d and "retrans" in d:
            split_list = d.split()
            idx = 0
            for elem in split_list:
                elem = elem.strip()
                elem = elem.lower()
                if "bps" in elem:
                    if elem == "kbps":
                        tput_list.append(float(split_list[idx - 6]) * 1000)
                    elif elem == "bps":
                        tput_list.append(float(split_list[idx - 6]) * 1000000)
                    elif elem == "gbps":
                        tput_list.append(float(split_list[idx - 6]) / 1000)
                    elif elem == "mbps":
                        tput_list.append(float(split_list[idx - 6]))                            
    return tput_list