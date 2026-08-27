class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        l1_list = []
        while l1:
            l1_list.append(l1.val)
            l1 = l1.next

        l2_list = []
        while l2:
            l2_list.append(l2.val)
            l2 = l2.next

        n = len(l1_list)
        m = len(l2_list)
        str_l1 = ""
        str_l2 = ""
        result_l3 = ""

        for i in range(n-1,-1,-1):
            str_l1 += str(l1_list[i])
        for j in range(m-1,-1,-1):
            str_l2 += str(l2_list[j])

        result = int(str_l2) + int(str_l1)

        for k in str(result):
            result_l3 += str(k)

        digit_list = [int(digit) for digit in result_l3]

        dummy = ListNode(0)
        curr = dummy
        for digit in digit_list[::-1]:
            curr.next = ListNode(digit)
            curr = curr.next

        return dummy.next

