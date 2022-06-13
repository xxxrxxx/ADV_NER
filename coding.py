def deletK(head,n):
    pre=head
    cur=head
    for _ in range(n):
        cur=cur.next

    while cur:
        cur=cur.next
        pre=pre.next
    pre.next=pre.next.next
    return pre
