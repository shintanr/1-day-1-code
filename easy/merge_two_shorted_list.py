class Solution(object):
    def merge_two_lists(self, l1, l2):
        dummy = ListNode(0)
        current = dummy
        
        while l1 and l2:
            if l1.val < l2.val:
                current.next = l1
                l1 = l1.next
            else:
                current.next = l2
                l2 = l2.next
            current = current.next
        
        current.next = l1 or l2
        
        return dummy.next
    
    # langkah kerjanya 
    # ada 2 list yang akan di merge yaitu l1 dan l2
    # lakukan pengecekan jika l1 dan l2 tidak sama dengan None
    # jika l1.val < l2.val maka current.next = l1 dan l1 = l1.next
    
    
    #penjelasan:
    # membuat dummy node dengan value 0 untuk menampung hasil merge dari l1 dan l2
    # membuat current node yang menunjuk ke dummy node untuk melakukan pengecekan dan penambahan node selanjutnya 
    # lakukan perulangan selama l1 dan l2 tidak sama dengan None untuk mengecek apakah l1 dan l2 sudah mencapai akhir 
    # jika l1.val < l2.val maka current.next = l1 dan l1 = l1.next 
    # jika tidak maka current.next = l2 dan l2 = l2.next
    # current = current.next
    # current.next = l1 atau l2
    # return dummy.next
    # Time complexity: O(n) karena melakukan perulangan sebanyak n kali 
    # Space complexity: O(1) karena hanya menggunakan variabel current dan dummy 
 
    
    