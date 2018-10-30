def heatwave(befyestdata,yestdata,todata):
    if befyestdata<yestdata:
        if yestdata<todata:
            return ("Lyon, We have a heatwave");
        else:
            return ("No worries, we are not in a heatwave");
    else:
        return ("No worries, we are not in a heatwave");



