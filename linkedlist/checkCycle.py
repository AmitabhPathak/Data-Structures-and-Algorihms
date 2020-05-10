def checkCycle(linklist):
    marker1=linklist
    marker2=linklist
    while marker2!=None and marker2.next!=None:
        marker1=marker1.next
        marker2=marker2.next.next
        if(marker2==marker1):
            return True
    return False